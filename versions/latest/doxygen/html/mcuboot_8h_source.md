---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/mcuboot_8h_source.html
original_path: doxygen/html/mcuboot_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mcuboot.h

[Go to the documentation of this file.](mcuboot_8h.md)

1/\*

2 \* Copyright (c) 2017 Nordic Semiconductor ASA

3 \* Copyright (c) 2016 Linaro Limited

4 \*

5 \* SPDX-License-Identifier: Apache-2.0

6 \*/

7

15

16#ifndef ZEPHYR\_INCLUDE\_DFU\_MCUBOOT\_H\_

17#define ZEPHYR\_INCLUDE\_DFU\_MCUBOOT\_H\_

18

19#include <[stdbool.h](stdbool_8h.md)>

20#include <stddef.h>

21#include <[sys/types.h](lib_2libc_2minimal_2include_2sys_2types_8h.md)>

22

23#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

24

32

33#ifdef \_\_cplusplus

34extern "C" {

35#endif

36

37#ifdef BOOT\_SWAP\_TYPE\_NONE

38#if BOOT\_SWAP\_TYPE\_NONE != 1 /\*ensure the same definition in MCUboot \*/

39#error "definition incompatible"

40#endif

41#else

[ 43](group__mcuboot__api.md#gabb6482b898e8307074d8aef01b1102b7)#define BOOT\_SWAP\_TYPE\_NONE 1

44#endif

45

46#ifdef BOOT\_SWAP\_TYPE\_TEST

47#if BOOT\_SWAP\_TYPE\_TEST != 2 /\*ensure the same definition in MCUboot \*/

48#error "definition incompatible"

49#endif

50#else

[ 52](group__mcuboot__api.md#ga3aa4415c47231a120c4cab455ea0beef)#define BOOT\_SWAP\_TYPE\_TEST 2

53#endif

54

55#ifdef BOOT\_SWAP\_TYPE\_PERM

56#if BOOT\_SWAP\_TYPE\_PERM != 3 /\*ensure the same definition in MCUboot \*/

57#error "definition incompatible"

58#endif

59#else

[ 61](group__mcuboot__api.md#ga09ebc9ba28e294e71388480bb9e4f677)#define BOOT\_SWAP\_TYPE\_PERM 3

62#endif

63

64#ifdef BOOT\_SWAP\_TYPE\_REVERT

65#if BOOT\_SWAP\_TYPE\_REVERT != 4 /\*ensure the same definition in MCUboot \*/

66#error "definition incompatible"

67#endif

68#else

[ 70](group__mcuboot__api.md#ga8ca7bd765c6ab669db0774c0b0122494)#define BOOT\_SWAP\_TYPE\_REVERT 4

71#endif

72

73#ifdef BOOT\_SWAP\_TYPE\_FAIL

74#if BOOT\_SWAP\_TYPE\_FAIL != 5 /\*ensure the same definition in MCUboot \*/

75#error "definition incompatible"

76#endif

77#else

[ 79](group__mcuboot__api.md#ga28cb43e6bfacdd285d95751cda80de13)#define BOOT\_SWAP\_TYPE\_FAIL 5

80#endif

81

[ 82](group__mcuboot__api.md#ga1e697351ff503f9a53b17916e63cce06)#define BOOT\_IMG\_VER\_STRLEN\_MAX 25 /\* 255.255.65535.4294967295\0 \*/

83

84

[ 92](structmcuboot__img__sem__ver.md)struct [mcuboot\_img\_sem\_ver](structmcuboot__img__sem__ver.md) {

[ 93](structmcuboot__img__sem__ver.md#ae6fa8e6cc51e57e24a2d99670e543998) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [major](structmcuboot__img__sem__ver.md#ae6fa8e6cc51e57e24a2d99670e543998);

[ 94](structmcuboot__img__sem__ver.md#a3ab711b800ab894e201d175b491a9552) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [minor](structmcuboot__img__sem__ver.md#a3ab711b800ab894e201d175b491a9552);

[ 95](structmcuboot__img__sem__ver.md#aabecc9fffb8ec7a7f02f2894f8d6e0f0) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [revision](structmcuboot__img__sem__ver.md#aabecc9fffb8ec7a7f02f2894f8d6e0f0);

[ 96](structmcuboot__img__sem__ver.md#abf2e489560daefaa0c5d33e9c7535dab) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [build\_num](structmcuboot__img__sem__ver.md#abf2e489560daefaa0c5d33e9c7535dab);

97};

98

[ 108](structmcuboot__img__header__v1.md)struct [mcuboot\_img\_header\_v1](structmcuboot__img__header__v1.md) {

[ 110](structmcuboot__img__header__v1.md#a83a042079d850f383eef7a46cad14fa4) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [image\_size](structmcuboot__img__header__v1.md#a83a042079d850f383eef7a46cad14fa4);

[ 112](structmcuboot__img__header__v1.md#a01dd3b50bb00accf4108b08c01df4e2b) struct [mcuboot\_img\_sem\_ver](structmcuboot__img__sem__ver.md) [sem\_ver](structmcuboot__img__header__v1.md#a01dd3b50bb00accf4108b08c01df4e2b);

113};

114

[ 126](structmcuboot__img__header.md)struct [mcuboot\_img\_header](structmcuboot__img__header.md) {

[ 132](structmcuboot__img__header.md#ab5147e9586062d4dd5b381af13f1e82d) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [mcuboot\_version](structmcuboot__img__header.md#ab5147e9586062d4dd5b381af13f1e82d);

138 union {

[ 140](structmcuboot__img__header.md#aff12aff412ea774f96948e7db0b25009) struct [mcuboot\_img\_header\_v1](structmcuboot__img__header__v1.md) [v1](structmcuboot__img__header.md#aff12aff412ea774f96948e7db0b25009);

[ 141](structmcuboot__img__header.md#a34f5595bbd5b974c04386b568c88e39f) } [h](structmcuboot__img__header.md#a34f5595bbd5b974c04386b568c88e39f);

142};

143

[ 158](group__mcuboot__api.md#ga652ffad55e2917c62a62f6463935fe59)int [boot\_read\_bank\_header](group__mcuboot__api.md#ga652ffad55e2917c62a62f6463935fe59)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) area\_id,

159 struct [mcuboot\_img\_header](structmcuboot__img__header.md) \*header,

160 size\_t header\_size);

161

[ 176](group__mcuboot__api.md#ga2eadd700521a8b94dea3d3d04c9f5bd8)bool [boot\_is\_img\_confirmed](group__mcuboot__api.md#ga2eadd700521a8b94dea3d3d04c9f5bd8)(void);

177

[ 190](group__mcuboot__api.md#ga95ccc9e1c7460fec16b9ce9ac8ad7a72)int [boot\_write\_img\_confirmed](group__mcuboot__api.md#ga95ccc9e1c7460fec16b9ce9ac8ad7a72)(void);

191

[ 206](group__mcuboot__api.md#gaa0f2410f520ef57e6d793c169639a6f8)int [boot\_write\_img\_confirmed\_multi](group__mcuboot__api.md#gaa0f2410f520ef57e6d793c169639a6f8)(int image\_index);

207

[ 214](group__mcuboot__api.md#gaa0ce517ba1c0b21c4898762fab959b12)int [mcuboot\_swap\_type](group__mcuboot__api.md#gaa0ce517ba1c0b21c4898762fab959b12)(void);

215

[ 225](group__mcuboot__api.md#ga1e679c6fefe7deaaed9a2265ce69cf1e)int [mcuboot\_swap\_type\_multi](group__mcuboot__api.md#ga1e679c6fefe7deaaed9a2265ce69cf1e)(int image\_index);

226

227

[ 229](group__mcuboot__api.md#ga9ed69fcd1ebf57cc356ce2bb835853f7)#define BOOT\_UPGRADE\_TEST 0

[ 230](group__mcuboot__api.md#gab48b79d246df6ebc712040c5ee00aa73)#define BOOT\_UPGRADE\_PERMANENT 1

231

[ 242](group__mcuboot__api.md#gad47f2356938a7b5acf8e0bbe4d9e4494)int [boot\_request\_upgrade](group__mcuboot__api.md#gad47f2356938a7b5acf8e0bbe4d9e4494)(int permanent);

243

[ 256](group__mcuboot__api.md#gae9e0e43663c3671aa4b4df6d30511d39)int [boot\_request\_upgrade\_multi](group__mcuboot__api.md#gae9e0e43663c3671aa4b4df6d30511d39)(int image\_index, int permanent);

257

[ 264](group__mcuboot__api.md#ga03b691762d00e4cab6a5bd91979d8d80)int [boot\_erase\_img\_bank](group__mcuboot__api.md#ga03b691762d00e4cab6a5bd91979d8d80)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) area\_id);

265

[ 272](group__mcuboot__api.md#ga6fa12d4058bbb78b7d8f35b436f0009c)[ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) [boot\_get\_area\_trailer\_status\_offset](group__mcuboot__api.md#ga6fa12d4058bbb78b7d8f35b436f0009c)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) area\_id);

273

[ 281](group__mcuboot__api.md#ga7b4443f339f2935895f01dfb80c6b460)[ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) [boot\_get\_trailer\_status\_offset](group__mcuboot__api.md#ga7b4443f339f2935895f01dfb80c6b460)(size\_t area\_size);

282

283#ifdef \_\_cplusplus

284}

285#endif

286

290

291#endif /\* ZEPHYR\_INCLUDE\_DFU\_MCUBOOT\_H\_ \*/

[boot\_erase\_img\_bank](group__mcuboot__api.md#ga03b691762d00e4cab6a5bd91979d8d80)

int boot\_erase\_img\_bank(uint8\_t area\_id)

Erase the image Bank.

[mcuboot\_swap\_type\_multi](group__mcuboot__api.md#ga1e679c6fefe7deaaed9a2265ce69cf1e)

int mcuboot\_swap\_type\_multi(int image\_index)

Determines the action, if any, that mcuboot will take on the next reboot.

[boot\_is\_img\_confirmed](group__mcuboot__api.md#ga2eadd700521a8b94dea3d3d04c9f5bd8)

bool boot\_is\_img\_confirmed(void)

Check if the currently running image is confirmed as OK.

[boot\_read\_bank\_header](group__mcuboot__api.md#ga652ffad55e2917c62a62f6463935fe59)

int boot\_read\_bank\_header(uint8\_t area\_id, struct mcuboot\_img\_header \*header, size\_t header\_size)

Read the MCUboot image header information from an image bank.

[boot\_get\_area\_trailer\_status\_offset](group__mcuboot__api.md#ga6fa12d4058bbb78b7d8f35b436f0009c)

ssize\_t boot\_get\_area\_trailer\_status\_offset(uint8\_t area\_id)

Get the offset of the status in the image bank.

[boot\_get\_trailer\_status\_offset](group__mcuboot__api.md#ga7b4443f339f2935895f01dfb80c6b460)

ssize\_t boot\_get\_trailer\_status\_offset(size\_t area\_size)

Get the offset of the status from an image bank size.

[boot\_write\_img\_confirmed](group__mcuboot__api.md#ga95ccc9e1c7460fec16b9ce9ac8ad7a72)

int boot\_write\_img\_confirmed(void)

Marks the currently running image as confirmed.

[mcuboot\_swap\_type](group__mcuboot__api.md#gaa0ce517ba1c0b21c4898762fab959b12)

int mcuboot\_swap\_type(void)

Determines the action, if any, that mcuboot will take on the next reboot.

[boot\_write\_img\_confirmed\_multi](group__mcuboot__api.md#gaa0f2410f520ef57e6d793c169639a6f8)

int boot\_write\_img\_confirmed\_multi(int image\_index)

Marks the image with the given index in the primary slot as confirmed.

[boot\_request\_upgrade](group__mcuboot__api.md#gad47f2356938a7b5acf8e0bbe4d9e4494)

int boot\_request\_upgrade(int permanent)

Marks the image in slot 1 as pending.

[boot\_request\_upgrade\_multi](group__mcuboot__api.md#gae9e0e43663c3671aa4b4df6d30511d39)

int boot\_request\_upgrade\_multi(int image\_index, int permanent)

Marks the image with the given index in the secondary slot as pending.

[types.h](include_2zephyr_2types_8h.md)

[types.h](lib_2libc_2minimal_2include_2sys_2types_8h.md)

[ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118)

\_\_SIZE\_TYPE\_\_ ssize\_t

**Definition** types.h:28

[stdbool.h](stdbool_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[mcuboot\_img\_header\_v1](structmcuboot__img__header__v1.md)

Model for the MCUboot image header as of version 1.

**Definition** mcuboot.h:108

[mcuboot\_img\_header\_v1::sem\_ver](structmcuboot__img__header__v1.md#a01dd3b50bb00accf4108b08c01df4e2b)

struct mcuboot\_img\_sem\_ver sem\_ver

The image version.

**Definition** mcuboot.h:112

[mcuboot\_img\_header\_v1::image\_size](structmcuboot__img__header__v1.md#a83a042079d850f383eef7a46cad14fa4)

uint32\_t image\_size

The size of the image, in bytes.

**Definition** mcuboot.h:110

[mcuboot\_img\_header](structmcuboot__img__header.md)

Model for the MCUBoot image header.

**Definition** mcuboot.h:126

[mcuboot\_img\_header::h](structmcuboot__img__header.md#a34f5595bbd5b974c04386b568c88e39f)

union mcuboot\_img\_header::@205062151061022111344000230326144127133004125136 h

The header information.

[mcuboot\_img\_header::mcuboot\_version](structmcuboot__img__header.md#ab5147e9586062d4dd5b381af13f1e82d)

uint32\_t mcuboot\_version

The version of MCUboot the header is built for.

**Definition** mcuboot.h:132

[mcuboot\_img\_header::v1](structmcuboot__img__header.md#aff12aff412ea774f96948e7db0b25009)

struct mcuboot\_img\_header\_v1 v1

Header information for MCUboot version 1.

**Definition** mcuboot.h:140

[mcuboot\_img\_sem\_ver](structmcuboot__img__sem__ver.md)

MCUboot image header representation for image version.

**Definition** mcuboot.h:92

[mcuboot\_img\_sem\_ver::minor](structmcuboot__img__sem__ver.md#a3ab711b800ab894e201d175b491a9552)

uint8\_t minor

**Definition** mcuboot.h:94

[mcuboot\_img\_sem\_ver::revision](structmcuboot__img__sem__ver.md#aabecc9fffb8ec7a7f02f2894f8d6e0f0)

uint16\_t revision

**Definition** mcuboot.h:95

[mcuboot\_img\_sem\_ver::build\_num](structmcuboot__img__sem__ver.md#abf2e489560daefaa0c5d33e9c7535dab)

uint32\_t build\_num

**Definition** mcuboot.h:96

[mcuboot\_img\_sem\_ver::major](structmcuboot__img__sem__ver.md#ae6fa8e6cc51e57e24a2d99670e543998)

uint8\_t major

**Definition** mcuboot.h:93

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dfu](dir_b8bb0fd55a94366ea1f20beca08b160d.md)
- [mcuboot.h](mcuboot_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

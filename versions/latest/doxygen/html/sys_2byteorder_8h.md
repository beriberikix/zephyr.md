---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/sys_2byteorder_8h.html
original_path: doxygen/html/sys_2byteorder_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

byteorder.h File Reference

Byte order helpers.
[More...](#details)

`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <stddef.h>`  
`#include <[zephyr/sys/__assert.h](____assert_8h_source.md)>`  
`#include <[zephyr/toolchain.h](toolchain_8h_source.md)>`

[Go to the source code of this file.](sys_2byteorder_8h_source.md)

| Macros | |
| --- | --- |
| #define | [BSWAP\_16](#ab2cc6513b37ec58689c48cec167d3485)(x) |
| #define | [BSWAP\_24](#a0f16b3ee6b8adca36048becb05ff7393)(x) |
| #define | [BSWAP\_32](#accb24612c7ee9b52e4006eced1b45ff3)(x) |
| #define | [BSWAP\_48](#acdd30009239c79bd4b997fa1dcbd555f)(x) |
| #define | [BSWAP\_64](#adcf23836f6eaeff620cb63f43042e546)(x) |
| #define | [sys\_le16\_to\_cpu](#ae4176f3e082f21488dedcd02b406cb43)(val) |
|  | Convert 16-bit integer from little-endian to host endianness. |
| #define | [sys\_cpu\_to\_le16](#ae7f653c0bca81809b53d8a91854ca4c9)(val) |
|  | Convert 16-bit integer from host endianness to little-endian. |
| #define | [sys\_le24\_to\_cpu](#a0e7342005eb6840186a59c006a719c0d)(val) |
|  | Convert 24-bit integer from little-endian to host endianness. |
| #define | [sys\_cpu\_to\_le24](#a85bae5c9bd6e58923d97ef41b7fd2055)(val) |
|  | Convert 24-bit integer from host endianness to little-endian. |
| #define | [sys\_le32\_to\_cpu](#aa713ea0f2e2c64c05bd4a3596e44ce4e)(val) |
|  | Convert 32-bit integer from little-endian to host endianness. |
| #define | [sys\_cpu\_to\_le32](#a8cdffcb0ce27f2871e1f1d05dcc31b7b)(val) |
|  | Convert 32-bit integer from host endianness to little-endian. |
| #define | [sys\_le48\_to\_cpu](#ae34388c412959f7af9e233dbe81fbbe0)(val) |
|  | Convert 48-bit integer from little-endian to host endianness. |
| #define | [sys\_cpu\_to\_le48](#ad9f886d1a9ffe95fc5e1e9eb4e39c532)(val) |
|  | Convert 48-bit integer from host endianness to little-endian. |
| #define | [sys\_le64\_to\_cpu](#a3d4737fab89f1762e518630090db8368)(val) |
| #define | [sys\_cpu\_to\_le64](#a8730241a4c5701f689ac0ac1255331c7)(val) |
| #define | [sys\_be16\_to\_cpu](#a840037a5fd3d36817dc92a44469df704)(val) |
|  | Convert 16-bit integer from big-endian to host endianness. |
| #define | [sys\_cpu\_to\_be16](#a9e2c7b19bbba5343ee8c5f9740484a56)(val) |
|  | Convert 16-bit integer from host endianness to big-endian. |
| #define | [sys\_be24\_to\_cpu](#afbe8be1a0842354ab076b2530ef9a041)(val) |
|  | Convert 24-bit integer from big-endian to host endianness. |
| #define | [sys\_cpu\_to\_be24](#ab441316429ce3604ec359f2a20c76431)(val) |
|  | Convert 24-bit integer from host endianness to big-endian. |
| #define | [sys\_be32\_to\_cpu](#aee4cefae7f089197e77c487faafda269)(val) |
|  | Convert 32-bit integer from big-endian to host endianness. |
| #define | [sys\_cpu\_to\_be32](#a508d3b125adf1d30e8411381827c4f05)(val) |
|  | Convert 32-bit integer from host endianness to big-endian. |
| #define | [sys\_be48\_to\_cpu](#a93e948095f79ab51368f193472d5b030)(val) |
|  | Convert 48-bit integer from big-endian to host endianness. |
| #define | [sys\_cpu\_to\_be48](#abb089029e2e84ce70bee82b18341273d)(val) |
|  | Convert 48-bit integer from host endianness to big-endian. |
| #define | [sys\_be64\_to\_cpu](#abb4d263f2b9b1cbf1c8fbaec714fc411)(val) |
| #define | [sys\_cpu\_to\_be64](#a6ac423744c21c1e40aabd7ecb9b9e8d5)(val) |
| #define | [sys\_uint16\_to\_array](#aa85342d9fd48f33f91bf0c37d993b120)(val) |
|  | Convert 16-bit unsigned integer to byte array. |
| #define | [sys\_uint32\_to\_array](#a0cd4ca8ebebe4b3759252b936a3fdd3f)(val) |
|  | Convert 32-bit unsigned integer to byte array. |
| #define | [sys\_uint64\_to\_array](#a96ac1537a710d9fd88a5280bce3b5a04)(val) |
|  | Convert 64-bit unsigned integer to byte array. |

| Functions | |
| --- | --- |
| static void | [sys\_put\_be16](#a68df8f14dfc0d8715d16ac87dd4c73d2) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) val, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dst[2]) |
|  | Put a 16-bit integer as big-endian to arbitrary location. |
| static void | [sys\_put\_be24](#a7aa82f69d08ebde8077fc3d2ebfbc53b) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dst[3]) |
|  | Put a 24-bit integer as big-endian to arbitrary location. |
| static void | [sys\_put\_be32](#a21f25ff68591217034f3414594425286) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dst[4]) |
|  | Put a 32-bit integer as big-endian to arbitrary location. |
| static void | [sys\_put\_be48](#abe8d617e8a5469c303a512fe94a55443) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dst[6]) |
|  | Put a 48-bit integer as big-endian to arbitrary location. |
| static void | [sys\_put\_be64](#a3e0d2e4e85249497011f5f9ea0d2987c) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dst[8]) |
|  | Put a 64-bit integer as big-endian to arbitrary location. |
| static void | [sys\_put\_le16](#af8f30219c861bb07d097374204d386dd) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) val, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dst[2]) |
|  | Put a 16-bit integer as little-endian to arbitrary location. |
| static void | [sys\_put\_le24](#a10bdc6fccf288e1d5215dba9c031c730) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dst[3]) |
|  | Put a 24-bit integer as little-endian to arbitrary location. |
| static void | [sys\_put\_le32](#aff60d0dcda6a48df4ea248f898a92de0) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dst[4]) |
|  | Put a 32-bit integer as little-endian to arbitrary location. |
| static void | [sys\_put\_le48](#aa6950654cc7fd67ab4f83235da59665a) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dst[6]) |
|  | Put a 48-bit integer as little-endian to arbitrary location. |
| static void | [sys\_put\_le64](#a7d89d4b4b278fefa3e65fc6c3894a70c) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) val, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dst[8]) |
|  | Put a 64-bit integer as little-endian to arbitrary location. |
| static [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [sys\_get\_be16](#a91fae25b12126c2b35d240f56866184d) (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) src[2]) |
|  | Get a 16-bit integer stored in big-endian format. |
| static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [sys\_get\_be24](#ac65e83f46ef042862b675995f74fcd9b) (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) src[3]) |
|  | Get a 24-bit integer stored in big-endian format. |
| static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [sys\_get\_be32](#a4db31229c7a8a80dace3870664b6442d) (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) src[4]) |
|  | Get a 32-bit integer stored in big-endian format. |
| static [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [sys\_get\_be48](#acf0fa9761998529910e022b80126ff6b) (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) src[6]) |
|  | Get a 48-bit integer stored in big-endian format. |
| static [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [sys\_get\_be64](#ad8e00ff5c0b9e394291936d1a570c215) (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) src[8]) |
|  | Get a 64-bit integer stored in big-endian format. |
| static [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [sys\_get\_le16](#a5c2c537b960a29bdd29133f902a67f6a) (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) src[2]) |
|  | Get a 16-bit integer stored in little-endian format. |
| static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [sys\_get\_le24](#aa75ded65c52f8308de46670b78339b7c) (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) src[3]) |
|  | Get a 24-bit integer stored in little-endian format. |
| static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [sys\_get\_le32](#aa7422f922db351d2da1d52195d43b8a4) (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) src[4]) |
|  | Get a 32-bit integer stored in little-endian format. |
| static [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [sys\_get\_le48](#a601c3cefbdfd8befa336339a87fd70fd) (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) src[6]) |
|  | Get a 48-bit integer stored in little-endian format. |
| static [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [sys\_get\_le64](#a678b08370e157ce5eb7117832aa86408) (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) src[8]) |
|  | Get a 64-bit integer stored in little-endian format. |
| static void | [sys\_memcpy\_swap](#a00935c7276235df4c16dd0f9ef524e67) (void \*dst, const void \*src, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) length) |
|  | Swap one buffer content into another. |
| static void | [sys\_mem\_swap](#ae86b6050e71ec755abb284be3a02d28a) (void \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) length) |
|  | Swap buffer content. |

## Detailed Description

Byte order helpers.

## Macro Definition Documentation

## [◆ ](#ab2cc6513b37ec58689c48cec167d3485)BSWAP\_16

| #define BSWAP\_16 | ( |  | *x* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)) ((((x) >> 8) & 0xff) | (((x) & 0xff) << 8)))

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

## [◆ ](#a0f16b3ee6b8adca36048becb05ff7393)BSWAP\_24

| #define BSWAP\_24 | ( |  | *x* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)) ((((x) >> 16) & 0xff) | \

(((x)) & 0xff00) | \

(((x) & 0xff) << 16)))

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

## [◆ ](#accb24612c7ee9b52e4006eced1b45ff3)BSWAP\_32

| #define BSWAP\_32 | ( |  | *x* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)) ((((x) >> 24) & 0xff) | \

(((x) >> 8) & 0xff00) | \

(((x) & 0xff00) << 8) | \

(((x) & 0xff) << 24)))

## [◆ ](#acdd30009239c79bd4b997fa1dcbd555f)BSWAP\_48

| #define BSWAP\_48 | ( |  | *x* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)) ((((x) >> 40) & 0xff) | \

(((x) >> 24) & 0xff00) | \

(((x) >> 8) & 0xff0000) | \

(((x) & 0xff0000) << 8) | \

(((x) & 0xff00) << 24) | \

(((x) & 0xff) << 40)))

[uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

\_\_UINT64\_TYPE\_\_ uint64\_t

**Definition** stdint.h:91

## [◆ ](#adcf23836f6eaeff620cb63f43042e546)BSWAP\_64

| #define BSWAP\_64 | ( |  | *x* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)) ((((x) >> 56) & 0xff) | \

(((x) >> 40) & 0xff00) | \

(((x) >> 24) & 0xff0000) | \

(((x) >> 8) & 0xff000000) | \

(((x) & 0xff000000) << 8) | \

(((x) & 0xff0000) << 24) | \

(((x) & 0xff00) << 40) | \

(((x) & 0xff) << 56)))

## [◆ ](#a840037a5fd3d36817dc92a44469df704)sys\_be16\_to\_cpu

| #define sys\_be16\_to\_cpu | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(val)

Convert 16-bit integer from big-endian to host endianness.

Parameters
:   | val | 16-bit integer in big-endian format. |
    | --- | --- |

Returns
:   16-bit integer in host endianness.

## [◆ ](#afbe8be1a0842354ab076b2530ef9a041)sys\_be24\_to\_cpu

| #define sys\_be24\_to\_cpu | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(val)

Convert 24-bit integer from big-endian to host endianness.

Parameters
:   | val | 24-bit integer in big-endian format. |
    | --- | --- |

Returns
:   24-bit integer in host endianness.

## [◆ ](#aee4cefae7f089197e77c487faafda269)sys\_be32\_to\_cpu

| #define sys\_be32\_to\_cpu | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(val)

Convert 32-bit integer from big-endian to host endianness.

Parameters
:   | val | 32-bit integer in big-endian format. |
    | --- | --- |

Returns
:   32-bit integer in host endianness.

## [◆ ](#a93e948095f79ab51368f193472d5b030)sys\_be48\_to\_cpu

| #define sys\_be48\_to\_cpu | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(val)

Convert 48-bit integer from big-endian to host endianness.

Parameters
:   | val | 48-bit integer in big-endian format. |
    | --- | --- |

Returns
:   48-bit integer in host endianness.

## [◆ ](#abb4d263f2b9b1cbf1c8fbaec714fc411)sys\_be64\_to\_cpu

| #define sys\_be64\_to\_cpu | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(val)

## [◆ ](#a9e2c7b19bbba5343ee8c5f9740484a56)sys\_cpu\_to\_be16

| #define sys\_cpu\_to\_be16 | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(val)

Convert 16-bit integer from host endianness to big-endian.

Parameters
:   | val | 16-bit integer in host endianness. |
    | --- | --- |

Returns
:   16-bit integer in big-endian format.

## [◆ ](#ab441316429ce3604ec359f2a20c76431)sys\_cpu\_to\_be24

| #define sys\_cpu\_to\_be24 | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(val)

Convert 24-bit integer from host endianness to big-endian.

Parameters
:   | val | 24-bit integer in host endianness. |
    | --- | --- |

Returns
:   24-bit integer in big-endian format.

## [◆ ](#a508d3b125adf1d30e8411381827c4f05)sys\_cpu\_to\_be32

| #define sys\_cpu\_to\_be32 | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(val)

Convert 32-bit integer from host endianness to big-endian.

Parameters
:   | val | 32-bit integer in host endianness. |
    | --- | --- |

Returns
:   32-bit integer in big-endian format.

## [◆ ](#abb089029e2e84ce70bee82b18341273d)sys\_cpu\_to\_be48

| #define sys\_cpu\_to\_be48 | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(val)

Convert 48-bit integer from host endianness to big-endian.

Parameters
:   | val | 48-bit integer in host endianness. |
    | --- | --- |

Returns
:   48-bit integer in big-endian format.

## [◆ ](#a6ac423744c21c1e40aabd7ecb9b9e8d5)sys\_cpu\_to\_be64

| #define sys\_cpu\_to\_be64 | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

(val)

## [◆ ](#ae7f653c0bca81809b53d8a91854ca4c9)sys\_cpu\_to\_le16

| #define sys\_cpu\_to\_le16 | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[BSWAP\_16](#ab2cc6513b37ec58689c48cec167d3485)(val)

[BSWAP\_16](#ab2cc6513b37ec58689c48cec167d3485)

#define BSWAP\_16(x)

**Definition** byteorder.h:19

Convert 16-bit integer from host endianness to little-endian.

Parameters
:   | val | 16-bit integer in host endianness. |
    | --- | --- |

Returns
:   16-bit integer in little-endian format.

## [◆ ](#a85bae5c9bd6e58923d97ef41b7fd2055)sys\_cpu\_to\_le24

| #define sys\_cpu\_to\_le24 | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[BSWAP\_24](#a0f16b3ee6b8adca36048becb05ff7393)(val)

[BSWAP\_24](#a0f16b3ee6b8adca36048becb05ff7393)

#define BSWAP\_24(x)

**Definition** byteorder.h:20

Convert 24-bit integer from host endianness to little-endian.

Parameters
:   | val | 24-bit integer in host endianness. |
    | --- | --- |

Returns
:   24-bit integer in little-endian format.

## [◆ ](#a8cdffcb0ce27f2871e1f1d05dcc31b7b)sys\_cpu\_to\_le32

| #define sys\_cpu\_to\_le32 | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[BSWAP\_32](#accb24612c7ee9b52e4006eced1b45ff3)(val)

[BSWAP\_32](#accb24612c7ee9b52e4006eced1b45ff3)

#define BSWAP\_32(x)

**Definition** byteorder.h:23

Convert 32-bit integer from host endianness to little-endian.

Parameters
:   | val | 32-bit integer in host endianness. |
    | --- | --- |

Returns
:   32-bit integer in little-endian format.

## [◆ ](#ad9f886d1a9ffe95fc5e1e9eb4e39c532)sys\_cpu\_to\_le48

| #define sys\_cpu\_to\_le48 | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[BSWAP\_48](#acdd30009239c79bd4b997fa1dcbd555f)(val)

[BSWAP\_48](#acdd30009239c79bd4b997fa1dcbd555f)

#define BSWAP\_48(x)

**Definition** byteorder.h:27

Convert 48-bit integer from host endianness to little-endian.

Parameters
:   | val | 48-bit integer in host endianness. |
    | --- | --- |

Returns
:   48-bit integer in little-endian format.

## [◆ ](#a8730241a4c5701f689ac0ac1255331c7)sys\_cpu\_to\_le64

| #define sys\_cpu\_to\_le64 | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[BSWAP\_64](#adcf23836f6eaeff620cb63f43042e546)(val)

[BSWAP\_64](#adcf23836f6eaeff620cb63f43042e546)

#define BSWAP\_64(x)

**Definition** byteorder.h:33

## [◆ ](#ae4176f3e082f21488dedcd02b406cb43)sys\_le16\_to\_cpu

| #define sys\_le16\_to\_cpu | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[BSWAP\_16](#ab2cc6513b37ec58689c48cec167d3485)(val)

Convert 16-bit integer from little-endian to host endianness.

Parameters
:   | val | 16-bit integer in little-endian format. |
    | --- | --- |

Returns
:   16-bit integer in host endianness.

## [◆ ](#a0e7342005eb6840186a59c006a719c0d)sys\_le24\_to\_cpu

| #define sys\_le24\_to\_cpu | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[BSWAP\_24](#a0f16b3ee6b8adca36048becb05ff7393)(val)

Convert 24-bit integer from little-endian to host endianness.

Parameters
:   | val | 24-bit integer in little-endian format. |
    | --- | --- |

Returns
:   24-bit integer in host endianness.

## [◆ ](#aa713ea0f2e2c64c05bd4a3596e44ce4e)sys\_le32\_to\_cpu

| #define sys\_le32\_to\_cpu | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[BSWAP\_32](#accb24612c7ee9b52e4006eced1b45ff3)(val)

Convert 32-bit integer from little-endian to host endianness.

Parameters
:   | val | 32-bit integer in little-endian format. |
    | --- | --- |

Returns
:   32-bit integer in host endianness.

## [◆ ](#ae34388c412959f7af9e233dbe81fbbe0)sys\_le48\_to\_cpu

| #define sys\_le48\_to\_cpu | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[BSWAP\_48](#acdd30009239c79bd4b997fa1dcbd555f)(val)

Convert 48-bit integer from little-endian to host endianness.

Parameters
:   | val | 48-bit integer in little-endian format. |
    | --- | --- |

Returns
:   48-bit integer in host endianness.

## [◆ ](#a3d4737fab89f1762e518630090db8368)sys\_le64\_to\_cpu

| #define sys\_le64\_to\_cpu | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[BSWAP\_64](#adcf23836f6eaeff620cb63f43042e546)(val)

## [◆ ](#aa85342d9fd48f33f91bf0c37d993b120)sys\_uint16\_to\_array

| #define sys\_uint16\_to\_array | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

{ \

(((val) >> 8) & 0xff), \

((val) & 0xff)}

Convert 16-bit unsigned integer to byte array.

Byte order aware macro to treat an unsigned integer as an array, rather than an integer literal. For example, 0x0123 would be converted to {0x01, 0x23} for big endian machines, and {0x23, 0x01} for little endian machines.

Parameters
:   | val | 16-bit unsigned integer. |
    | --- | --- |

Returns
:   16-bit unsigned integer as byte array.

## [◆ ](#a0cd4ca8ebebe4b3759252b936a3fdd3f)sys\_uint32\_to\_array

| #define sys\_uint32\_to\_array | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

{ \

(((val) >> 24) & 0xff), \

(((val) >> 16) & 0xff), \

(((val) >> 8) & 0xff), \

((val) & 0xff)}

Convert 32-bit unsigned integer to byte array.

Byte order aware macro to treat an unsigned integer as an array, rather than an integer literal. For example, 0x01234567 would be converted to {0x01, 0x23, 0x45, 0x67} for big endian machines, and {0x67, 0x45, 0x23, 0x01} for little endian machines.

Parameters
:   | val | 32-bit unsigned integer. |
    | --- | --- |

Returns
:   32-bit unsigned integer as byte array.

## [◆ ](#a96ac1537a710d9fd88a5280bce3b5a04)sys\_uint64\_to\_array

| #define sys\_uint64\_to\_array | ( |  | *val* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

{ \

(((val) >> 56) & 0xff), \

(((val) >> 48) & 0xff), \

(((val) >> 40) & 0xff), \

(((val) >> 32) & 0xff), \

(((val) >> 24) & 0xff), \

(((val) >> 16) & 0xff), \

(((val) >> 8) & 0xff), \

((val) & 0xff)}

Convert 64-bit unsigned integer to byte array.

Byte order aware macro to treat an unsigned integer as an array, rather than an integer literal. For example, 0x0123456789abcdef would be converted to {0x01, 0x23, 0x45, 0x67, 0x89, 0xab, 0xcd, 0xef} for big endian machines, and {0xef, 0xcd, 0xab, 0x89, 0x67, 0x45, 0x23, 0x01} for little endian machines.

Parameters
:   | val | 64-bit unsigned integer. |
    | --- | --- |

Returns
:   64-bit unsigned integer as byte array.

## Function Documentation

## [◆ ](#a91fae25b12126c2b35d240f56866184d)sys\_get\_be16()

| | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) sys\_get\_be16 | ( | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *src*[2] | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

Get a 16-bit integer stored in big-endian format.

Get a 16-bit integer, stored in big-endian format in a potentially unaligned memory location, and convert it to the host endianness.

Parameters
:   | src | Location of the big-endian 16-bit integer to get. |
    | --- | --- |

Returns
:   16-bit integer in host endianness.

## [◆ ](#ac65e83f46ef042862b675995f74fcd9b)sys\_get\_be24()

| | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) sys\_get\_be24 | ( | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *src*[3] | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

Get a 24-bit integer stored in big-endian format.

Get a 24-bit integer, stored in big-endian format in a potentially unaligned memory location, and convert it to the host endianness.

Parameters
:   | src | Location of the big-endian 24-bit integer to get. |
    | --- | --- |

Returns
:   24-bit integer in host endianness.

## [◆ ](#a4db31229c7a8a80dace3870664b6442d)sys\_get\_be32()

| | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) sys\_get\_be32 | ( | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *src*[4] | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

Get a 32-bit integer stored in big-endian format.

Get a 32-bit integer, stored in big-endian format in a potentially unaligned memory location, and convert it to the host endianness.

Parameters
:   | src | Location of the big-endian 32-bit integer to get. |
    | --- | --- |

Returns
:   32-bit integer in host endianness.

## [◆ ](#acf0fa9761998529910e022b80126ff6b)sys\_get\_be48()

| | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) sys\_get\_be48 | ( | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *src*[6] | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

Get a 48-bit integer stored in big-endian format.

Get a 48-bit integer, stored in big-endian format in a potentially unaligned memory location, and convert it to the host endianness.

Parameters
:   | src | Location of the big-endian 48-bit integer to get. |
    | --- | --- |

Returns
:   48-bit integer in host endianness.

## [◆ ](#ad8e00ff5c0b9e394291936d1a570c215)sys\_get\_be64()

| | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) sys\_get\_be64 | ( | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *src*[8] | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

Get a 64-bit integer stored in big-endian format.

Get a 64-bit integer, stored in big-endian format in a potentially unaligned memory location, and convert it to the host endianness.

Parameters
:   | src | Location of the big-endian 64-bit integer to get. |
    | --- | --- |

Returns
:   64-bit integer in host endianness.

## [◆ ](#a5c2c537b960a29bdd29133f902a67f6a)sys\_get\_le16()

| | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) sys\_get\_le16 | ( | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *src*[2] | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

Get a 16-bit integer stored in little-endian format.

Get a 16-bit integer, stored in little-endian format in a potentially unaligned memory location, and convert it to the host endianness.

Parameters
:   | src | Location of the little-endian 16-bit integer to get. |
    | --- | --- |

Returns
:   16-bit integer in host endianness.

## [◆ ](#aa75ded65c52f8308de46670b78339b7c)sys\_get\_le24()

| | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) sys\_get\_le24 | ( | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *src*[3] | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

Get a 24-bit integer stored in little-endian format.

Get a 24-bit integer, stored in little-endian format in a potentially unaligned memory location, and convert it to the host endianness.

Parameters
:   | src | Location of the little-endian 24-bit integer to get. |
    | --- | --- |

Returns
:   24-bit integer in host endianness.

## [◆ ](#aa7422f922db351d2da1d52195d43b8a4)sys\_get\_le32()

| | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) sys\_get\_le32 | ( | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *src*[4] | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

Get a 32-bit integer stored in little-endian format.

Get a 32-bit integer, stored in little-endian format in a potentially unaligned memory location, and convert it to the host endianness.

Parameters
:   | src | Location of the little-endian 32-bit integer to get. |
    | --- | --- |

Returns
:   32-bit integer in host endianness.

## [◆ ](#a601c3cefbdfd8befa336339a87fd70fd)sys\_get\_le48()

| | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) sys\_get\_le48 | ( | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *src*[6] | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

Get a 48-bit integer stored in little-endian format.

Get a 48-bit integer, stored in little-endian format in a potentially unaligned memory location, and convert it to the host endianness.

Parameters
:   | src | Location of the little-endian 48-bit integer to get. |
    | --- | --- |

Returns
:   48-bit integer in host endianness.

## [◆ ](#a678b08370e157ce5eb7117832aa86408)sys\_get\_le64()

| | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) sys\_get\_le64 | ( | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *src*[8] | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

Get a 64-bit integer stored in little-endian format.

Get a 64-bit integer, stored in little-endian format in a potentially unaligned memory location, and convert it to the host endianness.

Parameters
:   | src | Location of the little-endian 64-bit integer to get. |
    | --- | --- |

Returns
:   64-bit integer in host endianness.

## [◆ ](#ae86b6050e71ec755abb284be3a02d28a)sys\_mem\_swap()

| | void sys\_mem\_swap | ( | void \* | *buf*, | | --- | --- | --- | --- | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *length* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Swap buffer content.

In-place memory swap, where final content will be reversed. I.e.: buf[n] will be put in buf[end-n] Where n is an index and 'end' the last index of buf.

Parameters
:   | buf | A valid pointer on a memory area to swap |
    | --- | --- |
    | length | Size of buf memory area |

## [◆ ](#a00935c7276235df4c16dd0f9ef524e67)sys\_memcpy\_swap()

| | void sys\_memcpy\_swap | ( | void \* | *dst*, | | --- | --- | --- | --- | |  |  | const void \* | *src*, | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *length* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Swap one buffer content into another.

Copy the content of src buffer into dst buffer in reversed order, i.e.: src[n] will be put in dst[end-n] Where n is an index and 'end' the last index in both arrays. The 2 memory pointers must be pointing to different areas, and have a minimum size of given length.

Parameters
:   | dst | A valid pointer on a memory area where to copy the data in |
    | --- | --- |
    | src | A valid pointer on a memory area where to copy the data from |
    | length | Size of both dst and src memory areas |

## [◆ ](#a68df8f14dfc0d8715d16ac87dd4c73d2)sys\_put\_be16()

| | void sys\_put\_be16 | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *val*, | | --- | --- | --- | --- | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *dst*[2] ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Put a 16-bit integer as big-endian to arbitrary location.

Put a 16-bit integer, originally in host endianness, to a potentially unaligned memory location in big-endian format.

Parameters
:   | val | 16-bit integer in host endianness. |
    | --- | --- |
    | dst | Destination memory address to store the result. |

## [◆ ](#a7aa82f69d08ebde8077fc3d2ebfbc53b)sys\_put\_be24()

| | void sys\_put\_be24 | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *val*, | | --- | --- | --- | --- | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *dst*[3] ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Put a 24-bit integer as big-endian to arbitrary location.

Put a 24-bit integer, originally in host endianness, to a potentially unaligned memory location in big-endian format.

Parameters
:   | val | 24-bit integer in host endianness. |
    | --- | --- |
    | dst | Destination memory address to store the result. |

## [◆ ](#a21f25ff68591217034f3414594425286)sys\_put\_be32()

| | void sys\_put\_be32 | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *val*, | | --- | --- | --- | --- | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *dst*[4] ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Put a 32-bit integer as big-endian to arbitrary location.

Put a 32-bit integer, originally in host endianness, to a potentially unaligned memory location in big-endian format.

Parameters
:   | val | 32-bit integer in host endianness. |
    | --- | --- |
    | dst | Destination memory address to store the result. |

## [◆ ](#abe8d617e8a5469c303a512fe94a55443)sys\_put\_be48()

| | void sys\_put\_be48 | ( | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *val*, | | --- | --- | --- | --- | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *dst*[6] ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Put a 48-bit integer as big-endian to arbitrary location.

Put a 48-bit integer, originally in host endianness, to a potentially unaligned memory location in big-endian format.

Parameters
:   | val | 48-bit integer in host endianness. |
    | --- | --- |
    | dst | Destination memory address to store the result. |

## [◆ ](#a3e0d2e4e85249497011f5f9ea0d2987c)sys\_put\_be64()

| | void sys\_put\_be64 | ( | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *val*, | | --- | --- | --- | --- | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *dst*[8] ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Put a 64-bit integer as big-endian to arbitrary location.

Put a 64-bit integer, originally in host endianness, to a potentially unaligned memory location in big-endian format.

Parameters
:   | val | 64-bit integer in host endianness. |
    | --- | --- |
    | dst | Destination memory address to store the result. |

## [◆ ](#af8f30219c861bb07d097374204d386dd)sys\_put\_le16()

| | void sys\_put\_le16 | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *val*, | | --- | --- | --- | --- | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *dst*[2] ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Put a 16-bit integer as little-endian to arbitrary location.

Put a 16-bit integer, originally in host endianness, to a potentially unaligned memory location in little-endian format.

Parameters
:   | val | 16-bit integer in host endianness. |
    | --- | --- |
    | dst | Destination memory address to store the result. |

## [◆ ](#a10bdc6fccf288e1d5215dba9c031c730)sys\_put\_le24()

| | void sys\_put\_le24 | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *val*, | | --- | --- | --- | --- | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *dst*[3] ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Put a 24-bit integer as little-endian to arbitrary location.

Put a 24-bit integer, originally in host endianness, to a potentially unaligned memory location in little-endian format.

Parameters
:   | val | 24-bit integer in host endianness. |
    | --- | --- |
    | dst | Destination memory address to store the result. |

## [◆ ](#aff60d0dcda6a48df4ea248f898a92de0)sys\_put\_le32()

| | void sys\_put\_le32 | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *val*, | | --- | --- | --- | --- | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *dst*[4] ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Put a 32-bit integer as little-endian to arbitrary location.

Put a 32-bit integer, originally in host endianness, to a potentially unaligned memory location in little-endian format.

Parameters
:   | val | 32-bit integer in host endianness. |
    | --- | --- |
    | dst | Destination memory address to store the result. |

## [◆ ](#aa6950654cc7fd67ab4f83235da59665a)sys\_put\_le48()

| | void sys\_put\_le48 | ( | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *val*, | | --- | --- | --- | --- | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *dst*[6] ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Put a 48-bit integer as little-endian to arbitrary location.

Put a 48-bit integer, originally in host endianness, to a potentially unaligned memory location in little-endian format.

Parameters
:   | val | 48-bit integer in host endianness. |
    | --- | --- |
    | dst | Destination memory address to store the result. |

## [◆ ](#a7d89d4b4b278fefa3e65fc6c3894a70c)sys\_put\_le64()

| | void sys\_put\_le64 | ( | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *val*, | | --- | --- | --- | --- | |  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *dst*[8] ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

Put a 64-bit integer as little-endian to arbitrary location.

Put a 64-bit integer, originally in host endianness, to a potentially unaligned memory location in little-endian format.

Parameters
:   | val | 64-bit integer in host endianness. |
    | --- | --- |
    | dst | Destination memory address to store the result. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [byteorder.h](sys_2byteorder_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

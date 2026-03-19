---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__crc.html
original_path: doxygen/html/group__crc.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

CRC

[Operating System Services](group__os__services.md) » [Checksum](group__checksum.md)

| Enumerations | |
| --- | --- |
| enum | [crc\_type](#gabc40e4ffd6da1175eb8ee8573a527edd) {     [CRC4](#ggabc40e4ffd6da1175eb8ee8573a527eddaef5caa552f890f4c7e887dfe1a06bc22) , [CRC4\_TI](#ggabc40e4ffd6da1175eb8ee8573a527edda3a8effe9651199c20669daf033bbe59f) , [CRC7\_BE](#ggabc40e4ffd6da1175eb8ee8573a527edda218e7d92cae035c594e267fb0ed0ae6a) , [CRC8](#ggabc40e4ffd6da1175eb8ee8573a527edda852cb403a2665ed279b28679f11567d8) ,     [CRC8\_CCITT](#ggabc40e4ffd6da1175eb8ee8573a527eddae00c2275c0a5ac47b64c221feadfc3eb) , [CRC8\_ROHC](#ggabc40e4ffd6da1175eb8ee8573a527eddad0cba27d3a1347c21fc34cfd3aa0eab5) , [CRC16](#ggabc40e4ffd6da1175eb8ee8573a527edda27369d6d16d5fdf2a44111924c019e11) , [CRC16\_ANSI](#ggabc40e4ffd6da1175eb8ee8573a527edda4a5e69eba1f74c0bd028356c9fb0f1f6) ,     [CRC16\_CCITT](#ggabc40e4ffd6da1175eb8ee8573a527eddacdf0c4de024efc53edd374ad22c6da30) , [CRC16\_ITU\_T](#ggabc40e4ffd6da1175eb8ee8573a527edda3fdbd9451fc39959f46714a2f46ca42c) , [CRC24\_PGP](#ggabc40e4ffd6da1175eb8ee8573a527eddac7805fb845479f192a855292bdb03f43) , [CRC32\_C](#ggabc40e4ffd6da1175eb8ee8573a527edda4036b6c556c8aa1307c1ff7ff1626148) ,     [CRC32\_IEEE](#ggabc40e4ffd6da1175eb8ee8573a527eddaecf71323e57da8d4f7e45d154b1059d8)   } |
|  | CRC algorithm enumeration. [More...](#gabc40e4ffd6da1175eb8ee8573a527edd) |

| Functions | |
| --- | --- |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [crc16](#ga204a779aa0c1a152763ea8edc6fc3a8c) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) poly, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) seed, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*src, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Generic function for computing a CRC-16 without input or output reflection. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [crc16\_reflect](#gaccbcb5b80cf8deaac252474ecc6d9914) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) poly, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) seed, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*src, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Generic function for computing a CRC-16 with input and output reflection. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [crc8](#gaa614e73ee7484ca0424fa7d14a54bbb6) (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*src, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) polynomial, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) initial\_value, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) reversed) |
|  | Generic function for computing CRC 8. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [crc16\_ccitt](#ga74fa5608612c629291d15bc00b1c411c) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) seed, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*src, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Compute the checksum of a buffer with polynomial 0x1021, reflecting input and output. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [crc16\_itu\_t](#ga5502729e443496719de338e8b6692ac1) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) seed, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*src, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Compute the checksum of a buffer with polynomial 0x1021, no reflection of input or output. |
| static [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [crc16\_ansi](#gaac3ac50c029b656f5cc070e6c742601a) (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*src, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Compute the ANSI (or Modbus) variant of CRC-16. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [crc32\_ieee](#gafc24e79ed7f978f5bb813091ef318982) (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Generate IEEE conform CRC32 checksum. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [crc32\_ieee\_update](#ga17476d4af14603e322986ef603ce8530) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) crc, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Update an IEEE conforming CRC32 checksum. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [crc32\_c](#ga88d510b3958aee0990ca345aba260bc1) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) crc, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) first\_pkt, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) last\_pkt) |
|  | Calculate CRC32C (Castagnoli) checksum. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [crc8\_ccitt](#ga9a925de71cd0255a22c769dc4b130da5) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) initial\_value, const void \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Compute CCITT variant of CRC 8. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [crc8\_rohc](#ga7a8f4387a2d0163165557446d018f041) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) initial\_value, const void \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Compute ROHC variant of CRC 8. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [crc7\_be](#ga1169005fd900b2787035044eeea38af1) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) seed, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*src, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Compute the CRC-7 checksum of a buffer. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [crc4\_ti](#ga322365098ec65bde3d55b0c059896668) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) seed, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*src, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Compute the CRC-4 checksum of a buffer. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [crc4](#ga4458d7743f9a3394fb68cddcc100e456) (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*src, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) polynomial, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) initial\_value, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) reversed) |
|  | Generic function for computing CRC 4. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [crc24\_pgp](#gaebe7a9494dec69568b4f5cc95bf0fac2) (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Generate an OpenPGP CRC-24 checksum as defined in RFC 4880 section 6.1. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [crc24\_pgp\_update](#ga4523b3cf8dbc05ea44258d1652fbb969) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) crc, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Update an OpenPGP CRC-24 checksum. |
| static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [crc\_by\_type](#ga5d7f493210e56fb18b8199c9d8a17f33) (enum [crc\_type](#gabc40e4ffd6da1175eb8ee8573a527edd) type, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*src, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) seed, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) poly, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) reflect, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) first, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) last) |
|  | Compute a CRC checksum, in a generic way. |

## Detailed Description

## Enumeration Type Documentation

## [◆ ](#gabc40e4ffd6da1175eb8ee8573a527edd)crc\_type

| enum [crc\_type](#gabc40e4ffd6da1175eb8ee8573a527edd) |
| --- |

`#include <[crc.h](crc_8h.md)>`

CRC algorithm enumeration.

These values should be used with the [CRC](group__crc.md "CRC") dispatch function.

| Enumerator | |
| --- | --- |
| CRC4 | Use [crc4](#ga4458d7743f9a3394fb68cddcc100e456). |
| CRC4\_TI | Use [crc4\_ti](#ga322365098ec65bde3d55b0c059896668). |
| CRC7\_BE | Use [crc7\_be](#ga1169005fd900b2787035044eeea38af1). |
| CRC8 | Use [crc8](#gaa614e73ee7484ca0424fa7d14a54bbb6). |
| CRC8\_CCITT | Use [crc8\_ccitt](#ga9a925de71cd0255a22c769dc4b130da5). |
| CRC8\_ROHC | Use [crc8\_rohc](#ga7a8f4387a2d0163165557446d018f041). |
| CRC16 | Use [crc16](#ga204a779aa0c1a152763ea8edc6fc3a8c). |
| CRC16\_ANSI | Use [crc16\_ansi](#gaac3ac50c029b656f5cc070e6c742601a). |
| CRC16\_CCITT | Use [crc16\_ccitt](#ga74fa5608612c629291d15bc00b1c411c). |
| CRC16\_ITU\_T | Use [crc16\_itu\_t](#ga5502729e443496719de338e8b6692ac1). |
| CRC24\_PGP | Use [crc24\_pgp](#gaebe7a9494dec69568b4f5cc95bf0fac2). |
| CRC32\_C | Use [crc32\_c](#ga88d510b3958aee0990ca345aba260bc1). |
| CRC32\_IEEE | Use [crc32\_ieee](#gafc24e79ed7f978f5bb813091ef318982). |

## Function Documentation

## [◆ ](#ga204a779aa0c1a152763ea8edc6fc3a8c)crc16()

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) crc16 | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *poly*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *seed*, |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *src*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len* ) |

`#include <[crc.h](crc_8h.md)>`

Generic function for computing a CRC-16 without input or output reflection.

Compute CRC-16 by passing in the address of the input, the input length and polynomial used in addition to the initial value. This is O(n\*8) where n is the length of the buffer provided. No reflection is performed.

Note
:   If you are planning to use a CRC based on poly 0x1012 the functions [crc16\_itu\_t()](#ga5502729e443496719de338e8b6692ac1) is faster and thus recommended over this one.

Parameters
:   | poly | The polynomial to use omitting the leading x^16 coefficient |
    | --- | --- |
    | seed | Initial value for the CRC computation |
    | src | Input bytes for the computation |
    | len | Length of the input in bytes |

Returns
:   The computed CRC16 value (without any XOR applied to it)

## [◆ ](#gaac3ac50c029b656f5cc070e6c742601a)crc16\_ansi()

| | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) crc16\_ansi | ( | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *src*, | | --- | --- | --- | --- | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[crc.h](crc_8h.md)>`

Compute the ANSI (or Modbus) variant of CRC-16.

The ANSI variant of CRC-16 uses 0x8005 (0xA001 reflected) as its polynomial with the initial \* value set to 0xffff.

Parameters
:   | src | Input bytes for the computation |
    | --- | --- |
    | len | Length of the input in bytes |

Returns
:   The computed CRC16 value

## [◆ ](#ga74fa5608612c629291d15bc00b1c411c)crc16\_ccitt()

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) crc16\_ccitt | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *seed*, |
| --- | --- | --- | --- |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *src*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len* ) |

`#include <[crc.h](crc_8h.md)>`

Compute the checksum of a buffer with polynomial 0x1021, reflecting input and output.

This function is able to calculate any CRC that uses 0x1021 as it polynomial and requires reflecting both the input and the output. It is a fast variant that runs in O(n) time, where n is the length of the input buffer.

The following checksums can, among others, be calculated by this function, depending on the value provided for the initial seed and the value the final calculated CRC is XORed with:

- CRC-16/CCITT, CRC-16/CCITT-TRUE, CRC-16/KERMIT [https://reveng.sourceforge.io/crc-catalogue/16.htm#crc.cat.crc-16-kermit](https://reveng.sourceforge.io/crc-catalogue/16.htm#crc.cat.crc-16-kermit) initial seed: 0x0000, xor output: 0x0000
- CRC-16/X-25, CRC-16/IBM-SDLC, CRC-16/ISO-HDLC [https://reveng.sourceforge.io/crc-catalogue/16.htm#crc.cat.crc-16-ibm-sdlc](https://reveng.sourceforge.io/crc-catalogue/16.htm#crc.cat.crc-16-ibm-sdlc) initial seed: 0xffff, xor output: 0xffff

Note
:   To calculate the CRC across non-contiguous blocks use the return value from block N-1 as the seed for block N.

See ITU-T Recommendation V.41 (November 1988).

Parameters
:   | seed | Value to seed the CRC with |
    | --- | --- |
    | src | Input bytes for the computation |
    | len | Length of the input in bytes |

Returns
:   The computed CRC16 value (without any XOR applied to it)

## [◆ ](#ga5502729e443496719de338e8b6692ac1)crc16\_itu\_t()

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) crc16\_itu\_t | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *seed*, |
| --- | --- | --- | --- |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *src*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len* ) |

`#include <[crc.h](crc_8h.md)>`

Compute the checksum of a buffer with polynomial 0x1021, no reflection of input or output.

This function is able to calculate any CRC that uses 0x1021 as it polynomial and requires no reflection on both the input and the output. It is a fast variant that runs in O(n) time, where n is the length of the input buffer.

The following checksums can, among others, be calculated by this function, depending on the value provided for the initial seed and the value the final calculated CRC is XORed with:

- CRC-16/XMODEM, CRC-16/ACORN, CRC-16/LTE [https://reveng.sourceforge.io/crc-catalogue/16.htm#crc.cat.crc-16-xmodem](https://reveng.sourceforge.io/crc-catalogue/16.htm#crc.cat.crc-16-xmodem) initial seed: 0x0000, xor output: 0x0000
- CRC16/CCITT-FALSE, CRC-16/IBM-3740, CRC-16/AUTOSAR [https://reveng.sourceforge.io/crc-catalogue/16.htm#crc.cat.crc-16-ibm-3740](https://reveng.sourceforge.io/crc-catalogue/16.htm#crc.cat.crc-16-ibm-3740) initial seed: 0xffff, xor output: 0x0000
- CRC-16/GSM [https://reveng.sourceforge.io/crc-catalogue/16.htm#crc.cat.crc-16-gsm](https://reveng.sourceforge.io/crc-catalogue/16.htm#crc.cat.crc-16-gsm) initial seed: 0x0000, xor output: 0xffff

Note
:   To calculate the CRC across non-contiguous blocks use the return value from block N-1 as the seed for block N.

See ITU-T Recommendation V.41 (November 1988) (MSB first).

Parameters
:   | seed | Value to seed the CRC with |
    | --- | --- |
    | src | Input bytes for the computation |
    | len | Length of the input in bytes |

Returns
:   The computed CRC16 value (without any XOR applied to it)

## [◆ ](#gaccbcb5b80cf8deaac252474ecc6d9914)crc16\_reflect()

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) crc16\_reflect | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *poly*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *seed*, |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *src*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len* ) |

`#include <[crc.h](crc_8h.md)>`

Generic function for computing a CRC-16 with input and output reflection.

Compute CRC-16 by passing in the address of the input, the input length and polynomial used in addition to the initial value. This is O(n\*8) where n is the length of the buffer provided. Both input and output are reflected.

Note
:   If you are planning to use a CRC based on poly 0x1012 the function [crc16\_ccitt()](#ga74fa5608612c629291d15bc00b1c411c) is faster and thus recommended over this one.

The following checksums can, among others, be calculated by this function, depending on the value provided for the initial seed and the value the final calculated CRC is XORed with:

- CRC-16/ANSI, CRC-16/MODBUS, CRC-16/USB, CRC-16/IBM [https://reveng.sourceforge.io/crc-catalogue/16.htm#crc.cat.crc-16-modbus](https://reveng.sourceforge.io/crc-catalogue/16.htm#crc.cat.crc-16-modbus) poly: 0x8005 (0xA001) initial seed: 0xffff, xor output: 0x0000

Parameters
:   | poly | The polynomial to use omitting the leading x^16 coefficient. Important: please reflect the poly. For example, use 0xA001 instead of 0x8005 for CRC-16-MODBUS. |
    | --- | --- |
    | seed | Initial value for the CRC computation |
    | src | Input bytes for the computation |
    | len | Length of the input in bytes |

Returns
:   The computed CRC16 value (without any XOR applied to it)

## [◆ ](#gaebe7a9494dec69568b4f5cc95bf0fac2)crc24\_pgp()

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) crc24\_pgp | ( | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *data*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len* ) |

`#include <[crc.h](crc_8h.md)>`

Generate an OpenPGP CRC-24 checksum as defined in RFC 4880 section 6.1.

Parameters
:   | data | A pointer to the data on which the CRC will be calculated. |
    | --- | --- |
    | len | Data length in bytes. |

Returns
:   The CRC-24 value.

## [◆ ](#ga4523b3cf8dbc05ea44258d1652fbb969)crc24\_pgp\_update()

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) crc24\_pgp\_update | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *crc*, |
| --- | --- | --- | --- |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *data*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len* ) |

`#include <[crc.h](crc_8h.md)>`

Update an OpenPGP CRC-24 checksum.

Parameters
:   | [CRC](group__crc.md) | The CRC-24 checksum that needs to be updated. The full 32-bit value of the CRC needs to be used between calls, do not mask the value to keep only the last 24 bits. |
    | --- | --- |
    | data | A pointer to the data on which the CRC will be calculated. |
    | len | Data length in bytes. |

Returns
:   The CRC-24 value. When the last buffer of data has been processed, mask the value with CRC24\_FINAL\_VALUE\_MASK to keep only the meaningful 24 bits of the CRC result.

## [◆ ](#ga88d510b3958aee0990ca345aba260bc1)crc32\_c()

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) crc32\_c | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *crc*, |
| --- | --- | --- | --- |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *data*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len*, |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *first\_pkt*, |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *last\_pkt* ) |

`#include <[crc.h](crc_8h.md)>`

Calculate CRC32C (Castagnoli) checksum.

Parameters
:   | [CRC](group__crc.md) | CRC32C checksum that needs to be updated. |
    | --- | --- |
    | data | Pointer to data on which the CRC should be calculated. |
    | len | Data length. |
    | first\_pkt | Whether this is the first packet in the stream. |
    | last\_pkt | Whether this is the last packet in the stream. |

Returns
:   CRC32 value.

## [◆ ](#gafc24e79ed7f978f5bb813091ef318982)crc32\_ieee()

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) crc32\_ieee | ( | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *data*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len* ) |

`#include <[crc.h](crc_8h.md)>`

Generate IEEE conform CRC32 checksum.

Parameters
:   | data | Pointer to data on which the CRC should be calculated. |
    | --- | --- |
    | len | Data length. |

Returns
:   CRC32 value.

## [◆ ](#ga17476d4af14603e322986ef603ce8530)crc32\_ieee\_update()

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) crc32\_ieee\_update | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *crc*, |
| --- | --- | --- | --- |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *data*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len* ) |

`#include <[crc.h](crc_8h.md)>`

Update an IEEE conforming CRC32 checksum.

Parameters
:   | [CRC](group__crc.md) | CRC32 checksum that needs to be updated. |
    | --- | --- |
    | data | Pointer to data on which the CRC should be calculated. |
    | len | Data length. |

Returns
:   CRC32 value.

## [◆ ](#ga4458d7743f9a3394fb68cddcc100e456)crc4()

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) crc4 | ( | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *src*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *polynomial*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *initial\_value*, |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *reversed* ) |

`#include <[crc.h](crc_8h.md)>`

Generic function for computing CRC 4.

Compute CRC 4 by passing in the address of the input, the input length and polynomial used in addition to the initial value. The input buffer must be aligned to a whole byte. It is guaranteed that 4 most significant bits of the result will be set to zero.

Parameters
:   | src | Input bytes for the computation |
    | --- | --- |
    | len | Length of the input in bytes |
    | polynomial | The polynomial to use omitting the leading x^4 coefficient |
    | initial\_value | Initial value for the CRC computation |
    | reversed | Should we use reflected/reversed values or not |

Returns
:   The computed CRC4 value

## [◆ ](#ga322365098ec65bde3d55b0c059896668)crc4\_ti()

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) crc4\_ti | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *seed*, |
| --- | --- | --- | --- |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *src*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len* ) |

`#include <[crc.h](crc_8h.md)>`

Compute the CRC-4 checksum of a buffer.

Used by the TMAG5170 sensor. Uses 0x03 as the polynomial with no reflection. 4 most significant bits of the CRC result will be set to zero.

Parameters
:   | seed | Value to seed the CRC with |
    | --- | --- |
    | src | Input bytes for the computation |
    | len | Length of the input in bytes |

Returns
:   The computed CRC4 value

## [◆ ](#ga1169005fd900b2787035044eeea38af1)crc7\_be()

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) crc7\_be | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *seed*, |
| --- | --- | --- | --- |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *src*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len* ) |

`#include <[crc.h](crc_8h.md)>`

Compute the CRC-7 checksum of a buffer.

See JESD84-A441. Used by the MMC protocol. Uses 0x09 as the polynomial with no reflection. The CRC is left justified, so bit 7 of the result is bit 6 of the CRC.

Parameters
:   | seed | Value to seed the CRC with |
    | --- | --- |
    | src | Input bytes for the computation |
    | len | Length of the input in bytes |

Returns
:   The computed CRC7 value

## [◆ ](#gaa614e73ee7484ca0424fa7d14a54bbb6)crc8()

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) crc8 | ( | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *src*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *polynomial*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *initial\_value*, |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *reversed* ) |

`#include <[crc.h](crc_8h.md)>`

Generic function for computing CRC 8.

Compute CRC 8 by passing in the address of the input, the input length and polynomial used in addition to the initial value.

Parameters
:   | src | Input bytes for the computation |
    | --- | --- |
    | len | Length of the input in bytes |
    | polynomial | The polynomial to use omitting the leading x^8 coefficient |
    | initial\_value | Initial value for the CRC computation |
    | reversed | Should we use reflected/reversed values or not |

Returns
:   The computed CRC8 value

## [◆ ](#ga9a925de71cd0255a22c769dc4b130da5)crc8\_ccitt()

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) crc8\_ccitt | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *initial\_value*, |
| --- | --- | --- | --- |
|  |  | const void \* | *buf*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len* ) |

`#include <[crc.h](crc_8h.md)>`

Compute CCITT variant of CRC 8.

Normal CCITT variant of CRC 8 is using 0x07.

Parameters
:   | initial\_value | Initial value for the CRC computation |
    | --- | --- |
    | buf | Input bytes for the computation |
    | len | Length of the input in bytes |

Returns
:   The computed CRC8 value

## [◆ ](#ga7a8f4387a2d0163165557446d018f041)crc8\_rohc()

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) crc8\_rohc | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *initial\_value*, |
| --- | --- | --- | --- |
|  |  | const void \* | *buf*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len* ) |

`#include <[crc.h](crc_8h.md)>`

Compute ROHC variant of CRC 8.

ROHC (Robust Header Compression) variant of CRC 8. Uses 0x07 as the polynomial with reflection.

Parameters
:   | initial\_value | Initial value for the CRC computation |
    | --- | --- |
    | buf | Input bytes for the computation |
    | len | Length of the input in bytes |

Returns
:   The computed CRC8 value

## [◆ ](#ga5d7f493210e56fb18b8199c9d8a17f33)crc\_by\_type()

| | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) crc\_by\_type | ( | enum [crc\_type](#gabc40e4ffd6da1175eb8ee8573a527edd) | *type*, | | --- | --- | --- | --- | |  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *src*, | |  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len*, | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *seed*, | |  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *poly*, | |  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *reflect*, | |  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *first*, | |  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *last* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[crc.h](crc_8h.md)>`

Compute a CRC checksum, in a generic way.

This is a dispatch function that calls the individual CRC routine determined by `type`.

For 7, 8, 16 and 24-bit CRCs, the relevant `seed` and `poly` values should be passed in via the least-significant byte(s).

Similarly, for 7, 8, 16 and 24-bit CRCs, the relevant result is stored in the least-significant byte(s) of the returned value.

Parameters
:   | type | CRC algorithm to use. |
    | --- | --- |
    | src | Input bytes for the computation |
    | len | Length of the input in bytes |
    | seed | Value to seed the CRC with |
    | poly | The polynomial to use omitting the leading coefficient |
    | reflect | Should we use reflected/reversed values or not |
    | first | Whether this is the first packet in the stream. |
    | last | Whether this is the last packet in the stream. |

Returns
:   [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) the computed CRC value

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

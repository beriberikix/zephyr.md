---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/wifi__utils_8h_source.html
original_path: doxygen/html/wifi__utils_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

wifi\_utils.h

[Go to the documentation of this file.](wifi__utils_8h.md)

1/\*

2 \* Copyright (c) 2023 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

11

12#ifndef ZEPHYR\_INCLUDE\_NET\_WIFI\_UTILS\_H\_

13#define ZEPHYR\_INCLUDE\_NET\_WIFI\_UTILS\_H\_

14

15#ifdef \_\_cplusplus

16extern "C" {

17#endif

18

23

30

[ 31](group__wifi__mgmt.md#ga1104c3c97b460f9f3e15a7a9c56e80af)#define WIFI\_UTILS\_MAX\_BAND\_STR\_LEN 3

[ 32](group__wifi__mgmt.md#gaacc3c661affda7b376a4024efd645f0b)#define WIFI\_UTILS\_MAX\_CHAN\_STR\_LEN 4

33

[ 56](group__wifi__mgmt.md#ga4c91cd7dff0fd9e5402970f3222dc20d)int [wifi\_utils\_parse\_scan\_bands](group__wifi__mgmt.md#ga4c91cd7dff0fd9e5402970f3222dc20d)(char \*scan\_bands\_str, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*band\_map);

57

58

[ 69](group__wifi__mgmt.md#ga471a96d3fb6d610a591508b52d4c05a4)int [wifi\_utils\_parse\_scan\_ssids](group__wifi__mgmt.md#ga471a96d3fb6d610a591508b52d4c05a4)(char \*scan\_ssids\_str,

70 const char \*ssids[],

71 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) num\_ssids);

72

73

[ 102](group__wifi__mgmt.md#gaba9f3117bcef9da1efc1841d3bd9adfd)int [wifi\_utils\_parse\_scan\_chan](group__wifi__mgmt.md#gaba9f3117bcef9da1efc1841d3bd9adfd)(char \*scan\_chan\_str,

103 struct [wifi\_band\_channel](structwifi__band__channel.md) \*chan,

104 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) max\_channels);

105

106

[ 116](group__wifi__mgmt.md#gaf1872d0ed2efd3737a36dcc0ab13f18e)bool [wifi\_utils\_validate\_chan](group__wifi__mgmt.md#gaf1872d0ed2efd3737a36dcc0ab13f18e)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) band,

117 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) chan);

118

[ 127](group__wifi__mgmt.md#gaf408ba9f75354d3eca735b4804fdf199)bool [wifi\_utils\_validate\_chan\_2g](group__wifi__mgmt.md#gaf408ba9f75354d3eca735b4804fdf199)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) chan);

128

[ 137](group__wifi__mgmt.md#gae013eee6d6b74126c29d6ca7b2036310)bool [wifi\_utils\_validate\_chan\_5g](group__wifi__mgmt.md#gae013eee6d6b74126c29d6ca7b2036310)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) chan);

138

[ 147](group__wifi__mgmt.md#ga2606742e23f48da5ca1660aeac47888b)bool [wifi\_utils\_validate\_chan\_6g](group__wifi__mgmt.md#ga2606742e23f48da5ca1660aeac47888b)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) chan);

148

152

156

157#ifdef \_\_cplusplus

158}

159#endif

160#endif /\* ZEPHYR\_INCLUDE\_NET\_WIFI\_UTILS\_H\_ \*/

[wifi\_utils\_validate\_chan\_6g](group__wifi__mgmt.md#ga2606742e23f48da5ca1660aeac47888b)

bool wifi\_utils\_validate\_chan\_6g(uint16\_t chan)

Validate a channel against the 6 GHz band.

[wifi\_utils\_parse\_scan\_ssids](group__wifi__mgmt.md#ga471a96d3fb6d610a591508b52d4c05a4)

int wifi\_utils\_parse\_scan\_ssids(char \*scan\_ssids\_str, const char \*ssids[], uint8\_t num\_ssids)

Append a string containing an SSID to an array of SSID strings.

[wifi\_utils\_parse\_scan\_bands](group__wifi__mgmt.md#ga4c91cd7dff0fd9e5402970f3222dc20d)

int wifi\_utils\_parse\_scan\_bands(char \*scan\_bands\_str, uint8\_t \*band\_map)

Convert a band specification string to a bitmap representing the bands.

[wifi\_utils\_parse\_scan\_chan](group__wifi__mgmt.md#gaba9f3117bcef9da1efc1841d3bd9adfd)

int wifi\_utils\_parse\_scan\_chan(char \*scan\_chan\_str, struct wifi\_band\_channel \*chan, uint8\_t max\_channels)

Convert a string containing a specification of scan channels to an array.

[wifi\_utils\_validate\_chan\_5g](group__wifi__mgmt.md#gae013eee6d6b74126c29d6ca7b2036310)

bool wifi\_utils\_validate\_chan\_5g(uint16\_t chan)

Validate a channel against the 5 GHz band.

[wifi\_utils\_validate\_chan](group__wifi__mgmt.md#gaf1872d0ed2efd3737a36dcc0ab13f18e)

bool wifi\_utils\_validate\_chan(uint8\_t band, uint16\_t chan)

Validate a channel against a band.

[wifi\_utils\_validate\_chan\_2g](group__wifi__mgmt.md#gaf408ba9f75354d3eca735b4804fdf199)

bool wifi\_utils\_validate\_chan\_2g(uint16\_t chan)

Validate a channel against the 2.4 GHz band.

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[wifi\_band\_channel](structwifi__band__channel.md)

Wi-Fi structure to uniquely identify a band-channel pair.

**Definition** wifi\_mgmt.h:257

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [wifi\_utils.h](wifi__utils_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

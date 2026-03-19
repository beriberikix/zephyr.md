---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/wifi__credentials_8h.html
original_path: doxygen/html/wifi__credentials_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

wifi\_credentials.h File Reference

`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`  
`#include <[zephyr/net/wifi.h](wifi_8h_source.md)>`  
`#include <[zephyr/kernel.h](kernel_8h_source.md)>`

[Go to the source code of this file.](wifi__credentials_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [wifi\_credentials\_header](structwifi__credentials__header.md) |
|  | Wi-Fi credentials entry header. [More...](structwifi__credentials__header.md#details) |
| struct | [wifi\_credentials\_personal](structwifi__credentials__personal.md) |
|  | Wi-Fi Personal credentials entry. [More...](structwifi__credentials__personal.md#details) |
| struct | [wifi\_credentials\_enterprise](structwifi__credentials__enterprise.md) |
|  | Wi-Fi Enterprise credentials entry. [More...](structwifi__credentials__enterprise.md#details) |

| Macros | |
| --- | --- |
| #define | [WIFI\_CREDENTIALS\_FLAG\_BSSID](group__wifi__credentials.md#ga656bc737cf1bceffc1cf85d06419cec9)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| #define | [WIFI\_CREDENTIALS\_FLAG\_FAVORITE](group__wifi__credentials.md#ga34c10ac642daf7ee05c1b940c01f8932)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| #define | [WIFI\_CREDENTIALS\_FLAG\_2\_4GHz](group__wifi__credentials.md#ga179a3abf6a1a44b0bee0d2a9736ece0c)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| #define | [WIFI\_CREDENTIALS\_FLAG\_5GHz](group__wifi__credentials.md#ga22d0707e4e4d2fd082563f7c1ebf5308)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| #define | [WIFI\_CREDENTIALS\_FLAG\_MFP\_REQUIRED](group__wifi__credentials.md#gab9a8dd24857d6ddb22ae96096a3ee75c)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| #define | [WIFI\_CREDENTIALS\_FLAG\_MFP\_DISABLED](group__wifi__credentials.md#ga973e4e6faafa8f8b946d3164b1daf95d)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
| #define | [WIFI\_CREDENTIALS\_MAX\_PASSWORD\_LEN](group__wifi__credentials.md#gaf9d3ffe6c9120a7fbc248c3ee66f42fa)   [MAX](group__sys-util.md#gafa99ec4acc4ecb2dc3c2d05da15d0e3f)([WIFI\_PSK\_MAX\_LEN](group__wifi__mgmt.md#gad7c3b99c974b342935180a28fdc5ddfc), CONFIG\_WIFI\_CREDENTIALS\_SAE\_PASSWORD\_LENGTH) |

| Typedefs | |
| --- | --- |
| typedef void(\* | [wifi\_credentials\_ssid\_cb](group__wifi__credentials.md#ga30c9333f10e8e8d03f268fb5c9a69562)) (void \*cb\_arg, const char \*ssid, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) ssid\_len) |
|  | Callback type for wifi\_credentials\_for\_each\_ssid. |

| Functions | |
| --- | --- |
| int | [wifi\_credentials\_get\_by\_ssid\_personal](group__wifi__credentials.md#ga548522fbc6b5fdcff4585c34f3565c82) (const char \*ssid, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) ssid\_len, enum [wifi\_security\_type](group__wifi__mgmt.md#gadde31a04fa25ed805115c6b31854cd9c) \*type, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*bssid\_buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) bssid\_buf\_len, char \*password\_buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) password\_buf\_len, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*password\_len, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*channel, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*timeout) |
|  | Get credentials for given SSID. |
| int | [wifi\_credentials\_set\_personal](group__wifi__credentials.md#ga28b13d11cca692921252e98788552957) (const char \*ssid, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) ssid\_len, enum [wifi\_security\_type](group__wifi__mgmt.md#gadde31a04fa25ed805115c6b31854cd9c) type, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*bssid, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) bssid\_len, const char \*password, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) password\_len, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) channel, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) timeout) |
|  | Set credentials for given SSID. |
| int | [wifi\_credentials\_get\_by\_ssid\_personal\_struct](group__wifi__credentials.md#ga3d83001e713206ec07f94996137537d5) (const char \*ssid, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) ssid\_len, struct [wifi\_credentials\_personal](structwifi__credentials__personal.md) \*buf) |
|  | Get credentials for given SSID by struct. |
| int | [wifi\_credentials\_set\_personal\_struct](group__wifi__credentials.md#ga1b5525c7a6a7ca312236a2c674d94055) (const struct [wifi\_credentials\_personal](structwifi__credentials__personal.md) \*creds) |
|  | Set credentials for given SSID by struct. |
| int | [wifi\_credentials\_delete\_by\_ssid](group__wifi__credentials.md#ga644d29db8091512a977f8e27b245975e) (const char \*ssid, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) ssid\_len) |
|  | Delete credentials for given SSID. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [wifi\_credentials\_is\_empty](group__wifi__credentials.md#ga467ef5e15a637c33cb1926a3548ffb9e) (void) |
|  | Check if credentials storage is empty. |
| int | [wifi\_credentials\_delete\_all](group__wifi__credentials.md#gade76c60899e42fc2af5f7e93143c21ad) (void) |
|  | Deletes all stored Wi-Fi credentials. |
| void | [wifi\_credentials\_for\_each\_ssid](group__wifi__credentials.md#ga3a5b20d07afc52cc452a9c55998ebcf7) ([wifi\_credentials\_ssid\_cb](group__wifi__credentials.md#ga30c9333f10e8e8d03f268fb5c9a69562) cb, void \*cb\_arg) |
|  | Call callback for each registered SSID. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [wifi\_credentials.h](wifi__credentials_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

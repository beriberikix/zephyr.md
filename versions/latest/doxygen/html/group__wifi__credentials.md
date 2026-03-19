---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__wifi__credentials.html
original_path: doxygen/html/group__wifi__credentials.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Wi-Fi credentials library

[Connectivity](group__connectivity.md) » [Networking](group__networking.md)

Library that provides a way to store and load Wi-Fi credentials.
[More...](#details)

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
| #define | [WIFI\_CREDENTIALS\_FLAG\_BSSID](#ga656bc737cf1bceffc1cf85d06419cec9)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| #define | [WIFI\_CREDENTIALS\_FLAG\_FAVORITE](#ga34c10ac642daf7ee05c1b940c01f8932)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| #define | [WIFI\_CREDENTIALS\_FLAG\_2\_4GHz](#ga179a3abf6a1a44b0bee0d2a9736ece0c)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| #define | [WIFI\_CREDENTIALS\_FLAG\_5GHz](#ga22d0707e4e4d2fd082563f7c1ebf5308)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| #define | [WIFI\_CREDENTIALS\_FLAG\_MFP\_REQUIRED](#gab9a8dd24857d6ddb22ae96096a3ee75c)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| #define | [WIFI\_CREDENTIALS\_FLAG\_MFP\_DISABLED](#ga973e4e6faafa8f8b946d3164b1daf95d)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
| #define | [WIFI\_CREDENTIALS\_MAX\_PASSWORD\_LEN](#gaf9d3ffe6c9120a7fbc248c3ee66f42fa)   [MAX](group__sys-util.md#gafa99ec4acc4ecb2dc3c2d05da15d0e3f)([WIFI\_PSK\_MAX\_LEN](group__wifi__mgmt.md#gad7c3b99c974b342935180a28fdc5ddfc), CONFIG\_WIFI\_CREDENTIALS\_SAE\_PASSWORD\_LENGTH) |

| Typedefs | |
| --- | --- |
| typedef void(\* | [wifi\_credentials\_ssid\_cb](#ga30c9333f10e8e8d03f268fb5c9a69562)) (void \*cb\_arg, const char \*ssid, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) ssid\_len) |
|  | Callback type for wifi\_credentials\_for\_each\_ssid. |

| Functions | |
| --- | --- |
| int | [wifi\_credentials\_get\_by\_ssid\_personal](#ga548522fbc6b5fdcff4585c34f3565c82) (const char \*ssid, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) ssid\_len, enum [wifi\_security\_type](group__wifi__mgmt.md#gadde31a04fa25ed805115c6b31854cd9c) \*type, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*bssid\_buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) bssid\_buf\_len, char \*password\_buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) password\_buf\_len, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*password\_len, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*[flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*channel, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*timeout) |
|  | Get credentials for given SSID. |
| int | [wifi\_credentials\_set\_personal](#ga28b13d11cca692921252e98788552957) (const char \*ssid, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) ssid\_len, enum [wifi\_security\_type](group__wifi__mgmt.md#gadde31a04fa25ed805115c6b31854cd9c) type, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*bssid, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) bssid\_len, const char \*password, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) password\_len, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9), [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) channel, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) timeout) |
|  | Set credentials for given SSID. |
| int | [wifi\_credentials\_get\_by\_ssid\_personal\_struct](#ga3d83001e713206ec07f94996137537d5) (const char \*ssid, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) ssid\_len, struct [wifi\_credentials\_personal](structwifi__credentials__personal.md) \*buf) |
|  | Get credentials for given SSID by struct. |
| int | [wifi\_credentials\_set\_personal\_struct](#ga1b5525c7a6a7ca312236a2c674d94055) (const struct [wifi\_credentials\_personal](structwifi__credentials__personal.md) \*creds) |
|  | Set credentials for given SSID by struct. |
| int | [wifi\_credentials\_delete\_by\_ssid](#ga644d29db8091512a977f8e27b245975e) (const char \*ssid, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) ssid\_len) |
|  | Delete credentials for given SSID. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [wifi\_credentials\_is\_empty](#ga467ef5e15a637c33cb1926a3548ffb9e) (void) |
|  | Check if credentials storage is empty. |
| int | [wifi\_credentials\_delete\_all](#gade76c60899e42fc2af5f7e93143c21ad) (void) |
|  | Deletes all stored Wi-Fi credentials. |
| void | [wifi\_credentials\_for\_each\_ssid](#ga3a5b20d07afc52cc452a9c55998ebcf7) ([wifi\_credentials\_ssid\_cb](#ga30c9333f10e8e8d03f268fb5c9a69562) cb, void \*cb\_arg) |
|  | Call callback for each registered SSID. |

## Detailed Description

Library that provides a way to store and load Wi-Fi credentials.

Since
:   4.0

Version
:   0.1.0

## Macro Definition Documentation

## [◆ ](#ga179a3abf6a1a44b0bee0d2a9736ece0c)WIFI\_CREDENTIALS\_FLAG\_2\_4GHz

| #define WIFI\_CREDENTIALS\_FLAG\_2\_4GHz   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(2) |
| --- |

`#include <[wifi_credentials.h](wifi__credentials_8h.md)>`

## [◆ ](#ga22d0707e4e4d2fd082563f7c1ebf5308)WIFI\_CREDENTIALS\_FLAG\_5GHz

| #define WIFI\_CREDENTIALS\_FLAG\_5GHz   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(3) |
| --- |

`#include <[wifi_credentials.h](wifi__credentials_8h.md)>`

## [◆ ](#ga656bc737cf1bceffc1cf85d06419cec9)WIFI\_CREDENTIALS\_FLAG\_BSSID

| #define WIFI\_CREDENTIALS\_FLAG\_BSSID   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0) |
| --- |

`#include <[wifi_credentials.h](wifi__credentials_8h.md)>`

## [◆ ](#ga34c10ac642daf7ee05c1b940c01f8932)WIFI\_CREDENTIALS\_FLAG\_FAVORITE

| #define WIFI\_CREDENTIALS\_FLAG\_FAVORITE   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1) |
| --- |

`#include <[wifi_credentials.h](wifi__credentials_8h.md)>`

## [◆ ](#ga973e4e6faafa8f8b946d3164b1daf95d)WIFI\_CREDENTIALS\_FLAG\_MFP\_DISABLED

| #define WIFI\_CREDENTIALS\_FLAG\_MFP\_DISABLED   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(5) |
| --- |

`#include <[wifi_credentials.h](wifi__credentials_8h.md)>`

## [◆ ](#gab9a8dd24857d6ddb22ae96096a3ee75c)WIFI\_CREDENTIALS\_FLAG\_MFP\_REQUIRED

| #define WIFI\_CREDENTIALS\_FLAG\_MFP\_REQUIRED   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(4) |
| --- |

`#include <[wifi_credentials.h](wifi__credentials_8h.md)>`

## [◆ ](#gaf9d3ffe6c9120a7fbc248c3ee66f42fa)WIFI\_CREDENTIALS\_MAX\_PASSWORD\_LEN

| #define WIFI\_CREDENTIALS\_MAX\_PASSWORD\_LEN   [MAX](group__sys-util.md#gafa99ec4acc4ecb2dc3c2d05da15d0e3f)([WIFI\_PSK\_MAX\_LEN](group__wifi__mgmt.md#gad7c3b99c974b342935180a28fdc5ddfc), CONFIG\_WIFI\_CREDENTIALS\_SAE\_PASSWORD\_LENGTH) |
| --- |

`#include <[wifi_credentials.h](wifi__credentials_8h.md)>`

## Typedef Documentation

## [◆ ](#ga30c9333f10e8e8d03f268fb5c9a69562)wifi\_credentials\_ssid\_cb

| typedef void(\* wifi\_credentials\_ssid\_cb) (void \*cb\_arg, const char \*ssid, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) ssid\_len) |
| --- |

`#include <[wifi_credentials.h](wifi__credentials_8h.md)>`

Callback type for wifi\_credentials\_for\_each\_ssid.

Parameters
:   | [in] | cb\_arg | arguments for the callback function. Appropriate cb\_arg is transferred by wifi\_credentials\_for\_each\_ssid. |
    | --- | --- | --- |
    | [in] | ssid | SSID |
    | [in] | ssid\_len | length of SSID |

## Function Documentation

## [◆ ](#gade76c60899e42fc2af5f7e93143c21ad)wifi\_credentials\_delete\_all()

| int wifi\_credentials\_delete\_all | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[wifi_credentials.h](wifi__credentials_8h.md)>`

Deletes all stored Wi-Fi credentials.

This function deletes all Wi-Fi credentials that have been stored in the system. It is typically used when you want to clear all saved networks.

Returns
:   0 on successful, otherwise a negative error code

## [◆ ](#ga644d29db8091512a977f8e27b245975e)wifi\_credentials\_delete\_by\_ssid()

| int wifi\_credentials\_delete\_by\_ssid | ( | const char \* | *ssid*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *ssid\_len* ) |

`#include <[wifi_credentials.h](wifi__credentials_8h.md)>`

Delete credentials for given SSID.

Parameters
:   | [in] | ssid | SSID to look for |
    | --- | --- | --- |
    | [in] | ssid\_len | length of SSID |

Returns
:   -ENOENT if No network with this SSID was found.
:   0 on success, otherwise a negative error code

## [◆ ](#ga3a5b20d07afc52cc452a9c55998ebcf7)wifi\_credentials\_for\_each\_ssid()

| void wifi\_credentials\_for\_each\_ssid | ( | [wifi\_credentials\_ssid\_cb](#ga30c9333f10e8e8d03f268fb5c9a69562) | *cb*, |
| --- | --- | --- | --- |
|  |  | void \* | *cb\_arg* ) |

`#include <[wifi_credentials.h](wifi__credentials_8h.md)>`

Call callback for each registered SSID.

Parameters
:   | cb | callback |
    | --- | --- |
    | cb\_arg | argument for callback function |

## [◆ ](#ga548522fbc6b5fdcff4585c34f3565c82)wifi\_credentials\_get\_by\_ssid\_personal()

| int wifi\_credentials\_get\_by\_ssid\_personal | ( | const char \* | *ssid*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *ssid\_len*, |
|  |  | enum [wifi\_security\_type](group__wifi__mgmt.md#gadde31a04fa25ed805115c6b31854cd9c) \* | *type*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *bssid\_buf*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *bssid\_buf\_len*, |
|  |  | char \* | *password\_buf*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *password\_buf\_len*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \* | *password\_len*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \* | *flags*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *channel*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \* | *timeout* ) |

`#include <[wifi_credentials.h](wifi__credentials_8h.md)>`

Get credentials for given SSID.

Parameters
:   | [in] | ssid | SSID to look for |
    | --- | --- | --- |
    | [in] | ssid\_len | length of SSID |
    | [out] | type | Wi-Fi security type |
    | [out] | bssid\_buf | buffer to store BSSID if it was fixed |
    | [in] | bssid\_buf\_len | length of bssid\_buf |
    | [out] | password\_buf | buffer to store password |
    | [in] | password\_buf\_len | length of password\_buf |
    | [out] | password\_len | length of password |
    | [out] | [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) | flags |
    | [out] | channel | channel |
    | [out] | timeout | timeout |

Returns
:   0 Success.
:   -ENOENT No network with this SSID was found.
:   -EINVAL A required buffer was NULL or invalid SSID length.
:   -EPROTO The network with this SSID is not a personal network.

## [◆ ](#ga3d83001e713206ec07f94996137537d5)wifi\_credentials\_get\_by\_ssid\_personal\_struct()

| int wifi\_credentials\_get\_by\_ssid\_personal\_struct | ( | const char \* | *ssid*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *ssid\_len*, |
|  |  | struct [wifi\_credentials\_personal](structwifi__credentials__personal.md) \* | *buf* ) |

`#include <[wifi_credentials.h](wifi__credentials_8h.md)>`

Get credentials for given SSID by struct.

Parameters
:   | [in] | ssid | SSID to look for |
    | --- | --- | --- |
    | [in] | ssid\_len | length of SSID |
    | [out] | buf | credentials Pointer to struct where credentials are stored |

Returns
:   0 Success.
:   -ENOENT No network with this SSID was found.
:   -EINVAL A required buffer was NULL or too small.
:   -EPROTO The network with this SSID is not a personal network.

## [◆ ](#ga467ef5e15a637c33cb1926a3548ffb9e)wifi\_credentials\_is\_empty()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) wifi\_credentials\_is\_empty | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[wifi_credentials.h](wifi__credentials_8h.md)>`

Check if credentials storage is empty.

Returns
:   true if credential storage is empty, otherwise false

## [◆ ](#ga28b13d11cca692921252e98788552957)wifi\_credentials\_set\_personal()

| int wifi\_credentials\_set\_personal | ( | const char \* | *ssid*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *ssid\_len*, |
|  |  | enum [wifi\_security\_type](group__wifi__mgmt.md#gadde31a04fa25ed805115c6b31854cd9c) | *type*, |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *bssid*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *bssid\_len*, |
|  |  | const char \* | *password*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *password\_len*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *flags*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *channel*, |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *timeout* ) |

`#include <[wifi_credentials.h](wifi__credentials_8h.md)>`

Set credentials for given SSID.

Parameters
:   | [in] | ssid | SSID to look for |
    | --- | --- | --- |
    | [in] | ssid\_len | length of SSID |
    | [in] | type | Wi-Fi security type |
    | [in] | bssid | BSSID (may be NULL) |
    | [in] | bssid\_len | length of BSSID buffer (either 0 or WIFI\_MAC\_ADDR\_LEN) |
    | [in] | password | password |
    | [in] | password\_len | length of password |
    | [in] | [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) | flags |
    | [in] | channel | Channel |
    | [in] | timeout | Timeout |

Returns
:   0 Success. Credentials are stored in persistent storage.
:   -EINVAL A required buffer was NULL or security type is not supported.
:   -ENOTSUP Security type is not supported.
:   -ENOBUFS All slots are already taken.

## [◆ ](#ga1b5525c7a6a7ca312236a2c674d94055)wifi\_credentials\_set\_personal\_struct()

| int wifi\_credentials\_set\_personal\_struct | ( | const struct [wifi\_credentials\_personal](structwifi__credentials__personal.md) \* | *creds* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[wifi_credentials.h](wifi__credentials_8h.md)>`

Set credentials for given SSID by struct.

Parameters
:   | [in] | creds | credentials Pointer to struct from which credentials are loaded |
    | --- | --- | --- |

Returns
:   0 Success.
:   -ENOENT No network with this SSID was found.
:   -EINVAL A required buffer was NULL or incorrect size.
:   -ENOBUFS All slots are already taken.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

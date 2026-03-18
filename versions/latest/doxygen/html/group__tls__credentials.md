---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__tls__credentials.html
original_path: doxygen/html/group__tls__credentials.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

TLS credentials management

[Connectivity](group__connectivity.md) » [Networking](group__networking.md)

TLS credentials management.
[More...](#details)

| Typedefs | |
| --- | --- |
| typedef int | [sec\_tag\_t](#gaadfe9694309e473f7be74ed98dfb36d3) |
|  | Secure tag, a reference to TLS credential. |

| Enumerations | |
| --- | --- |
| enum | [tls\_credential\_type](#ga3a754894d0162634b59d60e319f37cd5) {     [TLS\_CREDENTIAL\_NONE](#gga3a754894d0162634b59d60e319f37cd5a7009a9f266011529e64ec4e4c6692315) , [TLS\_CREDENTIAL\_CA\_CERTIFICATE](#gga3a754894d0162634b59d60e319f37cd5adcf949c1422f4d3b38795ae40d2321d5) , [TLS\_CREDENTIAL\_SERVER\_CERTIFICATE](#gga3a754894d0162634b59d60e319f37cd5a541cc34b6fd5af911e633154e54f52f4) , [TLS\_CREDENTIAL\_PRIVATE\_KEY](#gga3a754894d0162634b59d60e319f37cd5a406e8bb1f992af5a72921f47b140840e) ,     [TLS\_CREDENTIAL\_PSK](#gga3a754894d0162634b59d60e319f37cd5accc6ad916ee6c6badafcc4c23e2a47df) , [TLS\_CREDENTIAL\_PSK\_ID](#gga3a754894d0162634b59d60e319f37cd5a1edcd43ba510558e4b1315e1bb86560d)   } |
|  | TLS credential types. [More...](#ga3a754894d0162634b59d60e319f37cd5) |

| Functions | |
| --- | --- |
| int | [tls\_credential\_add](#ga640ff6dd3eb4d5017feaab6fab2bb2f7) ([sec\_tag\_t](#gaadfe9694309e473f7be74ed98dfb36d3) tag, enum [tls\_credential\_type](#ga3a754894d0162634b59d60e319f37cd5) type, const void \*cred, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) credlen) |
|  | Add a TLS credential. |
| int | [tls\_credential\_get](#gac3ac4ca887faf6c1f2ae60c6a08f8795) ([sec\_tag\_t](#gaadfe9694309e473f7be74ed98dfb36d3) tag, enum [tls\_credential\_type](#ga3a754894d0162634b59d60e319f37cd5) type, void \*cred, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*credlen) |
|  | Get a TLS credential. |
| int | [tls\_credential\_delete](#ga9d8b47a7a2675fb3b3c6ee346e925aca) ([sec\_tag\_t](#gaadfe9694309e473f7be74ed98dfb36d3) tag, enum [tls\_credential\_type](#ga3a754894d0162634b59d60e319f37cd5) type) |
|  | Delete a TLS credential. |

## Detailed Description

TLS credentials management.

## Typedef Documentation

## [◆ ](#gaadfe9694309e473f7be74ed98dfb36d3)sec\_tag\_t

| typedef int [sec\_tag\_t](#gaadfe9694309e473f7be74ed98dfb36d3) |
| --- |

`#include <[tls_credentials.h](tls__credentials_8h.md)>`

Secure tag, a reference to TLS credential.

Secure tag can be used to reference credential after it was registered in the system.

Note
:   Some TLS credentials come in pairs:

    - TLS\_CREDENTIAL\_SERVER\_CERTIFICATE with TLS\_CREDENTIAL\_PRIVATE\_KEY,
    - TLS\_CREDENTIAL\_PSK with TLS\_CREDENTIAL\_PSK\_ID. Such pairs of credentials must be assigned the same secure tag to be correctly handled in the system.
:   Negative values are reserved for internal use.

## Enumeration Type Documentation

## [◆ ](#ga3a754894d0162634b59d60e319f37cd5)tls\_credential\_type

| enum [tls\_credential\_type](#ga3a754894d0162634b59d60e319f37cd5) |
| --- |

`#include <[tls_credentials.h](tls__credentials_8h.md)>`

TLS credential types.

| Enumerator | |
| --- | --- |
| TLS\_CREDENTIAL\_NONE | Unspecified credential. |
| TLS\_CREDENTIAL\_CA\_CERTIFICATE | A trusted CA certificate.  Use this to authenticate remote servers. Used with certificate-based ciphersuites. |
| TLS\_CREDENTIAL\_SERVER\_CERTIFICATE | A public server certificate.  Use this to register your own server certificate. Should be registered together with a corresponding private key. Used with certificate-based ciphersuites. |
| TLS\_CREDENTIAL\_PRIVATE\_KEY | Private key.  Should be registered together with a corresponding public certificate. Used with certificate-based ciphersuites. |
| TLS\_CREDENTIAL\_PSK | Pre-shared key.  Should be registered together with a corresponding PSK identity. Used with PSK-based ciphersuites. |
| TLS\_CREDENTIAL\_PSK\_ID | Pre-shared key identity.  Should be registered together with a corresponding PSK. Used with PSK-based ciphersuites. |

## Function Documentation

## [◆ ](#ga640ff6dd3eb4d5017feaab6fab2bb2f7)tls\_credential\_add()

| int tls\_credential\_add | ( | [sec\_tag\_t](#gaadfe9694309e473f7be74ed98dfb36d3) | *tag*, |
| --- | --- | --- | --- |
|  |  | enum [tls\_credential\_type](#ga3a754894d0162634b59d60e319f37cd5) | *type*, |
|  |  | const void \* | *cred*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *credlen* ) |

`#include <[tls_credentials.h](tls__credentials_8h.md)>`

Add a TLS credential.

This function adds a TLS credential, that can be used by TLS/DTLS for authentication.

Parameters
:   | tag | A security tag that credential will be referenced with. |
    | --- | --- |
    | type | A TLS/DTLS credential type. |
    | cred | A TLS/DTLS credential. |
    | credlen | A TLS/DTLS credential length. |

Return values
:   | 0 | TLS credential successfully added. |
    | --- | --- |
    | -EACCES | Access to the TLS credential subsystem was denied. |
    | -ENOMEM | Not enough memory to add new TLS credential. |
    | -EEXIST | TLS credential of specific tag and type already exists. |

## [◆ ](#ga9d8b47a7a2675fb3b3c6ee346e925aca)tls\_credential\_delete()

| int tls\_credential\_delete | ( | [sec\_tag\_t](#gaadfe9694309e473f7be74ed98dfb36d3) | *tag*, |
| --- | --- | --- | --- |
|  |  | enum [tls\_credential\_type](#ga3a754894d0162634b59d60e319f37cd5) | *type* ) |

`#include <[tls_credentials.h](tls__credentials_8h.md)>`

Delete a TLS credential.

This function removes a TLS credential, referenced by `tag` secure tag of `type`.

Parameters
:   | tag | A security tag corresponding to removed credential. |
    | --- | --- |
    | type | A TLS/DTLS credential type of removed credential. |

Return values
:   | 0 | TLS credential successfully deleted. |
    | --- | --- |
    | -EACCES | Access to the TLS credential subsystem was denied. |
    | -ENOENT | Requested TLS credential was not found. |

## [◆ ](#gac3ac4ca887faf6c1f2ae60c6a08f8795)tls\_credential\_get()

| int tls\_credential\_get | ( | [sec\_tag\_t](#gaadfe9694309e473f7be74ed98dfb36d3) | *tag*, |
| --- | --- | --- | --- |
|  |  | enum [tls\_credential\_type](#ga3a754894d0162634b59d60e319f37cd5) | *type*, |
|  |  | void \* | *cred*, |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \* | *credlen* ) |

`#include <[tls_credentials.h](tls__credentials_8h.md)>`

Get a TLS credential.

This function gets an already registered TLS credential, referenced by `tag` secure tag of `type`.

Parameters
:   | tag | A security tag of requested credential. |
    | --- | --- |
    | type | A TLS/DTLS credential type of requested credential. |
    | cred | A buffer for TLS/DTLS credential. |
    | credlen | A buffer size on input. TLS/DTLS credential length on output. |

Return values
:   | 0 | TLS credential successfully obtained. |
    | --- | --- |
    | -EACCES | Access to the TLS credential subsystem was denied. |
    | -ENOENT | Requested TLS credential was not found. |
    | -EFBIG | Requested TLS credential does not fit in the buffer provided. |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

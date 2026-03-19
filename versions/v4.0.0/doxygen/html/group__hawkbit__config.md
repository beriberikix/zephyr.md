---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__hawkbit__config.html
original_path: doxygen/html/group__hawkbit__config.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

hawkBit configuration API

[Third-party](group__third__party.md) » [hawkBit Firmware Over-the-Air](group__hawkbit.md)

hawkBit configuration API.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [hawkbit\_runtime\_config](structhawkbit__runtime__config.md) |
|  | hawkBit configuration structure. [More...](structhawkbit__runtime__config.md#details) |

| Functions | |
| --- | --- |
| int | [hawkbit\_set\_config](#ga5e6a1e2e49b75a44a9f13f059ed7d3f6) (struct [hawkbit\_runtime\_config](structhawkbit__runtime__config.md) \*config) |
|  | Set the hawkBit server configuration settings. |
| struct [hawkbit\_runtime\_config](structhawkbit__runtime__config.md) | [hawkbit\_get\_config](#gaae46014585251b53afe726d42475d739) (void) |
|  | Get the hawkBit server configuration settings. |
| static int | [hawkbit\_set\_server\_addr](#gaa49efdafe94e1d36a537aff962df41d5) (char \*addr\_str) |
|  | Set the hawkBit server address. |
| static int | [hawkbit\_set\_server\_port](#ga78ef6a168132940040ad04498f0b462d) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) port) |
|  | Set the hawkBit server port. |
| static int | [hawkbit\_set\_ddi\_security\_token](#gaa2799669246cc817bb8e294a8fbfb3d2) (char \*token) |
|  | Set the hawkBit security token. |
| static int | [hawkbit\_set\_tls\_tag](#ga5c73e9ba4dd9788e22fdb11f1f2b81ee) ([sec\_tag\_t](group__tls__credentials.md#gaadfe9694309e473f7be74ed98dfb36d3) tag) |
|  | Set the hawkBit TLS tag. |
| static char \* | [hawkbit\_get\_server\_addr](#gacbbaed38e2ace7d8dcc78e40b286b5e9) (void) |
|  | Get the hawkBit server address. |
| static [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [hawkbit\_get\_server\_port](#ga3674fc406aa20fe4770ff0c729817b7c) (void) |
|  | Get the hawkBit server port. |
| static char \* | [hawkbit\_get\_ddi\_security\_token](#gadc4aea2dac4915a434a10e6e055f54f7) (void) |
|  | Get the hawkBit security token. |
| static [sec\_tag\_t](group__tls__credentials.md#gaadfe9694309e473f7be74ed98dfb36d3) | [hawkbit\_get\_tls\_tag](#ga694e5f4fbcae451eb90a019f6d1f3b81) (void) |
|  | Get the hawkBit TLS tag. |
| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) | [hawkbit\_get\_action\_id](#ga0ca5f633e902137ecda068ab312d52db) (void) |
|  | Get the hawkBit action id. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [hawkbit\_get\_poll\_interval](#ga46c56cee1a89abd81a328ef3f91648bb) (void) |
|  | Get the hawkBit poll interval. |

## Detailed Description

hawkBit configuration API.

## Function Documentation

## [◆ ](#ga0ca5f633e902137ecda068ab312d52db)hawkbit\_get\_action\_id()

| [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) hawkbit\_get\_action\_id | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[config.h](config_8h.md)>`

Get the hawkBit action id.

Returns
:   Action id.

## [◆ ](#gaae46014585251b53afe726d42475d739)hawkbit\_get\_config()

| struct [hawkbit\_runtime\_config](structhawkbit__runtime__config.md) hawkbit\_get\_config | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[config.h](config_8h.md)>`

Get the hawkBit server configuration settings.

Returns
:   Configuration settings.

## [◆ ](#gadc4aea2dac4915a434a10e6e055f54f7)hawkbit\_get\_ddi\_security\_token()

| | char \* hawkbit\_get\_ddi\_security\_token | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[config.h](config_8h.md)>`

Get the hawkBit security token.

Returns
:   Security token.

## [◆ ](#ga46c56cee1a89abd81a328ef3f91648bb)hawkbit\_get\_poll\_interval()

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) hawkbit\_get\_poll\_interval | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[config.h](config_8h.md)>`

Get the hawkBit poll interval.

Returns
:   Poll interval.

## [◆ ](#gacbbaed38e2ace7d8dcc78e40b286b5e9)hawkbit\_get\_server\_addr()

| | char \* hawkbit\_get\_server\_addr | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[config.h](config_8h.md)>`

Get the hawkBit server address.

Returns
:   Server address.

## [◆ ](#ga3674fc406aa20fe4770ff0c729817b7c)hawkbit\_get\_server\_port()

| | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) hawkbit\_get\_server\_port | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[config.h](config_8h.md)>`

Get the hawkBit server port.

Returns
:   Server port.

## [◆ ](#ga694e5f4fbcae451eb90a019f6d1f3b81)hawkbit\_get\_tls\_tag()

| | [sec\_tag\_t](group__tls__credentials.md#gaadfe9694309e473f7be74ed98dfb36d3) hawkbit\_get\_tls\_tag | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[config.h](config_8h.md)>`

Get the hawkBit TLS tag.

Returns
:   TLS tag.

## [◆ ](#ga5e6a1e2e49b75a44a9f13f059ed7d3f6)hawkbit\_set\_config()

| int hawkbit\_set\_config | ( | struct [hawkbit\_runtime\_config](structhawkbit__runtime__config.md) \* | *config* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[config.h](config_8h.md)>`

Set the hawkBit server configuration settings.

Parameters
:   | config | Configuration settings to set. |
    | --- | --- |

Return values
:   | 0 | on success. |
    | --- | --- |
    | -EAGAIN | if probe is currently running. |

## [◆ ](#gaa2799669246cc817bb8e294a8fbfb3d2)hawkbit\_set\_ddi\_security\_token()

| | int hawkbit\_set\_ddi\_security\_token | ( | char \* | *token* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[config.h](config_8h.md)>`

Set the hawkBit security token.

Parameters
:   | token | Security token to set. |
    | --- | --- |

Return values
:   | 0 | on success. |
    | --- | --- |
    | -EAGAIN | if probe is currently running. |

## [◆ ](#gaa49efdafe94e1d36a537aff962df41d5)hawkbit\_set\_server\_addr()

| | int hawkbit\_set\_server\_addr | ( | char \* | *addr\_str* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[config.h](config_8h.md)>`

Set the hawkBit server address.

Parameters
:   | addr\_str | Server address to set. |
    | --- | --- |

Return values
:   | 0 | on success. |
    | --- | --- |
    | -EAGAIN | if probe is currently running. |

## [◆ ](#ga78ef6a168132940040ad04498f0b462d)hawkbit\_set\_server\_port()

| | int hawkbit\_set\_server\_port | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *port* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[config.h](config_8h.md)>`

Set the hawkBit server port.

Parameters
:   | port | Server port to set. |
    | --- | --- |

Return values
:   | 0 | on success. |
    | --- | --- |
    | -EAGAIN | if probe is currently running. |

## [◆ ](#ga5c73e9ba4dd9788e22fdb11f1f2b81ee)hawkbit\_set\_tls\_tag()

| | int hawkbit\_set\_tls\_tag | ( | [sec\_tag\_t](group__tls__credentials.md#gaadfe9694309e473f7be74ed98dfb36d3) | *tag* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[config.h](config_8h.md)>`

Set the hawkBit TLS tag.

Parameters
:   | tag | TLS tag to set. |
    | --- | --- |

Return values
:   | 0 | on success. |
    | --- | --- |
    | -EAGAIN | if probe is currently running. |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__modem__ubx.html
original_path: doxygen/html/group__modem__ubx.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Modem Ubx

[Connectivity](group__connectivity.md) » [Modem APIs](group__modem.md)

Modem Ubx.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [ubx\_frame](structubx__frame.md) |
| struct | [modem\_ubx\_script](structmodem__ubx__script.md) |
| struct | [modem\_ubx](structmodem__ubx.md) |
| struct | [modem\_ubx\_config](structmodem__ubx__config.md) |

| Macros | |
| --- | --- |
| #define | [UBX\_FRM\_HEADER\_SZ](#ga703255ca4aee83952007115eb74aba50)   6 |
| #define | [UBX\_FRM\_FOOTER\_SZ](#ga36bcc1dda3daf89377b9cde87f642ecb)   2 |
| #define | [UBX\_FRM\_SZ\_WITHOUT\_PAYLOAD](#ga76c616ef547947b5aed71cf516db69e9)   ([UBX\_FRM\_HEADER\_SZ](#ga703255ca4aee83952007115eb74aba50) + [UBX\_FRM\_FOOTER\_SZ](#ga36bcc1dda3daf89377b9cde87f642ecb)) |
| #define | [UBX\_FRM\_SZ](#ga658ec1be18701eeb8464e36690719ddf)(payload\_size) |
| #define | [UBX\_PREAMBLE\_SYNC\_CHAR\_1](#ga1693f3584605a0197076cba71c79b0df)   0xB5 |
| #define | [UBX\_PREAMBLE\_SYNC\_CHAR\_2](#gad8d6229db563db619d4f0a9f225fb640)   0x62 |
| #define | [UBX\_FRM\_PREAMBLE\_SYNC\_CHAR\_1\_IDX](#ga56b16b79385bffdb4a46f1c09b80eb73)   0 |
| #define | [UBX\_FRM\_PREAMBLE\_SYNC\_CHAR\_2\_IDX](#gaf72f72cd97e07540452342fdd1868dff)   1 |
| #define | [UBX\_FRM\_MSG\_CLASS\_IDX](#ga258a47c93ef596c2807aaf0e7b810cd0)   2 |
| #define | [UBX\_FRM\_MSG\_ID\_IDX](#ga9c2428d2a7867b94638aa2108e23ec55)   3 |
| #define | [UBX\_FRM\_PAYLOAD\_SZ\_L\_IDX](#ga500d87a31bc1a34cb50997b0d754bf91)   4 |
| #define | [UBX\_FRM\_PAYLOAD\_SZ\_H\_IDX](#gaab0afee791670adfa80410bad0147482)   5 |
| #define | [UBX\_FRM\_PAYLOAD\_IDX](#ga0fbb8dfbf14547637c9f5dd4ed9e9762)   6 |
| #define | [UBX\_FRM\_CHECKSUM\_START\_IDX](#gac5f7efa1d5c4bc4b7d9e48a41ad412a2)   2 |
| #define | [UBX\_FRM\_CHECKSUM\_STOP\_IDX](#gab29f0a6e9d33f39c57b598a75695146f)(frame\_len) |
| #define | [UBX\_PAYLOAD\_SZ\_MAX](#ga9c66cd27732153c56d0872339bc3deae)   256 |
| #define | [UBX\_FRM\_SZ\_MAX](#gae3aeb2a4570fce67fda95961335ee30c)   [UBX\_FRM\_SZ](#ga658ec1be18701eeb8464e36690719ddf)([UBX\_PAYLOAD\_SZ\_MAX](#ga9c66cd27732153c56d0872339bc3deae)) |

| Functions | |
| --- | --- |
| int | [modem\_ubx\_attach](#ga4e459f955e34c9059702c3d7f9794948) (struct [modem\_ubx](structmodem__ubx.md) \*ubx, struct modem\_pipe \*pipe) |
|  | Attach pipe to Modem Ubx. |
| void | [modem\_ubx\_release](#ga68210f4afd5880c532d82fd0bac1d933) (struct [modem\_ubx](structmodem__ubx.md) \*ubx) |
|  | Release pipe from Modem Ubx instance. |
| int | [modem\_ubx\_init](#gaf49363fb4decb4656566b508a061212f) (struct [modem\_ubx](structmodem__ubx.md) \*ubx, const struct [modem\_ubx\_config](structmodem__ubx__config.md) \*config) |
|  | Initialize Modem Ubx instance. |
| int | [modem\_ubx\_run\_script](#ga25319c784f0293c25c38b494cf9d2a53) (struct [modem\_ubx](structmodem__ubx.md) \*ubx, const struct [modem\_ubx\_script](structmodem__ubx__script.md) \*script) |
|  | Writes the ubx frame in script.request and reads back its response (if available). |
| int | [modem\_ubx\_create\_frame](#ga5d6b36f127836c5b06cde37f098c8775) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[ubx\_frame](structubx__frame.md), [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) ubx\_frame\_size, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) msg\_cls, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) msg\_id, const void \*payload, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) payload\_size) |
|  | Initialize ubx frame. |

## Detailed Description

Modem Ubx.

## Macro Definition Documentation

## [◆ ](#gac5f7efa1d5c4bc4b7d9e48a41ad412a2)UBX\_FRM\_CHECKSUM\_START\_IDX

| #define UBX\_FRM\_CHECKSUM\_START\_IDX   2 |
| --- |

`#include <[ubx.h](ubx_8h.md)>`

## [◆ ](#gab29f0a6e9d33f39c57b598a75695146f)UBX\_FRM\_CHECKSUM\_STOP\_IDX

| #define UBX\_FRM\_CHECKSUM\_STOP\_IDX | ( |  | *frame\_len* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ubx.h](ubx_8h.md)>`

**Value:**

(frame\_len - 2)

## [◆ ](#ga36bcc1dda3daf89377b9cde87f642ecb)UBX\_FRM\_FOOTER\_SZ

| #define UBX\_FRM\_FOOTER\_SZ   2 |
| --- |

`#include <[ubx.h](ubx_8h.md)>`

## [◆ ](#ga703255ca4aee83952007115eb74aba50)UBX\_FRM\_HEADER\_SZ

| #define UBX\_FRM\_HEADER\_SZ   6 |
| --- |

`#include <[ubx.h](ubx_8h.md)>`

## [◆ ](#ga258a47c93ef596c2807aaf0e7b810cd0)UBX\_FRM\_MSG\_CLASS\_IDX

| #define UBX\_FRM\_MSG\_CLASS\_IDX   2 |
| --- |

`#include <[ubx.h](ubx_8h.md)>`

## [◆ ](#ga9c2428d2a7867b94638aa2108e23ec55)UBX\_FRM\_MSG\_ID\_IDX

| #define UBX\_FRM\_MSG\_ID\_IDX   3 |
| --- |

`#include <[ubx.h](ubx_8h.md)>`

## [◆ ](#ga0fbb8dfbf14547637c9f5dd4ed9e9762)UBX\_FRM\_PAYLOAD\_IDX

| #define UBX\_FRM\_PAYLOAD\_IDX   6 |
| --- |

`#include <[ubx.h](ubx_8h.md)>`

## [◆ ](#gaab0afee791670adfa80410bad0147482)UBX\_FRM\_PAYLOAD\_SZ\_H\_IDX

| #define UBX\_FRM\_PAYLOAD\_SZ\_H\_IDX   5 |
| --- |

`#include <[ubx.h](ubx_8h.md)>`

## [◆ ](#ga500d87a31bc1a34cb50997b0d754bf91)UBX\_FRM\_PAYLOAD\_SZ\_L\_IDX

| #define UBX\_FRM\_PAYLOAD\_SZ\_L\_IDX   4 |
| --- |

`#include <[ubx.h](ubx_8h.md)>`

## [◆ ](#ga56b16b79385bffdb4a46f1c09b80eb73)UBX\_FRM\_PREAMBLE\_SYNC\_CHAR\_1\_IDX

| #define UBX\_FRM\_PREAMBLE\_SYNC\_CHAR\_1\_IDX   0 |
| --- |

`#include <[ubx.h](ubx_8h.md)>`

## [◆ ](#gaf72f72cd97e07540452342fdd1868dff)UBX\_FRM\_PREAMBLE\_SYNC\_CHAR\_2\_IDX

| #define UBX\_FRM\_PREAMBLE\_SYNC\_CHAR\_2\_IDX   1 |
| --- |

`#include <[ubx.h](ubx_8h.md)>`

## [◆ ](#ga658ec1be18701eeb8464e36690719ddf)UBX\_FRM\_SZ

| #define UBX\_FRM\_SZ | ( |  | *payload\_size* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ubx.h](ubx_8h.md)>`

**Value:**

(payload\_size + [UBX\_FRM\_SZ\_WITHOUT\_PAYLOAD](#ga76c616ef547947b5aed71cf516db69e9))

[UBX\_FRM\_SZ\_WITHOUT\_PAYLOAD](#ga76c616ef547947b5aed71cf516db69e9)

#define UBX\_FRM\_SZ\_WITHOUT\_PAYLOAD

**Definition** ubx.h:29

## [◆ ](#gae3aeb2a4570fce67fda95961335ee30c)UBX\_FRM\_SZ\_MAX

| #define UBX\_FRM\_SZ\_MAX   [UBX\_FRM\_SZ](#ga658ec1be18701eeb8464e36690719ddf)([UBX\_PAYLOAD\_SZ\_MAX](#ga9c66cd27732153c56d0872339bc3deae)) |
| --- |

`#include <[ubx.h](ubx_8h.md)>`

## [◆ ](#ga76c616ef547947b5aed71cf516db69e9)UBX\_FRM\_SZ\_WITHOUT\_PAYLOAD

| #define UBX\_FRM\_SZ\_WITHOUT\_PAYLOAD   ([UBX\_FRM\_HEADER\_SZ](#ga703255ca4aee83952007115eb74aba50) + [UBX\_FRM\_FOOTER\_SZ](#ga36bcc1dda3daf89377b9cde87f642ecb)) |
| --- |

`#include <[ubx.h](ubx_8h.md)>`

## [◆ ](#ga9c66cd27732153c56d0872339bc3deae)UBX\_PAYLOAD\_SZ\_MAX

| #define UBX\_PAYLOAD\_SZ\_MAX   256 |
| --- |

`#include <[ubx.h](ubx_8h.md)>`

## [◆ ](#ga1693f3584605a0197076cba71c79b0df)UBX\_PREAMBLE\_SYNC\_CHAR\_1

| #define UBX\_PREAMBLE\_SYNC\_CHAR\_1   0xB5 |
| --- |

`#include <[ubx.h](ubx_8h.md)>`

## [◆ ](#gad8d6229db563db619d4f0a9f225fb640)UBX\_PREAMBLE\_SYNC\_CHAR\_2

| #define UBX\_PREAMBLE\_SYNC\_CHAR\_2   0x62 |
| --- |

`#include <[ubx.h](ubx_8h.md)>`

## Function Documentation

## [◆ ](#ga4e459f955e34c9059702c3d7f9794948)modem\_ubx\_attach()

| int modem\_ubx\_attach | ( | struct [modem\_ubx](structmodem__ubx.md) \* | *ubx*, |
| --- | --- | --- | --- |
|  |  | struct modem\_pipe \* | *pipe* ) |

`#include <[ubx.h](ubx_8h.md)>`

Attach pipe to Modem Ubx.

Parameters
:   | ubx | Modem Ubx instance |
    | --- | --- |
    | pipe | Pipe instance to attach Modem Ubx instance to |

Returns
:   0 if successful
:   negative errno code if failure

Note
:   Modem Ubx instance is enabled if successful

## [◆ ](#ga5d6b36f127836c5b06cde37f098c8775)modem\_ubx\_create\_frame()

| int modem\_ubx\_create\_frame | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *ubx\_frame*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *ubx\_frame\_size*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *msg\_cls*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *msg\_id*, |
|  |  | const void \* | *payload*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *payload\_size* ) |

`#include <[ubx.h](ubx_8h.md)>`

Initialize ubx frame.

Parameters
:   | [ubx\_frame](structubx__frame.md) | Ubx frame buffer |
    | --- | --- |
    | ubx\_frame\_size | Ubx frame buffer size |
    | msg\_cls | Message class |
    | msg\_id | Message id |
    | payload | Payload buffer |
    | payload\_size | Payload buffer size |

Returns
:   positive integer denoting the length of the ubx frame created
:   negative errno code if failure

## [◆ ](#gaf49363fb4decb4656566b508a061212f)modem\_ubx\_init()

| int modem\_ubx\_init | ( | struct [modem\_ubx](structmodem__ubx.md) \* | *ubx*, |
| --- | --- | --- | --- |
|  |  | const struct [modem\_ubx\_config](structmodem__ubx__config.md) \* | *config* ) |

`#include <[ubx.h](ubx_8h.md)>`

Initialize Modem Ubx instance.

Parameters
:   | ubx | Modem Ubx instance |
    | --- | --- |
    | config | Configuration which shall be applied to the Modem Ubx instance |

Note
:   Modem Ubx instance must be attached to a pipe instance

## [◆ ](#ga68210f4afd5880c532d82fd0bac1d933)modem\_ubx\_release()

| void modem\_ubx\_release | ( | struct [modem\_ubx](structmodem__ubx.md) \* | *ubx* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ubx.h](ubx_8h.md)>`

Release pipe from Modem Ubx instance.

Parameters
:   | ubx | Modem Ubx instance |
    | --- | --- |

## [◆ ](#ga25319c784f0293c25c38b494cf9d2a53)modem\_ubx\_run\_script()

| int modem\_ubx\_run\_script | ( | struct [modem\_ubx](structmodem__ubx.md) \* | *ubx*, |
| --- | --- | --- | --- |
|  |  | const struct [modem\_ubx\_script](structmodem__ubx__script.md) \* | *script* ) |

`#include <[ubx.h](ubx_8h.md)>`

Writes the ubx frame in script.request and reads back its response (if available).

For each ubx frame sent, the device responds in 0, 1 or both of the following ways:

1. The device sends back a UBX-ACK frame to denote 'acknowledge' and 'not-acknowledge'. Note: the message id of UBX-ACK frame determines whether the device acknowledged. Ex: when we send a UBX-CFG frame, the device responds with a UBX-ACK frame.
2. The device sends back the same frame that we sent to it, with it's payload populated. It's used to get the current configuration corresponding to the frame that we sent. Ex: frame types such as "get" or "poll" ubx frames respond this way. This response (if received) is written to script.response.

This function writes the ubx frame in script.request then reads back it's response. If script.match is not NULL, then every ubx frame received from the device is compared with script.match to check if a match occurred. This could be used to match UBX-ACK frame sent from the device by populating script.match with UBX-ACK that the script expects to receive.

The script terminates when either of the following happens:

1. script.match is successfully received and matched.
2. timeout (denoted by script.timeout) occurs.

   Parameters
   :   | ubx | Modem Ubx instance |
       | --- | --- |
       | script | Script to be executed |

   Note
   :   The length of ubx frame in the script.request should not exceed UBX\_FRM\_SZ\_MAX
   :   Modem Ubx instance must be attached to a pipe instance

   Returns
   :   0 if device acknowledged via UBX-ACK and no "get" response was received
   :   positive integer denoting the length of "get" response that was received
   :   negative errno code if failure

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

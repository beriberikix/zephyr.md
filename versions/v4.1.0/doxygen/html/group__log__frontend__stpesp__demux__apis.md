---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__log__frontend__stpesp__demux__apis.html
original_path: doxygen/html/group__log__frontend__stpesp__demux__apis.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Logging frontend STMESP Demultiplexer API

[Trace and Debug Domain APIs](group__log__frontend__stmesp__apis.md)

| Data Structures | |
| --- | --- |
| struct | [log\_frontend\_stmesp\_demux\_log\_header](structlog__frontend__stmesp__demux__log__header.md) |
|  | Logging message header. [More...](structlog__frontend__stmesp__demux__log__header.md#details) |
| union | [log\_frontend\_stmesp\_demux\_header](unionlog__frontend__stmesp__demux__header.md) |
|  | Union for writing raw data to the logging message header. [More...](unionlog__frontend__stmesp__demux__header.md#details) |
| struct | [log\_frontend\_stmesp\_demux\_packet\_generic](structlog__frontend__stmesp__demux__packet__generic.md) |
|  | Generic STP demux packet. [More...](structlog__frontend__stmesp__demux__packet__generic.md#details) |
| struct | [log\_frontend\_stmesp\_demux\_log](structlog__frontend__stmesp__demux__log.md) |
|  | Packet with logging message. [More...](structlog__frontend__stmesp__demux__log.md#details) |
| struct | [log\_frontend\_stmesp\_demux\_trace\_point](structlog__frontend__stmesp__demux__trace__point.md) |
|  | Packet with trace point. [More...](structlog__frontend__stmesp__demux__trace__point.md#details) |
| struct | [log\_frontend\_stmesp\_demux\_hw\_event](structlog__frontend__stmesp__demux__hw__event.md) |
|  | Packet with HW event. [More...](structlog__frontend__stmesp__demux__hw__event.md#details) |
| union | [log\_frontend\_stmesp\_demux\_packet](unionlog__frontend__stmesp__demux__packet.md) |
|  | Union of all packet types. [More...](unionlog__frontend__stmesp__demux__packet.md#details) |
| struct | [log\_frontend\_stmesp\_demux\_config](structlog__frontend__stmesp__demux__config.md) |
|  | Demultiplexer configuration. [More...](structlog__frontend__stmesp__demux__config.md#details) |

| Macros | |
| --- | --- |
| #define | [LOG\_FRONTEND\_STMESP\_DEMUX\_MAJOR\_BITS](#ga33581c39a57eca7f96fea9c29386a3e3)   3 |
|  | Bits used to store major index. |
| #define | [LOG\_FRONTEND\_STMESP\_DEMUX\_LEVEL\_BITS](#gaf2b7019394d33a082fec5ab2d2785257)   3 |
|  | Bits used to store severity level. |
| #define | [LOG\_FRONTEND\_STMESP\_DEMUX\_TLENGTH\_BITS](#gaeaf76dcb74836740115c9b6e3fece73b)   16 |
|  | Bits used to store total length. |
| #define | [LOG\_FRONTEND\_STMESP\_DEMUX\_PLENGTH\_BITS](#ga56ad2b8067d56b9ccedefd57ad5aa0c2)   10 |
|  | Bits used to store package length. |
| #define | [LOG\_FRONTEND\_STMESP\_DEMUX\_MAJOR\_MAX](#ga8f23994b914214a2c83d2e9aa63f0cb5)   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)([LOG\_FRONTEND\_STMESP\_DEMUX\_MAJOR\_BITS](#ga33581c39a57eca7f96fea9c29386a3e3)) |
|  | Maximum number of supported majors. |
| #define | [LOG\_FRONTEND\_STMESP\_DEMUX\_TYPE\_LOG](#ga0f6129f8e757a6ef4b02779e57ff58f7)   0 |
|  | Log message type. |
| #define | [LOG\_FRONTEND\_STMESP\_DEMUX\_TYPE\_TRACE\_POINT](#ga7a428120f117a62a5d649f18111364c2)   1 |
|  | Trace point message type. |
| #define | [LOG\_FRONTEND\_STMESP\_DEMUX\_TYPE\_HW\_EVENT](#ga67cbf7c7892b76c7347b229a0452bfa3)   2 |
|  | HW event message type. |

| Functions | |
| --- | --- |
| int | [log\_frontend\_stmesp\_demux\_init](#ga97f9ac1d7b459e9d3d715b5367e29a31) (const struct [log\_frontend\_stmesp\_demux\_config](structlog__frontend__stmesp__demux__config.md) \*config) |
|  | Initialize the demultiplexer. |
| void | [log\_frontend\_stmesp\_demux\_major](#ga8be4ca332fa9145fad72a6b45245a9ff) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) id) |
|  | Indicate major opcode in the STPv2 stream. |
| void | [log\_frontend\_stmesp\_demux\_channel](#ga4f86c0cfb38fa05389462045019a6650) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) id) |
|  | Indicate channel opcode in the STPv2 stream. |
| int | [log\_frontend\_stmesp\_demux\_packet\_start](#gaed29a1869e710cd95c19c48c67a36aa8) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*data, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*ts) |
|  | Indicate detected packet start (DMTS). |
| int | [log\_frontend\_stmesp\_demux\_log0](#ga6a25dd796a8759009e14b5770f7653a9) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) source\_id, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*ts) |
|  | Indicate optimized log message with no arguments. |
| void | [log\_frontend\_stmesp\_demux\_source\_id](#gae5925a640c401cc09dd744945eafd51c) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) source\_id) |
|  | Indicate source ID. |
| void | [log\_frontend\_stmesp\_demux\_timestamp](#ga184cc4d266a010aa094a45aba0fad638) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) ts) |
|  | Indicate timestamp. |
| void | [log\_frontend\_stmesp\_demux\_data](#ga235c0d680cb674b6e99d886497f257d5) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Indicate data. |
| void | [log\_frontend\_stmesp\_demux\_packet\_end](#ga38e05a234824b0adbeca16cb3e21cc75) (void) |
|  | Indicate packet end (Flag). |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [log\_frontend\_stmesp\_demux\_get\_dropped](#gaa624af8e67b4be013f0ec1507d805c34) (void) |
|  | Get number of dropped messages and reset the counter. |
| union [log\_frontend\_stmesp\_demux\_packet](unionlog__frontend__stmesp__demux__packet.md) | [log\_frontend\_stmesp\_demux\_claim](#gaf7b66578311278e6d58312ea239c9c0c) (void) |
|  | Claim packet. |
| void | [log\_frontend\_stmesp\_demux\_free](#gad9c13b59d1e09a240ed35b03b04b1a96) (union [log\_frontend\_stmesp\_demux\_packet](unionlog__frontend__stmesp__demux__packet.md) packet) |
|  | Free previously claimed packet. |
| const char \* | [log\_frontend\_stmesp\_demux\_sname\_get](#ga10621a1e4c5b875650b3ff89b3e97297) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) m\_id, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) s\_id) |
|  | Get source name for a turbo log message. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [log\_frontend\_stmesp\_demux\_is\_idle](#ga1d693b8936666f7b352fd7e25535ac16) (void) |
|  | Check if there are any started but not completed log messages. |
| void | [log\_frontend\_stmesp\_demux\_reset](#ga487c9163e6477a879136350d4c109641) (void) |
|  | Close any opened messages and mark them as invalid. |
| int | [log\_frontend\_stmesp\_demux\_max\_utilization](#ga7be93bc9ad1ecfe37f5af64adf029f39) (void) |
|  | Get maximum buffer utilization. |

## Detailed Description

## Macro Definition Documentation

## [◆ ](#gaf2b7019394d33a082fec5ab2d2785257)LOG\_FRONTEND\_STMESP\_DEMUX\_LEVEL\_BITS

| #define LOG\_FRONTEND\_STMESP\_DEMUX\_LEVEL\_BITS   3 |
| --- |

`#include <[log_frontend_stmesp_demux.h](log__frontend__stmesp__demux_8h.md)>`

Bits used to store severity level.

## [◆ ](#ga33581c39a57eca7f96fea9c29386a3e3)LOG\_FRONTEND\_STMESP\_DEMUX\_MAJOR\_BITS

| #define LOG\_FRONTEND\_STMESP\_DEMUX\_MAJOR\_BITS   3 |
| --- |

`#include <[log_frontend_stmesp_demux.h](log__frontend__stmesp__demux_8h.md)>`

Bits used to store major index.

## [◆ ](#ga8f23994b914214a2c83d2e9aa63f0cb5)LOG\_FRONTEND\_STMESP\_DEMUX\_MAJOR\_MAX

| #define LOG\_FRONTEND\_STMESP\_DEMUX\_MAJOR\_MAX   [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)([LOG\_FRONTEND\_STMESP\_DEMUX\_MAJOR\_BITS](#ga33581c39a57eca7f96fea9c29386a3e3)) |
| --- |

`#include <[log_frontend_stmesp_demux.h](log__frontend__stmesp__demux_8h.md)>`

Maximum number of supported majors.

## [◆ ](#ga56ad2b8067d56b9ccedefd57ad5aa0c2)LOG\_FRONTEND\_STMESP\_DEMUX\_PLENGTH\_BITS

| #define LOG\_FRONTEND\_STMESP\_DEMUX\_PLENGTH\_BITS   10 |
| --- |

`#include <[log_frontend_stmesp_demux.h](log__frontend__stmesp__demux_8h.md)>`

Bits used to store package length.

## [◆ ](#gaeaf76dcb74836740115c9b6e3fece73b)LOG\_FRONTEND\_STMESP\_DEMUX\_TLENGTH\_BITS

| #define LOG\_FRONTEND\_STMESP\_DEMUX\_TLENGTH\_BITS   16 |
| --- |

`#include <[log_frontend_stmesp_demux.h](log__frontend__stmesp__demux_8h.md)>`

Bits used to store total length.

## [◆ ](#ga67cbf7c7892b76c7347b229a0452bfa3)LOG\_FRONTEND\_STMESP\_DEMUX\_TYPE\_HW\_EVENT

| #define LOG\_FRONTEND\_STMESP\_DEMUX\_TYPE\_HW\_EVENT   2 |
| --- |

`#include <[log_frontend_stmesp_demux.h](log__frontend__stmesp__demux_8h.md)>`

HW event message type.

## [◆ ](#ga0f6129f8e757a6ef4b02779e57ff58f7)LOG\_FRONTEND\_STMESP\_DEMUX\_TYPE\_LOG

| #define LOG\_FRONTEND\_STMESP\_DEMUX\_TYPE\_LOG   0 |
| --- |

`#include <[log_frontend_stmesp_demux.h](log__frontend__stmesp__demux_8h.md)>`

Log message type.

## [◆ ](#ga7a428120f117a62a5d649f18111364c2)LOG\_FRONTEND\_STMESP\_DEMUX\_TYPE\_TRACE\_POINT

| #define LOG\_FRONTEND\_STMESP\_DEMUX\_TYPE\_TRACE\_POINT   1 |
| --- |

`#include <[log_frontend_stmesp_demux.h](log__frontend__stmesp__demux_8h.md)>`

Trace point message type.

## Function Documentation

## [◆ ](#ga4f86c0cfb38fa05389462045019a6650)log\_frontend\_stmesp\_demux\_channel()

| void log\_frontend\_stmesp\_demux\_channel | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[log_frontend_stmesp_demux.h](log__frontend__stmesp__demux_8h.md)>`

Indicate channel opcode in the STPv2 stream.

Parameters
:   | id | Channel ID. |
    | --- | --- |

## [◆ ](#gaf7b66578311278e6d58312ea239c9c0c)log\_frontend\_stmesp\_demux\_claim()

| union [log\_frontend\_stmesp\_demux\_packet](unionlog__frontend__stmesp__demux__packet.md) log\_frontend\_stmesp\_demux\_claim | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[log_frontend_stmesp_demux.h](log__frontend__stmesp__demux_8h.md)>`

Claim packet.

Get pointer to the pending packet with logging message. Packet must be freed using [log\_frontend\_stmesp\_demux\_free](#gad9c13b59d1e09a240ed35b03b04b1a96).

Returns
:   Pointer to the packet or NULL.

## [◆ ](#ga235c0d680cb674b6e99d886497f257d5)log\_frontend\_stmesp\_demux\_data()

| void log\_frontend\_stmesp\_demux\_data | ( | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *data*, |
| --- | --- | --- | --- |
|  |  | [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | *len* ) |

`#include <[log_frontend_stmesp_demux.h](log__frontend__stmesp__demux_8h.md)>`

Indicate data.

Parameters
:   | data | Data buffer. |
    | --- | --- |
    | len | Length. |

## [◆ ](#gad9c13b59d1e09a240ed35b03b04b1a96)log\_frontend\_stmesp\_demux\_free()

| void log\_frontend\_stmesp\_demux\_free | ( | union [log\_frontend\_stmesp\_demux\_packet](unionlog__frontend__stmesp__demux__packet.md) | *packet* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[log_frontend_stmesp_demux.h](log__frontend__stmesp__demux_8h.md)>`

Free previously claimed packet.

See [log\_frontend\_stmesp\_demux\_claim](#gaf7b66578311278e6d58312ea239c9c0c).

Parameters
:   | packet | Packet. |
    | --- | --- |

## [◆ ](#gaa624af8e67b4be013f0ec1507d805c34)log\_frontend\_stmesp\_demux\_get\_dropped()

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) log\_frontend\_stmesp\_demux\_get\_dropped | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[log_frontend_stmesp_demux.h](log__frontend__stmesp__demux_8h.md)>`

Get number of dropped messages and reset the counter.

Message can be dropped if there is no room in the packet buffer.

Returns
:   Number of dropped messages.

## [◆ ](#ga97f9ac1d7b459e9d3d715b5367e29a31)log\_frontend\_stmesp\_demux\_init()

| int log\_frontend\_stmesp\_demux\_init | ( | const struct [log\_frontend\_stmesp\_demux\_config](structlog__frontend__stmesp__demux__config.md) \* | *config* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[log_frontend_stmesp_demux.h](log__frontend__stmesp__demux_8h.md)>`

Initialize the demultiplexer.

Parameters
:   | config | Configuration. |
    | --- | --- |

Return values
:   | 0 | on success. |
    | --- | --- |
    | -EINVAL | on invalid configuration. |

## [◆ ](#ga1d693b8936666f7b352fd7e25535ac16)log\_frontend\_stmesp\_demux\_is\_idle()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) log\_frontend\_stmesp\_demux\_is\_idle | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[log_frontend_stmesp_demux.h](log__frontend__stmesp__demux_8h.md)>`

Check if there are any started but not completed log messages.

Return values
:   | True | There is no pending started log message. |
    | --- | --- |
    | False | There is pending message. |

## [◆ ](#ga6a25dd796a8759009e14b5770f7653a9)log\_frontend\_stmesp\_demux\_log0()

| int log\_frontend\_stmesp\_demux\_log0 | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *source\_id*, |
| --- | --- | --- | --- |
|  |  | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \* | *ts* ) |

`#include <[log_frontend_stmesp_demux.h](log__frontend__stmesp__demux_8h.md)>`

Indicate optimized log message with no arguments.

Parameters
:   | source\_id | Source ID. |
    | --- | --- |
    | ts | Timestamp. Can be NULL. |

## [◆ ](#ga8be4ca332fa9145fad72a6b45245a9ff)log\_frontend\_stmesp\_demux\_major()

| void log\_frontend\_stmesp\_demux\_major | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[log_frontend_stmesp_demux.h](log__frontend__stmesp__demux_8h.md)>`

Indicate major opcode in the STPv2 stream.

Parameters
:   | id | Master ID. |
    | --- | --- |

## [◆ ](#ga7be93bc9ad1ecfe37f5af64adf029f39)log\_frontend\_stmesp\_demux\_max\_utilization()

| int log\_frontend\_stmesp\_demux\_max\_utilization | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[log_frontend_stmesp_demux.h](log__frontend__stmesp__demux_8h.md)>`

Get maximum buffer utilization.

Return values
:   | Non-negative | Maximum buffer utilization. |
    | --- | --- |
    | -ENOTSUP | Feature not enabled. |

## [◆ ](#ga38e05a234824b0adbeca16cb3e21cc75)log\_frontend\_stmesp\_demux\_packet\_end()

| void log\_frontend\_stmesp\_demux\_packet\_end | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[log_frontend_stmesp_demux.h](log__frontend__stmesp__demux_8h.md)>`

Indicate packet end (Flag).

## [◆ ](#gaed29a1869e710cd95c19c48c67a36aa8)log\_frontend\_stmesp\_demux\_packet\_start()

| int log\_frontend\_stmesp\_demux\_packet\_start | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \* | *data*, |
| --- | --- | --- | --- |
|  |  | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \* | *ts* ) |

`#include <[log_frontend_stmesp_demux.h](log__frontend__stmesp__demux_8h.md)>`

Indicate detected packet start (DMTS).

Parameters
:   | data | Data. Can be NULL which indicates trace point without data. |
    | --- | --- |
    | ts | Timestamp. Can be NULL. |

## [◆ ](#ga487c9163e6477a879136350d4c109641)log\_frontend\_stmesp\_demux\_reset()

| void log\_frontend\_stmesp\_demux\_reset | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[log_frontend_stmesp_demux.h](log__frontend__stmesp__demux_8h.md)>`

Close any opened messages and mark them as invalid.

## [◆ ](#ga10621a1e4c5b875650b3ff89b3e97297)log\_frontend\_stmesp\_demux\_sname\_get()

| const char \* log\_frontend\_stmesp\_demux\_sname\_get | ( | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | *m\_id*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *s\_id* ) |

`#include <[log_frontend_stmesp_demux.h](log__frontend__stmesp__demux_8h.md)>`

Get source name for a turbo log message.

During a boot cooprocessors (FLPR and PPR) are sending location in memory where their source data is stored. If application core is an owner of those cores it has access to that memory and based on chip ID and source ID it can retrieve the source name.

Parameters
:   | m\_id | Major ID. |
    | --- | --- |
    | s\_id | Source ID. |

Returns
:   Pointer to a string which is a source name or unknown name if source name cannot be retrieved.

## [◆ ](#gae5925a640c401cc09dd744945eafd51c)log\_frontend\_stmesp\_demux\_source\_id()

| void log\_frontend\_stmesp\_demux\_source\_id | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *source\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[log_frontend_stmesp_demux.h](log__frontend__stmesp__demux_8h.md)>`

Indicate source ID.

Parameters
:   | source\_id | Source ID. |
    | --- | --- |

## [◆ ](#ga184cc4d266a010aa094a45aba0fad638)log\_frontend\_stmesp\_demux\_timestamp()

| void log\_frontend\_stmesp\_demux\_timestamp | ( | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *ts* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[log_frontend_stmesp_demux.h](log__frontend__stmesp__demux_8h.md)>`

Indicate timestamp.

Timestamp is separated from packet start because according to STM spec (3.2.2) it is possible that timestamp is assigned to a later packet.

Parameters
:   | ts | Timestamp. |
    | --- | --- |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

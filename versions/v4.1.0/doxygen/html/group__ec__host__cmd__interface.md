---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__ec__host__cmd__interface.html
original_path: doxygen/html/group__ec__host__cmd__interface.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

EC Host Command Interface

[Device Driver APIs](group__io__interfaces.md)

EC Host Command Interface.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [ec\_host\_cmd\_rx\_ctx](structec__host__cmd__rx__ctx.md) |
|  | Context for host command backend and handler to pass rx data. [More...](structec__host__cmd__rx__ctx.md#details) |
| struct | [ec\_host\_cmd\_tx\_buf](structec__host__cmd__tx__buf.md) |
|  | Context for host command backend and handler to pass tx data. [More...](structec__host__cmd__tx__buf.md#details) |
| struct | [ec\_host\_cmd\_backend\_api](structec__host__cmd__backend__api.md) |
| struct | [ec\_host\_cmd](structec__host__cmd.md) |
| struct | [ec\_host\_cmd\_handler\_args](structec__host__cmd__handler__args.md) |
|  | Arguments passed into every installed host command handler. [More...](structec__host__cmd__handler__args.md#details) |
| struct | [ec\_host\_cmd\_handler](structec__host__cmd__handler.md) |
|  | Structure use for statically registering host command handlers. [More...](structec__host__cmd__handler.md#details) |
| struct | [ec\_host\_cmd\_request\_header](structec__host__cmd__request__header.md) |
|  | Header for requests from host to embedded controller. [More...](structec__host__cmd__request__header.md#details) |
| struct | [ec\_host\_cmd\_response\_header](structec__host__cmd__response__header.md) |
|  | Header for responses from embedded controller to host. [More...](structec__host__cmd__response__header.md#details) |

| Macros | |
| --- | --- |
| #define | [EC\_HOST\_CMD\_HANDLER](#gaed5a8c4ba3648ae9e6284502f6a48dc7)(\_id, \_function, \_version\_mask, \_request\_type, \_response\_type) |
|  | Statically define and register a host command handler. |
| #define | [EC\_HOST\_CMD\_HANDLER\_UNBOUND](#ga2dae15d1db72c7c9b5f879284a990e13)(\_id, \_function, \_version\_mask) |
|  | Statically define and register a host command handler without sizes. |

| Typedefs | |
| --- | --- |
| typedef int(\* | [ec\_host\_cmd\_backend\_api\_init](#ga811b9c355942811f0fee22c1fa8a5787)) (const struct [ec\_host\_cmd\_backend](structec__host__cmd__backend.md) \*backend, struct [ec\_host\_cmd\_rx\_ctx](structec__host__cmd__rx__ctx.md) \*rx\_ctx, struct [ec\_host\_cmd\_tx\_buf](structec__host__cmd__tx__buf.md) \*tx) |
|  | Initialize a host command backend. |
| typedef int(\* | [ec\_host\_cmd\_backend\_api\_send](#ga1097b2148a5e7e6bf9f2a67e54dd5ba5)) (const struct [ec\_host\_cmd\_backend](structec__host__cmd__backend.md) \*backend) |
|  | Sends data to the host. |
| typedef void(\* | [ec\_host\_cmd\_user\_cb\_t](#gaa6ea251ee113cc15fd085ef12b76a573)) (const struct [ec\_host\_cmd\_rx\_ctx](structec__host__cmd__rx__ctx.md) \*rx\_ctx, void \*user\_data) |
| typedef enum [ec\_host\_cmd\_status](#ga9b0b87983dcc92ea55ebfa1aecf82a8f)(\* | [ec\_host\_cmd\_in\_progress\_cb\_t](#gacf91301985634f9a12cd80db5e818821)) (void \*user\_data) |
| typedef enum [ec\_host\_cmd\_status](#ga9b0b87983dcc92ea55ebfa1aecf82a8f)(\* | [ec\_host\_cmd\_handler\_cb](#ga027ae23ea11a0ec7711725d1b28125d7)) (struct [ec\_host\_cmd\_handler\_args](structec__host__cmd__handler__args.md) \*args) |

| Enumerations | |
| --- | --- |
| enum | [ec\_host\_cmd\_status](#ga9b0b87983dcc92ea55ebfa1aecf82a8f) {     [EC\_HOST\_CMD\_SUCCESS](#gga9b0b87983dcc92ea55ebfa1aecf82a8fa6a6e394a69d6575caf92646a63195b4e) = 0 , [EC\_HOST\_CMD\_INVALID\_COMMAND](#gga9b0b87983dcc92ea55ebfa1aecf82a8fad43b4a713754d52b77313f2222fe2432) = 1 , [EC\_HOST\_CMD\_ERROR](#gga9b0b87983dcc92ea55ebfa1aecf82a8fa45e8b4169e1a88afcb3be1011f2da201) = 2 , [EC\_HOST\_CMD\_INVALID\_PARAM](#gga9b0b87983dcc92ea55ebfa1aecf82a8fae252c89c64d8ee5d65d7e6cf42c8fe1d) = 3 ,     [EC\_HOST\_CMD\_ACCESS\_DENIED](#gga9b0b87983dcc92ea55ebfa1aecf82a8fad8fef524b7ccf571f7abdf8dec56fb5c) = 4 , [EC\_HOST\_CMD\_INVALID\_RESPONSE](#gga9b0b87983dcc92ea55ebfa1aecf82a8faff7377e35d78c46ae49085488e7e71b9) = 5 , [EC\_HOST\_CMD\_INVALID\_VERSION](#gga9b0b87983dcc92ea55ebfa1aecf82a8fa6b0ab5efe8c76a022787be84b43e1b39) = 6 , [EC\_HOST\_CMD\_INVALID\_CHECKSUM](#gga9b0b87983dcc92ea55ebfa1aecf82a8fa6ba692b3ff01ab6f382e7d5e4a7dd301) = 7 ,     [EC\_HOST\_CMD\_IN\_PROGRESS](#gga9b0b87983dcc92ea55ebfa1aecf82a8fa619eeb03065f2729a69c7f26c90d8c2e) = 8 , [EC\_HOST\_CMD\_UNAVAILABLE](#gga9b0b87983dcc92ea55ebfa1aecf82a8fa75dc8b9ba661e52c48735ea85360e996) = 9 , [EC\_HOST\_CMD\_TIMEOUT](#gga9b0b87983dcc92ea55ebfa1aecf82a8fadeacab16ecc96772c137b65352dddf26) = 10 , [EC\_HOST\_CMD\_OVERFLOW](#gga9b0b87983dcc92ea55ebfa1aecf82a8fae62986949bad505a8be6c46d19b4e443) = 11 ,     [EC\_HOST\_CMD\_INVALID\_HEADER](#gga9b0b87983dcc92ea55ebfa1aecf82a8fa48a29fa396646f39c6d95f28d6ce986b) = 12 , [EC\_HOST\_CMD\_REQUEST\_TRUNCATED](#gga9b0b87983dcc92ea55ebfa1aecf82a8fa35758ca8b95b79a7c1140319164a7c00) = 13 , [EC\_HOST\_CMD\_RESPONSE\_TOO\_BIG](#gga9b0b87983dcc92ea55ebfa1aecf82a8fae6cadca18d937481814ae72023d54ff5) = 14 , [EC\_HOST\_CMD\_BUS\_ERROR](#gga9b0b87983dcc92ea55ebfa1aecf82a8fadeb0f80d5150733aa4f1803ee2b19fd2) = 15 ,     [EC\_HOST\_CMD\_BUSY](#gga9b0b87983dcc92ea55ebfa1aecf82a8fa20b2d8c80da5ba25bb06501eec00afa1) = 16 , [EC\_HOST\_CMD\_INVALID\_HEADER\_VERSION](#gga9b0b87983dcc92ea55ebfa1aecf82a8fa4c242c6a48fdf8991488df445512fcc5) = 17 , [EC\_HOST\_CMD\_INVALID\_HEADER\_CRC](#gga9b0b87983dcc92ea55ebfa1aecf82a8fa9a7bc527e81b60c2af1b3e16d17ac57e) = 18 , [EC\_HOST\_CMD\_INVALID\_DATA\_CRC](#gga9b0b87983dcc92ea55ebfa1aecf82a8fa370917fb952a8ed478260290dc59c985) = 19 ,     [EC\_HOST\_CMD\_DUP\_UNAVAILABLE](#gga9b0b87983dcc92ea55ebfa1aecf82a8fa3897851061e4708d98f2ca385bea1a80) = 20 , [EC\_HOST\_CMD\_MAX](#gga9b0b87983dcc92ea55ebfa1aecf82a8fad202e5ae4fac72a7fb3d1f4a7dff3ba9) = UINT16\_MAX   } |
|  | Host command response codes (16-bit). [More...](#ga9b0b87983dcc92ea55ebfa1aecf82a8f) |
| enum | [ec\_host\_cmd\_log\_level](#ga70cbd55129ef589688c6d2f5999337c9) {     [EC\_HOST\_CMD\_DEBUG\_OFF](#gga70cbd55129ef589688c6d2f5999337c9a7f293daec1f211c20145b25728421d38) , [EC\_HOST\_CMD\_DEBUG\_NORMAL](#gga70cbd55129ef589688c6d2f5999337c9a9b5eaf7f57c8fb8537995ac2cd932c81) , [EC\_HOST\_CMD\_DEBUG\_EVERY](#gga70cbd55129ef589688c6d2f5999337c9a6c10f7c18f897dc5475cd4b6fcf199d6) , [EC\_HOST\_CMD\_DEBUG\_PARAMS](#gga70cbd55129ef589688c6d2f5999337c9a7b4ec42c191d5a4231a2b1551c6e45a1) ,     [EC\_HOST\_CMD\_DEBUG\_MODES](#gga70cbd55129ef589688c6d2f5999337c9a8fe3708b71fbb8e82cc799dc42b7231b)   } |
| enum | [ec\_host\_cmd\_state](#gabf0f1243bf55cb70078f2a9fd0a755ec) { [EC\_HOST\_CMD\_STATE\_DISABLED](#ggabf0f1243bf55cb70078f2a9fd0a755eca394e27c2841c50c94daf273712a3a7af) = 0 , [EC\_HOST\_CMD\_STATE\_RECEIVING](#ggabf0f1243bf55cb70078f2a9fd0a755eca009b14c05655b9ebfdfac70fc77d2e20) , [EC\_HOST\_CMD\_STATE\_PROCESSING](#ggabf0f1243bf55cb70078f2a9fd0a755eca2e0d060db73eba1e4ecf9726868f6ed8) , [EC\_HOST\_CMD\_STATE\_SENDING](#ggabf0f1243bf55cb70078f2a9fd0a755ecac766c64d188e3df91f7ed40a84a9ef46) } |

| Functions | |
| --- | --- |
| struct [ec\_host\_cmd\_backend](structec__host__cmd__backend.md) \* | [ec\_host\_cmd\_backend\_get\_espi](#ga32d7a58724694ab753efbf7f81e8d940) (const struct [device](structdevice.md) \*dev) |
|  | Get the eSPI Host Command backend pointer. |
| struct [ec\_host\_cmd\_backend](structec__host__cmd__backend.md) \* | [ec\_host\_cmd\_backend\_get\_shi\_npcx](#gaa4562dd46503cf8844a546b102ce01e9) (void) |
|  | Get the SHI NPCX Host Command backend pointer. |
| struct [ec\_host\_cmd\_backend](structec__host__cmd__backend.md) \* | [ec\_host\_cmd\_backend\_get\_shi\_ite](#ga892fec4587de508805fdf5ace9dd1050) (void) |
|  | Get the SHI ITE Host Command backend pointer. |
| struct [ec\_host\_cmd\_backend](structec__host__cmd__backend.md) \* | [ec\_host\_cmd\_backend\_get\_uart](#ga558b7690dad9a9a5eb8771fcfeba3b63) (const struct [device](structdevice.md) \*dev) |
|  | Get the UART Host Command backend pointer. |
| struct [ec\_host\_cmd\_backend](structec__host__cmd__backend.md) \* | [ec\_host\_cmd\_backend\_get\_spi](#ga12574d2eff8f07fd36967ccbc7600e1c) (struct [gpio\_dt\_spec](structgpio__dt__spec.md) \*cs) |
|  | Get the SPI Host Command backend pointer. |
| int | [ec\_host\_cmd\_init](#gaab1fdcb0fd13a19447d262d496b8aed9) (struct [ec\_host\_cmd\_backend](structec__host__cmd__backend.md) \*backend) |
|  | Initialize the host command subsystem. |
| int | [ec\_host\_cmd\_send\_response](#ga95f36f8cf2d21ea73bd8a36f3f7303e8) (enum [ec\_host\_cmd\_status](#ga9b0b87983dcc92ea55ebfa1aecf82a8f) status, const struct [ec\_host\_cmd\_handler\_args](structec__host__cmd__handler__args.md) \*args) |
|  | Send the host command response. |
| void | [ec\_host\_cmd\_rx\_notify](#gadbee4a2588abeb6db63f70a90b67a8fb) (void) |
|  | Signal a new host command. |
| void | [ec\_host\_cmd\_set\_user\_cb](#gaaf267a44816e5f856db2092fca681d3e) ([ec\_host\_cmd\_user\_cb\_t](#gaa6ea251ee113cc15fd085ef12b76a573) cb, void \*user\_data) |
|  | Install a user callback for receiving a host command. |
| const struct [ec\_host\_cmd](structec__host__cmd.md) \* | [ec\_host\_cmd\_get\_hc](#gaf3b87533037c4d865641643736904d02) (void) |
|  | Get the main ec host command structure. |
| FUNC\_NORETURN void | [ec\_host\_cmd\_task](#gaaa3dc6c413b9637a3817cf82e138b27a) (void) |
|  | The thread function for Host Command subsystem. |
| int | [ec\_host\_cmd\_add\_suppressed](#ga9f734642958684ca654a3c786b2ceb74) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) cmd\_id) |
|  | Add a suppressed command. |

## Detailed Description

EC Host Command Interface.

Since
:   2.4

Version
:   0.1.0

## Macro Definition Documentation

## [◆ ](#gaed5a8c4ba3648ae9e6284502f6a48dc7)EC\_HOST\_CMD\_HANDLER

| #define EC\_HOST\_CMD\_HANDLER | ( |  | *\_id*, |
| --- | --- | --- | --- |
|  |  |  | *\_function*, |
|  |  |  | *\_version\_mask*, |
|  |  |  | *\_request\_type*, |
|  |  |  | *\_response\_type* ) |

`#include <[ec_host_cmd.h](ec__host__cmd_8h.md)>`

**Value:**

const [STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)([ec\_host\_cmd\_handler](structec__host__cmd__handler.md), \_\_cmd##\_id) = { \

.handler = \_function, \

.id = \_id, \

.version\_mask = \_version\_mask, \

.min\_rqt\_size = sizeof(\_request\_type), \

.min\_rsp\_size = sizeof(\_response\_type), \

}

[STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)

#define STRUCT\_SECTION\_ITERABLE(struct\_type, varname)

Defines a new element for an iterable section.

**Definition** iterable\_sections.h:216

[ec\_host\_cmd\_handler](structec__host__cmd__handler.md)

Structure use for statically registering host command handlers.

**Definition** ec\_host\_cmd.h:145

Statically define and register a host command handler.

Helper macro to statically define and register a host command handler that has a compile-time-fixed sizes for its both request and response structures.

Parameters
:   | \_id | Id of host command to handle request for. |
    | --- | --- |
    | \_function | Name of handler function. |
    | \_version\_mask | The bitfield of all versions that the *\_function* supports. E.g. [BIT(0)](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c "Unsigned integer with bit position n set (signed in assembly language).") corresponds to version 0. |
    | \_request\_type | The datatype of the request parameters for *\_function*. |
    | \_response\_type | The datatype of the response parameters for *\_function*. |

## [◆ ](#ga2dae15d1db72c7c9b5f879284a990e13)EC\_HOST\_CMD\_HANDLER\_UNBOUND

| #define EC\_HOST\_CMD\_HANDLER\_UNBOUND | ( |  | *\_id*, |
| --- | --- | --- | --- |
|  |  |  | *\_function*, |
|  |  |  | *\_version\_mask* ) |

`#include <[ec_host_cmd.h](ec__host__cmd_8h.md)>`

**Value:**

const [STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)([ec\_host\_cmd\_handler](structec__host__cmd__handler.md), \_\_cmd##\_id) = { \

.handler = \_function, \

.id = \_id, \

.version\_mask = \_version\_mask, \

.min\_rqt\_size = 0, \

.min\_rsp\_size = 0, \

}

Statically define and register a host command handler without sizes.

Helper macro to statically define and register a host command handler whose request or response structure size is not known as compile time.

Parameters
:   | \_id | Id of host command to handle request for. |
    | --- | --- |
    | \_function | Name of handler function. |
    | \_version\_mask | The bitfield of all versions that the *\_function* supports. E.g. [BIT(0)](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c "Unsigned integer with bit position n set (signed in assembly language).") corresponds to version 0. |

## Typedef Documentation

## [◆ ](#ga811b9c355942811f0fee22c1fa8a5787)ec\_host\_cmd\_backend\_api\_init

| typedef int(\* ec\_host\_cmd\_backend\_api\_init) (const struct [ec\_host\_cmd\_backend](structec__host__cmd__backend.md) \*backend, struct [ec\_host\_cmd\_rx\_ctx](structec__host__cmd__rx__ctx.md) \*rx\_ctx, struct [ec\_host\_cmd\_tx\_buf](structec__host__cmd__tx__buf.md) \*tx) |
| --- |

`#include <[backend.h](backend_8h.md)>`

Initialize a host command backend.

This routine initializes a host command backend. It includes initialization a device used to communication and setting up buffers. This function is called by the ec\_host\_cmd\_init function.

Parameters
:   | [in] | backend | Pointer to the backend structure for the driver instance. |
    | --- | --- | --- |
    | [in,out] | rx\_ctx | Pointer to the receive context object. These objects are used to receive data from the driver when the host sends data. The buf member can be assigned by the backend. |
    | [in,out] | tx | Pointer to the transmit buffer object. The buf and len\_max members can be assigned by the backend. These objects are used to send data by the backend with the [ec\_host\_cmd\_backend\_api\_send](#ga1097b2148a5e7e6bf9f2a67e54dd5ba5) function. |

Return values
:   | 0 | if successful |
    | --- | --- |

## [◆ ](#ga1097b2148a5e7e6bf9f2a67e54dd5ba5)ec\_host\_cmd\_backend\_api\_send

| typedef int(\* ec\_host\_cmd\_backend\_api\_send) (const struct [ec\_host\_cmd\_backend](structec__host__cmd__backend.md) \*backend) |
| --- |

`#include <[backend.h](backend_8h.md)>`

Sends data to the host.

Sends data from tx buf that was passed via [ec\_host\_cmd\_backend\_api\_init](#ga811b9c355942811f0fee22c1fa8a5787) function.

Parameters
:   | backend | Pointer to the backed to send data. |
    | --- | --- |

Return values
:   | 0 | if successful. |
    | --- | --- |

## [◆ ](#ga027ae23ea11a0ec7711725d1b28125d7)ec\_host\_cmd\_handler\_cb

| typedef enum [ec\_host\_cmd\_status](#ga9b0b87983dcc92ea55ebfa1aecf82a8f)(\* ec\_host\_cmd\_handler\_cb) (struct [ec\_host\_cmd\_handler\_args](structec__host__cmd__handler__args.md) \*args) |
| --- |

`#include <[ec_host_cmd.h](ec__host__cmd_8h.md)>`

## [◆ ](#gacf91301985634f9a12cd80db5e818821)ec\_host\_cmd\_in\_progress\_cb\_t

| typedef enum [ec\_host\_cmd\_status](#ga9b0b87983dcc92ea55ebfa1aecf82a8f)(\* ec\_host\_cmd\_in\_progress\_cb\_t) (void \*user\_data) |
| --- |

`#include <[ec_host_cmd.h](ec__host__cmd_8h.md)>`

## [◆ ](#gaa6ea251ee113cc15fd085ef12b76a573)ec\_host\_cmd\_user\_cb\_t

| typedef void(\* ec\_host\_cmd\_user\_cb\_t) (const struct [ec\_host\_cmd\_rx\_ctx](structec__host__cmd__rx__ctx.md) \*rx\_ctx, void \*user\_data) |
| --- |

`#include <[ec_host_cmd.h](ec__host__cmd_8h.md)>`

## Enumeration Type Documentation

## [◆ ](#ga70cbd55129ef589688c6d2f5999337c9)ec\_host\_cmd\_log\_level

| enum [ec\_host\_cmd\_log\_level](#ga70cbd55129ef589688c6d2f5999337c9) |
| --- |

`#include <[ec_host_cmd.h](ec__host__cmd_8h.md)>`

| Enumerator | |
| --- | --- |
| EC\_HOST\_CMD\_DEBUG\_OFF |  |
| EC\_HOST\_CMD\_DEBUG\_NORMAL |  |
| EC\_HOST\_CMD\_DEBUG\_EVERY |  |
| EC\_HOST\_CMD\_DEBUG\_PARAMS |  |
| EC\_HOST\_CMD\_DEBUG\_MODES |  |

## [◆ ](#gabf0f1243bf55cb70078f2a9fd0a755ec)ec\_host\_cmd\_state

| enum [ec\_host\_cmd\_state](#gabf0f1243bf55cb70078f2a9fd0a755ec) |
| --- |

`#include <[ec_host_cmd.h](ec__host__cmd_8h.md)>`

| Enumerator | |
| --- | --- |
| EC\_HOST\_CMD\_STATE\_DISABLED |  |
| EC\_HOST\_CMD\_STATE\_RECEIVING |  |
| EC\_HOST\_CMD\_STATE\_PROCESSING |  |
| EC\_HOST\_CMD\_STATE\_SENDING |  |

## [◆ ](#ga9b0b87983dcc92ea55ebfa1aecf82a8f)ec\_host\_cmd\_status

| enum [ec\_host\_cmd\_status](#ga9b0b87983dcc92ea55ebfa1aecf82a8f) |
| --- |

`#include <[ec_host_cmd.h](ec__host__cmd_8h.md)>`

Host command response codes (16-bit).

| Enumerator | |
| --- | --- |
| EC\_HOST\_CMD\_SUCCESS | Host command was successful. |
| EC\_HOST\_CMD\_INVALID\_COMMAND | The specified command id is not recognized or supported. |
| EC\_HOST\_CMD\_ERROR | Generic Error. |
| EC\_HOST\_CMD\_INVALID\_PARAM | One of more of the input request parameters is invalid. |
| EC\_HOST\_CMD\_ACCESS\_DENIED | Host command is not permitted. |
| EC\_HOST\_CMD\_INVALID\_RESPONSE | Response was invalid (e.g.  not version 3 of header). |
| EC\_HOST\_CMD\_INVALID\_VERSION | Host command id version unsupported. |
| EC\_HOST\_CMD\_INVALID\_CHECKSUM | Checksum did not match. |
| EC\_HOST\_CMD\_IN\_PROGRESS | A host command is currently being processed. |
| EC\_HOST\_CMD\_UNAVAILABLE | Requested information is currently unavailable. |
| EC\_HOST\_CMD\_TIMEOUT | Timeout during processing. |
| EC\_HOST\_CMD\_OVERFLOW | Data or table overflow. |
| EC\_HOST\_CMD\_INVALID\_HEADER | Header is invalid or unsupported (e.g.  not version 3 of header). |
| EC\_HOST\_CMD\_REQUEST\_TRUNCATED | Did not receive all expected request data. |
| EC\_HOST\_CMD\_RESPONSE\_TOO\_BIG | Response was too big to send within one response packet. |
| EC\_HOST\_CMD\_BUS\_ERROR | Error on underlying communication bus. |
| EC\_HOST\_CMD\_BUSY | System busy.  Should retry later. |
| EC\_HOST\_CMD\_INVALID\_HEADER\_VERSION | Header version invalid. |
| EC\_HOST\_CMD\_INVALID\_HEADER\_CRC | Header CRC invalid. |
| EC\_HOST\_CMD\_INVALID\_DATA\_CRC | Data CRC invalid. |
| EC\_HOST\_CMD\_DUP\_UNAVAILABLE | Can't resend response. |
| EC\_HOST\_CMD\_MAX |  |

## Function Documentation

## [◆ ](#ga9f734642958684ca654a3c786b2ceb74)ec\_host\_cmd\_add\_suppressed()

| int ec\_host\_cmd\_add\_suppressed | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *cmd\_id* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ec_host_cmd.h](ec__host__cmd_8h.md)>`

Add a suppressed command.

Suppressed commands are not logged. Add a command to be suppressed.

Parameters
:   | [in] | cmd\_id | A command id to be suppressed. |
    | --- | --- | --- |

Return values
:   | 0 | if successful, -EIO if exceeded max number of suppressed commands. |
    | --- | --- |

## [◆ ](#ga32d7a58724694ab753efbf7f81e8d940)ec\_host\_cmd\_backend\_get\_espi()

| struct [ec\_host\_cmd\_backend](structec__host__cmd__backend.md) \* ec\_host\_cmd\_backend\_get\_espi | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[backend.h](backend_8h.md)>`

Get the eSPI Host Command backend pointer.

Get the eSPI pointer backend and pass a pointer to eSPI device instance that will be used for the Host Command communication.

Parameters
:   | dev | Pointer to eSPI device instance. |
    | --- | --- |

Return values
:   | The | eSPI backend pointer. |
    | --- | --- |

## [◆ ](#ga892fec4587de508805fdf5ace9dd1050)ec\_host\_cmd\_backend\_get\_shi\_ite()

| struct [ec\_host\_cmd\_backend](structec__host__cmd__backend.md) \* ec\_host\_cmd\_backend\_get\_shi\_ite | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[backend.h](backend_8h.md)>`

Get the SHI ITE Host Command backend pointer.

Return values
:   | the | SHI ITE backend pointer |
    | --- | --- |

## [◆ ](#gaa4562dd46503cf8844a546b102ce01e9)ec\_host\_cmd\_backend\_get\_shi\_npcx()

| struct [ec\_host\_cmd\_backend](structec__host__cmd__backend.md) \* ec\_host\_cmd\_backend\_get\_shi\_npcx | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[backend.h](backend_8h.md)>`

Get the SHI NPCX Host Command backend pointer.

Return values
:   | the | SHI NPCX backend pointer |
    | --- | --- |

## [◆ ](#ga12574d2eff8f07fd36967ccbc7600e1c)ec\_host\_cmd\_backend\_get\_spi()

| struct [ec\_host\_cmd\_backend](structec__host__cmd__backend.md) \* ec\_host\_cmd\_backend\_get\_spi | ( | struct [gpio\_dt\_spec](structgpio__dt__spec.md) \* | *cs* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[backend.h](backend_8h.md)>`

Get the SPI Host Command backend pointer.

Get the SPI pointer backend and pass a chip select pin that will be used for the Host Command communication.

Parameters
:   | cs | Chip select pin.. |
    | --- | --- |

Return values
:   | The | SPI backend pointer. |
    | --- | --- |

## [◆ ](#ga558b7690dad9a9a5eb8771fcfeba3b63)ec\_host\_cmd\_backend\_get\_uart()

| struct [ec\_host\_cmd\_backend](structec__host__cmd__backend.md) \* ec\_host\_cmd\_backend\_get\_uart | ( | const struct [device](structdevice.md) \* | *dev* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[backend.h](backend_8h.md)>`

Get the UART Host Command backend pointer.

Get the UART pointer backend and pass a pointer to UART device instance that will be used for the Host Command communication.

Parameters
:   | dev | Pointer to UART device instance. |
    | --- | --- |

Return values
:   | The | UART backend pointer. |
    | --- | --- |

## [◆ ](#gaf3b87533037c4d865641643736904d02)ec\_host\_cmd\_get\_hc()

| const struct [ec\_host\_cmd](structec__host__cmd.md) \* ec\_host\_cmd\_get\_hc | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ec_host_cmd.h](ec__host__cmd_8h.md)>`

Get the main ec host command structure.

This routine returns a pointer to the main host command structure. It allows the application code to get inside information for any reason e.g. the host command thread id.

Return values
:   | A | pointer to the main host command structure |
    | --- | --- |

## [◆ ](#gaab1fdcb0fd13a19447d262d496b8aed9)ec\_host\_cmd\_init()

| int ec\_host\_cmd\_init | ( | struct [ec\_host\_cmd\_backend](structec__host__cmd__backend.md) \* | *backend* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ec_host_cmd.h](ec__host__cmd_8h.md)>`

Initialize the host command subsystem.

This routine initializes the host command subsystem. It includes initialization of a backend and the handler. When the application configures the zephyr,host-cmd-espi-backend/zephyr,host-cmd-shi-backend/ zephyr,host-cmd-uart-backend chosen node and `CONFIG_EC_HOST_CMD_INITIALIZE_AT_BOOT` is set, the chosen backend automatically calls this routine at `CONFIG_EC_HOST_CMD_INIT_PRIORITY`. Applications that require a run-time selection of the backend must set `CONFIG_EC_HOST_CMD_INITIALIZE_AT_BOOT` to n and must explicitly call this routine.

Parameters
:   | [in] | backend | Pointer to the backend structure to initialize. |
    | --- | --- | --- |

Return values
:   | 0 | if successful |
    | --- | --- |

## [◆ ](#gadbee4a2588abeb6db63f70a90b67a8fb)ec\_host\_cmd\_rx\_notify()

| void ec\_host\_cmd\_rx\_notify | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ec_host_cmd.h](ec__host__cmd_8h.md)>`

Signal a new host command.

Signal that a new host command has been received. The function should be called by a backend after copying data to the rx buffer and setting the length.

## [◆ ](#ga95f36f8cf2d21ea73bd8a36f3f7303e8)ec\_host\_cmd\_send\_response()

| int ec\_host\_cmd\_send\_response | ( | enum [ec\_host\_cmd\_status](#ga9b0b87983dcc92ea55ebfa1aecf82a8f) | *status*, |
| --- | --- | --- | --- |
|  |  | const struct [ec\_host\_cmd\_handler\_args](structec__host__cmd__handler__args.md) \* | *args* ) |

`#include <[ec_host_cmd.h](ec__host__cmd_8h.md)>`

Send the host command response.

This routine sends the host command response. It should be used to send IN\_PROGRESS status or if the host command handler doesn't return e.g. reboot command.

Parameters
:   | [in] | status | Host command status to be sent. |
    | --- | --- | --- |
    | [in] | args | Pointer of a structure passed to the handler. |

Return values
:   | 0 | if successful. |
    | --- | --- |

## [◆ ](#gaaf267a44816e5f856db2092fca681d3e)ec\_host\_cmd\_set\_user\_cb()

| void ec\_host\_cmd\_set\_user\_cb | ( | [ec\_host\_cmd\_user\_cb\_t](#gaa6ea251ee113cc15fd085ef12b76a573) | *cb*, |
| --- | --- | --- | --- |
|  |  | void \* | *user\_data* ) |

`#include <[ec_host_cmd.h](ec__host__cmd_8h.md)>`

Install a user callback for receiving a host command.

It allows installing a custom procedure needed by a user after receiving a command.

Parameters
:   | [in] | cb | A callback to be installed. |
    | --- | --- | --- |
    | [in] | user\_data | User data to be passed to the callback. |

## [◆ ](#gaaa3dc6c413b9637a3817cf82e138b27a)ec\_host\_cmd\_task()

| FUNC\_NORETURN void ec\_host\_cmd\_task | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[ec_host_cmd.h](ec__host__cmd_8h.md)>`

The thread function for Host Command subsystem.

This routine calls the Host Command thread entry function. If `CONFIG_EC_HOST_CMD_DEDICATED_THREAD` is not defined, a new thread is not created, and this function has to be called by application code. It doesn't return.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

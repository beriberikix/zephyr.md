---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/group__modbus.html
original_path: doxygen/html/group__modbus.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

MODBUS

[Device Driver APIs](group__io__interfaces.md)

MODBUS transport protocol API.
[More...](#details)

| Data Structures | |
| --- | --- |
| struct | [modbus\_adu](structmodbus__adu.md) |
|  | Frame struct used internally and for raw ADU support. [More...](structmodbus__adu.md#details) |
| struct | [modbus\_user\_callbacks](structmodbus__user__callbacks.md) |
|  | Modbus Server User Callback structure. [More...](structmodbus__user__callbacks.md#details) |
| struct | [modbus\_serial\_param](structmodbus__serial__param.md) |
|  | Modbus serial line parameter. [More...](structmodbus__serial__param.md#details) |
| struct | [modbus\_server\_param](structmodbus__server__param.md) |
|  | Modbus server parameter. [More...](structmodbus__server__param.md#details) |
| struct | [modbus\_raw\_cb](structmodbus__raw__cb.md) |
| struct | [modbus\_iface\_param](structmodbus__iface__param.md) |
|  | User parameter structure to configure Modbus interface as client or server. [More...](structmodbus__iface__param.md#details) |

| Macros | |
| --- | --- |
| #define | [MODBUS\_MBAP\_LENGTH](#ga1015513d4d3b6621fc18dcfda79116a2)   7 |
|  | Length of MBAP Header. |
| #define | [MODBUS\_MBAP\_AND\_FC\_LENGTH](#gae8a6fcfc117e7c4b2ac32aef90155698)   ([MODBUS\_MBAP\_LENGTH](#ga1015513d4d3b6621fc18dcfda79116a2) + 1) |
|  | Length of MBAP Header plus function code. |
| #define | [MODBUS\_CUSTOM\_FC\_DEFINE](#gaa0acc60971d0f773719431173632fd30)(name, user\_cb, user\_fc, userdata) |
|  | INTERNAL\_HIDDEN. |

| Typedefs | |
| --- | --- |
| typedef int(\* | [modbus\_raw\_cb\_t](#ga6d74be1fffb9d5697fe5708827aa7ef1)) (const int iface, const struct [modbus\_adu](structmodbus__adu.md) \*adu, void \*user\_data) |
|  | ADU raw callback function signature. |
| typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* | [modbus\_custom\_cb\_t](#ga2a7ba41a2fb7f6bf5194c02dcab07ae3)) (const int iface, const struct [modbus\_adu](structmodbus__adu.md) \*const rx\_adu, struct [modbus\_adu](structmodbus__adu.md) \*const tx\_adu, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*const excep\_code, void \*const user\_data) |
|  | Custom function code handler function signature. |

| Enumerations | |
| --- | --- |
| enum | [modbus\_mode](#ga4bd8913e1c77a1e4b19585caa9f77c2e) { [MODBUS\_MODE\_RTU](#gga4bd8913e1c77a1e4b19585caa9f77c2ea52033dc2ef37fc286a590b1f97d946ef) , [MODBUS\_MODE\_ASCII](#gga4bd8913e1c77a1e4b19585caa9f77c2eafdf029741cc1bdecb2cb9baf4f06732a) , [MODBUS\_MODE\_RAW](#gga4bd8913e1c77a1e4b19585caa9f77c2ea4d05b2cfd56ccf15eb1d8c7bb71071ec) } |
|  | Modbus interface mode. [More...](#ga4bd8913e1c77a1e4b19585caa9f77c2e) |

| Functions | |
| --- | --- |
| int | [modbus\_read\_coils](#ga05b118dc87ebe3739cac4e9572104ffb) (const int iface, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) unit\_id, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) start\_addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*const coil\_tbl, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) num\_coils) |
|  | Coil read (FC01). |
| int | [modbus\_read\_dinputs](#ga921fd6036ff1b8a416dc02e30bb6e653) (const int iface, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) unit\_id, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) start\_addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*const di\_tbl, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) num\_di) |
|  | Read discrete inputs (FC02). |
| int | [modbus\_read\_holding\_regs](#ga7d7221b32fbf2395e69e25ef2dbaa036) (const int iface, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) unit\_id, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) start\_addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*const reg\_buf, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) num\_regs) |
|  | Read holding registers (FC03). |
| int | [modbus\_read\_input\_regs](#ga5ff31ca21cf2d1b081d172228d6c2154) (const int iface, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) unit\_id, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) start\_addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*const reg\_buf, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) num\_regs) |
|  | Read input registers (FC04). |
| int | [modbus\_write\_coil](#gaccac4f72b5d66a5a2e6c444dda251c41) (const int iface, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) unit\_id, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) coil\_addr, const [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) coil\_state) |
|  | Write single coil (FC05). |
| int | [modbus\_write\_holding\_reg](#gaf06d2553af8b8e9ab58f54b8b7e2055b) (const int iface, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) unit\_id, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) start\_addr, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) reg\_val) |
|  | Write single holding register (FC06). |
| int | [modbus\_request\_diagnostic](#gac924251f66ca6f357d8b7d90075df210) (const int iface, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) unit\_id, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) sfunc, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) data, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*const data\_out) |
|  | Read diagnostic (FC08). |
| int | [modbus\_write\_coils](#gac0fa22cd0d1fa861fdbc04b65ea60d7e) (const int iface, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) unit\_id, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) start\_addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*const coil\_tbl, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) num\_coils) |
|  | Write coils (FC15). |
| int | [modbus\_write\_holding\_regs](#gadc8273292e0efc8c0d65c00eea7a22c5) (const int iface, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) unit\_id, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) start\_addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*const reg\_buf, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) num\_regs) |
|  | Write holding registers (FC16). |
| int | [modbus\_read\_holding\_regs\_fp](#ga9a8ae6fb4b1aee398f5b19f074d07ea9) (const int iface, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) unit\_id, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) start\_addr, float \*const reg\_buf, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) num\_regs) |
|  | Read floating-point holding registers (FC03). |
| int | [modbus\_write\_holding\_regs\_fp](#ga762da245db3ca4f60fb3aa6c5783c73d) (const int iface, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) unit\_id, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) start\_addr, float \*const reg\_buf, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) num\_regs) |
|  | Write floating-point holding registers (FC16). |
| int | [modbus\_iface\_get\_by\_name](#gaa17880a268d6b3b9553de835c800af27) (const char \*iface\_name) |
|  | Get Modbus interface index according to interface name. |
| int | [modbus\_init\_server](#gae4d34276c467bf54e0849a1098e56f8b) (const int iface, struct [modbus\_iface\_param](structmodbus__iface__param.md) param) |
|  | Configure Modbus Interface as raw ADU server. |
| int | [modbus\_init\_client](#ga943eff819ecf1bc268714783047888ef) (const int iface, struct [modbus\_iface\_param](structmodbus__iface__param.md) param) |
|  | Configure Modbus Interface as raw ADU client. |
| int | [modbus\_disable](#ga32a6319cc51eb5a98dcb58b3231b9d34) (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) iface) |
|  | Disable Modbus Interface. |
| int | [modbus\_raw\_submit\_rx](#ga6d40e9eda6b8ead6d071d4192ffe489b) (const int iface, const struct [modbus\_adu](structmodbus__adu.md) \*adu) |
|  | Submit raw ADU. |
| void | [modbus\_raw\_put\_header](#ga8fdae6a92e27a845296c9d8ce4b8078e) (const struct [modbus\_adu](structmodbus__adu.md) \*adu, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*header) |
|  | Put MBAP header into a buffer. |
| void | [modbus\_raw\_get\_header](#ga333072d3536d7b6f0680ceecc2c5bddf) (struct [modbus\_adu](structmodbus__adu.md) \*adu, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*header) |
|  | Get MBAP header from a buffer. |
| void | [modbus\_raw\_set\_server\_failure](#gad250c40ba13a7d8c9189de17d1fd31aa) (struct [modbus\_adu](structmodbus__adu.md) \*adu) |
|  | Set Server Device Failure exception. |
| int | [modbus\_raw\_backend\_txn](#ga7aa5dfd6e457980e9e9b8a77810ec31e) (const int iface, struct [modbus\_adu](structmodbus__adu.md) \*adu) |
|  | Use interface as backend to send and receive ADU. |
| int | [modbus\_register\_user\_fc](#gacd88a4f35a13cc6864654927296803c4) (const int iface, struct modbus\_custom\_fc \*custom\_fc) |
|  | Register a user-defined function code handler. |

| Modbus exception codes | |
| --- | --- |
| #define | [MODBUS\_EXC\_NONE](#ga12557dda3e72ac45aefee3f9cbb18960)   0 |
|  | No exception. |
| #define | [MODBUS\_EXC\_ILLEGAL\_FC](#ga934994f66a61c0d11d00dd52a748cc78)   1 |
|  | Illegal function code. |
| #define | [MODBUS\_EXC\_ILLEGAL\_DATA\_ADDR](#ga9ab4fc4caaf2e051ae697d44a9fa98e3)   2 |
|  | Illegal data address. |
| #define | [MODBUS\_EXC\_ILLEGAL\_DATA\_VAL](#ga5bcd9c7edd91d59af1453cde2376412f)   3 |
|  | Illegal data value. |
| #define | [MODBUS\_EXC\_SERVER\_DEVICE\_FAILURE](#ga6bcf75ff2d522f1a542caa41b47a5ac8)   4 |
|  | Server device failure. |
| #define | [MODBUS\_EXC\_ACK](#ga9cfec884c72b7fc404d82c16f57e858d)   5 |
|  | Acknowledge. |
| #define | [MODBUS\_EXC\_SERVER\_DEVICE\_BUSY](#ga37f02ccee238e7c8ab33f150b2bcd793)   6 |
|  | Server device busy. |
| #define | [MODBUS\_EXC\_MEM\_PARITY\_ERROR](#gad9b56cf73a31d77cd78d48695ea44659)   8 |
|  | Memory parity error. |
| #define | [MODBUS\_EXC\_GW\_PATH\_UNAVAILABLE](#ga9903d7d283c11a4b8854ef5706b5aaba)   10 |
|  | Gateway path unavailable. |
| #define | [MODBUS\_EXC\_GW\_TARGET\_FAILED\_TO\_RESP](#gae61e3ee73e2288006f3dd2f081b4d1de)   11 |
|  | Gateway target device failed to respond. |

## Detailed Description

MODBUS transport protocol API.

## Macro Definition Documentation

## [◆ ](#gaa0acc60971d0f773719431173632fd30)MODBUS\_CUSTOM\_FC\_DEFINE

| #define MODBUS\_CUSTOM\_FC\_DEFINE | ( |  | *name*, |
| --- | --- | --- | --- |
|  |  |  | *user\_cb*, |
|  |  |  | *user\_fc*, |
|  |  |  | *userdata* ) |

`#include <[modbus.h](modbus_8h.md)>`

**Value:**

static struct modbus\_custom\_fc modbus\_cfg\_##name = { \

.cb = user\_cb, \

.user\_data = userdata, \

.fc = user\_fc, \

.excep\_code = [MODBUS\_EXC\_NONE](#ga12557dda3e72ac45aefee3f9cbb18960), \

}

[MODBUS\_EXC\_NONE](#ga12557dda3e72ac45aefee3f9cbb18960)

#define MODBUS\_EXC\_NONE

No exception.

**Definition** modbus.h:48

INTERNAL\_HIDDEN.

Helper macro for initializing custom function code structs

## [◆ ](#ga9cfec884c72b7fc404d82c16f57e858d)MODBUS\_EXC\_ACK

| #define MODBUS\_EXC\_ACK   5 |
| --- |

`#include <[modbus.h](modbus_8h.md)>`

Acknowledge.

## [◆ ](#ga9903d7d283c11a4b8854ef5706b5aaba)MODBUS\_EXC\_GW\_PATH\_UNAVAILABLE

| #define MODBUS\_EXC\_GW\_PATH\_UNAVAILABLE   10 |
| --- |

`#include <[modbus.h](modbus_8h.md)>`

Gateway path unavailable.

## [◆ ](#gae61e3ee73e2288006f3dd2f081b4d1de)MODBUS\_EXC\_GW\_TARGET\_FAILED\_TO\_RESP

| #define MODBUS\_EXC\_GW\_TARGET\_FAILED\_TO\_RESP   11 |
| --- |

`#include <[modbus.h](modbus_8h.md)>`

Gateway target device failed to respond.

## [◆ ](#ga9ab4fc4caaf2e051ae697d44a9fa98e3)MODBUS\_EXC\_ILLEGAL\_DATA\_ADDR

| #define MODBUS\_EXC\_ILLEGAL\_DATA\_ADDR   2 |
| --- |

`#include <[modbus.h](modbus_8h.md)>`

Illegal data address.

## [◆ ](#ga5bcd9c7edd91d59af1453cde2376412f)MODBUS\_EXC\_ILLEGAL\_DATA\_VAL

| #define MODBUS\_EXC\_ILLEGAL\_DATA\_VAL   3 |
| --- |

`#include <[modbus.h](modbus_8h.md)>`

Illegal data value.

## [◆ ](#ga934994f66a61c0d11d00dd52a748cc78)MODBUS\_EXC\_ILLEGAL\_FC

| #define MODBUS\_EXC\_ILLEGAL\_FC   1 |
| --- |

`#include <[modbus.h](modbus_8h.md)>`

Illegal function code.

## [◆ ](#gad9b56cf73a31d77cd78d48695ea44659)MODBUS\_EXC\_MEM\_PARITY\_ERROR

| #define MODBUS\_EXC\_MEM\_PARITY\_ERROR   8 |
| --- |

`#include <[modbus.h](modbus_8h.md)>`

Memory parity error.

## [◆ ](#ga12557dda3e72ac45aefee3f9cbb18960)MODBUS\_EXC\_NONE

| #define MODBUS\_EXC\_NONE   0 |
| --- |

`#include <[modbus.h](modbus_8h.md)>`

No exception.

## [◆ ](#ga37f02ccee238e7c8ab33f150b2bcd793)MODBUS\_EXC\_SERVER\_DEVICE\_BUSY

| #define MODBUS\_EXC\_SERVER\_DEVICE\_BUSY   6 |
| --- |

`#include <[modbus.h](modbus_8h.md)>`

Server device busy.

## [◆ ](#ga6bcf75ff2d522f1a542caa41b47a5ac8)MODBUS\_EXC\_SERVER\_DEVICE\_FAILURE

| #define MODBUS\_EXC\_SERVER\_DEVICE\_FAILURE   4 |
| --- |

`#include <[modbus.h](modbus_8h.md)>`

Server device failure.

## [◆ ](#gae8a6fcfc117e7c4b2ac32aef90155698)MODBUS\_MBAP\_AND\_FC\_LENGTH

| #define MODBUS\_MBAP\_AND\_FC\_LENGTH   ([MODBUS\_MBAP\_LENGTH](#ga1015513d4d3b6621fc18dcfda79116a2) + 1) |
| --- |

`#include <[modbus.h](modbus_8h.md)>`

Length of MBAP Header plus function code.

## [◆ ](#ga1015513d4d3b6621fc18dcfda79116a2)MODBUS\_MBAP\_LENGTH

| #define MODBUS\_MBAP\_LENGTH   7 |
| --- |

`#include <[modbus.h](modbus_8h.md)>`

Length of MBAP Header.

## Typedef Documentation

## [◆ ](#ga2a7ba41a2fb7f6bf5194c02dcab07ae3)modbus\_custom\_cb\_t

| typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* modbus\_custom\_cb\_t) (const int iface, const struct [modbus\_adu](structmodbus__adu.md) \*const rx\_adu, struct [modbus\_adu](structmodbus__adu.md) \*const tx\_adu, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*const excep\_code, void \*const user\_data) |
| --- |

`#include <[modbus.h](modbus_8h.md)>`

Custom function code handler function signature.

Modbus allows user defined function codes which can be used to extend the base protocol. These callbacks can also be used to implement function codes currently not supported by Zephyr's Modbus subsystem.

If an error occurs during the handling of the request, the handler should signal this by setting excep\_code to a modbus exception code.

User data pointer can be used to pass state between subsequent calls to the handler.

Parameters
:   | iface | Modbus interface index |
    | --- | --- |
    | rx\_adu | Pointer to the received ADU struct |
    | tx\_adu | Pointer to the outgoing ADU struct |
    | excep\_code | Pointer to possible exception code |
    | user\_data | Pointer to user data |

Return values
:   | [true](stdbool_8h.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7) | If response should be sent, false otherwise |
    | --- | --- |

## [◆ ](#ga6d74be1fffb9d5697fe5708827aa7ef1)modbus\_raw\_cb\_t

| typedef int(\* modbus\_raw\_cb\_t) (const int iface, const struct [modbus\_adu](structmodbus__adu.md) \*adu, void \*user\_data) |
| --- |

`#include <[modbus.h](modbus_8h.md)>`

ADU raw callback function signature.

Parameters
:   | iface | Modbus RTU interface index |
    | --- | --- |
    | adu | Pointer to the RAW ADU struct to send |
    | user\_data | Pointer to the user data |

Return values
:   | 0 | If transfer was successful |
    | --- | --- |

## Enumeration Type Documentation

## [◆ ](#ga4bd8913e1c77a1e4b19585caa9f77c2e)modbus\_mode

| enum [modbus\_mode](#ga4bd8913e1c77a1e4b19585caa9f77c2e) |
| --- |

`#include <[modbus.h](modbus_8h.md)>`

Modbus interface mode.

| Enumerator | |
| --- | --- |
| MODBUS\_MODE\_RTU | Modbus over serial line RTU mode. |
| MODBUS\_MODE\_ASCII | Modbus over serial line ASCII mode. |
| MODBUS\_MODE\_RAW | Modbus raw ADU mode. |

## Function Documentation

## [◆ ](#ga32a6319cc51eb5a98dcb58b3231b9d34)modbus\_disable()

| int modbus\_disable | ( | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *iface* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[modbus.h](modbus_8h.md)>`

Disable Modbus Interface.

This function is called to disable Modbus interface.

Parameters
:   | iface | Modbus interface index |
    | --- | --- |

Return values
:   | 0 | If the function was successful |
    | --- | --- |

## [◆ ](#gaa17880a268d6b3b9553de835c800af27)modbus\_iface\_get\_by\_name()

| int modbus\_iface\_get\_by\_name | ( | const char \* | *iface\_name* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[modbus.h](modbus_8h.md)>`

Get Modbus interface index according to interface name.

If there is more than one interface, it can be used to clearly identify interfaces in the application.

Parameters
:   | iface\_name | Modbus interface name |
    | --- | --- |

Return values
:   | Modbus | interface index or negative error value. |
    | --- | --- |

## [◆ ](#ga943eff819ecf1bc268714783047888ef)modbus\_init\_client()

| int modbus\_init\_client | ( | const int | *iface*, |
| --- | --- | --- | --- |
|  |  | struct [modbus\_iface\_param](structmodbus__iface__param.md) | *param* ) |

`#include <[modbus.h](modbus_8h.md)>`

Configure Modbus Interface as raw ADU client.

Parameters
:   | iface | Modbus RTU interface index |
    | --- | --- |
    | param | Configuration parameter of the client interface |

Return values
:   | 0 | If the function was successful |
    | --- | --- |

## [◆ ](#gae4d34276c467bf54e0849a1098e56f8b)modbus\_init\_server()

| int modbus\_init\_server | ( | const int | *iface*, |
| --- | --- | --- | --- |
|  |  | struct [modbus\_iface\_param](structmodbus__iface__param.md) | *param* ) |

`#include <[modbus.h](modbus_8h.md)>`

Configure Modbus Interface as raw ADU server.

Parameters
:   | iface | Modbus RTU interface index |
    | --- | --- |
    | param | Configuration parameter of the server interface |

Return values
:   | 0 | If the function was successful |
    | --- | --- |

## [◆ ](#ga7aa5dfd6e457980e9e9b8a77810ec31e)modbus\_raw\_backend\_txn()

| int modbus\_raw\_backend\_txn | ( | const int | *iface*, |
| --- | --- | --- | --- |
|  |  | struct [modbus\_adu](structmodbus__adu.md) \* | *adu* ) |

`#include <[modbus.h](modbus_8h.md)>`

Use interface as backend to send and receive ADU.

This function overwrites ADU passed by the pointer and generates exception responses if backend interface is misconfigured or target device is unreachable.

Parameters
:   | iface | Modbus client interface index |
    | --- | --- |
    | adu | Pointer to the RAW ADU struct |

Return values
:   | 0 | If transfer was successful |
    | --- | --- |

## [◆ ](#ga333072d3536d7b6f0680ceecc2c5bddf)modbus\_raw\_get\_header()

| void modbus\_raw\_get\_header | ( | struct [modbus\_adu](structmodbus__adu.md) \* | *adu*, |
| --- | --- | --- | --- |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *header* ) |

`#include <[modbus.h](modbus_8h.md)>`

Get MBAP header from a buffer.

Parameters
:   | adu | Pointer to the RAW ADU struct |
    | --- | --- |
    | header | Pointer to the buffer containing MBAP header |

## [◆ ](#ga8fdae6a92e27a845296c9d8ce4b8078e)modbus\_raw\_put\_header()

| void modbus\_raw\_put\_header | ( | const struct [modbus\_adu](structmodbus__adu.md) \* | *adu*, |
| --- | --- | --- | --- |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | *header* ) |

`#include <[modbus.h](modbus_8h.md)>`

Put MBAP header into a buffer.

Parameters
:   | adu | Pointer to the RAW ADU struct |
    | --- | --- |
    | header | Pointer to the buffer in which MBAP header will be placed. |

## [◆ ](#gad250c40ba13a7d8c9189de17d1fd31aa)modbus\_raw\_set\_server\_failure()

| void modbus\_raw\_set\_server\_failure | ( | struct [modbus\_adu](structmodbus__adu.md) \* | *adu* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[modbus.h](modbus_8h.md)>`

Set Server Device Failure exception.

This function modifies ADU passed by the pointer.

Parameters
:   | adu | Pointer to the RAW ADU struct |
    | --- | --- |

## [◆ ](#ga6d40e9eda6b8ead6d071d4192ffe489b)modbus\_raw\_submit\_rx()

| int modbus\_raw\_submit\_rx | ( | const int | *iface*, |
| --- | --- | --- | --- |
|  |  | const struct [modbus\_adu](structmodbus__adu.md) \* | *adu* ) |

`#include <[modbus.h](modbus_8h.md)>`

Submit raw ADU.

Parameters
:   | iface | Modbus RTU interface index |
    | --- | --- |
    | adu | Pointer to the RAW ADU struct that is received |

Return values
:   | 0 | If transfer was successful |
    | --- | --- |

## [◆ ](#ga05b118dc87ebe3739cac4e9572104ffb)modbus\_read\_coils()

| int modbus\_read\_coils | ( | const int | *iface*, |
| --- | --- | --- | --- |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *unit\_id*, |
|  |  | const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *start\_addr*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*const | *coil\_tbl*, |
|  |  | const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *num\_coils* ) |

`#include <[modbus.h](modbus_8h.md)>`

Coil read (FC01).

Sends a Modbus message to read the status of coils from a server.

Parameters
:   | iface | Modbus interface index |
    | --- | --- |
    | unit\_id | Modbus unit ID of the server |
    | start\_addr | Coil starting address |
    | coil\_tbl | Pointer to an array of bytes containing the value of the coils read. The format is:  ```                 MSB                               LSB                 B7   B6   B5   B4   B3   B2   B1   B0                 ------------------------------------- coil_tbl[0]     #8   #7                            #1 coil_tbl[1]     #16  #15                           #9      :      : ``` |

Note that the array that will be receiving the coil values must be greater than or equal to: (num\_coils - 1) / 8 + 1

Parameters
:   | num\_coils | Quantity of coils to read |
    | --- | --- |

Return values
:   | 0 | If the function was successful |
    | --- | --- |

## [◆ ](#ga921fd6036ff1b8a416dc02e30bb6e653)modbus\_read\_dinputs()

| int modbus\_read\_dinputs | ( | const int | *iface*, |
| --- | --- | --- | --- |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *unit\_id*, |
|  |  | const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *start\_addr*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*const | *di\_tbl*, |
|  |  | const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *num\_di* ) |

`#include <[modbus.h](modbus_8h.md)>`

Read discrete inputs (FC02).

Sends a Modbus message to read the status of discrete inputs from a server.

Parameters
:   | iface | Modbus interface index |
    | --- | --- |
    | unit\_id | Modbus unit ID of the server |
    | start\_addr | Discrete input starting address |
    | di\_tbl | Pointer to an array that will receive the state of the discrete inputs. The format of the array is as follows:  ```               MSB                               LSB               B7   B6   B5   B4   B3   B2   B1   B0               ------------------------------------- di_tbl[0]     #8   #7                            #1 di_tbl[1]     #16  #15                           #9      :      : ``` |

Note that the array that will be receiving the discrete input values must be greater than or equal to: (num\_di - 1) / 8 + 1

Parameters
:   | num\_di | Quantity of discrete inputs to read |
    | --- | --- |

Return values
:   | 0 | If the function was successful |
    | --- | --- |

## [◆ ](#ga7d7221b32fbf2395e69e25ef2dbaa036)modbus\_read\_holding\_regs()

| int modbus\_read\_holding\_regs | ( | const int | *iface*, |
| --- | --- | --- | --- |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *unit\_id*, |
|  |  | const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *start\_addr*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*const | *reg\_buf*, |
|  |  | const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *num\_regs* ) |

`#include <[modbus.h](modbus_8h.md)>`

Read holding registers (FC03).

Sends a Modbus message to read the value of holding registers from a server.

Parameters
:   | iface | Modbus interface index |
    | --- | --- |
    | unit\_id | Modbus unit ID of the server |
    | start\_addr | Register starting address |
    | reg\_buf | Is a pointer to an array that will receive the current values of the holding registers from the server. The array pointed to by 'reg\_buf' needs to be able to hold at least 'num\_regs' entries. |
    | num\_regs | Quantity of registers to read |

Return values
:   | 0 | If the function was successful |
    | --- | --- |

## [◆ ](#ga9a8ae6fb4b1aee398f5b19f074d07ea9)modbus\_read\_holding\_regs\_fp()

| int modbus\_read\_holding\_regs\_fp | ( | const int | *iface*, |
| --- | --- | --- | --- |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *unit\_id*, |
|  |  | const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *start\_addr*, |
|  |  | float \*const | *reg\_buf*, |
|  |  | const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *num\_regs* ) |

`#include <[modbus.h](modbus_8h.md)>`

Read floating-point holding registers (FC03).

Sends a Modbus message to read the value of floating-point holding registers from a server unit.

Parameters
:   | iface | Modbus interface index |
    | --- | --- |
    | unit\_id | Modbus unit ID of the server |
    | start\_addr | Register starting address |
    | reg\_buf | Is a pointer to an array that will receive the current values of the holding registers from the server. The array pointed to by 'reg\_buf' needs to be able to hold at least 'num\_regs' entries. |
    | num\_regs | Quantity of registers to read |

Return values
:   | 0 | If the function was successful |
    | --- | --- |

## [◆ ](#ga5ff31ca21cf2d1b081d172228d6c2154)modbus\_read\_input\_regs()

| int modbus\_read\_input\_regs | ( | const int | *iface*, |
| --- | --- | --- | --- |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *unit\_id*, |
|  |  | const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *start\_addr*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*const | *reg\_buf*, |
|  |  | const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *num\_regs* ) |

`#include <[modbus.h](modbus_8h.md)>`

Read input registers (FC04).

Sends a Modbus message to read the value of input registers from a server.

Parameters
:   | iface | Modbus interface index |
    | --- | --- |
    | unit\_id | Modbus unit ID of the server |
    | start\_addr | Register starting address |
    | reg\_buf | Is a pointer to an array that will receive the current value of the holding registers from the server. The array pointed to by 'reg\_buf' needs to be able to hold at least 'num\_regs' entries. |
    | num\_regs | Quantity of registers to read |

Return values
:   | 0 | If the function was successful |
    | --- | --- |

## [◆ ](#gacd88a4f35a13cc6864654927296803c4)modbus\_register\_user\_fc()

| int modbus\_register\_user\_fc | ( | const int | *iface*, |
| --- | --- | --- | --- |
|  |  | struct modbus\_custom\_fc \* | *custom\_fc* ) |

`#include <[modbus.h](modbus_8h.md)>`

Register a user-defined function code handler.

The Modbus specification allows users to define standard function codes missing from Zephyr's Modbus implementation as well as add non-standard function codes in the ranges 65 to 72 and 100 to 110 (decimal), as per specification.

This function registers a new handler at runtime for the given function code.

Parameters
:   | iface | Modbus client interface index |
    | --- | --- |
    | custom\_fc | User defined function code and callback pair |

Return values
:   | 0 | on success |
    | --- | --- |

## [◆ ](#gac924251f66ca6f357d8b7d90075df210)modbus\_request\_diagnostic()

| int modbus\_request\_diagnostic | ( | const int | *iface*, |
| --- | --- | --- | --- |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *unit\_id*, |
|  |  | const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *sfunc*, |
|  |  | const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *data*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*const | *data\_out* ) |

`#include <[modbus.h](modbus_8h.md)>`

Read diagnostic (FC08).

Sends a Modbus message to perform a diagnostic function of a server unit.

Parameters
:   | iface | Modbus interface index |
    | --- | --- |
    | unit\_id | Modbus unit ID of the server |
    | sfunc | Diagnostic sub-function code |
    | data | Sub-function data |
    | data\_out | Pointer to the data value |

Return values
:   | 0 | If the function was successful |
    | --- | --- |

## [◆ ](#gaccac4f72b5d66a5a2e6c444dda251c41)modbus\_write\_coil()

| int modbus\_write\_coil | ( | const int | *iface*, |
| --- | --- | --- | --- |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *unit\_id*, |
|  |  | const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *coil\_addr*, |
|  |  | const [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *coil\_state* ) |

`#include <[modbus.h](modbus_8h.md)>`

Write single coil (FC05).

Sends a Modbus message to write the value of single coil to a server.

Parameters
:   | iface | Modbus interface index |
    | --- | --- |
    | unit\_id | Modbus unit ID of the server |
    | coil\_addr | Coils starting address |
    | coil\_state | Is the desired state of the coil |

Return values
:   | 0 | If the function was successful |
    | --- | --- |

## [◆ ](#gac0fa22cd0d1fa861fdbc04b65ea60d7e)modbus\_write\_coils()

| int modbus\_write\_coils | ( | const int | *iface*, |
| --- | --- | --- | --- |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *unit\_id*, |
|  |  | const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *start\_addr*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*const | *coil\_tbl*, |
|  |  | const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *num\_coils* ) |

`#include <[modbus.h](modbus_8h.md)>`

Write coils (FC15).

Sends a Modbus message to write to coils on a server unit.

Parameters
:   | iface | Modbus interface index |
    | --- | --- |
    | unit\_id | Modbus unit ID of the server |
    | start\_addr | Coils starting address |
    | coil\_tbl | Pointer to an array of bytes containing the value of the coils to write. The format is:  ```                 MSB                               LSB                 B7   B6   B5   B4   B3   B2   B1   B0                 ------------------------------------- coil_tbl[0]     #8   #7                            #1 coil_tbl[1]     #16  #15                           #9      :      : ``` |

Note that the array that will be receiving the coil values must be greater than or equal to: (num\_coils - 1) / 8 + 1

Parameters
:   | num\_coils | Quantity of coils to write |
    | --- | --- |

Return values
:   | 0 | If the function was successful |
    | --- | --- |

## [◆ ](#gaf06d2553af8b8e9ab58f54b8b7e2055b)modbus\_write\_holding\_reg()

| int modbus\_write\_holding\_reg | ( | const int | *iface*, |
| --- | --- | --- | --- |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *unit\_id*, |
|  |  | const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *start\_addr*, |
|  |  | const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *reg\_val* ) |

`#include <[modbus.h](modbus_8h.md)>`

Write single holding register (FC06).

Sends a Modbus message to write the value of single holding register to a server unit.

Parameters
:   | iface | Modbus interface index |
    | --- | --- |
    | unit\_id | Modbus unit ID of the server |
    | start\_addr | Coils starting address |
    | reg\_val | Desired value of the holding register |

Return values
:   | 0 | If the function was successful |
    | --- | --- |

## [◆ ](#gadc8273292e0efc8c0d65c00eea7a22c5)modbus\_write\_holding\_regs()

| int modbus\_write\_holding\_regs | ( | const int | *iface*, |
| --- | --- | --- | --- |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *unit\_id*, |
|  |  | const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *start\_addr*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*const | *reg\_buf*, |
|  |  | const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *num\_regs* ) |

`#include <[modbus.h](modbus_8h.md)>`

Write holding registers (FC16).

Sends a Modbus message to write to integer holding registers to a server unit.

Parameters
:   | iface | Modbus interface index |
    | --- | --- |
    | unit\_id | Modbus unit ID of the server |
    | start\_addr | Register starting address |
    | reg\_buf | Is a pointer to an array containing the value of the holding registers to write. Note that the array containing the register values must be greater than or equal to 'num\_regs' |
    | num\_regs | Quantity of registers to write |

Return values
:   | 0 | If the function was successful |
    | --- | --- |

## [◆ ](#ga762da245db3ca4f60fb3aa6c5783c73d)modbus\_write\_holding\_regs\_fp()

| int modbus\_write\_holding\_regs\_fp | ( | const int | *iface*, |
| --- | --- | --- | --- |
|  |  | const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *unit\_id*, |
|  |  | const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *start\_addr*, |
|  |  | float \*const | *reg\_buf*, |
|  |  | const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *num\_regs* ) |

`#include <[modbus.h](modbus_8h.md)>`

Write floating-point holding registers (FC16).

Sends a Modbus message to write to floating-point holding registers to a server unit.

Parameters
:   | iface | Modbus interface index |
    | --- | --- |
    | unit\_id | Modbus unit ID of the server |
    | start\_addr | Register starting address |
    | reg\_buf | Is a pointer to an array containing the value of the holding registers to write. Note that the array containing the register values must be greater than or equal to 'num\_regs' |
    | num\_regs | Quantity of registers to write |

Return values
:   | 0 | If the function was successful |
    | --- | --- |

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

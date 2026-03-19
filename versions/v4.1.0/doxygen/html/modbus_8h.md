---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/modbus_8h.html
original_path: doxygen/html/modbus_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

modbus.h File Reference

`#include <[zephyr/drivers/uart.h](drivers_2uart_8h_source.md)>`  
`#include <[zephyr/sys/slist.h](slist_8h_source.md)>`

[Go to the source code of this file.](modbus_8h_source.md)

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
| #define | [MODBUS\_MBAP\_LENGTH](group__modbus.md#ga1015513d4d3b6621fc18dcfda79116a2)   7 |
|  | Length of MBAP Header. |
| #define | [MODBUS\_MBAP\_AND\_FC\_LENGTH](group__modbus.md#gae8a6fcfc117e7c4b2ac32aef90155698)   ([MODBUS\_MBAP\_LENGTH](group__modbus.md#ga1015513d4d3b6621fc18dcfda79116a2) + 1) |
|  | Length of MBAP Header plus function code. |
| #define | [MODBUS\_CUSTOM\_FC\_DEFINE](group__modbus.md#gaa0acc60971d0f773719431173632fd30)(name, user\_cb, user\_fc, userdata) |
|  | INTERNAL\_HIDDEN. |
| Modbus exception codes | |
| #define | [MODBUS\_EXC\_NONE](group__modbus.md#ga12557dda3e72ac45aefee3f9cbb18960)   0 |
|  | No exception. |
| #define | [MODBUS\_EXC\_ILLEGAL\_FC](group__modbus.md#ga934994f66a61c0d11d00dd52a748cc78)   1 |
|  | Illegal function code. |
| #define | [MODBUS\_EXC\_ILLEGAL\_DATA\_ADDR](group__modbus.md#ga9ab4fc4caaf2e051ae697d44a9fa98e3)   2 |
|  | Illegal data address. |
| #define | [MODBUS\_EXC\_ILLEGAL\_DATA\_VAL](group__modbus.md#ga5bcd9c7edd91d59af1453cde2376412f)   3 |
|  | Illegal data value. |
| #define | [MODBUS\_EXC\_SERVER\_DEVICE\_FAILURE](group__modbus.md#ga6bcf75ff2d522f1a542caa41b47a5ac8)   4 |
|  | Server device failure. |
| #define | [MODBUS\_EXC\_ACK](group__modbus.md#ga9cfec884c72b7fc404d82c16f57e858d)   5 |
|  | Acknowledge. |
| #define | [MODBUS\_EXC\_SERVER\_DEVICE\_BUSY](group__modbus.md#ga37f02ccee238e7c8ab33f150b2bcd793)   6 |
|  | Server device busy. |
| #define | [MODBUS\_EXC\_MEM\_PARITY\_ERROR](group__modbus.md#gad9b56cf73a31d77cd78d48695ea44659)   8 |
|  | Memory parity error. |
| #define | [MODBUS\_EXC\_GW\_PATH\_UNAVAILABLE](group__modbus.md#ga9903d7d283c11a4b8854ef5706b5aaba)   10 |
|  | Gateway path unavailable. |
| #define | [MODBUS\_EXC\_GW\_TARGET\_FAILED\_TO\_RESP](group__modbus.md#gae61e3ee73e2288006f3dd2f081b4d1de)   11 |
|  | Gateway target device failed to respond. |

| Typedefs | |
| --- | --- |
| typedef int(\* | [modbus\_raw\_cb\_t](group__modbus.md#ga6d74be1fffb9d5697fe5708827aa7ef1)) (const int iface, const struct [modbus\_adu](structmodbus__adu.md) \*adu, void \*user\_data) |
|  | ADU raw callback function signature. |
| typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* | [modbus\_custom\_cb\_t](group__modbus.md#ga2a7ba41a2fb7f6bf5194c02dcab07ae3)) (const int iface, const struct [modbus\_adu](structmodbus__adu.md) \*const rx\_adu, struct [modbus\_adu](structmodbus__adu.md) \*const tx\_adu, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*const excep\_code, void \*const user\_data) |
|  | Custom function code handler function signature. |

| Enumerations | |
| --- | --- |
| enum | [modbus\_mode](group__modbus.md#ga4bd8913e1c77a1e4b19585caa9f77c2e) { [MODBUS\_MODE\_RTU](group__modbus.md#gga4bd8913e1c77a1e4b19585caa9f77c2ea52033dc2ef37fc286a590b1f97d946ef) , [MODBUS\_MODE\_ASCII](group__modbus.md#gga4bd8913e1c77a1e4b19585caa9f77c2eafdf029741cc1bdecb2cb9baf4f06732a) , [MODBUS\_MODE\_RAW](group__modbus.md#gga4bd8913e1c77a1e4b19585caa9f77c2ea4d05b2cfd56ccf15eb1d8c7bb71071ec) } |
|  | Modbus interface mode. [More...](group__modbus.md#ga4bd8913e1c77a1e4b19585caa9f77c2e) |

| Functions | |
| --- | --- |
| int | [modbus\_read\_coils](group__modbus.md#ga05b118dc87ebe3739cac4e9572104ffb) (const int iface, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) unit\_id, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) start\_addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*const coil\_tbl, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) num\_coils) |
|  | Coil read (FC01). |
| int | [modbus\_read\_dinputs](group__modbus.md#ga921fd6036ff1b8a416dc02e30bb6e653) (const int iface, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) unit\_id, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) start\_addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*const di\_tbl, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) num\_di) |
|  | Read discrete inputs (FC02). |
| int | [modbus\_read\_holding\_regs](group__modbus.md#ga7d7221b32fbf2395e69e25ef2dbaa036) (const int iface, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) unit\_id, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) start\_addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*const reg\_buf, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) num\_regs) |
|  | Read holding registers (FC03). |
| int | [modbus\_read\_input\_regs](group__modbus.md#ga5ff31ca21cf2d1b081d172228d6c2154) (const int iface, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) unit\_id, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) start\_addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*const reg\_buf, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) num\_regs) |
|  | Read input registers (FC04). |
| int | [modbus\_write\_coil](group__modbus.md#gaccac4f72b5d66a5a2e6c444dda251c41) (const int iface, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) unit\_id, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) coil\_addr, const [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) coil\_state) |
|  | Write single coil (FC05). |
| int | [modbus\_write\_holding\_reg](group__modbus.md#gaf06d2553af8b8e9ab58f54b8b7e2055b) (const int iface, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) unit\_id, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) start\_addr, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) reg\_val) |
|  | Write single holding register (FC06). |
| int | [modbus\_request\_diagnostic](group__modbus.md#gac924251f66ca6f357d8b7d90075df210) (const int iface, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) unit\_id, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) sfunc, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) data, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*const data\_out) |
|  | Read diagnostic (FC08). |
| int | [modbus\_write\_coils](group__modbus.md#gac0fa22cd0d1fa861fdbc04b65ea60d7e) (const int iface, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) unit\_id, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) start\_addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*const coil\_tbl, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) num\_coils) |
|  | Write coils (FC15). |
| int | [modbus\_write\_holding\_regs](group__modbus.md#gadc8273292e0efc8c0d65c00eea7a22c5) (const int iface, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) unit\_id, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) start\_addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*const reg\_buf, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) num\_regs) |
|  | Write holding registers (FC16). |
| int | [modbus\_read\_holding\_regs\_fp](group__modbus.md#ga9a8ae6fb4b1aee398f5b19f074d07ea9) (const int iface, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) unit\_id, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) start\_addr, float \*const reg\_buf, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) num\_regs) |
|  | Read floating-point holding registers (FC03). |
| int | [modbus\_write\_holding\_regs\_fp](group__modbus.md#ga762da245db3ca4f60fb3aa6c5783c73d) (const int iface, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) unit\_id, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) start\_addr, float \*const reg\_buf, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) num\_regs) |
|  | Write floating-point holding registers (FC16). |
| int | [modbus\_iface\_get\_by\_name](group__modbus.md#gaa17880a268d6b3b9553de835c800af27) (const char \*iface\_name) |
|  | Get Modbus interface index according to interface name. |
| int | [modbus\_init\_server](group__modbus.md#gae4d34276c467bf54e0849a1098e56f8b) (const int iface, struct [modbus\_iface\_param](structmodbus__iface__param.md) param) |
|  | Configure Modbus Interface as raw ADU server. |
| int | [modbus\_init\_client](group__modbus.md#ga943eff819ecf1bc268714783047888ef) (const int iface, struct [modbus\_iface\_param](structmodbus__iface__param.md) param) |
|  | Configure Modbus Interface as raw ADU client. |
| int | [modbus\_disable](group__modbus.md#ga32a6319cc51eb5a98dcb58b3231b9d34) (const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) iface) |
|  | Disable Modbus Interface. |
| int | [modbus\_raw\_submit\_rx](group__modbus.md#ga6d40e9eda6b8ead6d071d4192ffe489b) (const int iface, const struct [modbus\_adu](structmodbus__adu.md) \*adu) |
|  | Submit raw ADU. |
| void | [modbus\_raw\_put\_header](group__modbus.md#ga8fdae6a92e27a845296c9d8ce4b8078e) (const struct [modbus\_adu](structmodbus__adu.md) \*adu, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*header) |
|  | Put MBAP header into a buffer. |
| void | [modbus\_raw\_get\_header](group__modbus.md#ga333072d3536d7b6f0680ceecc2c5bddf) (struct [modbus\_adu](structmodbus__adu.md) \*adu, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*header) |
|  | Get MBAP header from a buffer. |
| void | [modbus\_raw\_set\_server\_failure](group__modbus.md#gad250c40ba13a7d8c9189de17d1fd31aa) (struct [modbus\_adu](structmodbus__adu.md) \*adu) |
|  | Set Server Device Failure exception. |
| int | [modbus\_raw\_backend\_txn](group__modbus.md#ga7aa5dfd6e457980e9e9b8a77810ec31e) (const int iface, struct [modbus\_adu](structmodbus__adu.md) \*adu) |
|  | Use interface as backend to send and receive ADU. |
| int | [modbus\_register\_user\_fc](group__modbus.md#gacd88a4f35a13cc6864654927296803c4) (const int iface, struct modbus\_custom\_fc \*custom\_fc) |
|  | Register a user-defined function code handler. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [modbus](dir_4256a22177f338086a49d2e4cf070454.md)
- [modbus.h](modbus_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

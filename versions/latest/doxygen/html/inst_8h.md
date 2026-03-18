---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/inst_8h.html
original_path: doxygen/html/inst_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

inst.h File Reference

`#include <[zephyr/bluetooth/gatt.h](gatt_8h_source.md)>`  
`#include <[zephyr/sys/iterable_sections.h](sys_2iterable__sections_8h_source.md)>`  
`#include <[zephyr/sys/slist.h](slist_8h_source.md)>`

[Go to the source code of this file.](inst_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [bt\_nus\_inst](structbt__nus__inst.md) |

| Macros | |
| --- | --- |
| #define | [BT\_UUID\_NUS\_SERVICE](#a3752da6f7063510a04551609672b2583)   [BT\_UUID\_DECLARE\_128](group__bt__uuid.md#gadece715e13e2a529aa55c298ff760bf0)([BT\_UUID\_NUS\_SRV\_VAL](nus_8h.md#a8da4aaa9c77a537805c7b5bff7fc4aa6)) |
| #define | [BT\_UUID\_NUS\_TX\_CHAR](#ad652d719c4f193d433156afcb3d8fe87)   [BT\_UUID\_DECLARE\_128](group__bt__uuid.md#gadece715e13e2a529aa55c298ff760bf0)([BT\_UUID\_NUS\_TX\_CHAR\_VAL](nus_8h.md#a7636b61879884e6f6fc8e871ae09160b)) |
| #define | [BT\_UUID\_NUS\_RX\_CHAR](#aa9e0e0a89747210a3ebc36d85ce973d2)   [BT\_UUID\_DECLARE\_128](group__bt__uuid.md#gadece715e13e2a529aa55c298ff760bf0)([BT\_UUID\_NUS\_RX\_CHAR\_VAL](nus_8h.md#ada90c739cf936ec52008fcc4f272e207)) |

| Functions | |
| --- | --- |
| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) | [nus\_bt\_chr\_write](#a3bb5cd4e4367d402f377cee751f9b434) (struct bt\_conn \*conn, const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \*attr, const void \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) offset, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Required as the service may be instantiated outside of the module. |
| void | [nus\_ccc\_cfg\_changed](#a964bdf4d6c01f257533c0a5c337f562e) (const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \*attr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) value) |

## Macro Definition Documentation

## [◆ ](#aa9e0e0a89747210a3ebc36d85ce973d2)BT\_UUID\_NUS\_RX\_CHAR

| #define BT\_UUID\_NUS\_RX\_CHAR   [BT\_UUID\_DECLARE\_128](group__bt__uuid.md#gadece715e13e2a529aa55c298ff760bf0)([BT\_UUID\_NUS\_RX\_CHAR\_VAL](nus_8h.md#ada90c739cf936ec52008fcc4f272e207)) |
| --- |

## [◆ ](#a3752da6f7063510a04551609672b2583)BT\_UUID\_NUS\_SERVICE

| #define BT\_UUID\_NUS\_SERVICE   [BT\_UUID\_DECLARE\_128](group__bt__uuid.md#gadece715e13e2a529aa55c298ff760bf0)([BT\_UUID\_NUS\_SRV\_VAL](nus_8h.md#a8da4aaa9c77a537805c7b5bff7fc4aa6)) |
| --- |

## [◆ ](#ad652d719c4f193d433156afcb3d8fe87)BT\_UUID\_NUS\_TX\_CHAR

| #define BT\_UUID\_NUS\_TX\_CHAR   [BT\_UUID\_DECLARE\_128](group__bt__uuid.md#gadece715e13e2a529aa55c298ff760bf0)([BT\_UUID\_NUS\_TX\_CHAR\_VAL](nus_8h.md#a7636b61879884e6f6fc8e871ae09160b)) |
| --- |

## Function Documentation

## [◆ ](#a3bb5cd4e4367d402f377cee751f9b434)nus\_bt\_chr\_write()

| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) nus\_bt\_chr\_write | ( | struct bt\_conn \* | *conn*, |
| --- | --- | --- | --- |
|  |  | const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \* | *attr*, |
|  |  | const void \* | *buf*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *len*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *offset*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *flags* ) |

Required as the service may be instantiated outside of the module.

## [◆ ](#a964bdf4d6c01f257533c0a5c337f562e)nus\_ccc\_cfg\_changed()

| void nus\_ccc\_cfg\_changed | ( | const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \* | *attr*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *value* ) |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [services](dir_e4028deab123aca136adb6f86dc413ad.md)
- [nus](dir_41b6aa38490ac2da296b10fec5e4989c.md)
- [inst.h](inst_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

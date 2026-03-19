---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/group__bt__gatt__server.html
original_path: doxygen/html/group__bt__gatt__server.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

GATT Server APIs

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Generic Attribute Profile (GATT)](group__bt__gatt.md)

| Data Structures | |
| --- | --- |
| struct | [bt\_gatt\_ccc\_cfg](structbt__gatt__ccc__cfg.md) |
|  | GATT CCC configuration entry. [More...](structbt__gatt__ccc__cfg.md#details) |
| struct | [bt\_gatt\_notify\_params](structbt__gatt__notify__params.md) |
|  | GATT notification parameters. [More...](structbt__gatt__notify__params.md#details) |
| struct | [bt\_gatt\_indicate\_params](structbt__gatt__indicate__params.md) |
|  | GATT Indicate Value parameters. [More...](structbt__gatt__indicate__params.md#details) |

| Macros | |
| --- | --- |
| #define | [BT\_GATT\_SERVICE\_DEFINE](#ga04c7887fb67107bd060dd023fd3186d5)(\_name, ...) |
|  | Statically define and register a service. |
| #define | [BT\_GATT\_SERVICE\_INSTANCE\_DEFINE](#ga8bb3aeef20465d7f6e38f6bbddef74e5)( \_name, \_instances, \_instance\_num, \_attrs\_def) |
|  | Statically define service structure array. |
| #define | [BT\_GATT\_SERVICE](#ga7d413ec013b91a633ec24d80d2814e2b)(\_attrs) |
|  | Service Structure Declaration Macro. |
| #define | [BT\_GATT\_PRIMARY\_SERVICE](#gaacada0ff1029af959b6fcd6703d4a0bf)(\_service) |
|  | Primary Service Declaration Macro. |
| #define | [BT\_GATT\_SECONDARY\_SERVICE](#gaecb4d30282677d3450ad79c5f83f3445)(\_service) |
|  | Secondary Service Declaration Macro. |
| #define | [BT\_GATT\_INCLUDE\_SERVICE](#ga08ffee706d271b75a54b1b99249dba24)(\_service\_incl) |
|  | Include Service Declaration Macro. |
| #define | [BT\_GATT\_CHRC\_INIT](#ga7f19592a722c41d6c1d2421d166dd78a)(\_uuid, \_handle, \_props) |
|  | Gatt Characterisitc Initialization Macro. |
| #define | [BT\_GATT\_CHARACTERISTIC](#ga9e739546dbd906d3b3c4f1ed5ad9f41e)(\_uuid, \_props, \_perm, \_read, \_write, \_user\_data) |
|  | Characteristic and Value Declaration Macro. |
| #define | [BT\_GATT\_CCC\_MAX](#gac1c0a195c1ec1ff2cdd5bf6d0ba6ad00)   0 |
|  | BT\_GATT\_CCC\_MAX is defined depending on whether `CONFIG_BT_SETTINGS_CCC_LAZY_LOADING` or `CONFIG_BT_CONN` is set. |
| #define | [BT\_GATT\_CCC\_INITIALIZER](#ga59fd77199435e461e03a80c7121bb869)(\_changed, \_write, \_match) |
|  | Initialize Client Characteristic Configuration Declaration Macro. |
| #define | [BT\_GATT\_CCC\_MANAGED](#gad8b296ecfd1139680f21da7904b9f585)(\_ccc, \_perm) |
|  | Managed Client Characteristic Configuration Declaration Macro. |
| #define | [BT\_GATT\_CCC](#ga140b9c25d10244bebd9c891f881fdc94)(\_changed, \_perm) |
|  | Client Characteristic Configuration Declaration Macro. |
| #define | [BT\_GATT\_CEP](#ga55a82cada1093c4ff75fe5504ac504b1)(\_value) |
|  | Characteristic Extended Properties Declaration Macro. |
| #define | [BT\_GATT\_CUD](#ga1e1cd9d0853e2dcbefcb85fda44dc9c7)(\_value, \_perm) |
|  | Characteristic User Format Descriptor Declaration Macro. |
| #define | [BT\_GATT\_CPF](#ga3835fcfdf7a5f917e21c9d17e75162be)(\_value) |
|  | Characteristic Presentation Format Descriptor Declaration Macro. |
| #define | [BT\_GATT\_DESCRIPTOR](#ga83207fc083454327004f7d3c3e5b3840)(\_uuid, \_perm, \_read, \_write, \_user\_data) |
|  | Descriptor Declaration Macro. |
| #define | [BT\_GATT\_ATTRIBUTE](#gac4abfeb068d16dcdaceee812c12bf406)(\_uuid, \_perm, \_read, \_write, \_user\_data) |
|  | Attribute Declaration Macro. |

| Typedefs | |
| --- | --- |
| typedef [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)(\* | [bt\_gatt\_attr\_func\_t](#ga60284611c90729b289fe806524ba9209)) (const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \*attr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) handle, void \*user\_data) |
|  | Attribute iterator callback. |
| typedef void(\* | [bt\_gatt\_complete\_func\_t](#gac55832607b95f394d26a64ed1cfe5bba)) (struct bt\_conn \*conn, void \*user\_data) |
|  | Notification complete result callback. |
| typedef void(\* | [bt\_gatt\_indicate\_func\_t](#ga1294850e6bdcbe7a8f42f2956fd837a8)) (struct bt\_conn \*conn, struct [bt\_gatt\_indicate\_params](structbt__gatt__indicate__params.md) \*params, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) err) |
|  | Indication complete result callback. |
| typedef void(\* | [bt\_gatt\_indicate\_params\_destroy\_t](#ga5d47ed9eaea22c8f00db14329daee8fe)) (struct [bt\_gatt\_indicate\_params](structbt__gatt__indicate__params.md) \*params) |
|  | Callback to destroy or clean up the GATT Indicate Value parameters. |

| Enumerations | |
| --- | --- |
| enum | { [BT\_GATT\_ITER\_STOP](#gga11c5a2eb0b62de9a2493ad5335fae383aa3f2a25e27c7065a2c7bb2a9ff09542e) = 0 , [BT\_GATT\_ITER\_CONTINUE](#gga11c5a2eb0b62de9a2493ad5335fae383aea569feffa4815d3443e12be78c684f5) } |
|  | to be used as return values for [bt\_gatt\_attr\_func\_t](#ga60284611c90729b289fe806524ba9209) and [bt\_gatt\_read\_func\_t](group__bt__gatt__client.md#ga1ca94b4f2b6c456b6134e05127993569 "bt_gatt_read_func_t") type callbacks. [More...](#ga11c5a2eb0b62de9a2493ad5335fae383) |

| Functions | |
| --- | --- |
| static const char \* | [bt\_gatt\_err\_to\_str](#gaf6d3f1e904f1a847afeb30236bad98a2) (int gatt\_err) |
|  | Converts a GATT error to string. |
| void | [bt\_gatt\_cb\_register](#ga270c8a52bf3d512defc373f8c29b59f2) (struct [bt\_gatt\_cb](structbt__gatt__cb.md) \*cb) |
|  | Register GATT callbacks. |
| int | [bt\_gatt\_authorization\_cb\_register](#ga5eee6afc6db391ffeda295d298bf6a56) (const struct [bt\_gatt\_authorization\_cb](structbt__gatt__authorization__cb.md) \*cb) |
|  | Register GATT authorization callbacks. |
| int | [bt\_gatt\_service\_register](#gab4d9cfea04e44445d5dc30ad52842b64) (struct [bt\_gatt\_service](structbt__gatt__service.md) \*svc) |
|  | Register GATT service. |
| int | [bt\_gatt\_service\_unregister](#gaf5bf0205fad5f7ad187b764d23deba6b) (struct [bt\_gatt\_service](structbt__gatt__service.md) \*svc) |
|  | Unregister GATT service. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [bt\_gatt\_service\_is\_registered](#gae5c1e8b7bb1e673e228f03d1d084be9a) (const struct [bt\_gatt\_service](structbt__gatt__service.md) \*svc) |
|  | Check if GATT service is registered. |
| void | [bt\_gatt\_foreach\_attr\_type](#gad8d8f513004f391167212d7bf9f7ff10) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) start\_handle, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) end\_handle, const struct [bt\_uuid](structbt__uuid.md) \*uuid, const void \*attr\_data, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) num\_matches, [bt\_gatt\_attr\_func\_t](#ga60284611c90729b289fe806524ba9209) func, void \*user\_data) |
|  | Attribute iterator by type. |
| static void | [bt\_gatt\_foreach\_attr](#gaa93b5e0f2870ed135447bead903c175a) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) start\_handle, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) end\_handle, [bt\_gatt\_attr\_func\_t](#ga60284611c90729b289fe806524ba9209) func, void \*user\_data) |
|  | Attribute iterator. |
| struct [bt\_gatt\_attr](structbt__gatt__attr.md) \* | [bt\_gatt\_attr\_next](#ga35cecaa43b00b374062d29cca1479d85) (const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \*attr) |
|  | Iterate to the next attribute. |
| struct [bt\_gatt\_attr](structbt__gatt__attr.md) \* | [bt\_gatt\_find\_by\_uuid](#gad2f3272b1dc42378104b492ec7caf6b0) (const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \*attr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) attr\_count, const struct [bt\_uuid](structbt__uuid.md) \*uuid) |
|  | Find Attribute by UUID. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [bt\_gatt\_attr\_get\_handle](#ga2d51136ea1bd6cdb50900639506fd9f7) (const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \*attr) |
|  | Get Attribute handle. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [bt\_gatt\_attr\_value\_handle](#ga99738cf4f05eae4c6da17cc3420827d8) (const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \*attr) |
|  | Get the handle of the characteristic value descriptor. |
| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) | [bt\_gatt\_attr\_read](#gaf6d253849932b706ec7f303568980dfa) (struct bt\_conn \*conn, const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \*attr, void \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) buf\_len, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) offset, const void \*value, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) value\_len) |
|  | Generic Read Attribute value helper. |
| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) | [bt\_gatt\_attr\_read\_service](#gacae81c0f272bad7e6ac93c0d13b678c6) (struct bt\_conn \*conn, const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \*attr, void \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) offset) |
|  | Read Service Attribute helper. |
| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) | [bt\_gatt\_attr\_read\_included](#ga4313a63decac2c8b7c4a1764df3d53ea) (struct bt\_conn \*conn, const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \*attr, void \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) offset) |
|  | Read Include Attribute helper. |
| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) | [bt\_gatt\_attr\_read\_chrc](#gad58b526a06334530c13292d14a11257c) (struct bt\_conn \*conn, const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \*attr, void \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) offset) |
|  | Read Characteristic Attribute helper. |
| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) | [bt\_gatt\_attr\_read\_ccc](#ga2e85b42136e2c6a4cb5b7ad8a2532573) (struct bt\_conn \*conn, const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \*attr, void \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) offset) |
|  | Read Client Characteristic Configuration Attribute helper. |
| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) | [bt\_gatt\_attr\_write\_ccc](#gabba965b676650a55cb9934072b34c75e) (struct bt\_conn \*conn, const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \*attr, const void \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) offset, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Write Client Characteristic Configuration Attribute helper. |
| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) | [bt\_gatt\_attr\_read\_cep](#ga5893166f1b24f437a94ccf1fc57c7917) (struct bt\_conn \*conn, const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \*attr, void \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) offset) |
|  | Read Characteristic Extended Properties Attribute helper. |
| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) | [bt\_gatt\_attr\_read\_cud](#ga29421c8788b47b6a648704d27d5f0d28) (struct bt\_conn \*conn, const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \*attr, void \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) offset) |
|  | Read Characteristic User Description Descriptor Attribute helper. |
| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) | [bt\_gatt\_attr\_read\_cpf](#ga5ae96590a0aaa5c4c3863a4a14d80fdd) (struct bt\_conn \*conn, const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \*attr, void \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) offset) |
|  | Read Characteristic Presentation format Descriptor Attribute helper. |
| int | [bt\_gatt\_notify\_cb](#ga55e3ef7cb43b8acb0a27643c78390146) (struct bt\_conn \*conn, struct [bt\_gatt\_notify\_params](structbt__gatt__notify__params.md) \*params) |
|  | Notify attribute value change. |
| int | [bt\_gatt\_notify\_multiple](#ga8071d6063f85c0a78155f6b2ac2da635) (struct bt\_conn \*conn, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) num\_params, struct [bt\_gatt\_notify\_params](structbt__gatt__notify__params.md) params[]) |
|  | Send multiple notifications in a single PDU. |
| static int | [bt\_gatt\_notify](#ga74ee552864c563aa5bc939f37395c14a) (struct bt\_conn \*conn, const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \*attr, const void \*data, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len) |
|  | Notify attribute value change. |
| static int | [bt\_gatt\_notify\_uuid](#ga24bae284dbc71cd4075649c4bc348b7c) (struct bt\_conn \*conn, const struct [bt\_uuid](structbt__uuid.md) \*uuid, const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \*attr, const void \*data, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len) |
|  | Notify attribute value change by UUID. |
| int | [bt\_gatt\_indicate](#ga4f2272692cc0f1d44638828012296c80) (struct bt\_conn \*conn, struct [bt\_gatt\_indicate\_params](structbt__gatt__indicate__params.md) \*params) |
|  | Indicate attribute value change. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [bt\_gatt\_is\_subscribed](#gabd4df0a264dae10e43797992a567be7d) (struct bt\_conn \*conn, const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \*attr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) ccc\_type) |
|  | Check if connection have subscribed to attribute. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [bt\_gatt\_get\_mtu](#ga351fd7658eaecbbfa60f1769119ef733) (struct bt\_conn \*conn) |
|  | Get ATT MTU for a connection. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [bt\_gatt\_get\_uatt\_mtu](#ga6653de5e245cae6dc12cd0b45acbe028) (struct bt\_conn \*conn) |
|  | Get Unenhanced ATT (UATT) MTU for a connection. |

## Detailed Description

## Macro Definition Documentation

## [◆ ](#gac4abfeb068d16dcdaceee812c12bf406)BT\_GATT\_ATTRIBUTE

| #define BT\_GATT\_ATTRIBUTE | ( |  | *\_uuid*, |
| --- | --- | --- | --- |
|  |  |  | *\_perm*, |
|  |  |  | *\_read*, |
|  |  |  | *\_write*, |
|  |  |  | *\_user\_data* ) |

`#include <[gatt.h](gatt_8h.md)>`

**Value:**

{ \

.uuid = \_uuid, \

.read = \_read, \

.write = \_write, \

.user\_data = \_user\_data, \

.handle = 0, \

.perm = \_perm, \

}

Attribute Declaration Macro.

Helper macro to declare an attribute.

Parameters
:   | \_uuid | Attribute uuid. |
    | --- | --- |
    | \_perm | Attribute access permissions, a bitmap of [bt\_gatt\_perm](group__bt__gatt.md#ga96e57500d2340a45badb23701cc43833 "bt_gatt_perm") values. |
    | \_read | Attribute read callback ([bt\_gatt\_attr\_read\_func\_t](group__bt__gatt.md#ga57e36bf94652531964fd4237c203fe7b "bt_gatt_attr_read_func_t")). |
    | \_write | Attribute write callback ([bt\_gatt\_attr\_write\_func\_t](group__bt__gatt.md#ga3fd8527a0f3e8f3699dc0d3b0339eba1 "bt_gatt_attr_write_func_t")). |
    | \_user\_data | Attribute user data. |

## [◆ ](#ga140b9c25d10244bebd9c891f881fdc94)BT\_GATT\_CCC

| #define BT\_GATT\_CCC | ( |  | *\_changed*, |
| --- | --- | --- | --- |
|  |  |  | *\_perm* ) |

`#include <[gatt.h](gatt_8h.md)>`

**Value:**

[BT\_GATT\_CCC\_MANAGED](#gad8b296ecfd1139680f21da7904b9f585)(((struct \_bt\_gatt\_ccc[]) \

{[BT\_GATT\_CCC\_INITIALIZER](#ga59fd77199435e461e03a80c7121bb869)(\_changed, [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4), [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4))}), \_perm)

[BT\_GATT\_CCC\_INITIALIZER](#ga59fd77199435e461e03a80c7121bb869)

#define BT\_GATT\_CCC\_INITIALIZER(\_changed, \_write, \_match)

Initialize Client Characteristic Configuration Declaration Macro.

**Definition** gatt.h:1140

[BT\_GATT\_CCC\_MANAGED](#gad8b296ecfd1139680f21da7904b9f585)

#define BT\_GATT\_CCC\_MANAGED(\_ccc, \_perm)

Managed Client Characteristic Configuration Declaration Macro.

**Definition** gatt.h:1157

[NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4)

#define NULL

**Definition** iar\_missing\_defs.h:20

Client Characteristic Configuration Declaration Macro.

Helper macro to declare a CCC attribute.

Parameters
:   | \_changed | Configuration changed callback. |
    | --- | --- |
    | \_perm | CCC access permissions, a bitmap of [bt\_gatt\_perm](group__bt__gatt.md#ga96e57500d2340a45badb23701cc43833 "bt_gatt_perm") values. |

## [◆ ](#ga59fd77199435e461e03a80c7121bb869)BT\_GATT\_CCC\_INITIALIZER

| #define BT\_GATT\_CCC\_INITIALIZER | ( |  | *\_changed*, |
| --- | --- | --- | --- |
|  |  |  | *\_write*, |
|  |  |  | *\_match* ) |

`#include <[gatt.h](gatt_8h.md)>`

**Value:**

{ \

.cfg = {}, \

.cfg\_changed = \_changed, \

.cfg\_write = \_write, \

.cfg\_match = \_match, \

}

Initialize Client Characteristic Configuration Declaration Macro.

Helper macro to initialize a Managed CCC attribute value.

Parameters
:   | \_changed | Configuration changed callback. |
    | --- | --- |
    | \_write | Configuration write callback. |
    | \_match | Configuration match callback. |

## [◆ ](#gad8b296ecfd1139680f21da7904b9f585)BT\_GATT\_CCC\_MANAGED

| #define BT\_GATT\_CCC\_MANAGED | ( |  | *\_ccc*, |
| --- | --- | --- | --- |
|  |  |  | *\_perm* ) |

`#include <[gatt.h](gatt_8h.md)>`

**Value:**

[BT\_GATT\_ATTRIBUTE](#gac4abfeb068d16dcdaceee812c12bf406)([BT\_UUID\_GATT\_CCC](group__bt__uuid.md#ga03a2d3f0ce89508b794d5c87a4303057), \_perm, \

[bt\_gatt\_attr\_read\_ccc](#ga2e85b42136e2c6a4cb5b7ad8a2532573), [bt\_gatt\_attr\_write\_ccc](#gabba965b676650a55cb9934072b34c75e), \

\_ccc)

[bt\_gatt\_attr\_read\_ccc](#ga2e85b42136e2c6a4cb5b7ad8a2532573)

ssize\_t bt\_gatt\_attr\_read\_ccc(struct bt\_conn \*conn, const struct bt\_gatt\_attr \*attr, void \*buf, uint16\_t len, uint16\_t offset)

Read Client Characteristic Configuration Attribute helper.

[bt\_gatt\_attr\_write\_ccc](#gabba965b676650a55cb9934072b34c75e)

ssize\_t bt\_gatt\_attr\_write\_ccc(struct bt\_conn \*conn, const struct bt\_gatt\_attr \*attr, const void \*buf, uint16\_t len, uint16\_t offset, uint8\_t flags)

Write Client Characteristic Configuration Attribute helper.

[BT\_GATT\_ATTRIBUTE](#gac4abfeb068d16dcdaceee812c12bf406)

#define BT\_GATT\_ATTRIBUTE(\_uuid, \_perm, \_read, \_write, \_user\_data)

Attribute Declaration Macro.

**Definition** gatt.h:1300

[BT\_UUID\_GATT\_CCC](group__bt__uuid.md#ga03a2d3f0ce89508b794d5c87a4303057)

#define BT\_UUID\_GATT\_CCC

GATT Client Characteristic Configuration.

**Definition** uuid.h:886

Managed Client Characteristic Configuration Declaration Macro.

Helper macro to declare a Managed CCC attribute.

Parameters
:   | \_ccc | CCC attribute user data, shall point to a \_bt\_gatt\_ccc. |
    | --- | --- |
    | \_perm | CCC access permissions, a bitmap of [bt\_gatt\_perm](group__bt__gatt.md#ga96e57500d2340a45badb23701cc43833 "bt_gatt_perm") values. |

## [◆ ](#gac1c0a195c1ec1ff2cdd5bf6d0ba6ad00)BT\_GATT\_CCC\_MAX

| #define BT\_GATT\_CCC\_MAX   0 |
| --- |

`#include <[gatt.h](gatt_8h.md)>`

BT\_GATT\_CCC\_MAX is defined depending on whether `CONFIG_BT_SETTINGS_CCC_LAZY_LOADING` or `CONFIG_BT_CONN` is set.

`CONFIG_BT_SETTINGS_CCC_LAZY_LOADING` will set BT\_GATT\_CCC\_MAX to `CONFIG_BT_MAX_CONN` `CONFIG_BT_CONN` will set BT\_GATT\_CCC\_MAX to `CONFIG_BT_MAX_PAIRED` + `CONFIG_BT_MAX_CONN` If neither are set, BT\_GATT\_CCC\_MAX is 0.

## [◆ ](#ga55a82cada1093c4ff75fe5504ac504b1)BT\_GATT\_CEP

| #define BT\_GATT\_CEP | ( |  | *\_value* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[gatt.h](gatt_8h.md)>`

**Value:**

[BT\_GATT\_DESCRIPTOR](#ga83207fc083454327004f7d3c3e5b3840)([BT\_UUID\_GATT\_CEP](group__bt__uuid.md#ga6aa143b721d810f1536d7431a9bf7cc7), [BT\_GATT\_PERM\_READ](group__bt__gatt.md#gga96e57500d2340a45badb23701cc43833a9afb838c2cef657e9cd035ef27521f17), \

[bt\_gatt\_attr\_read\_cep](#ga5893166f1b24f437a94ccf1fc57c7917), [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4), (void \*)\_value)

[bt\_gatt\_attr\_read\_cep](#ga5893166f1b24f437a94ccf1fc57c7917)

ssize\_t bt\_gatt\_attr\_read\_cep(struct bt\_conn \*conn, const struct bt\_gatt\_attr \*attr, void \*buf, uint16\_t len, uint16\_t offset)

Read Characteristic Extended Properties Attribute helper.

[BT\_GATT\_DESCRIPTOR](#ga83207fc083454327004f7d3c3e5b3840)

#define BT\_GATT\_DESCRIPTOR(\_uuid, \_perm, \_read, \_write, \_user\_data)

Descriptor Declaration Macro.

**Definition** gatt.h:1285

[BT\_GATT\_PERM\_READ](group__bt__gatt.md#gga96e57500d2340a45badb23701cc43833a9afb838c2cef657e9cd035ef27521f17)

@ BT\_GATT\_PERM\_READ

Attribute read permission.

**Definition** gatt.h:45

[BT\_UUID\_GATT\_CEP](group__bt__uuid.md#ga6aa143b721d810f1536d7431a9bf7cc7)

#define BT\_UUID\_GATT\_CEP

GATT Characteristic Extended Properties.

**Definition** uuid.h:868

Characteristic Extended Properties Declaration Macro.

Helper macro to declare a CEP attribute.

Parameters
:   | \_value | Pointer to a struct [bt\_gatt\_cep](structbt__gatt__cep.md "Characteristic Extended Properties Attribute Value."). |
    | --- | --- |

## [◆ ](#ga9e739546dbd906d3b3c4f1ed5ad9f41e)BT\_GATT\_CHARACTERISTIC

| #define BT\_GATT\_CHARACTERISTIC | ( |  | *\_uuid*, |
| --- | --- | --- | --- |
|  |  |  | *\_props*, |
|  |  |  | *\_perm*, |
|  |  |  | *\_read*, |
|  |  |  | *\_write*, |
|  |  |  | *\_user\_data* ) |

`#include <[gatt.h](gatt_8h.md)>`

**Value:**

[BT\_GATT\_ATTRIBUTE](#gac4abfeb068d16dcdaceee812c12bf406)([BT\_UUID\_GATT\_CHRC](group__bt__uuid.md#gadcedbbe1c432c4ac737e54b318e01a0f), [BT\_GATT\_PERM\_READ](group__bt__gatt.md#gga96e57500d2340a45badb23701cc43833a9afb838c2cef657e9cd035ef27521f17), \

[bt\_gatt\_attr\_read\_chrc](#gad58b526a06334530c13292d14a11257c), [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4), \

((struct [bt\_gatt\_chrc](structbt__gatt__chrc.md)[]) { \

BT\_GATT\_CHRC\_INIT(\_uuid, 0U, \_props), \

})), \

[BT\_GATT\_ATTRIBUTE](#gac4abfeb068d16dcdaceee812c12bf406)(\_uuid, \_perm, \_read, \_write, \_user\_data)

[bt\_gatt\_attr\_read\_chrc](#gad58b526a06334530c13292d14a11257c)

ssize\_t bt\_gatt\_attr\_read\_chrc(struct bt\_conn \*conn, const struct bt\_gatt\_attr \*attr, void \*buf, uint16\_t len, uint16\_t offset)

Read Characteristic Attribute helper.

[BT\_UUID\_GATT\_CHRC](group__bt__uuid.md#gadcedbbe1c432c4ac737e54b318e01a0f)

#define BT\_UUID\_GATT\_CHRC

GATT Characteristic.

**Definition** uuid.h:859

[bt\_gatt\_chrc](structbt__gatt__chrc.md)

Attribute Value of a Characteristic Declaration.

**Definition** gatt.h:480

Characteristic and Value Declaration Macro.

Helper macro to declare a characteristic attribute along with its attribute value.

Parameters
:   | \_uuid | Characteristic attribute uuid. |
    | --- | --- |
    | \_props | Characteristic attribute properties, a bitmap of BT\_GATT\_CHRC\_\* macros. |
    | \_perm | Characteristic Attribute access permissions, a bitmap of [bt\_gatt\_perm](group__bt__gatt.md#ga96e57500d2340a45badb23701cc43833 "bt_gatt_perm") values. |
    | \_read | Characteristic Attribute read callback ([bt\_gatt\_attr\_read\_func\_t](group__bt__gatt.md#ga57e36bf94652531964fd4237c203fe7b "bt_gatt_attr_read_func_t")). |
    | \_write | Characteristic Attribute write callback ([bt\_gatt\_attr\_write\_func\_t](group__bt__gatt.md#ga3fd8527a0f3e8f3699dc0d3b0339eba1 "bt_gatt_attr_write_func_t")). |
    | \_user\_data | Characteristic Attribute user data. |

## [◆ ](#ga7f19592a722c41d6c1d2421d166dd78a)BT\_GATT\_CHRC\_INIT

| #define BT\_GATT\_CHRC\_INIT | ( |  | *\_uuid*, |
| --- | --- | --- | --- |
|  |  |  | *\_handle*, |
|  |  |  | *\_props* ) |

`#include <[gatt.h](gatt_8h.md)>`

**Value:**

{ \

.uuid = \_uuid, \

.value\_handle = \_handle, \

.properties = \_props, \

}

Gatt Characterisitc Initialization Macro.

Helper macro used within the [BT\_GATT\_CHARACTERISTIC](#ga9e739546dbd906d3b3c4f1ed5ad9f41e) macro in the GATT attribute declaration to set the attribute user data.

Parameters
:   | \_uuid | Characteristic attribute uuid. |
    | --- | --- |
    | \_handle | Characcteristic attribute handle at init. |
    | \_props | Characteristic attribute properties, a bitmap of BT\_GATT\_CHRC\_\* macros. |

## [◆ ](#ga3835fcfdf7a5f917e21c9d17e75162be)BT\_GATT\_CPF

| #define BT\_GATT\_CPF | ( |  | *\_value* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[gatt.h](gatt_8h.md)>`

**Value:**

[BT\_GATT\_DESCRIPTOR](#ga83207fc083454327004f7d3c3e5b3840)([BT\_UUID\_GATT\_CPF](group__bt__uuid.md#ga331a61702ffe9b15bac0de3d60414022), [BT\_GATT\_PERM\_READ](group__bt__gatt.md#gga96e57500d2340a45badb23701cc43833a9afb838c2cef657e9cd035ef27521f17), \

[bt\_gatt\_attr\_read\_cpf](#ga5ae96590a0aaa5c4c3863a4a14d80fdd), [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4), (void \*)\_value)

[bt\_gatt\_attr\_read\_cpf](#ga5ae96590a0aaa5c4c3863a4a14d80fdd)

ssize\_t bt\_gatt\_attr\_read\_cpf(struct bt\_conn \*conn, const struct bt\_gatt\_attr \*attr, void \*buf, uint16\_t len, uint16\_t offset)

Read Characteristic Presentation format Descriptor Attribute helper.

[BT\_UUID\_GATT\_CPF](group__bt__uuid.md#ga331a61702ffe9b15bac0de3d60414022)

#define BT\_UUID\_GATT\_CPF

GATT Characteristic Presentation Format.

**Definition** uuid.h:904

Characteristic Presentation Format Descriptor Declaration Macro.

Helper macro to declare a CPF attribute.

Parameters
:   | \_value | Pointer to a struct [bt\_gatt\_cpf](structbt__gatt__cpf.md "GATT Characteristic Presentation Format Attribute Value."). |
    | --- | --- |

## [◆ ](#ga1e1cd9d0853e2dcbefcb85fda44dc9c7)BT\_GATT\_CUD

| #define BT\_GATT\_CUD | ( |  | *\_value*, |
| --- | --- | --- | --- |
|  |  |  | *\_perm* ) |

`#include <[gatt.h](gatt_8h.md)>`

**Value:**

[BT\_GATT\_DESCRIPTOR](#ga83207fc083454327004f7d3c3e5b3840)([BT\_UUID\_GATT\_CUD](group__bt__uuid.md#gaaaf94f5d918a1b6715cf4816b03875a2), \_perm, [bt\_gatt\_attr\_read\_cud](#ga29421c8788b47b6a648704d27d5f0d28), \

[NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4), (void \*)\_value)

[bt\_gatt\_attr\_read\_cud](#ga29421c8788b47b6a648704d27d5f0d28)

ssize\_t bt\_gatt\_attr\_read\_cud(struct bt\_conn \*conn, const struct bt\_gatt\_attr \*attr, void \*buf, uint16\_t len, uint16\_t offset)

Read Characteristic User Description Descriptor Attribute helper.

[BT\_UUID\_GATT\_CUD](group__bt__uuid.md#gaaaf94f5d918a1b6715cf4816b03875a2)

#define BT\_UUID\_GATT\_CUD

GATT Characteristic User Description.

**Definition** uuid.h:877

Characteristic User Format Descriptor Declaration Macro.

Helper macro to declare a CUD attribute.

Parameters
:   | \_value | User description NULL-terminated C string. |
    | --- | --- |
    | \_perm | Descriptor attribute access permissions, a bitmap of [bt\_gatt\_perm](group__bt__gatt.md#ga96e57500d2340a45badb23701cc43833 "bt_gatt_perm") values. |

## [◆ ](#ga83207fc083454327004f7d3c3e5b3840)BT\_GATT\_DESCRIPTOR

| #define BT\_GATT\_DESCRIPTOR | ( |  | *\_uuid*, |
| --- | --- | --- | --- |
|  |  |  | *\_perm*, |
|  |  |  | *\_read*, |
|  |  |  | *\_write*, |
|  |  |  | *\_user\_data* ) |

`#include <[gatt.h](gatt_8h.md)>`

**Value:**

[BT\_GATT\_ATTRIBUTE](#gac4abfeb068d16dcdaceee812c12bf406)(\_uuid, \_perm, \_read, \_write, \_user\_data)

Descriptor Declaration Macro.

Helper macro to declare a descriptor attribute.

Parameters
:   | \_uuid | Descriptor attribute uuid. |
    | --- | --- |
    | \_perm | Descriptor attribute access permissions, a bitmap of [bt\_gatt\_perm](group__bt__gatt.md#ga96e57500d2340a45badb23701cc43833 "bt_gatt_perm") values. |
    | \_read | Descriptor attribute read callback ([bt\_gatt\_attr\_read\_func\_t](group__bt__gatt.md#ga57e36bf94652531964fd4237c203fe7b "bt_gatt_attr_read_func_t")). |
    | \_write | Descriptor attribute write callback ([bt\_gatt\_attr\_write\_func\_t](group__bt__gatt.md#ga3fd8527a0f3e8f3699dc0d3b0339eba1 "bt_gatt_attr_write_func_t")). |
    | \_user\_data | Descriptor attribute user data. |

## [◆ ](#ga08ffee706d271b75a54b1b99249dba24)BT\_GATT\_INCLUDE\_SERVICE

| #define BT\_GATT\_INCLUDE\_SERVICE | ( |  | *\_service\_incl* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[gatt.h](gatt_8h.md)>`

**Value:**

[BT\_GATT\_ATTRIBUTE](#gac4abfeb068d16dcdaceee812c12bf406)([BT\_UUID\_GATT\_INCLUDE](group__bt__uuid.md#ga995596ff7374ebcb44d4706bc16234e4), [BT\_GATT\_PERM\_READ](group__bt__gatt.md#gga96e57500d2340a45badb23701cc43833a9afb838c2cef657e9cd035ef27521f17), \

[bt\_gatt\_attr\_read\_included](#ga4313a63decac2c8b7c4a1764df3d53ea), [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4), \_service\_incl)

[bt\_gatt\_attr\_read\_included](#ga4313a63decac2c8b7c4a1764df3d53ea)

ssize\_t bt\_gatt\_attr\_read\_included(struct bt\_conn \*conn, const struct bt\_gatt\_attr \*attr, void \*buf, uint16\_t len, uint16\_t offset)

Read Include Attribute helper.

[BT\_UUID\_GATT\_INCLUDE](group__bt__uuid.md#ga995596ff7374ebcb44d4706bc16234e4)

#define BT\_UUID\_GATT\_INCLUDE

GATT Include Service.

**Definition** uuid.h:850

Include Service Declaration Macro.

Helper macro to declare database internal include service attribute.

Parameters
:   | \_service\_incl | the first service attribute of service to include |
    | --- | --- |

## [◆ ](#gaacada0ff1029af959b6fcd6703d4a0bf)BT\_GATT\_PRIMARY\_SERVICE

| #define BT\_GATT\_PRIMARY\_SERVICE | ( |  | *\_service* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[gatt.h](gatt_8h.md)>`

**Value:**

[BT\_GATT\_ATTRIBUTE](#gac4abfeb068d16dcdaceee812c12bf406)([BT\_UUID\_GATT\_PRIMARY](group__bt__uuid.md#ga6e87ce1575494eb90358e074e8dbe276), [BT\_GATT\_PERM\_READ](group__bt__gatt.md#gga96e57500d2340a45badb23701cc43833a9afb838c2cef657e9cd035ef27521f17), \

[bt\_gatt\_attr\_read\_service](#gacae81c0f272bad7e6ac93c0d13b678c6), [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4), (void \*)\_service)

[bt\_gatt\_attr\_read\_service](#gacae81c0f272bad7e6ac93c0d13b678c6)

ssize\_t bt\_gatt\_attr\_read\_service(struct bt\_conn \*conn, const struct bt\_gatt\_attr \*attr, void \*buf, uint16\_t len, uint16\_t offset)

Read Service Attribute helper.

[BT\_UUID\_GATT\_PRIMARY](group__bt__uuid.md#ga6e87ce1575494eb90358e074e8dbe276)

#define BT\_UUID\_GATT\_PRIMARY

GATT Primary Service.

**Definition** uuid.h:832

Primary Service Declaration Macro.

Helper macro to declare a primary service attribute.

Parameters
:   | \_service | Service attribute value. |
    | --- | --- |

## [◆ ](#gaecb4d30282677d3450ad79c5f83f3445)BT\_GATT\_SECONDARY\_SERVICE

| #define BT\_GATT\_SECONDARY\_SERVICE | ( |  | *\_service* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[gatt.h](gatt_8h.md)>`

**Value:**

[BT\_GATT\_ATTRIBUTE](#gac4abfeb068d16dcdaceee812c12bf406)([BT\_UUID\_GATT\_SECONDARY](group__bt__uuid.md#gad084d3658e663b6b8e200be256c54cdb), [BT\_GATT\_PERM\_READ](group__bt__gatt.md#gga96e57500d2340a45badb23701cc43833a9afb838c2cef657e9cd035ef27521f17), \

[bt\_gatt\_attr\_read\_service](#gacae81c0f272bad7e6ac93c0d13b678c6), [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4), (void \*)\_service)

[BT\_UUID\_GATT\_SECONDARY](group__bt__uuid.md#gad084d3658e663b6b8e200be256c54cdb)

#define BT\_UUID\_GATT\_SECONDARY

GATT Secondary Service.

**Definition** uuid.h:841

Secondary Service Declaration Macro.

Helper macro to declare a secondary service attribute.

Note
:   A secondary service is only intended to be included from a primary service or another secondary service or other higher layer specification.

Parameters
:   | \_service | Service attribute value. |
    | --- | --- |

## [◆ ](#ga7d413ec013b91a633ec24d80d2814e2b)BT\_GATT\_SERVICE

| #define BT\_GATT\_SERVICE | ( |  | *\_attrs* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[gatt.h](gatt_8h.md)>`

**Value:**

{ \

.attrs = \_attrs, \

.attr\_count = [ARRAY\_SIZE](group__sys-util.md#ga70c57aae3eb654e205459b4362c8089a)(\_attrs), \

}

[ARRAY\_SIZE](group__sys-util.md#ga70c57aae3eb654e205459b4362c8089a)

#define ARRAY\_SIZE(array)

Number of elements in the given array.

**Definition** util.h:120

Service Structure Declaration Macro.

Helper macro to declare a service structure.

Parameters
:   | \_attrs | Service attributes. |
    | --- | --- |

## [◆ ](#ga04c7887fb67107bd060dd023fd3186d5)BT\_GATT\_SERVICE\_DEFINE

| #define BT\_GATT\_SERVICE\_DEFINE | ( |  | *\_name*, |
| --- | --- | --- | --- |
|  |  |  | ... ) |

`#include <[gatt.h](gatt_8h.md)>`

**Value:**

const struct [bt\_gatt\_attr](structbt__gatt__attr.md) attr\_##\_name[] = { \_\_VA\_ARGS\_\_ }; \

const [STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)([bt\_gatt\_service\_static](structbt__gatt__service__static.md), \_name) = \

BT\_GATT\_SERVICE(attr\_##\_name)

[STRUCT\_SECTION\_ITERABLE](group__iterable__section__apis.md#ga9104f42cbe4a67a931bed7f7cc8f600f)

#define STRUCT\_SECTION\_ITERABLE(struct\_type, varname)

Defines a new element for an iterable section.

**Definition** iterable\_sections.h:216

[bt\_gatt\_attr](structbt__gatt__attr.md)

GATT Attribute.

**Definition** gatt.h:227

[bt\_gatt\_service\_static](structbt__gatt__service__static.md)

Static GATT Service structure.

**Definition** gatt.h:318

Statically define and register a service.

Helper macro to statically define and register a service.

Parameters
:   | \_name | Service name. |
    | --- | --- |

## [◆ ](#ga8bb3aeef20465d7f6e38f6bbddef74e5)BT\_GATT\_SERVICE\_INSTANCE\_DEFINE

| #define BT\_GATT\_SERVICE\_INSTANCE\_DEFINE | ( |  | *\_name*, |
| --- | --- | --- | --- |
|  |  |  | *\_instances*, |
|  |  |  | *\_instance\_num*, |
|  |  |  | *\_attrs\_def* ) |

`#include <[gatt.h](gatt_8h.md)>`

**Value:**

BUILD\_ASSERT([ARRAY\_SIZE](group__sys-util.md#ga70c57aae3eb654e205459b4362c8089a)(\_instances) == \_instance\_num, \

"The number of array elements does not match its size"); \

LISTIFY(\_instance\_num, \_BT\_GATT\_ATTRS\_ARRAY\_DEFINE, (;), \

\_instances, \_attrs\_def); \

static struct [bt\_gatt\_service](structbt__gatt__service.md) \_name[] = { \

LISTIFY(\_instance\_num, \_BT\_GATT\_SERVICE\_ARRAY\_ITEM, (,)) \

}

[bt\_gatt\_service](structbt__gatt__service.md)

GATT Service structure.

**Definition** gatt.h:331

Statically define service structure array.

Helper macro to statically define service structure array. Each element of the array is linked to the service attribute array which is also defined in this scope using \_attrs\_def macro.

Parameters
:   | \_name | Name of service structure array. |
    | --- | --- |
    | \_instances | Array of instances to pass as user context to the attribute callbacks. |
    | \_instance\_num | Number of elements in instance array. |
    | \_attrs\_def | Macro provided by the user that defines attribute array for the service. This macro should accept single parameter which is the instance context. |

## Typedef Documentation

## [◆ ](#ga60284611c90729b289fe806524ba9209)bt\_gatt\_attr\_func\_t

| typedef [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)(\* bt\_gatt\_attr\_func\_t) (const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \*attr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) handle, void \*user\_data) |
| --- |

`#include <[gatt.h](gatt_8h.md)>`

Attribute iterator callback.

Parameters
:   | attr | Attribute found. |
    | --- | --- |
    | handle | Attribute handle found. |
    | user\_data | Data given. |

Returns
:   [BT\_GATT\_ITER\_CONTINUE](#gga11c5a2eb0b62de9a2493ad5335fae383aea569feffa4815d3443e12be78c684f5) if should continue to the next attribute.
:   [BT\_GATT\_ITER\_STOP](#gga11c5a2eb0b62de9a2493ad5335fae383aa3f2a25e27c7065a2c7bb2a9ff09542e) to stop.

## [◆ ](#gac55832607b95f394d26a64ed1cfe5bba)bt\_gatt\_complete\_func\_t

| typedef void(\* bt\_gatt\_complete\_func\_t) (struct bt\_conn \*conn, void \*user\_data) |
| --- |

`#include <[gatt.h](gatt_8h.md)>`

Notification complete result callback.

Parameters
:   | conn | Connection object. |
    | --- | --- |
    | user\_data | Data passed in by the user. |

## [◆ ](#ga1294850e6bdcbe7a8f42f2956fd837a8)bt\_gatt\_indicate\_func\_t

| typedef void(\* bt\_gatt\_indicate\_func\_t) (struct bt\_conn \*conn, struct [bt\_gatt\_indicate\_params](structbt__gatt__indicate__params.md) \*params, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) err) |
| --- |

`#include <[gatt.h](gatt_8h.md)>`

Indication complete result callback.

Parameters
:   | conn | Connection object. |
    | --- | --- |
    | params | Indication params object. |
    | err | ATT error code |

## [◆ ](#ga5d47ed9eaea22c8f00db14329daee8fe)bt\_gatt\_indicate\_params\_destroy\_t

| typedef void(\* bt\_gatt\_indicate\_params\_destroy\_t) (struct [bt\_gatt\_indicate\_params](structbt__gatt__indicate__params.md) \*params) |
| --- |

`#include <[gatt.h](gatt_8h.md)>`

Callback to destroy or clean up the GATT Indicate Value parameters.

This callback function is invoked to clean up any resources associated with the [bt\_gatt\_indicate\_params](structbt__gatt__indicate__params.md "GATT Indicate Value parameters.") structure once the GATT indication operation is completed.

Parameters
:   | params | Pointer to the GATT Indicate parameters structure to be cleaned up. |
    | --- | --- |

## Enumeration Type Documentation

## [◆ ](#ga11c5a2eb0b62de9a2493ad5335fae383)anonymous enum

| anonymous enum |
| --- |

`#include <[gatt.h](gatt_8h.md)>`

to be used as return values for [bt\_gatt\_attr\_func\_t](#ga60284611c90729b289fe806524ba9209) and [bt\_gatt\_read\_func\_t](group__bt__gatt__client.md#ga1ca94b4f2b6c456b6134e05127993569 "bt_gatt_read_func_t") type callbacks.

| Enumerator | |
| --- | --- |
| BT\_GATT\_ITER\_STOP |  |
| BT\_GATT\_ITER\_CONTINUE |  |

## Function Documentation

## [◆ ](#ga2d51136ea1bd6cdb50900639506fd9f7)bt\_gatt\_attr\_get\_handle()

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_gatt\_attr\_get\_handle | ( | const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \* | *attr* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[gatt.h](gatt_8h.md)>`

Get Attribute handle.

Parameters
:   | attr | An attribute object currently registered in the local ATT server. |
    | --- | --- |

Returns
:   Handle of the corresponding attribute or zero if the attribute could not be found.

## [◆ ](#ga35cecaa43b00b374062d29cca1479d85)bt\_gatt\_attr\_next()

| struct [bt\_gatt\_attr](structbt__gatt__attr.md) \* bt\_gatt\_attr\_next | ( | const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \* | *attr* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[gatt.h](gatt_8h.md)>`

Iterate to the next attribute.

Iterate to the next attribute following a given attribute.

Parameters
:   | attr | Current Attribute. |
    | --- | --- |

Returns
:   The next attribute or NULL if it cannot be found.

## [◆ ](#gaf6d253849932b706ec7f303568980dfa)bt\_gatt\_attr\_read()

| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) bt\_gatt\_attr\_read | ( | struct bt\_conn \* | *conn*, |
| --- | --- | --- | --- |
|  |  | const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \* | *attr*, |
|  |  | void \* | *buf*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *buf\_len*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *offset*, |
|  |  | const void \* | *value*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *value\_len* ) |

`#include <[gatt.h](gatt_8h.md)>`

Generic Read Attribute value helper.

Read attribute value from local database storing the result into buffer.

Parameters
:   | conn | Connection object. |
    | --- | --- |
    | attr | Attribute to read. |
    | buf | Buffer to store the value. |
    | buf\_len | Buffer length. |
    | offset | Start offset. |
    | value | Attribute value. |
    | value\_len | Length of the attribute value. |

Returns
:   number of bytes read in case of success or negative values in case of error.

## [◆ ](#ga2e85b42136e2c6a4cb5b7ad8a2532573)bt\_gatt\_attr\_read\_ccc()

| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) bt\_gatt\_attr\_read\_ccc | ( | struct bt\_conn \* | *conn*, |
| --- | --- | --- | --- |
|  |  | const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \* | *attr*, |
|  |  | void \* | *buf*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *len*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *offset* ) |

`#include <[gatt.h](gatt_8h.md)>`

Read Client Characteristic Configuration Attribute helper.

Read CCC attribute value from local database storing the result into buffer after encoding it.

Parameters
:   | conn | Connection object. |
    | --- | --- |
    | attr | Attribute to read. |
    | buf | Buffer to store the value read. |
    | len | Buffer length. |
    | offset | Start offset. |

Returns
:   number of bytes read in case of success or negative values in case of error.

## [◆ ](#ga5893166f1b24f437a94ccf1fc57c7917)bt\_gatt\_attr\_read\_cep()

| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) bt\_gatt\_attr\_read\_cep | ( | struct bt\_conn \* | *conn*, |
| --- | --- | --- | --- |
|  |  | const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \* | *attr*, |
|  |  | void \* | *buf*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *len*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *offset* ) |

`#include <[gatt.h](gatt_8h.md)>`

Read Characteristic Extended Properties Attribute helper.

Read CEP attribute value from local database storing the result into buffer after encoding it.

Note
:   Only use this with attributes which user\_data is a [bt\_gatt\_cep](structbt__gatt__cep.md "Characteristic Extended Properties Attribute Value.").

Parameters
:   | conn | Connection object |
    | --- | --- |
    | attr | Attribute to read |
    | buf | Buffer to store the value read |
    | len | Buffer length |
    | offset | Start offset |

Returns
:   number of bytes read in case of success or negative values in case of error.

## [◆ ](#gad58b526a06334530c13292d14a11257c)bt\_gatt\_attr\_read\_chrc()

| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) bt\_gatt\_attr\_read\_chrc | ( | struct bt\_conn \* | *conn*, |
| --- | --- | --- | --- |
|  |  | const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \* | *attr*, |
|  |  | void \* | *buf*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *len*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *offset* ) |

`#include <[gatt.h](gatt_8h.md)>`

Read Characteristic Attribute helper.

Read characteristic attribute value from local database storing the result into buffer after encoding it.

Note
:   Only use this with attributes which user\_data is a [bt\_gatt\_chrc](structbt__gatt__chrc.md "Attribute Value of a Characteristic Declaration.").

Parameters
:   | conn | Connection object. |
    | --- | --- |
    | attr | Attribute to read. |
    | buf | Buffer to store the value read. |
    | len | Buffer length. |
    | offset | Start offset. |

Returns
:   number of bytes read in case of success or negative values in case of error.

## [◆ ](#ga5ae96590a0aaa5c4c3863a4a14d80fdd)bt\_gatt\_attr\_read\_cpf()

| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) bt\_gatt\_attr\_read\_cpf | ( | struct bt\_conn \* | *conn*, |
| --- | --- | --- | --- |
|  |  | const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \* | *attr*, |
|  |  | void \* | *buf*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *len*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *offset* ) |

`#include <[gatt.h](gatt_8h.md)>`

Read Characteristic Presentation format Descriptor Attribute helper.

Read CPF attribute value from local database storing the result into buffer after encoding it.

Note
:   Only use this with attributes which user\_data is a [bt\_gatt\_cpf](structbt__gatt__cpf.md "bt_gatt_cpf").

Parameters
:   | conn | Connection object |
    | --- | --- |
    | attr | Attribute to read |
    | buf | Buffer to store the value read |
    | len | Buffer length |
    | offset | Start offset |

Returns
:   number of bytes read in case of success or negative values in case of error.

## [◆ ](#ga29421c8788b47b6a648704d27d5f0d28)bt\_gatt\_attr\_read\_cud()

| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) bt\_gatt\_attr\_read\_cud | ( | struct bt\_conn \* | *conn*, |
| --- | --- | --- | --- |
|  |  | const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \* | *attr*, |
|  |  | void \* | *buf*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *len*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *offset* ) |

`#include <[gatt.h](gatt_8h.md)>`

Read Characteristic User Description Descriptor Attribute helper.

Read CUD attribute value from local database storing the result into buffer after encoding it.

Note
:   Only use this with attributes which user\_data is a NULL-terminated C string.

Parameters
:   | conn | Connection object |
    | --- | --- |
    | attr | Attribute to read |
    | buf | Buffer to store the value read |
    | len | Buffer length |
    | offset | Start offset |

Returns
:   number of bytes read in case of success or negative values in case of error.

## [◆ ](#ga4313a63decac2c8b7c4a1764df3d53ea)bt\_gatt\_attr\_read\_included()

| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) bt\_gatt\_attr\_read\_included | ( | struct bt\_conn \* | *conn*, |
| --- | --- | --- | --- |
|  |  | const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \* | *attr*, |
|  |  | void \* | *buf*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *len*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *offset* ) |

`#include <[gatt.h](gatt_8h.md)>`

Read Include Attribute helper.

Read include service attribute value from local database storing the result into buffer after encoding it.

Note
:   Only use this with attributes which user\_data is a [bt\_gatt\_include](structbt__gatt__include.md "Include Attribute Value.").

Parameters
:   | conn | Connection object. |
    | --- | --- |
    | attr | Attribute to read. |
    | buf | Buffer to store the value read. |
    | len | Buffer length. |
    | offset | Start offset. |

Returns
:   number of bytes read in case of success or negative values in case of error.

## [◆ ](#gacae81c0f272bad7e6ac93c0d13b678c6)bt\_gatt\_attr\_read\_service()

| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) bt\_gatt\_attr\_read\_service | ( | struct bt\_conn \* | *conn*, |
| --- | --- | --- | --- |
|  |  | const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \* | *attr*, |
|  |  | void \* | *buf*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *len*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *offset* ) |

`#include <[gatt.h](gatt_8h.md)>`

Read Service Attribute helper.

Read service attribute value from local database storing the result into buffer after encoding it.

Note
:   Only use this with attributes which user\_data is a [bt\_uuid](structbt__uuid.md "This is a 'tentative' type and should be used as a pointer only.").

Parameters
:   | conn | Connection object. |
    | --- | --- |
    | attr | Attribute to read. |
    | buf | Buffer to store the value read. |
    | len | Buffer length. |
    | offset | Start offset. |

Returns
:   number of bytes read in case of success or negative values in case of error.

## [◆ ](#ga99738cf4f05eae4c6da17cc3420827d8)bt\_gatt\_attr\_value\_handle()

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_gatt\_attr\_value\_handle | ( | const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \* | *attr* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[gatt.h](gatt_8h.md)>`

Get the handle of the characteristic value descriptor.

Parameters
:   | attr | A Characteristic Attribute. |
    | --- | --- |

Note
:   The user\_data of the attribute must be of type [bt\_gatt\_chrc](structbt__gatt__chrc.md "bt_gatt_chrc") and the uuid shall be BT\_UUID\_GATT\_CHRC.

Returns
:   the handle of the corresponding Characteristic Value. The value will be zero (the invalid handle) if `attr` was not a characteristic attribute.

## [◆ ](#gabba965b676650a55cb9934072b34c75e)bt\_gatt\_attr\_write\_ccc()

| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) bt\_gatt\_attr\_write\_ccc | ( | struct bt\_conn \* | *conn*, |
| --- | --- | --- | --- |
|  |  | const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \* | *attr*, |
|  |  | const void \* | *buf*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *len*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *offset*, |
|  |  | [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | *flags* ) |

`#include <[gatt.h](gatt_8h.md)>`

Write Client Characteristic Configuration Attribute helper.

Write value in the buffer into CCC attribute.

Parameters
:   | conn | Connection object. |
    | --- | --- |
    | attr | Attribute to read. |
    | buf | Buffer to store the value read. |
    | len | Buffer length. |
    | offset | Start offset. |
    | [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9) | Write flags, see [bt\_gatt\_attr\_write\_flag](group__bt__gatt.md#ga830d437c8d0757f53af1de6aa3031906 "bt_gatt_attr_write_flag"). |

Returns
:   number of bytes written in case of success or negative values in case of error.

## [◆ ](#ga5eee6afc6db391ffeda295d298bf6a56)bt\_gatt\_authorization\_cb\_register()

| int bt\_gatt\_authorization\_cb\_register | ( | const struct [bt\_gatt\_authorization\_cb](structbt__gatt__authorization__cb.md) \* | *cb* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[gatt.h](gatt_8h.md)>`

Register GATT authorization callbacks.

Register callbacks to perform application-specific authorization of GATT operations on all registered GATT attributes. The callback structure must remain valid throughout the entire duration of the Bluetooth subsys activity.

The `CONFIG_BT_GATT_AUTHORIZATION_CUSTOM` Kconfig must be enabled to make this API functional.

This API allows the user to register only one callback structure concurrently. Passing NULL unregisters the previous set of callbacks and makes it possible to register a new one.

Parameters
:   | cb | Callback struct. |
    | --- | --- |

Returns
:   Zero on success or negative error code otherwise.

## [◆ ](#ga270c8a52bf3d512defc373f8c29b59f2)bt\_gatt\_cb\_register()

| void bt\_gatt\_cb\_register | ( | struct [bt\_gatt\_cb](structbt__gatt__cb.md) \* | *cb* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[gatt.h](gatt_8h.md)>`

Register GATT callbacks.

Register callbacks to monitor the state of GATT. The callback struct must remain valid for the remainder of the program.

Parameters
:   | cb | Callback struct. |
    | --- | --- |

## [◆ ](#gaf6d3f1e904f1a847afeb30236bad98a2)bt\_gatt\_err\_to\_str()

| | const char \* bt\_gatt\_err\_to\_str | ( | int | *gatt\_err* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[gatt.h](gatt_8h.md)>`

Converts a GATT error to string.

The GATT errors are created with [BT\_GATT\_ERR](group__bt__gatt.md#gaff31756c1bf8ee755e65b1e0fb689bb7 "BT_GATT_ERR").

The error codes are described in the Bluetooth Core specification, Vol 3, Part F, Section 3.4.1.1.

The ATT and GATT documentation found in Vol 4, Part F and Part G describe when the different error codes are used.

See also the defined BT\_ATT\_ERR\_\* macros.

Returns
:   The string representation of the GATT error code. If `CONFIG_BT_ATT_ERR_TO_STR` is not enabled, this just returns the empty string.

## [◆ ](#gad2f3272b1dc42378104b492ec7caf6b0)bt\_gatt\_find\_by\_uuid()

| struct [bt\_gatt\_attr](structbt__gatt__attr.md) \* bt\_gatt\_find\_by\_uuid | ( | const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \* | *attr*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *attr\_count*, |
|  |  | const struct [bt\_uuid](structbt__uuid.md) \* | *uuid* ) |

`#include <[gatt.h](gatt_8h.md)>`

Find Attribute by UUID.

Find the attribute with the matching UUID. To limit the search to a service set the attr to the service attributes and the attr\_count to the service attribute count .

Parameters
:   | attr | Pointer to an attribute that serves as the starting point for the search of a match for the UUID. Passing NULL will search the entire range. |
    | --- | --- |
    | attr\_count | The number of attributes from the starting point to search for a match for the UUID. Set to 0 to search until the end. |
    | uuid | UUID to match. |

## [◆ ](#gaa93b5e0f2870ed135447bead903c175a)bt\_gatt\_foreach\_attr()

| | void bt\_gatt\_foreach\_attr | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *start\_handle*, | | --- | --- | --- | --- | |  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *end\_handle*, | |  |  | [bt\_gatt\_attr\_func\_t](#ga60284611c90729b289fe806524ba9209) | *func*, | |  |  | void \* | *user\_data* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[gatt.h](gatt_8h.md)>`

Attribute iterator.

Iterate attributes in the given range.

Parameters
:   | start\_handle | Start handle. |
    | --- | --- |
    | end\_handle | End handle. |
    | func | Callback function. |
    | user\_data | Data to pass to the callback. |

## [◆ ](#gad8d8f513004f391167212d7bf9f7ff10)bt\_gatt\_foreach\_attr\_type()

| void bt\_gatt\_foreach\_attr\_type | ( | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *start\_handle*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *end\_handle*, |
|  |  | const struct [bt\_uuid](structbt__uuid.md) \* | *uuid*, |
|  |  | const void \* | *attr\_data*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *num\_matches*, |
|  |  | [bt\_gatt\_attr\_func\_t](#ga60284611c90729b289fe806524ba9209) | *func*, |
|  |  | void \* | *user\_data* ) |

`#include <[gatt.h](gatt_8h.md)>`

Attribute iterator by type.

Iterate attributes in the given range matching given UUID and/or data.

Parameters
:   | start\_handle | Start handle. |
    | --- | --- |
    | end\_handle | End handle. Often set to start\_handle + attr\_count or BT\_ATT\_LAST\_ATTRIBUTE\_HANDLE. |
    | uuid | UUID to match, passing NULL skips UUID matching. |
    | attr\_data | Attribute data to match, passing NULL skips data matching. |
    | num\_matches | Number matches, passing 0 makes it unlimited. |
    | func | Callback function. |
    | user\_data | Data to pass to the callback. |

## [◆ ](#ga351fd7658eaecbbfa60f1769119ef733)bt\_gatt\_get\_mtu()

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_gatt\_get\_mtu | ( | struct bt\_conn \* | *conn* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[gatt.h](gatt_8h.md)>`

Get ATT MTU for a connection.

Get negotiated ATT connection MTU, note that this does not equal the largest amount of attribute data that can be transferred within a single packet.

Parameters
:   | conn | Connection object. |
    | --- | --- |

Returns
:   MTU in bytes

## [◆ ](#ga6653de5e245cae6dc12cd0b45acbe028)bt\_gatt\_get\_uatt\_mtu()

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_gatt\_get\_uatt\_mtu | ( | struct bt\_conn \* | *conn* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[gatt.h](gatt_8h.md)>`

Get Unenhanced ATT (UATT) MTU for a connection.

Get UATT connection MTU.

The ATT\_MTU defines the largest size of an ATT PDU, encompassing the ATT opcode, additional fields, and any attribute value payload. Consequently, the maximum size of a value payload is less and varies based on the type of ATT PDU. For example, in an ATT\_HANDLE\_VALUE\_NTF PDU, the Attribute Value field can contain up to ATT\_MTU - 3 octets (size of opcode and handle).

Parameters
:   | conn | Connection object. |
    | --- | --- |

Returns
:   0 if `conn` does not have an UATT ATT\_MTU (e.g: disconnected).
:   Current UATT ATT\_MTU.

## [◆ ](#ga4f2272692cc0f1d44638828012296c80)bt\_gatt\_indicate()

| int bt\_gatt\_indicate | ( | struct bt\_conn \* | *conn*, |
| --- | --- | --- | --- |
|  |  | struct [bt\_gatt\_indicate\_params](structbt__gatt__indicate__params.md) \* | *params* ) |

`#include <[gatt.h](gatt_8h.md)>`

Indicate attribute value change.

Send an indication of attribute value change. if connection is NULL indicate all peer that have notification enabled via CCC otherwise do a direct indication only the given connection.

The attribute object on the parameters can be the so called Characteristic Declaration, which is usually declared with BT\_GATT\_CHARACTERISTIC followed by BT\_GATT\_CCC, or the Characteristic Value Declaration which is automatically created after the Characteristic Declaration when using BT\_GATT\_CHARACTERISTIC.

Alternatively it is possible to indicate by UUID by setting it on the parameters, when using this method the attribute if provided is used as the start range when looking up for possible matches.

Note
:   This procedure is asynchronous therefore the parameters need to remains valid while it is active. The procedure is active until the destroy callback is run.

Parameters
:   | conn | Connection object. |
    | --- | --- |
    | params | Indicate parameters. |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#gabd4df0a264dae10e43797992a567be7d)bt\_gatt\_is\_subscribed()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) bt\_gatt\_is\_subscribed | ( | struct bt\_conn \* | *conn*, |
| --- | --- | --- | --- |
|  |  | const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \* | *attr*, |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *ccc\_type* ) |

`#include <[gatt.h](gatt_8h.md)>`

Check if connection have subscribed to attribute.

Check if the connection has subscribed to an attribute value change.

The attribute object can be the so called Characteristic Declaration, which is usually declared with BT\_GATT\_CHARACTERISTIC followed by BT\_GATT\_CCC, or the Characteristic Value Declaration which is automatically created after the Characteristic Declaration when using BT\_GATT\_CHARACTERISTIC, or the Client Characteristic Configuration Descriptor (CCCD) which is created by BT\_GATT\_CCC.

Parameters
:   | conn | Connection object. |
    | --- | --- |
    | attr | Attribute object. |
    | ccc\_type | The subscription type, [BT\_GATT\_CCC\_NOTIFY](group__bt__gatt.md#ga240a10df32aa7a256a103ceee7211f8d "BT_GATT_CCC_NOTIFY") and/or [BT\_GATT\_CCC\_INDICATE](group__bt__gatt.md#ga60ff2ddcc2e3148881a2f15745ba06e8 "BT_GATT_CCC_INDICATE"). |

Returns
:   true if the attribute object has been subscribed.

## [◆ ](#ga74ee552864c563aa5bc939f37395c14a)bt\_gatt\_notify()

| | int bt\_gatt\_notify | ( | struct bt\_conn \* | *conn*, | | --- | --- | --- | --- | |  |  | const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \* | *attr*, | |  |  | const void \* | *data*, | |  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *len* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[gatt.h](gatt_8h.md)>`

Notify attribute value change.

Send notification of attribute value change, if connection is NULL notify all peer that have notification enabled via CCC otherwise do a direct notification only the given connection.

The attribute object on the parameters can be the so called Characteristic Declaration, which is usually declared with BT\_GATT\_CHARACTERISTIC followed by BT\_GATT\_CCC, or the Characteristic Value Declaration which is automatically created after the Characteristic Declaration when using BT\_GATT\_CHARACTERISTIC.

Parameters
:   | conn | Connection object. |
    | --- | --- |
    | attr | Characteristic or Characteristic Value attribute. |
    | data | Pointer to Attribute data. |
    | len | Attribute value length. |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#ga55e3ef7cb43b8acb0a27643c78390146)bt\_gatt\_notify\_cb()

| int bt\_gatt\_notify\_cb | ( | struct bt\_conn \* | *conn*, |
| --- | --- | --- | --- |
|  |  | struct [bt\_gatt\_notify\_params](structbt__gatt__notify__params.md) \* | *params* ) |

`#include <[gatt.h](gatt_8h.md)>`

Notify attribute value change.

This function works in the same way as [bt\_gatt\_notify](#ga74ee552864c563aa5bc939f37395c14a). With the addition that after sending the notification the callback function will be called.

The callback is run from System Workqueue context. When called from the System Workqueue context this API will not wait for resources for the callback but instead return an error. The number of pending callbacks can be increased with the `CONFIG_BT_CONN_TX_MAX` option.

Alternatively it is possible to notify by UUID by setting it on the parameters, when using this method the attribute if provided is used as the start range when looking up for possible matches.

Parameters
:   | conn | Connection object. |
    | --- | --- |
    | params | Notification parameters. |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#ga8071d6063f85c0a78155f6b2ac2da635)bt\_gatt\_notify\_multiple()

| int bt\_gatt\_notify\_multiple | ( | struct bt\_conn \* | *conn*, |
| --- | --- | --- | --- |
|  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *num\_params*, |
|  |  | struct [bt\_gatt\_notify\_params](structbt__gatt__notify__params.md) | *params*[] ) |

`#include <[gatt.h](gatt_8h.md)>`

Send multiple notifications in a single PDU.

The GATT Server will send a single ATT\_MULTIPLE\_HANDLE\_VALUE\_NTF PDU containing all the notifications passed to this API.

All params must have the same func and user\_data (due to implementation limitation). But func(user\_data) will be invoked for each parameter.

As this API may block to wait for Bluetooth Host resources, it is not recommended to call it from a cooperative thread or a Bluetooth callback.

The peer's GATT Client must write to this device's Client Supported Features attribute and set the bit for Multiple Handle Value Notifications before this API can be used.

Only use this API to force the use of the ATT\_MULTIPLE\_HANDLE\_VALUE\_NTF PDU. For standard applications, [bt\_gatt\_notify\_cb](#ga55e3ef7cb43b8acb0a27643c78390146) is preferred, as it will use this PDU if supported and automatically fallback to ATT\_HANDLE\_VALUE\_NTF when not supported by the peer.

This API has an additional limitation: it only accepts valid attribute references and not UUIDs like [bt\_gatt\_notify](#ga74ee552864c563aa5bc939f37395c14a) and [bt\_gatt\_notify\_cb](#ga55e3ef7cb43b8acb0a27643c78390146).

Parameters
:   | conn | Target client. Notifying all connected clients by passing [NULL](iar__missing__defs_8h.md#a070d2ce7b6bb7e5c05602aa8c308d0c4) is not yet supported, please use [bt\_gatt\_notify](#ga74ee552864c563aa5bc939f37395c14a) instead. |
    | --- | --- |
    | num\_params | Element count of params array. Has to be greater than 1. |
    | params | Array of notification parameters. It is okay to free this after calling this function. |

Return values
:   | 0 | Success. The PDU is queued for sending. |
    | --- | --- |
    | -EINVAL | - One of the attribute handles is invalid. - Only one parameter was passed. This API expects 2 or more. - Not all func were equal or not all user\_data were equal. - One of the characteristics is not notifiable. - An UUID was passed in one of the parameters. |
    | -ERANGE | - The notifications cannot all fit in a single ATT\_MULTIPLE\_HANDLE\_VALUE\_NTF. - They exceed the MTU of all open ATT bearers. |
    | -EPERM | The connection has a lower security level than required by one of the attributes. |
    | -EOPNOTSUPP | The peer hasn't yet communicated that it supports this PDU type. |

## [◆ ](#ga24bae284dbc71cd4075649c4bc348b7c)bt\_gatt\_notify\_uuid()

| | int bt\_gatt\_notify\_uuid | ( | struct bt\_conn \* | *conn*, | | --- | --- | --- | --- | |  |  | const struct [bt\_uuid](structbt__uuid.md) \* | *uuid*, | |  |  | const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \* | *attr*, | |  |  | const void \* | *data*, | |  |  | [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | *len* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

`#include <[gatt.h](gatt_8h.md)>`

Notify attribute value change by UUID.

Send notification of attribute value change, if connection is NULL notify all peer that have notification enabled via CCC otherwise do a direct notification only on the given connection.

The attribute object is the starting point for the search of the UUID.

Parameters
:   | conn | Connection object. |
    | --- | --- |
    | uuid | The UUID. If the server contains multiple services with the same UUID, then the first occurrence, starting from the attr given, is used. |
    | attr | Pointer to an attribute that serves as the starting point for the search of a match for the UUID. |
    | data | Pointer to Attribute data. |
    | len | Attribute value length. |

Returns
:   0 in case of success or negative value in case of error.

## [◆ ](#gae5c1e8b7bb1e673e228f03d1d084be9a)bt\_gatt\_service\_is\_registered()

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) bt\_gatt\_service\_is\_registered | ( | const struct [bt\_gatt\_service](structbt__gatt__service.md) \* | *svc* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[gatt.h](gatt_8h.md)>`

Check if GATT service is registered.

Parameters
:   | svc | Service to be checked. |
    | --- | --- |

Returns
:   true if registered or false if not register.

## [◆ ](#gab4d9cfea04e44445d5dc30ad52842b64)bt\_gatt\_service\_register()

| int bt\_gatt\_service\_register | ( | struct [bt\_gatt\_service](structbt__gatt__service.md) \* | *svc* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[gatt.h](gatt_8h.md)>`

Register GATT service.

To register a GATT service, applications can make use of macros such as [BT\_GATT\_PRIMARY\_SERVICE](#gaacada0ff1029af959b6fcd6703d4a0bf), [BT\_GATT\_CHARACTERISTIC](#ga9e739546dbd906d3b3c4f1ed5ad9f41e), [BT\_GATT\_DESCRIPTOR](#ga83207fc083454327004f7d3c3e5b3840), etc.

When using `CONFIG_BT_SETTINGS` then all services that should have bond configuration loaded, i.e. CCC values, must be registered before calling [settings\_load](group__settings.md#ga89c6d618df81f197cc5c1a2018b00648 "settings_load").

When using `CONFIG_BT_GATT_CACHING` and `CONFIG_BT_SETTINGS` then all services that should be included in the GATT Database Hash calculation should be added before calling [settings\_load](group__settings.md#ga89c6d618df81f197cc5c1a2018b00648 "settings_load"). All services registered after settings\_load will trigger a new database hash calculation and a new hash stored.

There are two situations where this function can be called: either before bt\_init() has been called, or after [settings\_load()](group__settings.md#ga89c6d618df81f197cc5c1a2018b00648 "Load serialized items from registered persistence sources.") has been called. Registering a service in the middle is not supported and will return an error.

Parameters
:   | svc | Service containing the available attributes |
    | --- | --- |

Returns
:   0 in case of success or negative value in case of error.
:   -EAGAIN if bt\_init() has been called but [settings\_load()](group__settings.md#ga89c6d618df81f197cc5c1a2018b00648 "Load serialized items from registered persistence sources.") hasn't yet.

## [◆ ](#gaf5bf0205fad5f7ad187b764d23deba6b)bt\_gatt\_service\_unregister()

| int bt\_gatt\_service\_unregister | ( | struct [bt\_gatt\_service](structbt__gatt__service.md) \* | *svc* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[gatt.h](gatt_8h.md)>`

Unregister GATT service.

Parameters
:   | svc | Service to be unregistered. |
    | --- | --- |

Returns
:   0 in case of success or negative value in case of error.

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

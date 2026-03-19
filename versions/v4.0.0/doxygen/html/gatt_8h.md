---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/gatt_8h.html
original_path: doxygen/html/gatt_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

gatt.h File Reference

Generic Attribute Profile handling.
[More...](#details)

`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <stddef.h>`  
`#include <[sys/types.h](lib_2libc_2minimal_2include_2sys_2types_8h_source.md)>`  
`#include <[zephyr/sys/slist.h](slist_8h_source.md)>`  
`#include <[zephyr/sys/util.h](sys_2util_8h_source.md)>`  
`#include <[zephyr/bluetooth/conn.h](conn_8h_source.md)>`  
`#include <[zephyr/bluetooth/uuid.h](uuid_8h_source.md)>`  
`#include <[zephyr/bluetooth/att.h](att_8h_source.md)>`  
`#include <[zephyr/sys/iterable_sections.h](sys_2iterable__sections_8h_source.md)>`

[Go to the source code of this file.](gatt_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [bt\_gatt\_attr](structbt__gatt__attr.md) |
|  | GATT Attribute. [More...](structbt__gatt__attr.md#details) |
| struct | [bt\_gatt\_service\_static](structbt__gatt__service__static.md) |
|  | GATT Service structure. [More...](structbt__gatt__service__static.md#details) |
| struct | [bt\_gatt\_service](structbt__gatt__service.md) |
|  | GATT Service structure. [More...](structbt__gatt__service.md#details) |
| struct | [bt\_gatt\_service\_val](structbt__gatt__service__val.md) |
|  | Service Attribute Value. [More...](structbt__gatt__service__val.md#details) |
| struct | [bt\_gatt\_include](structbt__gatt__include.md) |
|  | Include Attribute Value. [More...](structbt__gatt__include.md#details) |
| struct | [bt\_gatt\_cb](structbt__gatt__cb.md) |
|  | GATT callback structure. [More...](structbt__gatt__cb.md#details) |
| struct | [bt\_gatt\_authorization\_cb](structbt__gatt__authorization__cb.md) |
|  | GATT authorization callback structure. [More...](structbt__gatt__authorization__cb.md#details) |
| struct | [bt\_gatt\_chrc](structbt__gatt__chrc.md) |
|  | Characteristic Attribute Value. [More...](structbt__gatt__chrc.md#details) |
| struct | [bt\_gatt\_cep](structbt__gatt__cep.md) |
|  | Characteristic Extended Properties Attribute Value. [More...](structbt__gatt__cep.md#details) |
| struct | [bt\_gatt\_ccc](structbt__gatt__ccc.md) |
|  | Client Characteristic Configuration Attribute Value. [More...](structbt__gatt__ccc.md#details) |
| struct | [bt\_gatt\_scc](structbt__gatt__scc.md) |
|  | Server Characteristic Configuration Attribute Value. [More...](structbt__gatt__scc.md#details) |
| struct | [bt\_gatt\_cpf](structbt__gatt__cpf.md) |
|  | GATT Characteristic Presentation Format Attribute Value. [More...](structbt__gatt__cpf.md#details) |
| struct | [bt\_gatt\_ccc\_cfg](structbt__gatt__ccc__cfg.md) |
|  | GATT CCC configuration entry. [More...](structbt__gatt__ccc__cfg.md#details) |
| struct | [bt\_gatt\_notify\_params](structbt__gatt__notify__params.md) |
| struct | [bt\_gatt\_indicate\_params](structbt__gatt__indicate__params.md) |
|  | GATT Indicate Value parameters. [More...](structbt__gatt__indicate__params.md#details) |
| struct | [bt\_gatt\_exchange\_params](structbt__gatt__exchange__params.md) |
|  | GATT Exchange MTU parameters. [More...](structbt__gatt__exchange__params.md#details) |
| struct | [bt\_gatt\_discover\_params](structbt__gatt__discover__params.md) |
|  | GATT Discover Attributes parameters. [More...](structbt__gatt__discover__params.md#details) |
| struct | [bt\_gatt\_read\_params](structbt__gatt__read__params.md) |
|  | GATT Read parameters. [More...](structbt__gatt__read__params.md#details) |
| struct | [bt\_gatt\_write\_params](structbt__gatt__write__params.md) |
|  | GATT Write parameters. [More...](structbt__gatt__write__params.md#details) |
| struct | [bt\_gatt\_subscribe\_params](structbt__gatt__subscribe__params.md) |
|  | GATT Subscribe parameters. [More...](structbt__gatt__subscribe__params.md#details) |

| Macros | |
| --- | --- |
| #define | [BT\_GATT\_ERR](group__bt__gatt.md#gaff31756c1bf8ee755e65b1e0fb689bb7)(\_att\_err) |
|  | Construct error return value for attribute read and write callbacks. |
| #define | [BT\_GATT\_CHRC\_BROADCAST](group__bt__gatt.md#ga86bddd8211e7466b0457173a0dd412f0)   0x01 |
|  | Characteristic Properties Bit field values. |
| #define | [BT\_GATT\_CHRC\_READ](group__bt__gatt.md#gaa243a11d6d8b3e3be815c0893e0220f3)   0x02 |
|  | Characteristic read property. |
| #define | [BT\_GATT\_CHRC\_WRITE\_WITHOUT\_RESP](group__bt__gatt.md#ga9c029ca574eb3c5992685b279388ac85)   0x04 |
|  | Characteristic write without response property. |
| #define | [BT\_GATT\_CHRC\_WRITE](group__bt__gatt.md#gad482d8db34707e1f9da1d8e2ddd5507e)   0x08 |
|  | Characteristic write with response property. |
| #define | [BT\_GATT\_CHRC\_NOTIFY](group__bt__gatt.md#gab8cd9649bdfd125a26065a8ced762a98)   0x10 |
|  | Characteristic notify property. |
| #define | [BT\_GATT\_CHRC\_INDICATE](group__bt__gatt.md#gaa9639b9d655ea41767584b638add1f2b)   0x20 |
|  | Characteristic indicate property. |
| #define | [BT\_GATT\_CHRC\_AUTH](group__bt__gatt.md#gaab3a26a00f88a6eacd36f2841004204c)   0x40 |
|  | Characteristic Authenticated Signed Writes property. |
| #define | [BT\_GATT\_CHRC\_EXT\_PROP](group__bt__gatt.md#gac84d73a0ad50bfd149ad83181315de1a)   0x80 |
|  | Characteristic Extended Properties property. |
| #define | [BT\_GATT\_CEP\_RELIABLE\_WRITE](group__bt__gatt.md#gad1825f8deafc36d7e8f09c2835884fc6)   0x0001 |
|  | Characteristic Extended Properties Bit field values. |
| #define | [BT\_GATT\_CEP\_WRITABLE\_AUX](group__bt__gatt.md#ga64898ec8390c89c1fc5bdf0364220a43)   0x0002 |
| #define | [BT\_GATT\_CCC\_NOTIFY](group__bt__gatt.md#ga240a10df32aa7a256a103ceee7211f8d)   0x0001 |
|  | Client Characteristic Configuration Values. |
| #define | [BT\_GATT\_CCC\_INDICATE](group__bt__gatt.md#ga60ff2ddcc2e3148881a2f15745ba06e8)   0x0002 |
|  | Client Characteristic Configuration Indication. |
| #define | [BT\_GATT\_SCC\_BROADCAST](group__bt__gatt.md#ga7a7d3cfa6eec4baa0b57ec9c4bc41f7a)   0x0001 |
|  | Server Characteristic Configuration Values. |
| #define | [BT\_GATT\_SERVICE\_DEFINE](group__bt__gatt__server.md#ga04c7887fb67107bd060dd023fd3186d5)(\_name, ...) |
|  | Statically define and register a service. |
| #define | [BT\_GATT\_SERVICE\_INSTANCE\_DEFINE](group__bt__gatt__server.md#ga8bb3aeef20465d7f6e38f6bbddef74e5)( \_name, \_instances, \_instance\_num, \_attrs\_def) |
|  | Statically define service structure array. |
| #define | [BT\_GATT\_SERVICE](group__bt__gatt__server.md#ga7d413ec013b91a633ec24d80d2814e2b)(\_attrs) |
|  | Service Structure Declaration Macro. |
| #define | [BT\_GATT\_PRIMARY\_SERVICE](group__bt__gatt__server.md#gaacada0ff1029af959b6fcd6703d4a0bf)(\_service) |
|  | Primary Service Declaration Macro. |
| #define | [BT\_GATT\_SECONDARY\_SERVICE](group__bt__gatt__server.md#gaecb4d30282677d3450ad79c5f83f3445)(\_service) |
|  | Secondary Service Declaration Macro. |
| #define | [BT\_GATT\_INCLUDE\_SERVICE](group__bt__gatt__server.md#ga08ffee706d271b75a54b1b99249dba24)(\_service\_incl) |
|  | Include Service Declaration Macro. |
| #define | [BT\_GATT\_CHRC\_INIT](group__bt__gatt__server.md#ga7f19592a722c41d6c1d2421d166dd78a)(\_uuid, \_handle, \_props) |
| #define | [BT\_GATT\_CHARACTERISTIC](group__bt__gatt__server.md#ga9e739546dbd906d3b3c4f1ed5ad9f41e)(\_uuid, \_props, \_perm, \_read, \_write, \_user\_data) |
|  | Characteristic and Value Declaration Macro. |
| #define | [BT\_GATT\_CCC\_MAX](group__bt__gatt__server.md#gac1c0a195c1ec1ff2cdd5bf6d0ba6ad00)   0 |
| #define | [BT\_GATT\_CCC\_INITIALIZER](group__bt__gatt__server.md#ga59fd77199435e461e03a80c7121bb869)(\_changed, \_write, \_match) |
|  | Initialize Client Characteristic Configuration Declaration Macro. |
| #define | [BT\_GATT\_CCC\_MANAGED](group__bt__gatt__server.md#gad8b296ecfd1139680f21da7904b9f585)(\_ccc, \_perm) |
|  | Managed Client Characteristic Configuration Declaration Macro. |
| #define | [BT\_GATT\_CCC](group__bt__gatt__server.md#ga140b9c25d10244bebd9c891f881fdc94)(\_changed, \_perm) |
|  | Client Characteristic Configuration Declaration Macro. |
| #define | [BT\_GATT\_CEP](group__bt__gatt__server.md#ga55a82cada1093c4ff75fe5504ac504b1)(\_value) |
|  | Characteristic Extended Properties Declaration Macro. |
| #define | [BT\_GATT\_CUD](group__bt__gatt__server.md#ga1e1cd9d0853e2dcbefcb85fda44dc9c7)(\_value, \_perm) |
|  | Characteristic User Format Descriptor Declaration Macro. |
| #define | [BT\_GATT\_CPF](group__bt__gatt__server.md#ga3835fcfdf7a5f917e21c9d17e75162be)(\_value) |
|  | Characteristic Presentation Format Descriptor Declaration Macro. |
| #define | [BT\_GATT\_DESCRIPTOR](group__bt__gatt__server.md#ga83207fc083454327004f7d3c3e5b3840)(\_uuid, \_perm, \_read, \_write, \_user\_data) |
|  | Descriptor Declaration Macro. |
| #define | [BT\_GATT\_ATTRIBUTE](group__bt__gatt__server.md#gac4abfeb068d16dcdaceee812c12bf406)(\_uuid, \_perm, \_read, \_write, \_user\_data) |
|  | Attribute Declaration Macro. |
| #define | [BT\_GATT\_AUTO\_DISCOVER\_CCC\_HANDLE](group__bt__gatt__client.md#ga7ca44e95989a143ae0b21e4a5316561d)   0x0000U |
|  | Handle value to denote that the CCC will be automatically discovered. |

| Typedefs | |
| --- | --- |
| typedef [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118)(\* | [bt\_gatt\_attr\_read\_func\_t](group__bt__gatt.md#ga57e36bf94652531964fd4237c203fe7b)) (struct bt\_conn \*conn, const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \*attr, void \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) offset) |
|  | Attribute read callback. |
| typedef [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118)(\* | [bt\_gatt\_attr\_write\_func\_t](group__bt__gatt.md#ga3fd8527a0f3e8f3699dc0d3b0339eba1)) (struct bt\_conn \*conn, const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \*attr, const void \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) offset, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Attribute Value write implementation. |
| typedef [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)(\* | [bt\_gatt\_attr\_func\_t](group__bt__gatt__server.md#ga60284611c90729b289fe806524ba9209)) (const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \*attr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) handle, void \*user\_data) |
|  | Attribute iterator callback. |
| typedef void(\* | [bt\_gatt\_complete\_func\_t](group__bt__gatt__server.md#gac55832607b95f394d26a64ed1cfe5bba)) (struct bt\_conn \*conn, void \*user\_data) |
|  | Notification complete result callback. |
| typedef void(\* | [bt\_gatt\_indicate\_func\_t](group__bt__gatt__server.md#ga1294850e6bdcbe7a8f42f2956fd837a8)) (struct bt\_conn \*conn, struct [bt\_gatt\_indicate\_params](structbt__gatt__indicate__params.md) \*params, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) err) |
|  | Indication complete result callback. |
| typedef void(\* | [bt\_gatt\_indicate\_params\_destroy\_t](group__bt__gatt__server.md#ga5d47ed9eaea22c8f00db14329daee8fe)) (struct [bt\_gatt\_indicate\_params](structbt__gatt__indicate__params.md) \*params) |
| typedef [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)(\* | [bt\_gatt\_discover\_func\_t](group__bt__gatt__client.md#gabd3bcd3c1560956726574faed332fb13)) (struct bt\_conn \*conn, const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \*attr, struct [bt\_gatt\_discover\_params](structbt__gatt__discover__params.md) \*params) |
|  | Discover attribute callback function. |
| typedef [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)(\* | [bt\_gatt\_read\_func\_t](group__bt__gatt__client.md#ga1ca94b4f2b6c456b6134e05127993569)) (struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) err, struct [bt\_gatt\_read\_params](structbt__gatt__read__params.md) \*params, const void \*data, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) length) |
|  | Read callback function. |
| typedef void(\* | [bt\_gatt\_write\_func\_t](group__bt__gatt__client.md#ga2bca8c4a45f41e0400a9e0147f4baf50)) (struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) err, struct [bt\_gatt\_write\_params](structbt__gatt__write__params.md) \*params) |
|  | Write callback function. |
| typedef [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)(\* | [bt\_gatt\_notify\_func\_t](group__bt__gatt__client.md#gab3e53eb5f9bb1eda7bf612ef95755b4d)) (struct bt\_conn \*conn, struct [bt\_gatt\_subscribe\_params](structbt__gatt__subscribe__params.md) \*params, const void \*data, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) length) |
|  | Notification callback function. |
| typedef void(\* | [bt\_gatt\_subscribe\_func\_t](group__bt__gatt__client.md#ga2e914e63b4b91fa56bc3295283c43714)) (struct bt\_conn \*conn, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) err, struct [bt\_gatt\_subscribe\_params](structbt__gatt__subscribe__params.md) \*params) |
|  | Subscription callback function. |

| Enumerations | |
| --- | --- |
| enum | [bt\_gatt\_perm](group__bt__gatt.md#ga96e57500d2340a45badb23701cc43833) {     [BT\_GATT\_PERM\_NONE](group__bt__gatt.md#gga96e57500d2340a45badb23701cc43833a81a1c35d981593c4c0d344dd0f7e898a) = 0 , [BT\_GATT\_PERM\_READ](group__bt__gatt.md#gga96e57500d2340a45badb23701cc43833a9afb838c2cef657e9cd035ef27521f17) = BIT(0) , [BT\_GATT\_PERM\_WRITE](group__bt__gatt.md#gga96e57500d2340a45badb23701cc43833a0f611698ca511f565b247a813ea016cf) = BIT(1) , [BT\_GATT\_PERM\_READ\_ENCRYPT](group__bt__gatt.md#gga96e57500d2340a45badb23701cc43833a0d0afe4a6389102f85e355468cb7984d) = BIT(2) ,     [BT\_GATT\_PERM\_WRITE\_ENCRYPT](group__bt__gatt.md#gga96e57500d2340a45badb23701cc43833a662b9af6f435d788aa4e6829725f670f) = BIT(3) , [BT\_GATT\_PERM\_READ\_AUTHEN](group__bt__gatt.md#gga96e57500d2340a45badb23701cc43833ad83f4c03608f674c00ebc93e63d08583) = BIT(4) , [BT\_GATT\_PERM\_WRITE\_AUTHEN](group__bt__gatt.md#gga96e57500d2340a45badb23701cc43833add3893c94a788ff2e5256595a533a266) = BIT(5) , [BT\_GATT\_PERM\_PREPARE\_WRITE](group__bt__gatt.md#gga96e57500d2340a45badb23701cc43833ab384b61f6ead9d140011da917c950d79) = BIT(6) ,     [BT\_GATT\_PERM\_READ\_LESC](group__bt__gatt.md#gga96e57500d2340a45badb23701cc43833af62e397dfd87fe763b9c9fc1d5072f57) = BIT(7) , [BT\_GATT\_PERM\_WRITE\_LESC](group__bt__gatt.md#gga96e57500d2340a45badb23701cc43833ac56183af896e2a58439c625420efca94) = BIT(8)   } |
|  | GATT attribute permission bit field values. [More...](group__bt__gatt.md#ga96e57500d2340a45badb23701cc43833) |
| enum | { [BT\_GATT\_WRITE\_FLAG\_PREPARE](group__bt__gatt.md#gga11c5a2eb0b62de9a2493ad5335fae383a019cf6118a0cfacbfad20c1cc5838383) = BIT(0) , [BT\_GATT\_WRITE\_FLAG\_CMD](group__bt__gatt.md#gga11c5a2eb0b62de9a2493ad5335fae383a770df41b7d433e8ce349b19e4657ba78) = BIT(1) , [BT\_GATT\_WRITE\_FLAG\_EXECUTE](group__bt__gatt.md#gga11c5a2eb0b62de9a2493ad5335fae383ad4e8f43c03da10c15685bd1a0109708b) = BIT(2) } |
|  | GATT attribute write flags. [More...](group__bt__gatt.md#ga11c5a2eb0b62de9a2493ad5335fae383) |
| enum | { [BT\_GATT\_ITER\_STOP](group__bt__gatt__server.md#ggab94ce0108483b70392b31a621aa0712aaa3f2a25e27c7065a2c7bb2a9ff09542e) = 0 , [BT\_GATT\_ITER\_CONTINUE](group__bt__gatt__server.md#ggab94ce0108483b70392b31a621aa0712aaea569feffa4815d3443e12be78c684f5) } |
| enum | {     [BT\_GATT\_DISCOVER\_PRIMARY](group__bt__gatt__client.md#ggaa7bf94a9823d44c702cc26dc8ade8403ada9ac33aa77f6043da8133dcf269478f) , [BT\_GATT\_DISCOVER\_SECONDARY](group__bt__gatt__client.md#ggaa7bf94a9823d44c702cc26dc8ade8403a21be62548b816c7960a54dd6e3b37a97) , [BT\_GATT\_DISCOVER\_INCLUDE](group__bt__gatt__client.md#ggaa7bf94a9823d44c702cc26dc8ade8403a80afff1c83bb5ebb5603af699f2c26da) , [BT\_GATT\_DISCOVER\_CHARACTERISTIC](group__bt__gatt__client.md#ggaa7bf94a9823d44c702cc26dc8ade8403a71355dfe0bf30c88f9fe2f7da1ba10ae) ,     [BT\_GATT\_DISCOVER\_DESCRIPTOR](group__bt__gatt__client.md#ggaa7bf94a9823d44c702cc26dc8ade8403a0ccb2587aa8f21361c5d73847a33ecbe) , [BT\_GATT\_DISCOVER\_ATTRIBUTE](group__bt__gatt__client.md#ggaa7bf94a9823d44c702cc26dc8ade8403afe2167b873b848935d56f6ee7f2c444c) , [BT\_GATT\_DISCOVER\_STD\_CHAR\_DESC](group__bt__gatt__client.md#ggaa7bf94a9823d44c702cc26dc8ade8403a81a1f8737c415544a0f793f4e626bb61)   } |
|  | GATT Discover types. [More...](group__bt__gatt__client.md#gaa7bf94a9823d44c702cc26dc8ade8403) |
| enum | {     [BT\_GATT\_SUBSCRIBE\_FLAG\_VOLATILE](group__bt__gatt__client.md#gga07d7c3837ad936e586fdb11c0bd122d6aecdcb3baa850505f459523091c92a1cb) , [BT\_GATT\_SUBSCRIBE\_FLAG\_NO\_RESUB](group__bt__gatt__client.md#gga07d7c3837ad936e586fdb11c0bd122d6a30bfd3fb4bf4f17653ba00942ba2b2e6) , [BT\_GATT\_SUBSCRIBE\_FLAG\_WRITE\_PENDING](group__bt__gatt__client.md#gga07d7c3837ad936e586fdb11c0bd122d6afe1c3dc9380c33debd32a275d5bce8ad) , [BT\_GATT\_SUBSCRIBE\_FLAG\_SENT](group__bt__gatt__client.md#gga07d7c3837ad936e586fdb11c0bd122d6a56aa5f332d4098e3942d7a902198f7ab) ,     [BT\_GATT\_SUBSCRIBE\_NUM\_FLAGS](group__bt__gatt__client.md#gga07d7c3837ad936e586fdb11c0bd122d6a5640a1e06740a89859c5f4b183d58e79)   } |
|  | Subscription flags. [More...](group__bt__gatt__client.md#ga07d7c3837ad936e586fdb11c0bd122d6) |

| Functions | |
| --- | --- |
| static const char \* | [bt\_gatt\_err\_to\_str](group__bt__gatt__server.md#gaf6d3f1e904f1a847afeb30236bad98a2) (int gatt\_err) |
|  | Converts a GATT error to string. |
| void | [bt\_gatt\_cb\_register](group__bt__gatt__server.md#ga270c8a52bf3d512defc373f8c29b59f2) (struct [bt\_gatt\_cb](structbt__gatt__cb.md) \*cb) |
|  | Register GATT callbacks. |
| int | [bt\_gatt\_authorization\_cb\_register](group__bt__gatt__server.md#ga5eee6afc6db391ffeda295d298bf6a56) (const struct [bt\_gatt\_authorization\_cb](structbt__gatt__authorization__cb.md) \*cb) |
|  | Register GATT authorization callbacks. |
| int | [bt\_gatt\_service\_register](group__bt__gatt__server.md#gab4d9cfea04e44445d5dc30ad52842b64) (struct [bt\_gatt\_service](structbt__gatt__service.md) \*svc) |
|  | Register GATT service. |
| int | [bt\_gatt\_service\_unregister](group__bt__gatt__server.md#gaf5bf0205fad5f7ad187b764d23deba6b) (struct [bt\_gatt\_service](structbt__gatt__service.md) \*svc) |
|  | Unregister GATT service. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [bt\_gatt\_service\_is\_registered](group__bt__gatt__server.md#gae5c1e8b7bb1e673e228f03d1d084be9a) (const struct [bt\_gatt\_service](structbt__gatt__service.md) \*svc) |
|  | Check if GATT service is registered. |
| void | [bt\_gatt\_foreach\_attr\_type](group__bt__gatt__server.md#gad8d8f513004f391167212d7bf9f7ff10) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) start\_handle, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) end\_handle, const struct [bt\_uuid](structbt__uuid.md) \*uuid, const void \*attr\_data, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) num\_matches, [bt\_gatt\_attr\_func\_t](group__bt__gatt__server.md#ga60284611c90729b289fe806524ba9209) func, void \*user\_data) |
|  | Attribute iterator by type. |
| static void | [bt\_gatt\_foreach\_attr](group__bt__gatt__server.md#gaa93b5e0f2870ed135447bead903c175a) ([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) start\_handle, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) end\_handle, [bt\_gatt\_attr\_func\_t](group__bt__gatt__server.md#ga60284611c90729b289fe806524ba9209) func, void \*user\_data) |
|  | Attribute iterator. |
| struct [bt\_gatt\_attr](structbt__gatt__attr.md) \* | [bt\_gatt\_attr\_next](group__bt__gatt__server.md#ga35cecaa43b00b374062d29cca1479d85) (const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \*attr) |
|  | Iterate to the next attribute. |
| struct [bt\_gatt\_attr](structbt__gatt__attr.md) \* | [bt\_gatt\_find\_by\_uuid](group__bt__gatt__server.md#gad2f3272b1dc42378104b492ec7caf6b0) (const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \*attr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) attr\_count, const struct [bt\_uuid](structbt__uuid.md) \*uuid) |
|  | Find Attribute by UUID. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [bt\_gatt\_attr\_get\_handle](group__bt__gatt__server.md#ga2d51136ea1bd6cdb50900639506fd9f7) (const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \*attr) |
|  | Get Attribute handle. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [bt\_gatt\_attr\_value\_handle](group__bt__gatt__server.md#ga99738cf4f05eae4c6da17cc3420827d8) (const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \*attr) |
|  | Get the handle of the characteristic value descriptor. |
| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) | [bt\_gatt\_attr\_read](group__bt__gatt__server.md#gaf6d253849932b706ec7f303568980dfa) (struct bt\_conn \*conn, const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \*attr, void \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) buf\_len, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) offset, const void \*value, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) value\_len) |
|  | Generic Read Attribute value helper. |
| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) | [bt\_gatt\_attr\_read\_service](group__bt__gatt__server.md#gacae81c0f272bad7e6ac93c0d13b678c6) (struct bt\_conn \*conn, const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \*attr, void \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) offset) |
|  | Read Service Attribute helper. |
| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) | [bt\_gatt\_attr\_read\_included](group__bt__gatt__server.md#ga4313a63decac2c8b7c4a1764df3d53ea) (struct bt\_conn \*conn, const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \*attr, void \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) offset) |
|  | Read Include Attribute helper. |
| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) | [bt\_gatt\_attr\_read\_chrc](group__bt__gatt__server.md#gad58b526a06334530c13292d14a11257c) (struct bt\_conn \*conn, const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \*attr, void \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) offset) |
|  | Read Characteristic Attribute helper. |
| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) | [bt\_gatt\_attr\_read\_ccc](group__bt__gatt__server.md#ga2e85b42136e2c6a4cb5b7ad8a2532573) (struct bt\_conn \*conn, const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \*attr, void \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) offset) |
|  | Read Client Characteristic Configuration Attribute helper. |
| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) | [bt\_gatt\_attr\_write\_ccc](group__bt__gatt__server.md#gabba965b676650a55cb9934072b34c75e) (struct bt\_conn \*conn, const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \*attr, const void \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) offset, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [flags](parser_8h.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)) |
|  | Write Client Characteristic Configuration Attribute helper. |
| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) | [bt\_gatt\_attr\_read\_cep](group__bt__gatt__server.md#ga5893166f1b24f437a94ccf1fc57c7917) (struct bt\_conn \*conn, const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \*attr, void \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) offset) |
|  | Read Characteristic Extended Properties Attribute helper. |
| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) | [bt\_gatt\_attr\_read\_cud](group__bt__gatt__server.md#ga29421c8788b47b6a648704d27d5f0d28) (struct bt\_conn \*conn, const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \*attr, void \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) offset) |
|  | Read Characteristic User Description Descriptor Attribute helper. |
| [ssize\_t](lib_2libc_2minimal_2include_2sys_2types_8h.md#a5c5d83d87790efd59ea916c2b99f9118) | [bt\_gatt\_attr\_read\_cpf](group__bt__gatt__server.md#ga5ae96590a0aaa5c4c3863a4a14d80fdd) (struct bt\_conn \*conn, const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \*attr, void \*buf, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) offset) |
|  | Read Characteristic Presentation format Descriptor Attribute helper. |
| int | [bt\_gatt\_notify\_cb](group__bt__gatt__server.md#ga55e3ef7cb43b8acb0a27643c78390146) (struct bt\_conn \*conn, struct [bt\_gatt\_notify\_params](structbt__gatt__notify__params.md) \*params) |
|  | Notify attribute value change. |
| int | [bt\_gatt\_notify\_multiple](group__bt__gatt__server.md#ga8071d6063f85c0a78155f6b2ac2da635) (struct bt\_conn \*conn, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) num\_params, struct [bt\_gatt\_notify\_params](structbt__gatt__notify__params.md) params[]) |
|  | Send multiple notifications in a single PDU. |
| static int | [bt\_gatt\_notify](group__bt__gatt__server.md#ga74ee552864c563aa5bc939f37395c14a) (struct bt\_conn \*conn, const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \*attr, const void \*data, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len) |
|  | Notify attribute value change. |
| static int | [bt\_gatt\_notify\_uuid](group__bt__gatt__server.md#ga24bae284dbc71cd4075649c4bc348b7c) (struct bt\_conn \*conn, const struct [bt\_uuid](structbt__uuid.md) \*uuid, const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \*attr, const void \*data, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) len) |
|  | Notify attribute value change by UUID. |
| int | [bt\_gatt\_indicate](group__bt__gatt__server.md#ga4f2272692cc0f1d44638828012296c80) (struct bt\_conn \*conn, struct [bt\_gatt\_indicate\_params](structbt__gatt__indicate__params.md) \*params) |
|  | Indicate attribute value change. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [bt\_gatt\_is\_subscribed](group__bt__gatt__server.md#gabd4df0a264dae10e43797992a567be7d) (struct bt\_conn \*conn, const struct [bt\_gatt\_attr](structbt__gatt__attr.md) \*attr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) ccc\_type) |
|  | Check if connection have subscribed to attribute. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [bt\_gatt\_get\_mtu](group__bt__gatt__server.md#ga351fd7658eaecbbfa60f1769119ef733) (struct bt\_conn \*conn) |
|  | Get ATT MTU for a connection. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [bt\_gatt\_get\_uatt\_mtu](group__bt__gatt__server.md#ga6653de5e245cae6dc12cd0b45acbe028) (struct bt\_conn \*conn) |
|  | Get Unenhanced ATT (UATT) MTU for a connection. |
| int | [bt\_gatt\_exchange\_mtu](group__bt__gatt__client.md#ga0f41da23c6559a8254b04295aff8198d) (struct bt\_conn \*conn, struct [bt\_gatt\_exchange\_params](structbt__gatt__exchange__params.md) \*params) |
|  | Exchange MTU. |
| int | [bt\_gatt\_discover](group__bt__gatt__client.md#gac06a945e5f7939b6716bc4f2cea781bd) (struct bt\_conn \*conn, struct [bt\_gatt\_discover\_params](structbt__gatt__discover__params.md) \*params) |
|  | GATT Discover function. |
| int | [bt\_gatt\_read](group__bt__gatt__client.md#ga1a18dd726ab960a88d7f85f2a014141a) (struct bt\_conn \*conn, struct [bt\_gatt\_read\_params](structbt__gatt__read__params.md) \*params) |
|  | Read Attribute Value by handle. |
| int | [bt\_gatt\_write](group__bt__gatt__client.md#ga843a42e68e0497d88d3f655f8ffd58d4) (struct bt\_conn \*conn, struct [bt\_gatt\_write\_params](structbt__gatt__write__params.md) \*params) |
|  | Write Attribute Value by handle. |
| int | [bt\_gatt\_write\_without\_response\_cb](group__bt__gatt__client.md#ga49439413d12b5a8a1c68735e961ab6fa) (struct bt\_conn \*conn, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) handle, const void \*data, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) length, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) sign, [bt\_gatt\_complete\_func\_t](group__bt__gatt__server.md#gac55832607b95f394d26a64ed1cfe5bba) func, void \*user\_data) |
|  | Write Attribute Value by handle without response with callback. |
| static int | [bt\_gatt\_write\_without\_response](group__bt__gatt__client.md#ga9fc78e32230637a6f092da2400c50fe7) (struct bt\_conn \*conn, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) handle, const void \*data, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) length, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) sign) |
|  | Write Attribute Value by handle without response. |
| int | [bt\_gatt\_subscribe](group__bt__gatt__client.md#ga7d4a8e18f51ba6476886a15f81f48e5c) (struct bt\_conn \*conn, struct [bt\_gatt\_subscribe\_params](structbt__gatt__subscribe__params.md) \*params) |
|  | Subscribe Attribute Value Notification. |
| int | [bt\_gatt\_resubscribe](group__bt__gatt__client.md#ga791b8bb8a4c085b022fafc0535a63511) ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) id, const [bt\_addr\_le\_t](structbt__addr__le__t.md) \*peer, struct [bt\_gatt\_subscribe\_params](structbt__gatt__subscribe__params.md) \*params) |
|  | Resubscribe Attribute Value Notification subscription. |
| int | [bt\_gatt\_unsubscribe](group__bt__gatt__client.md#ga56509c9b8f73f729cfa5e75be22d79ae) (struct bt\_conn \*conn, struct [bt\_gatt\_subscribe\_params](structbt__gatt__subscribe__params.md) \*params) |
|  | Unsubscribe Attribute Value Notification. |
| void | [bt\_gatt\_cancel](group__bt__gatt__client.md#ga5193dea59a016692f94cf950d6b4f4f7) (struct bt\_conn \*conn, void \*params) |
|  | Try to cancel the first pending request identified by `params`. |

## Detailed Description

Generic Attribute Profile handling.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [gatt.h](gatt_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

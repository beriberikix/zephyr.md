---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/blob__cli_8h.html
original_path: doxygen/html/blob__cli_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

blob\_cli.h File Reference

`#include <[sys/types.h](lib_2libc_2minimal_2include_2sys_2types_8h_source.md)>`  
`#include <[zephyr/bluetooth/mesh/access.h](access_8h_source.md)>`  
`#include <[zephyr/bluetooth/mesh/blob.h](blob_8h_source.md)>`

[Go to the source code of this file.](blob__cli_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [bt\_mesh\_blob\_target\_pull](structbt__mesh__blob__target__pull.md) |
|  | Target node's Pull mode (Pull BLOB Transfer Mode) context used while sending chunks to the Target node. [More...](structbt__mesh__blob__target__pull.md#details) |
| struct | [bt\_mesh\_blob\_target](structbt__mesh__blob__target.md) |
|  | BLOB Transfer Client Target node. [More...](structbt__mesh__blob__target.md#details) |
| struct | [bt\_mesh\_blob\_xfer\_info](structbt__mesh__blob__xfer__info.md) |
|  | BLOB transfer information. [More...](structbt__mesh__blob__xfer__info.md#details) |
| struct | [bt\_mesh\_blob\_cli\_inputs](structbt__mesh__blob__cli__inputs.md) |
|  | BLOB Transfer Client transfer inputs. [More...](structbt__mesh__blob__cli__inputs.md#details) |
| struct | [bt\_mesh\_blob\_cli\_caps](structbt__mesh__blob__cli__caps.md) |
|  | Transfer capabilities of a Target node. [More...](structbt__mesh__blob__cli__caps.md#details) |
| struct | [bt\_mesh\_blob\_cli\_cb](structbt__mesh__blob__cli__cb.md) |
|  | Event handler callbacks for the BLOB Transfer Client model. [More...](structbt__mesh__blob__cli__cb.md#details) |
| struct | [bt\_mesh\_blob\_cli](structbt__mesh__blob__cli.md) |
|  | BLOB Transfer Client model instance. [More...](structbt__mesh__blob__cli.md#details) |

| Macros | |
| --- | --- |
| #define | [BT\_MESH\_MODEL\_BLOB\_CLI](group__bt__mesh__blob__cli.md#ga882e9cec348625c7990de4ee5eb7ed5a)(\_cli) |
|  | BLOB Transfer Client model Composition Data entry. |

| Enumerations | |
| --- | --- |
| enum | [bt\_mesh\_blob\_cli\_state](group__bt__mesh__blob__cli.md#gac86db11f09e53adb2e012bf9e446d073) {     [BT\_MESH\_BLOB\_CLI\_STATE\_NONE](group__bt__mesh__blob__cli.md#ggac86db11f09e53adb2e012bf9e446d073a39701bbca32d8e5604209ea9bfed4f67) , [BT\_MESH\_BLOB\_CLI\_STATE\_CAPS\_GET](group__bt__mesh__blob__cli.md#ggac86db11f09e53adb2e012bf9e446d073a62af740ae63c6fae5c57497cdb39e5de) , [BT\_MESH\_BLOB\_CLI\_STATE\_START](group__bt__mesh__blob__cli.md#ggac86db11f09e53adb2e012bf9e446d073a83147e88a189abaea6276d2e48817ba2) , [BT\_MESH\_BLOB\_CLI\_STATE\_BLOCK\_START](group__bt__mesh__blob__cli.md#ggac86db11f09e53adb2e012bf9e446d073afd1a1426dd70e55f37ab822154d6cbb2) ,     [BT\_MESH\_BLOB\_CLI\_STATE\_BLOCK\_SEND](group__bt__mesh__blob__cli.md#ggac86db11f09e53adb2e012bf9e446d073adb4647d56ef152bde695eda6931df7c9) , [BT\_MESH\_BLOB\_CLI\_STATE\_BLOCK\_CHECK](group__bt__mesh__blob__cli.md#ggac86db11f09e53adb2e012bf9e446d073a18e10582c69e8f41416bf6833bd0db3c) , [BT\_MESH\_BLOB\_CLI\_STATE\_XFER\_CHECK](group__bt__mesh__blob__cli.md#ggac86db11f09e53adb2e012bf9e446d073aa4f4df9bf0f1e3e2ef976ce56373dd96) , [BT\_MESH\_BLOB\_CLI\_STATE\_CANCEL](group__bt__mesh__blob__cli.md#ggac86db11f09e53adb2e012bf9e446d073a4914077b12568211537a0861e7c2c646) ,     [BT\_MESH\_BLOB\_CLI\_STATE\_SUSPENDED](group__bt__mesh__blob__cli.md#ggac86db11f09e53adb2e012bf9e446d073a7dd8ce9317e067084e9810b2fd8210d9) , [BT\_MESH\_BLOB\_CLI\_STATE\_XFER\_PROGRESS\_GET](group__bt__mesh__blob__cli.md#ggac86db11f09e53adb2e012bf9e446d073aeb4ee8f592692287b13a5e973d12413c)   } |
|  | BLOB Transfer Client state. [More...](group__bt__mesh__blob__cli.md#gac86db11f09e53adb2e012bf9e446d073) |

| Functions | |
| --- | --- |
| int | [bt\_mesh\_blob\_cli\_caps\_get](group__bt__mesh__blob__cli.md#gac401336775dc6274450d5e27ea1cd720) (struct [bt\_mesh\_blob\_cli](structbt__mesh__blob__cli.md) \*cli, const struct [bt\_mesh\_blob\_cli\_inputs](structbt__mesh__blob__cli__inputs.md) \*inputs) |
|  | Retrieve transfer capabilities for a list of Target nodes. |
| int | [bt\_mesh\_blob\_cli\_send](group__bt__mesh__blob__cli.md#ga708e4afb3d9e1d6a8fb02d8fd5ab78c2) (struct [bt\_mesh\_blob\_cli](structbt__mesh__blob__cli.md) \*cli, const struct [bt\_mesh\_blob\_cli\_inputs](structbt__mesh__blob__cli__inputs.md) \*inputs, const struct [bt\_mesh\_blob\_xfer](structbt__mesh__blob__xfer.md) \*xfer, const struct [bt\_mesh\_blob\_io](structbt__mesh__blob__io.md) \*io) |
|  | Perform a BLOB transfer. |
| int | [bt\_mesh\_blob\_cli\_suspend](group__bt__mesh__blob__cli.md#ga78487f10fae6c87edaaf4e6ec8f7362c) (struct [bt\_mesh\_blob\_cli](structbt__mesh__blob__cli.md) \*cli) |
|  | Suspend the active transfer. |
| int | [bt\_mesh\_blob\_cli\_resume](group__bt__mesh__blob__cli.md#ga5aed01e812215d153fdfafd6375cc453) (struct [bt\_mesh\_blob\_cli](structbt__mesh__blob__cli.md) \*cli) |
|  | Resume the suspended transfer. |
| void | [bt\_mesh\_blob\_cli\_cancel](group__bt__mesh__blob__cli.md#ga222c650657e9a7958b119d4dddd55783) (struct [bt\_mesh\_blob\_cli](structbt__mesh__blob__cli.md) \*cli) |
|  | Cancel an ongoing transfer. |
| int | [bt\_mesh\_blob\_cli\_xfer\_progress\_get](group__bt__mesh__blob__cli.md#ga17a73cb313dbfc6652b4bcf638b9a30f) (struct [bt\_mesh\_blob\_cli](structbt__mesh__blob__cli.md) \*cli, const struct [bt\_mesh\_blob\_cli\_inputs](structbt__mesh__blob__cli__inputs.md) \*inputs) |
|  | Get the progress of BLOB transfer. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [bt\_mesh\_blob\_cli\_xfer\_progress\_active\_get](group__bt__mesh__blob__cli.md#ga065196837cbf9d2626b5589ce2671441) (struct [bt\_mesh\_blob\_cli](structbt__mesh__blob__cli.md) \*cli) |
|  | Get the current progress of the active transfer in percent. |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [bt\_mesh\_blob\_cli\_is\_busy](group__bt__mesh__blob__cli.md#ga37bbc559b48ea8cfe7cb3ddf8cad24da) (struct [bt\_mesh\_blob\_cli](structbt__mesh__blob__cli.md) \*cli) |
|  | Get the current state of the BLOB Transfer Client. |
| void | [bt\_mesh\_blob\_cli\_set\_chunk\_interval\_ms](group__bt__mesh__blob__cli.md#ga047e0cd9817b2ff0a241b2ccfad2acf6) (struct [bt\_mesh\_blob\_cli](structbt__mesh__blob__cli.md) \*cli, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) interval\_ms) |
|  | Set chunk sending interval in ms. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [mesh](dir_cb009b76fe94f798a2c866bd15366281.md)
- [blob\_cli.h](blob__cli_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

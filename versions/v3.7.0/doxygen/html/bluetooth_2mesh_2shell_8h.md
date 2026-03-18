---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/bluetooth_2mesh_2shell_8h.html
original_path: doxygen/html/bluetooth_2mesh_2shell_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

shell.h File Reference

`#include <[zephyr/bluetooth/mesh.h](mesh_8h_source.md)>`

[Go to the source code of this file.](bluetooth_2mesh_2shell_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [bt\_mesh\_shell\_target](structbt__mesh__shell__target.md) |
|  | Target context for the mesh shell. [More...](structbt__mesh__shell__target.md#details) |

| Macros | |
| --- | --- |
| #define | [BT\_MESH\_SHELL\_CUR\_FAULTS\_MAX](#aac63a324676ab3297e509fc5d1afe951)   4 |
|  | Maximum number of faults the health server can have. |
| #define | [BT\_MESH\_SHELL\_HEALTH\_PUB\_DEFINE](#a8cd77ce286185c704e64c891d315a1d0)(\_name) |
|  | A helper to define a health publication context for shell with the shell's maximum number of faults the element can have. |

| Variables | |
| --- | --- |
| struct [bt\_mesh\_health\_srv](structbt__mesh__health__srv.md) | [bt\_mesh\_shell\_health\_srv](#a313cd00833d5b522a73a3ac5e4eb9596) |
|  | External reference to health server. |
| const struct [bt\_mesh\_models\_metadata\_entry](structbt__mesh__models__metadata__entry.md) | [health\_srv\_meta](#a5ccd2d0b4a3ff642a89fcd77dd0e935f) [] |
|  | External reference to health server metadata. |
| struct [bt\_mesh\_health\_cli](structbt__mesh__health__cli.md) | [bt\_mesh\_shell\_health\_cli](#a4c7a470a6d7cc91ea1b240756053d017) |
|  | External reference to health client. |
| struct [bt\_mesh\_dfu\_srv](structbt__mesh__dfu__srv.md) | [bt\_mesh\_shell\_dfu\_srv](#a0bac1827aa84e4801252c9b955373067) |
|  | External reference to Firmware Update Server. |
| struct [bt\_mesh\_dfu\_cli](structbt__mesh__dfu__cli.md) | [bt\_mesh\_shell\_dfu\_cli](#a9bc67c98117f6a8741bbd3e40f718b3b) |
|  | External reference to Firmware Update Client. |
| struct [bt\_mesh\_blob\_srv](structbt__mesh__blob__srv.md) | [bt\_mesh\_shell\_blob\_srv](#a4c4b37f663428cedfb466832963b9c1b) |
|  | External reference to BLOB Transfer Server. |
| struct [bt\_mesh\_blob\_cli](structbt__mesh__blob__cli.md) | [bt\_mesh\_shell\_blob\_cli](#accbfc012251815338ace23f8cb49fff6) |
|  | External reference to BLOB Transfer Client. |
| struct [bt\_mesh\_rpr\_cli](structbt__mesh__rpr__cli.md) | [bt\_mesh\_shell\_rpr\_cli](#a231f1c8492097ae23edb2aeb82139752) |
|  | External reference to Remote Provisioning Client. |
| struct [bt\_mesh\_prov](structbt__mesh__prov.md) | [bt\_mesh\_shell\_prov](#a1e999cded973436a218782acac1ab15b) |
|  | External reference to provisioning handler. |
| struct [bt\_mesh\_shell\_target](structbt__mesh__shell__target.md) | [bt\_mesh\_shell\_target\_ctx](#ab76d90bc284131a56904a2c1b9c19ae2) |
|  | External reference to shell target context. |

## Macro Definition Documentation

## [◆ ](#aac63a324676ab3297e509fc5d1afe951)BT\_MESH\_SHELL\_CUR\_FAULTS\_MAX

| #define BT\_MESH\_SHELL\_CUR\_FAULTS\_MAX   4 |
| --- |

Maximum number of faults the health server can have.

## [◆ ](#a8cd77ce286185c704e64c891d315a1d0)BT\_MESH\_SHELL\_HEALTH\_PUB\_DEFINE

| #define BT\_MESH\_SHELL\_HEALTH\_PUB\_DEFINE | ( |  | *\_name* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[BT\_MESH\_HEALTH\_PUB\_DEFINE](group__bt__mesh__health__srv.md#ga35c500e915092ec365862b11e76f92ad)(\_name, \

[BT\_MESH\_SHELL\_CUR\_FAULTS\_MAX](#aac63a324676ab3297e509fc5d1afe951));

[BT\_MESH\_SHELL\_CUR\_FAULTS\_MAX](#aac63a324676ab3297e509fc5d1afe951)

#define BT\_MESH\_SHELL\_CUR\_FAULTS\_MAX

Maximum number of faults the health server can have.

**Definition** shell.h:16

[BT\_MESH\_HEALTH\_PUB\_DEFINE](group__bt__mesh__health__srv.md#ga35c500e915092ec365862b11e76f92ad)

#define BT\_MESH\_HEALTH\_PUB\_DEFINE(\_name, \_max\_faults)

A helper to define a health publication context.

**Definition** health\_srv.h:146

A helper to define a health publication context for shell with the shell's maximum number of faults the element can have.

Parameters
:   | \_name | Name given to the publication context variable. |
    | --- | --- |

## Variable Documentation

## [◆ ](#accbfc012251815338ace23f8cb49fff6)bt\_mesh\_shell\_blob\_cli

| | struct [bt\_mesh\_blob\_cli](structbt__mesh__blob__cli.md) bt\_mesh\_shell\_blob\_cli | | --- | | extern |
| --- | --- | --- |

External reference to BLOB Transfer Client.

## [◆ ](#a4c4b37f663428cedfb466832963b9c1b)bt\_mesh\_shell\_blob\_srv

| | struct [bt\_mesh\_blob\_srv](structbt__mesh__blob__srv.md) bt\_mesh\_shell\_blob\_srv | | --- | | extern |
| --- | --- | --- |

External reference to BLOB Transfer Server.

## [◆ ](#a9bc67c98117f6a8741bbd3e40f718b3b)bt\_mesh\_shell\_dfu\_cli

| | struct [bt\_mesh\_dfu\_cli](structbt__mesh__dfu__cli.md) bt\_mesh\_shell\_dfu\_cli | | --- | | extern |
| --- | --- | --- |

External reference to Firmware Update Client.

## [◆ ](#a0bac1827aa84e4801252c9b955373067)bt\_mesh\_shell\_dfu\_srv

| | struct [bt\_mesh\_dfu\_srv](structbt__mesh__dfu__srv.md) bt\_mesh\_shell\_dfu\_srv | | --- | | extern |
| --- | --- | --- |

External reference to Firmware Update Server.

## [◆ ](#a4c7a470a6d7cc91ea1b240756053d017)bt\_mesh\_shell\_health\_cli

| | struct [bt\_mesh\_health\_cli](structbt__mesh__health__cli.md) bt\_mesh\_shell\_health\_cli | | --- | | extern |
| --- | --- | --- |

External reference to health client.

## [◆ ](#a313cd00833d5b522a73a3ac5e4eb9596)bt\_mesh\_shell\_health\_srv

| | struct [bt\_mesh\_health\_srv](structbt__mesh__health__srv.md) bt\_mesh\_shell\_health\_srv | | --- | | extern |
| --- | --- | --- |

External reference to health server.

## [◆ ](#a1e999cded973436a218782acac1ab15b)bt\_mesh\_shell\_prov

| | struct [bt\_mesh\_prov](structbt__mesh__prov.md) bt\_mesh\_shell\_prov | | --- | | extern |
| --- | --- | --- |

External reference to provisioning handler.

## [◆ ](#a231f1c8492097ae23edb2aeb82139752)bt\_mesh\_shell\_rpr\_cli

| | struct [bt\_mesh\_rpr\_cli](structbt__mesh__rpr__cli.md) bt\_mesh\_shell\_rpr\_cli | | --- | | extern |
| --- | --- | --- |

External reference to Remote Provisioning Client.

## [◆ ](#ab76d90bc284131a56904a2c1b9c19ae2)bt\_mesh\_shell\_target\_ctx

| | struct [bt\_mesh\_shell\_target](structbt__mesh__shell__target.md) bt\_mesh\_shell\_target\_ctx | | --- | | extern |
| --- | --- | --- |

External reference to shell target context.

## [◆ ](#a5ccd2d0b4a3ff642a89fcd77dd0e935f)health\_srv\_meta

| | const struct [bt\_mesh\_models\_metadata\_entry](structbt__mesh__models__metadata__entry.md) health\_srv\_meta[] | | --- | | extern |
| --- | --- | --- |

External reference to health server metadata.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [mesh](dir_cb009b76fe94f798a2c866bd15366281.md)
- [shell.h](bluetooth_2mesh_2shell_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

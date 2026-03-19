---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structbt__mesh__brg__cfg__cli__cb.html
original_path: doxygen/html/structbt__mesh__brg__cfg__cli__cb.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_mesh\_brg\_cfg\_cli\_cb Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md) » [Bridge Configuration Client Model](group__bt__mesh__brg__cfg__cli.md)

Mesh Bridge Configuration Client Status messages callback.
[More...](#details)

`#include <[brg_cfg_cli.h](brg__cfg__cli_8h_source.md)>`

| Data Fields | |
| --- | --- |
| void(\* | [bridge\_status](#ac045febf91cc95982985e6de094e403b) )(struct [bt\_mesh\_brg\_cfg\_cli](structbt__mesh__brg__cfg__cli.md) \*cli, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, enum [bt\_mesh\_brg\_cfg\_state](group__bt__mesh__brg__cfg.md#ga7bddcbe2b1196df6a1c80d8c213866f9) status) |
|  | Optional callback for Subnet Bridge Status message. |
| void(\* | [table\_size\_status](#afe8e0a5ed681630e826ff0aa3889cd88) )(struct [bt\_mesh\_brg\_cfg\_cli](structbt__mesh__brg__cfg__cli.md) \*cli, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) size) |
|  | Optional callback for Bridging Table Size Status message. |
| void(\* | [table\_status](#a608b74d78f2f4bb06130f40071ac93af) )(struct [bt\_mesh\_brg\_cfg\_cli](structbt__mesh__brg__cfg__cli.md) \*cli, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, struct [bt\_mesh\_brg\_cfg\_table\_status](structbt__mesh__brg__cfg__table__status.md) \*rsp) |
|  | Optional callback for Bridging Table Status message. |
| void(\* | [subnets\_list](#a947e2169ed2cb0964c082bd82c1b0943) )(struct [bt\_mesh\_brg\_cfg\_cli](structbt__mesh__brg__cfg__cli.md) \*cli, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, struct [bt\_mesh\_brg\_cfg\_subnets\_list](structbt__mesh__brg__cfg__subnets__list.md) \*rsp) |
|  | Optional callback for Bridged Subnets List message. |
| void(\* | [table\_list](#a3817e30dd90b161a7442604207ed0ba8) )(struct [bt\_mesh\_brg\_cfg\_cli](structbt__mesh__brg__cfg__cli.md) \*cli, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, struct [bt\_mesh\_brg\_cfg\_table\_list](structbt__mesh__brg__cfg__table__list.md) \*rsp) |
|  | Optional callback for Bridging Table List message. |

## Detailed Description

Mesh Bridge Configuration Client Status messages callback.

## Field Documentation

## [◆ ](#ac045febf91cc95982985e6de094e403b)bridge\_status

| void(\* bt\_mesh\_brg\_cfg\_cli\_cb::bridge\_status) (struct [bt\_mesh\_brg\_cfg\_cli](structbt__mesh__brg__cfg__cli.md) \*cli, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, enum [bt\_mesh\_brg\_cfg\_state](group__bt__mesh__brg__cfg.md#ga7bddcbe2b1196df6a1c80d8c213866f9) status) |
| --- |

Optional callback for Subnet Bridge Status message.

Handles received Subnet Bridge Status messages from a Bridge Configuration Server.

Parameters
:   | cli | Bridge Configuration Client context. |
    | --- | --- |
    | addr | Address of the sender. |
    | status | Status received from the server. |

## [◆ ](#a947e2169ed2cb0964c082bd82c1b0943)subnets\_list

| void(\* bt\_mesh\_brg\_cfg\_cli\_cb::subnets\_list) (struct [bt\_mesh\_brg\_cfg\_cli](structbt__mesh__brg__cfg__cli.md) \*cli, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, struct [bt\_mesh\_brg\_cfg\_subnets\_list](structbt__mesh__brg__cfg__subnets__list.md) \*rsp) |
| --- |

Optional callback for Bridged Subnets List message.

Handles received Bridged Subnets List messages from a Bridge Configuration Server.

Parameters
:   | cli | Bridge Configuration Client context. |
    | --- | --- |
    | addr | Address of the sender. |
    | rsp | Response received from the Bridging Configuration Server. |

## [◆ ](#a3817e30dd90b161a7442604207ed0ba8)table\_list

| void(\* bt\_mesh\_brg\_cfg\_cli\_cb::table\_list) (struct [bt\_mesh\_brg\_cfg\_cli](structbt__mesh__brg__cfg__cli.md) \*cli, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, struct [bt\_mesh\_brg\_cfg\_table\_list](structbt__mesh__brg__cfg__table__list.md) \*rsp) |
| --- |

Optional callback for Bridging Table List message.

Handles received Bridging Table List messages from a Bridge Configuration Server.

Parameters
:   | cli | Bridge Configuration Client context. |
    | --- | --- |
    | addr | Address of the sender. |
    | rsp | Response received from the Bridging Configuration Server. |

## [◆ ](#afe8e0a5ed681630e826ff0aa3889cd88)table\_size\_status

| void(\* bt\_mesh\_brg\_cfg\_cli\_cb::table\_size\_status) (struct [bt\_mesh\_brg\_cfg\_cli](structbt__mesh__brg__cfg__cli.md) \*cli, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) size) |
| --- |

Optional callback for Bridging Table Size Status message.

Handles received Bridging Table Size Status messages from a Bridge Configuration Server.

Parameters
:   | cli | Bridge Configuration Client context. |
    | --- | --- |
    | addr | Address of the sender. |
    | size | Size received from the server. |

## [◆ ](#a608b74d78f2f4bb06130f40071ac93af)table\_status

| void(\* bt\_mesh\_brg\_cfg\_cli\_cb::table\_status) (struct [bt\_mesh\_brg\_cfg\_cli](structbt__mesh__brg__cfg__cli.md) \*cli, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, struct [bt\_mesh\_brg\_cfg\_table\_status](structbt__mesh__brg__cfg__table__status.md) \*rsp) |
| --- |

Optional callback for Bridging Table Status message.

Handles received Bridging Table status messages from a Bridge Configuration Server.

Parameters
:   | cli | Bridge Configuration Client context. |
    | --- | --- |
    | addr | Address of the sender. |
    | rsp | Response received from the Bridging Configuration Server. |

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/mesh/[brg\_cfg\_cli.h](brg__cfg__cli_8h_source.md)

- [bt\_mesh\_brg\_cfg\_cli\_cb](structbt__mesh__brg__cfg__cli__cb.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

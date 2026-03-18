---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structbt__mesh__large__comp__data__cli__cb.html
original_path: doxygen/html/structbt__mesh__large__comp__data__cli__cb.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_mesh\_large\_comp\_data\_cli\_cb Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md) » [Large Composition Data Client model](group__bt__mesh__large__comp__data__cli.md)

Large Composition Data Status messages callbacks.
[More...](#details)

`#include <[large_comp_data_cli.h](large__comp__data__cli_8h_source.md)>`

| Data Fields | |
| --- | --- |
| void(\* | [large\_comp\_data\_status](#ab0e17df5eb165a44d70542b8edd36ab9) )(struct [bt\_mesh\_large\_comp\_data\_cli](structbt__mesh__large__comp__data__cli.md) \*cli, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, struct [bt\_mesh\_large\_comp\_data\_rsp](structbt__mesh__large__comp__data__rsp.md) \*rsp) |
|  | Optional callback for Large Composition Data Status message. |
| void(\* | [models\_metadata\_status](#ade54d137534ffb2274e366140f6cbd3c) )(struct [bt\_mesh\_large\_comp\_data\_cli](structbt__mesh__large__comp__data__cli.md) \*cli, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, struct [bt\_mesh\_large\_comp\_data\_rsp](structbt__mesh__large__comp__data__rsp.md) \*rsp) |
|  | Optional callback for Models Metadata Status message. |

## Detailed Description

Large Composition Data Status messages callbacks.

## Field Documentation

## [◆ ](#ab0e17df5eb165a44d70542b8edd36ab9)large\_comp\_data\_status

| void(\* bt\_mesh\_large\_comp\_data\_cli\_cb::large\_comp\_data\_status) (struct [bt\_mesh\_large\_comp\_data\_cli](structbt__mesh__large__comp__data__cli.md) \*cli, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, struct [bt\_mesh\_large\_comp\_data\_rsp](structbt__mesh__large__comp__data__rsp.md) \*rsp) |
| --- |

Optional callback for Large Composition Data Status message.

Handles received Large Composition Data Status messages from a Large Composition Data Server.

If the content of `rsp` is needed after exiting this callback, a user should deep copy it.

Parameters
:   | cli | Large Composition Data Client context. |
    | --- | --- |
    | addr | Address of the sender. |
    | rsp | Response received from the server. |

## [◆ ](#ade54d137534ffb2274e366140f6cbd3c)models\_metadata\_status

| void(\* bt\_mesh\_large\_comp\_data\_cli\_cb::models\_metadata\_status) (struct [bt\_mesh\_large\_comp\_data\_cli](structbt__mesh__large__comp__data__cli.md) \*cli, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, struct [bt\_mesh\_large\_comp\_data\_rsp](structbt__mesh__large__comp__data__rsp.md) \*rsp) |
| --- |

Optional callback for Models Metadata Status message.

Handles received Models Metadata Status messages from a Large Composition Data Server.

If the content of `rsp` is needed after exiting this callback, a user should deep copy it.

Parameters
:   | cli | Large Composition Data Client context. |
    | --- | --- |
    | addr | Address of the sender. |
    | rsp | Response received from the server. |

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/mesh/[large\_comp\_data\_cli.h](large__comp__data__cli_8h_source.md)

- [bt\_mesh\_large\_comp\_data\_cli\_cb](structbt__mesh__large__comp__data__cli__cb.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

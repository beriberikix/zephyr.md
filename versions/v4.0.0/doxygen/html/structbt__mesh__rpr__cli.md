---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structbt__mesh__rpr__cli.html
original_path: doxygen/html/structbt__mesh__rpr__cli.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_mesh\_rpr\_cli Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md) » [Remote Provisioning Client model](group__bt__mesh__rpr__cli.md)

Remote Provisioning Client model instance.
[More...](#details)

`#include <[rpr_cli.h](rpr__cli_8h_source.md)>`

| Data Fields | |
| --- | --- |
| void(\* | [scan\_report](#a32b3c63218b506d1bc5759640cb3fb81) )(struct [bt\_mesh\_rpr\_cli](structbt__mesh__rpr__cli.md) \*cli, const struct [bt\_mesh\_rpr\_node](structbt__mesh__rpr__node.md) \*[srv](#a8f5eea4cbb042f8a83050ad4ebfc64b7), struct [bt\_mesh\_rpr\_unprov](structbt__mesh__rpr__unprov.md) \*unprov, struct [net\_buf\_simple](structnet__buf__simple.md) \*adv\_data) |
|  | Scan report callback. |
| struct [bt\_mesh\_msg\_ack\_ctx](structbt__mesh__msg__ack__ctx.md) | [scan\_ack\_ctx](#a9cc5b67937ec8e0ff93ddfb55cb11528) |
| struct [bt\_mesh\_msg\_ack\_ctx](structbt__mesh__msg__ack__ctx.md) | [prov\_ack\_ctx](#a0e5a8d697b87f5f05bbce0aaa8c1fb1a) |
| struct { |  |
| struct [k\_work\_delayable](structk__work__delayable.md)   [timeout](#a64b12ca2ef9e47723c77a8af41eb0f89) |  |
| struct [bt\_mesh\_rpr\_node](structbt__mesh__rpr__node.md)   [srv](#a8f5eea4cbb042f8a83050ad4ebfc64b7) |  |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [time](#af03b9edb0a205e92182234c7a1355e0c) |  |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [tx\_pdu](#a68eaadc451224e155227d14102ff0a54) |  |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [rx\_pdu](#a8493c4b3c1e30cc0a6f58b765adb2e37) |  |
| enum [bt\_mesh\_rpr\_link\_state](group__bt__mesh__rpr.md#ga0266611238d10f8e97f2b07156991f43)   [state](#aa29cbb7e19cc659ce13b0b98604c93d5) |  |
| } | [link](#ad69049681d611aa48be4942745fb89a7) |
| const struct [bt\_mesh\_model](structbt__mesh__model.md) \* | [mod](#a188c9e610035b7225411b45733be5a85) |

## Detailed Description

Remote Provisioning Client model instance.

## Field Documentation

## [◆ ](#ad69049681d611aa48be4942745fb89a7)[struct]

| struct { ... } bt\_mesh\_rpr\_cli::link |
| --- |

## [◆ ](#a188c9e610035b7225411b45733be5a85)mod

| const struct [bt\_mesh\_model](structbt__mesh__model.md)\* bt\_mesh\_rpr\_cli::mod |
| --- |

## [◆ ](#a0e5a8d697b87f5f05bbce0aaa8c1fb1a)prov\_ack\_ctx

| struct [bt\_mesh\_msg\_ack\_ctx](structbt__mesh__msg__ack__ctx.md) bt\_mesh\_rpr\_cli::prov\_ack\_ctx |
| --- |

## [◆ ](#a8493c4b3c1e30cc0a6f58b765adb2e37)rx\_pdu

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_rpr\_cli::rx\_pdu |
| --- |

## [◆ ](#a9cc5b67937ec8e0ff93ddfb55cb11528)scan\_ack\_ctx

| struct [bt\_mesh\_msg\_ack\_ctx](structbt__mesh__msg__ack__ctx.md) bt\_mesh\_rpr\_cli::scan\_ack\_ctx |
| --- |

## [◆ ](#a32b3c63218b506d1bc5759640cb3fb81)scan\_report

| void(\* bt\_mesh\_rpr\_cli::scan\_report) (struct [bt\_mesh\_rpr\_cli](structbt__mesh__rpr__cli.md) \*cli, const struct [bt\_mesh\_rpr\_node](structbt__mesh__rpr__node.md) \*[srv](#a8f5eea4cbb042f8a83050ad4ebfc64b7), struct [bt\_mesh\_rpr\_unprov](structbt__mesh__rpr__unprov.md) \*unprov, struct [net\_buf\_simple](structnet__buf__simple.md) \*adv\_data) |
| --- |

Scan report callback.

Parameters
:   | cli | Remote Provisioning Client. |
    | --- | --- |
    | [srv](#a8f5eea4cbb042f8a83050ad4ebfc64b7) | Remote Provisioning Server. |
    | unprov | Unprovisioned device. |
    | adv\_data | Advertisement data for the unprovisioned device, or NULL if extended scanning hasn't been enabled. An empty buffer indicates that the extended scanning finished without collecting additional information. |

## [◆ ](#a8f5eea4cbb042f8a83050ad4ebfc64b7)srv

| struct [bt\_mesh\_rpr\_node](structbt__mesh__rpr__node.md) bt\_mesh\_rpr\_cli::srv |
| --- |

## [◆ ](#aa29cbb7e19cc659ce13b0b98604c93d5)state

| enum [bt\_mesh\_rpr\_link\_state](group__bt__mesh__rpr.md#ga0266611238d10f8e97f2b07156991f43) bt\_mesh\_rpr\_cli::state |
| --- |

## [◆ ](#af03b9edb0a205e92182234c7a1355e0c)time

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_rpr\_cli::time |
| --- |

## [◆ ](#a64b12ca2ef9e47723c77a8af41eb0f89)timeout

| struct [k\_work\_delayable](structk__work__delayable.md) bt\_mesh\_rpr\_cli::timeout |
| --- |

## [◆ ](#a68eaadc451224e155227d14102ff0a54)tx\_pdu

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_rpr\_cli::tx\_pdu |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/mesh/[rpr\_cli.h](rpr__cli_8h_source.md)

- [bt\_mesh\_rpr\_cli](structbt__mesh__rpr__cli.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

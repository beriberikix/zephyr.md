---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structbt__mesh__priv__beacon__cli.html
original_path: doxygen/html/structbt__mesh__priv__beacon__cli.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_mesh\_priv\_beacon\_cli Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md) » [Bluetooth Mesh Private Beacon Client](group__bt__mesh__priv__beacon__cli.md)

Mesh Private Beacon Client model.
[More...](#details)

`#include <[priv_beacon_cli.h](priv__beacon__cli_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const struct [bt\_mesh\_model](structbt__mesh__model.md) \* | [model](#a506b13407e466908d8a8684386bf3927) |
| struct [bt\_mesh\_msg\_ack\_ctx](structbt__mesh__msg__ack__ctx.md) | [ack\_ctx](#aa4105b00e2a3ad9027b888f0ebbea23e) |
| const struct [bt\_mesh\_priv\_beacon\_cli\_cb](structbt__mesh__priv__beacon__cli__cb.md) \* | [cb](#ab281b9ac10c54068372f90bccfe07feb) |
|  | Optional callback for Private Beacon Client Status messages. |

## Detailed Description

Mesh Private Beacon Client model.

## Field Documentation

## [◆ ](#aa4105b00e2a3ad9027b888f0ebbea23e)ack\_ctx

| struct [bt\_mesh\_msg\_ack\_ctx](structbt__mesh__msg__ack__ctx.md) bt\_mesh\_priv\_beacon\_cli::ack\_ctx |
| --- |

## [◆ ](#ab281b9ac10c54068372f90bccfe07feb)cb

| const struct [bt\_mesh\_priv\_beacon\_cli\_cb](structbt__mesh__priv__beacon__cli__cb.md)\* bt\_mesh\_priv\_beacon\_cli::cb |
| --- |

Optional callback for Private Beacon Client Status messages.

## [◆ ](#a506b13407e466908d8a8684386bf3927)model

| const struct [bt\_mesh\_model](structbt__mesh__model.md)\* bt\_mesh\_priv\_beacon\_cli::model |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/mesh/[priv\_beacon\_cli.h](priv__beacon__cli_8h_source.md)

- [bt\_mesh\_priv\_beacon\_cli](structbt__mesh__priv__beacon__cli.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

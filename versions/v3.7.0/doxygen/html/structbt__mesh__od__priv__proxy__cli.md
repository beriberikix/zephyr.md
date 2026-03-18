---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structbt__mesh__od__priv__proxy__cli.html
original_path: doxygen/html/structbt__mesh__od__priv__proxy__cli.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_mesh\_od\_priv\_proxy\_cli Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md) » [Bluetooth Mesh On-Demand Private GATT Proxy Client](group__bt__mesh__od__priv__proxy__cli.md)

On-Demand Private Proxy Client Model Context.
[More...](#details)

`#include <[od_priv_proxy_cli.h](od__priv__proxy__cli_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const struct [bt\_mesh\_model](structbt__mesh__model.md) \* | [model](#aeab540da0e42de4aa3e1550cd933f805) |
|  | Solicitation PDU RPL model entry pointer. |
| struct [bt\_mesh\_msg\_ack\_ctx](structbt__mesh__msg__ack__ctx.md) | [ack\_ctx](#a8f172612abc904718018a6c2d9002e5e) |
| void(\* | [od\_status](#aebd18bb98ded2e5dc3fca3fe121f3bc6) )(struct [bt\_mesh\_od\_priv\_proxy\_cli](structbt__mesh__od__priv__proxy__cli.md) \*cli, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)) |
|  | Optional callback for On-Demand Private Proxy Status messages. |

## Detailed Description

On-Demand Private Proxy Client Model Context.

## Field Documentation

## [◆ ](#a8f172612abc904718018a6c2d9002e5e)ack\_ctx

| struct [bt\_mesh\_msg\_ack\_ctx](structbt__mesh__msg__ack__ctx.md) bt\_mesh\_od\_priv\_proxy\_cli::ack\_ctx |
| --- |

## [◆ ](#aeab540da0e42de4aa3e1550cd933f805)model

| const struct [bt\_mesh\_model](structbt__mesh__model.md)\* bt\_mesh\_od\_priv\_proxy\_cli::model |
| --- |

Solicitation PDU RPL model entry pointer.

## [◆ ](#aebd18bb98ded2e5dc3fca3fe121f3bc6)od\_status

| void(\* bt\_mesh\_od\_priv\_proxy\_cli::od\_status) (struct [bt\_mesh\_od\_priv\_proxy\_cli](structbt__mesh__od__priv__proxy__cli.md) \*cli, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) addr, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)) |
| --- |

Optional callback for On-Demand Private Proxy Status messages.

Handles received On-Demand Private Proxy Status messages from a On-Demand Private Proxy server.The `state` param represents state of On-Demand Private Proxy server.

Parameters
:   | cli | On-Demand Private Proxy client that received the status message. |
    | --- | --- |
    | addr | Address of the sender. |
    | [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90) | State value. |

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/mesh/[od\_priv\_proxy\_cli.h](od__priv__proxy__cli_8h_source.md)

- [bt\_mesh\_od\_priv\_proxy\_cli](structbt__mesh__od__priv__proxy__cli.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

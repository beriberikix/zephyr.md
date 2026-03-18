---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structbt__mesh__dfu__cli.html
original_path: doxygen/html/structbt__mesh__dfu__cli.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_mesh\_dfu\_cli Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md) » [Bluetooth Mesh Device Firmware Update](group__bt__mesh__dfu.md) » [Firmware Uppdate Client model](group__bt__mesh__dfu__cli.md)

Firmware Update Client model instance.
[More...](#details)

`#include <[dfu_cli.h](dfu__cli_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const struct [bt\_mesh\_dfu\_cli\_cb](structbt__mesh__dfu__cli__cb.md) \* | [cb](#a18d31020aba939826aa34060a4a28121) |
|  | Callback structure. |
| struct [bt\_mesh\_blob\_cli](structbt__mesh__blob__cli.md) | [blob](#a945b5c9f70086ca57d3ee77704ece6fd) |
|  | Underlying BLOB Transfer Client. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [op](#a94924c2ad2654a14b23a07ea0351ec1b) |
| const struct [bt\_mesh\_model](structbt__mesh__model.md) \* | [mod](#ab882e681b4bfc66374503c83237f57dd) |
| struct { |  |
| const struct [bt\_mesh\_dfu\_slot](structbt__mesh__dfu__slot.md) \*   [slot](#a9396bb9e1245ab2613e3f7dfd753e793) |  |
| const struct [bt\_mesh\_blob\_io](structbt__mesh__blob__io.md) \*   [io](#a29a8240e5d47abaabf9d356bcdcba48d) |  |
| struct [bt\_mesh\_blob\_xfer](structbt__mesh__blob__xfer.md)   [blob](#a1848081925dce6ac2083ce5eb8fb0b33) |  |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [state](#aeaf4f0114a6a47ec6d866ce7b6714d47) |  |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [flags](#a3e5d177198a4c57ccd98a53c20490c89) |  |
| } | [xfer](#a9a8676e704a0346e1030f93d7ab6213c) |
| struct { |  |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [ttl](#a463a5c12df5ba3041c46c5c008d473da) |  |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [type](#a40b6dfe0c3dc545afc30cd18c5b498b2) |  |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [img\_cnt](#aa6f7be1a8dcd76f519e934654f96c909) |  |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)   [addr](#a67450510328c50e52fa97c80903508cd) |  |
| struct k\_sem   [sem](#af7ec498fa49b8e5cc0a3d67ad8dedee5) |  |
| void \*   [params](#ad6cc63e09b15d8471fde2192977be2ed) |  |
| [bt\_mesh\_dfu\_img\_cb\_t](group__bt__mesh__dfu__cli.md#ga2967b89e8fc3b848b70e493f6e821761)   [img\_cb](#a9531713e4659188de31015b66dfc38bc) |  |
| } | [req](#a8f5d37bda72f1a112428958404ddce63) |

## Detailed Description

Firmware Update Client model instance.

Should be initialized with [BT\_MESH\_DFU\_CLI\_INIT](group__bt__mesh__dfu__cli.md#ga0b10a95f9b7c806bfd8649280f535c96 "BT_MESH_DFU_CLI_INIT").

## Field Documentation

## [◆ ](#a67450510328c50e52fa97c80903508cd)addr

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_mesh\_dfu\_cli::addr |
| --- |

## [◆ ](#a1848081925dce6ac2083ce5eb8fb0b33)blob [1/2]

| struct [bt\_mesh\_blob\_xfer](structbt__mesh__blob__xfer.md) bt\_mesh\_dfu\_cli::blob |
| --- |

## [◆ ](#a945b5c9f70086ca57d3ee77704ece6fd)blob [2/2]

| struct [bt\_mesh\_blob\_cli](structbt__mesh__blob__cli.md) bt\_mesh\_dfu\_cli::blob |
| --- |

Underlying BLOB Transfer Client.

## [◆ ](#a18d31020aba939826aa34060a4a28121)cb

| const struct [bt\_mesh\_dfu\_cli\_cb](structbt__mesh__dfu__cli__cb.md)\* bt\_mesh\_dfu\_cli::cb |
| --- |

Callback structure.

## [◆ ](#a3e5d177198a4c57ccd98a53c20490c89)flags

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_dfu\_cli::flags |
| --- |

## [◆ ](#a9531713e4659188de31015b66dfc38bc)img\_cb

| [bt\_mesh\_dfu\_img\_cb\_t](group__bt__mesh__dfu__cli.md#ga2967b89e8fc3b848b70e493f6e821761) bt\_mesh\_dfu\_cli::img\_cb |
| --- |

## [◆ ](#aa6f7be1a8dcd76f519e934654f96c909)img\_cnt

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_dfu\_cli::img\_cnt |
| --- |

## [◆ ](#a29a8240e5d47abaabf9d356bcdcba48d)io

| const struct [bt\_mesh\_blob\_io](structbt__mesh__blob__io.md)\* bt\_mesh\_dfu\_cli::io |
| --- |

## [◆ ](#ab882e681b4bfc66374503c83237f57dd)mod

| const struct [bt\_mesh\_model](structbt__mesh__model.md)\* bt\_mesh\_dfu\_cli::mod |
| --- |

## [◆ ](#a94924c2ad2654a14b23a07ea0351ec1b)op

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bt\_mesh\_dfu\_cli::op |
| --- |

## [◆ ](#ad6cc63e09b15d8471fde2192977be2ed)params

| void\* bt\_mesh\_dfu\_cli::params |
| --- |

## [◆ ](#a8f5d37bda72f1a112428958404ddce63)[struct]

| struct { ... } bt\_mesh\_dfu\_cli::req |
| --- |

## [◆ ](#af7ec498fa49b8e5cc0a3d67ad8dedee5)sem

| struct k\_sem bt\_mesh\_dfu\_cli::sem |
| --- |

## [◆ ](#a9396bb9e1245ab2613e3f7dfd753e793)slot

| const struct [bt\_mesh\_dfu\_slot](structbt__mesh__dfu__slot.md)\* bt\_mesh\_dfu\_cli::slot |
| --- |

## [◆ ](#aeaf4f0114a6a47ec6d866ce7b6714d47)state

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_dfu\_cli::state |
| --- |

## [◆ ](#a463a5c12df5ba3041c46c5c008d473da)ttl

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_dfu\_cli::ttl |
| --- |

## [◆ ](#a40b6dfe0c3dc545afc30cd18c5b498b2)type

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_dfu\_cli::type |
| --- |

## [◆ ](#a9a8676e704a0346e1030f93d7ab6213c)[struct]

| struct { ... } bt\_mesh\_dfu\_cli::xfer |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/mesh/[dfu\_cli.h](dfu__cli_8h_source.md)

- [bt\_mesh\_dfu\_cli](structbt__mesh__dfu__cli.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structbt__mesh__blob__cli.html
original_path: doxygen/html/structbt__mesh__blob__cli.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_mesh\_blob\_cli Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md) » [Bluetooth Mesh BLOB Transfer Client model API](group__bt__mesh__blob__cli.md)

BLOB Transfer Client model instance.
[More...](#details)

`#include <[blob_cli.h](blob__cli_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const struct [bt\_mesh\_blob\_cli\_cb](structbt__mesh__blob__cli__cb.md) \* | [cb](#a6a0229165fe19af03a26e5cffa1e1486) |
|  | Event handler callbacks. |
| const struct [bt\_mesh\_model](structbt__mesh__model.md) \* | [mod](#ada23952593d2a498ed421895828f461f) |
| struct { |  |
| struct [bt\_mesh\_blob\_target](structbt__mesh__blob__target.md) \*   [target](#a519aa0aa7aa66ca67cdf813fee1632c3) |  |
| struct blob\_cli\_broadcast\_ctx   [ctx](#a850d232b04118d7564537dc6763a476c) |  |
| struct [k\_work\_delayable](structk__work__delayable.md)   [retry](#add07e03f13b276fafabeb9cc4ba94d32) |  |
| [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b)   [cli\_timestamp](#a850cc6f4426fec9dc9066953a1b992c8) |  |
| struct [k\_work\_delayable](structk__work__delayable.md)   [complete](#a21b064cceace34605e42d5c295f12cd5) |  |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)   [pending](#a1778ae8975ed4b9bc67616e5a0bdf3a9) |  |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [retries](#ab291086be3d9ecf03becd4200d783835) |  |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [sending](#a85fdd17b04a06e880f20a0e2b1319ff0): 1 |  |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)   [cancelled](#a6d70ac26b7fec22dfdc21f479d867ef7): 1 |  |
| } | [tx](#a388183549ed5b1af0d2ac09263611a33) |
| const struct [bt\_mesh\_blob\_io](structbt__mesh__blob__io.md) \* | [io](#a49f0d79d76aaea785a5ad9160be40e8a) |
| const struct [bt\_mesh\_blob\_cli\_inputs](structbt__mesh__blob__cli__inputs.md) \* | [inputs](#aa6c79f5476f96a35c731b63723b2c6cc) |
| const struct [bt\_mesh\_blob\_xfer](structbt__mesh__blob__xfer.md) \* | [xfer](#a9185cdadba15bce7b2bf2fcc6f85904a) |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [chunk\_interval\_ms](#a2ffd91b68c0aab92f16d9fb4eac79f9d) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [block\_count](#a645fdb1f0efb281b1faae4692a3404f1) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [chunk\_idx](#aafaf644e30e10a8ad9ca6dc8b680eff6) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [mtu\_size](#aafe943fcada25f32b9a31b8d7586032a) |
| enum [bt\_mesh\_blob\_cli\_state](group__bt__mesh__blob__cli.md#gac86db11f09e53adb2e012bf9e446d073) | [state](#ab131637681a0cf0b3ceebad015b28726) |
| struct [bt\_mesh\_blob\_block](structbt__mesh__blob__block.md) | [block](#ac95970f7fd6b00fca284121394110250) |
| struct [bt\_mesh\_blob\_cli\_caps](structbt__mesh__blob__cli__caps.md) | [caps](#aa7713e6ad0183d18946646df7a5cb6ab) |

## Detailed Description

BLOB Transfer Client model instance.

## Field Documentation

## [◆ ](#ac95970f7fd6b00fca284121394110250)block

| struct [bt\_mesh\_blob\_block](structbt__mesh__blob__block.md) bt\_mesh\_blob\_cli::block |
| --- |

## [◆ ](#a645fdb1f0efb281b1faae4692a3404f1)block\_count

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_mesh\_blob\_cli::block\_count |
| --- |

## [◆ ](#a6d70ac26b7fec22dfdc21f479d867ef7)cancelled

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_blob\_cli::cancelled |
| --- |

## [◆ ](#aa7713e6ad0183d18946646df7a5cb6ab)caps

| struct [bt\_mesh\_blob\_cli\_caps](structbt__mesh__blob__cli__caps.md) bt\_mesh\_blob\_cli::caps |
| --- |

## [◆ ](#a6a0229165fe19af03a26e5cffa1e1486)cb

| const struct [bt\_mesh\_blob\_cli\_cb](structbt__mesh__blob__cli__cb.md)\* bt\_mesh\_blob\_cli::cb |
| --- |

Event handler callbacks.

## [◆ ](#aafaf644e30e10a8ad9ca6dc8b680eff6)chunk\_idx

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_mesh\_blob\_cli::chunk\_idx |
| --- |

## [◆ ](#a2ffd91b68c0aab92f16d9fb4eac79f9d)chunk\_interval\_ms

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bt\_mesh\_blob\_cli::chunk\_interval\_ms |
| --- |

## [◆ ](#a850cc6f4426fec9dc9066953a1b992c8)cli\_timestamp

| [int64\_t](stdint_8h.md#ac714c0d2c1a4adb10e73cab29623314b) bt\_mesh\_blob\_cli::cli\_timestamp |
| --- |

## [◆ ](#a21b064cceace34605e42d5c295f12cd5)complete

| struct [k\_work\_delayable](structk__work__delayable.md) bt\_mesh\_blob\_cli::complete |
| --- |

## [◆ ](#a850d232b04118d7564537dc6763a476c)ctx

| struct blob\_cli\_broadcast\_ctx bt\_mesh\_blob\_cli::ctx |
| --- |

## [◆ ](#aa6c79f5476f96a35c731b63723b2c6cc)inputs

| const struct [bt\_mesh\_blob\_cli\_inputs](structbt__mesh__blob__cli__inputs.md)\* bt\_mesh\_blob\_cli::inputs |
| --- |

## [◆ ](#a49f0d79d76aaea785a5ad9160be40e8a)io

| const struct [bt\_mesh\_blob\_io](structbt__mesh__blob__io.md)\* bt\_mesh\_blob\_cli::io |
| --- |

## [◆ ](#ada23952593d2a498ed421895828f461f)mod

| const struct [bt\_mesh\_model](structbt__mesh__model.md)\* bt\_mesh\_blob\_cli::mod |
| --- |

## [◆ ](#aafe943fcada25f32b9a31b8d7586032a)mtu\_size

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_mesh\_blob\_cli::mtu\_size |
| --- |

## [◆ ](#a1778ae8975ed4b9bc67616e5a0bdf3a9)pending

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_mesh\_blob\_cli::pending |
| --- |

## [◆ ](#ab291086be3d9ecf03becd4200d783835)retries

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_blob\_cli::retries |
| --- |

## [◆ ](#add07e03f13b276fafabeb9cc4ba94d32)retry

| struct [k\_work\_delayable](structk__work__delayable.md) bt\_mesh\_blob\_cli::retry |
| --- |

## [◆ ](#a85fdd17b04a06e880f20a0e2b1319ff0)sending

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_mesh\_blob\_cli::sending |
| --- |

## [◆ ](#ab131637681a0cf0b3ceebad015b28726)state

| enum [bt\_mesh\_blob\_cli\_state](group__bt__mesh__blob__cli.md#gac86db11f09e53adb2e012bf9e446d073) bt\_mesh\_blob\_cli::state |
| --- |

## [◆ ](#a519aa0aa7aa66ca67cdf813fee1632c3)target

| struct [bt\_mesh\_blob\_target](structbt__mesh__blob__target.md)\* bt\_mesh\_blob\_cli::target |
| --- |

## [◆ ](#a388183549ed5b1af0d2ac09263611a33)[struct]

| struct { ... } bt\_mesh\_blob\_cli::tx |
| --- |

## [◆ ](#a9185cdadba15bce7b2bf2fcc6f85904a)xfer

| const struct [bt\_mesh\_blob\_xfer](structbt__mesh__blob__xfer.md)\* bt\_mesh\_blob\_cli::xfer |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/mesh/[blob\_cli.h](blob__cli_8h_source.md)

- [bt\_mesh\_blob\_cli](structbt__mesh__blob__cli.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

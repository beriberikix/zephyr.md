---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structbt__br__discovery__cb.html
original_path: doxygen/html/structbt__br__discovery__cb.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_br\_discovery\_cb Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Generic Access Profile (GAP)](group__bt__gap.md)

`#include <[classic.h](classic_8h_source.md)>`

| Data Fields | |
| --- | --- |
| void(\* | [recv](#a3315f86bf3c9dbf339aa2254e0679182) )(const struct [bt\_br\_discovery\_result](structbt__br__discovery__result.md) \*result) |
|  | An inquiry response received callback. |
| void(\* | [timeout](#a09c9f7258ea1739bf9330cf5c5bd882d) )(const struct [bt\_br\_discovery\_result](structbt__br__discovery__result.md) \*results, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) count) |
|  | The inquiry has stopped after discovery timeout. |
| [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) | [node](#a6ea814cabf9747cc7720ece9be59c8b9) |

## Field Documentation

## [◆ ](#a6ea814cabf9747cc7720ece9be59c8b9)node

| [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) bt\_br\_discovery\_cb::node |
| --- |

## [◆ ](#a3315f86bf3c9dbf339aa2254e0679182)recv

| void(\* bt\_br\_discovery\_cb::recv) (const struct [bt\_br\_discovery\_result](structbt__br__discovery__result.md) \*result) |
| --- |

An inquiry response received callback.

Parameters
:   | result | Storage used for discovery results |
    | --- | --- |

## [◆ ](#a09c9f7258ea1739bf9330cf5c5bd882d)timeout

| void(\* bt\_br\_discovery\_cb::timeout) (const struct [bt\_br\_discovery\_result](structbt__br__discovery__result.md) \*results, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) count) |
| --- |

The inquiry has stopped after discovery timeout.

Parameters
:   | results | Storage used for discovery results |
    | --- | --- |
    | count | Number of valid discovery results. |

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/classic/[classic.h](classic_8h_source.md)

- [bt\_br\_discovery\_cb](structbt__br__discovery__cb.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

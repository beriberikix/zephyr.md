---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structbt__mesh__dfd__srv.html
original_path: doxygen/html/structbt__mesh__dfd__srv.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_mesh\_dfd\_srv Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth Mesh](group__bt__mesh.md) » [Firmware Distribution models](group__bt__mesh__dfd.md) » [Firmware Distribution Server model](group__bt__mesh__dfd__srv.md)

Firmware Distribution Server instance.
[More...](#details)

`#include <[dfd_srv.h](dfd__srv_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const struct [bt\_mesh\_dfd\_srv\_cb](structbt__mesh__dfd__srv__cb.md) \* | [cb](#a7edbfa6bedb887a941b7567b9eeac8fd) |
| const struct [bt\_mesh\_model](structbt__mesh__model.md) \* | [mod](#a20bce6a528c1ef8433f55e8a4277a0ca) |
| struct [bt\_mesh\_dfu\_cli](structbt__mesh__dfu__cli.md) | [dfu](#a1d022e6e15350cd85999f0b07e34f519) |
| struct [bt\_mesh\_dfu\_target](structbt__mesh__dfu__target.md) | [targets](#abde92a8837d687ef213836d593bf979d) [0] |
| struct [bt\_mesh\_blob\_target\_pull](structbt__mesh__blob__target__pull.md) | [pull\_ctxs](#a1345da3143b1d3334a55ad8053967bf9) [0] |
| const struct [bt\_mesh\_blob\_io](structbt__mesh__blob__io.md) \* | [io](#a691eb383f51fd6e10b615ab8921005de) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [target\_cnt](#a67e4997a4367d9547a0ae9ff6c2017d6) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [slot\_idx](#af61665ebb2f46bd3e6277c6ee95ff68c) |
| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | [apply](#af1ac88ae8d9e1e42ff8a98d3969c359d) |
| enum [bt\_mesh\_dfd\_phase](group__bt__mesh__dfd.md#gab6562d62668ebcdb146be35b909c30c2) | [phase](#a4a7847580637713b305918c77210e3c0) |
| struct [bt\_mesh\_blob\_cli\_inputs](structbt__mesh__blob__cli__inputs.md) | [inputs](#a4e28f0e0845d1aeb6ebc03032ecfe813) |
| struct { |  |
| enum [bt\_mesh\_dfd\_upload\_phase](group__bt__mesh__dfd.md#ga1cce8331a0876c056b25175df32188fb)   [phase](#aa71e5affa0bf002499f3176794c6d9ca) |  |
| struct [bt\_mesh\_dfu\_slot](structbt__mesh__dfu__slot.md) \*   [slot](#a02b5ed65738bf08715bbc6a177c6f1ce) |  |
| const struct [flash\_area](structflash__area.md) \*   [area](#a52b10a938105d0fb22e72e30fc92df5c) |  |
| struct [bt\_mesh\_blob\_srv](structbt__mesh__blob__srv.md)   [blob](#ab538079d9f6b98f0de65583d6bdfe7f0) |  |
| } | [upload](#a26e4b13a8688f26c3330a2b0948bfc8d) |

## Detailed Description

Firmware Distribution Server instance.

## Field Documentation

## [◆ ](#af1ac88ae8d9e1e42ff8a98d3969c359d)apply

| [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) bt\_mesh\_dfd\_srv::apply |
| --- |

## [◆ ](#a52b10a938105d0fb22e72e30fc92df5c)area

| const struct [flash\_area](structflash__area.md)\* bt\_mesh\_dfd\_srv::area |
| --- |

## [◆ ](#ab538079d9f6b98f0de65583d6bdfe7f0)blob

| struct [bt\_mesh\_blob\_srv](structbt__mesh__blob__srv.md) bt\_mesh\_dfd\_srv::blob |
| --- |

## [◆ ](#a7edbfa6bedb887a941b7567b9eeac8fd)cb

| const struct [bt\_mesh\_dfd\_srv\_cb](structbt__mesh__dfd__srv__cb.md)\* bt\_mesh\_dfd\_srv::cb |
| --- |

## [◆ ](#a1d022e6e15350cd85999f0b07e34f519)dfu

| struct [bt\_mesh\_dfu\_cli](structbt__mesh__dfu__cli.md) bt\_mesh\_dfd\_srv::dfu |
| --- |

## [◆ ](#a4e28f0e0845d1aeb6ebc03032ecfe813)inputs

| struct [bt\_mesh\_blob\_cli\_inputs](structbt__mesh__blob__cli__inputs.md) bt\_mesh\_dfd\_srv::inputs |
| --- |

## [◆ ](#a691eb383f51fd6e10b615ab8921005de)io

| const struct [bt\_mesh\_blob\_io](structbt__mesh__blob__io.md)\* bt\_mesh\_dfd\_srv::io |
| --- |

## [◆ ](#a20bce6a528c1ef8433f55e8a4277a0ca)mod

| const struct [bt\_mesh\_model](structbt__mesh__model.md)\* bt\_mesh\_dfd\_srv::mod |
| --- |

## [◆ ](#aa71e5affa0bf002499f3176794c6d9ca)phase [1/2]

| enum [bt\_mesh\_dfd\_upload\_phase](group__bt__mesh__dfd.md#ga1cce8331a0876c056b25175df32188fb) bt\_mesh\_dfd\_srv::phase |
| --- |

## [◆ ](#a4a7847580637713b305918c77210e3c0)phase [2/2]

| enum [bt\_mesh\_dfd\_phase](group__bt__mesh__dfd.md#gab6562d62668ebcdb146be35b909c30c2) bt\_mesh\_dfd\_srv::phase |
| --- |

## [◆ ](#a1345da3143b1d3334a55ad8053967bf9)pull\_ctxs

| struct [bt\_mesh\_blob\_target\_pull](structbt__mesh__blob__target__pull.md) bt\_mesh\_dfd\_srv::pull\_ctxs[0] |
| --- |

## [◆ ](#a02b5ed65738bf08715bbc6a177c6f1ce)slot

| struct [bt\_mesh\_dfu\_slot](structbt__mesh__dfu__slot.md)\* bt\_mesh\_dfd\_srv::slot |
| --- |

## [◆ ](#af61665ebb2f46bd3e6277c6ee95ff68c)slot\_idx

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_mesh\_dfd\_srv::slot\_idx |
| --- |

## [◆ ](#a67e4997a4367d9547a0ae9ff6c2017d6)target\_cnt

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_mesh\_dfd\_srv::target\_cnt |
| --- |

## [◆ ](#abde92a8837d687ef213836d593bf979d)targets

| struct [bt\_mesh\_dfu\_target](structbt__mesh__dfu__target.md) bt\_mesh\_dfd\_srv::targets[0] |
| --- |

## [◆ ](#a26e4b13a8688f26c3330a2b0948bfc8d)[struct]

| struct { ... } bt\_mesh\_dfd\_srv::upload |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/mesh/[dfd\_srv.h](dfd__srv_8h_source.md)

- [bt\_mesh\_dfd\_srv](structbt__mesh__dfd__srv.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/sam0__eic_8h.html
original_path: doxygen/html/sam0__eic_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sam0\_eic.h File Reference

`#include <[zephyr/types.h](include_2zephyr_2types_8h_source.md)>`

[Go to the source code of this file.](sam0__eic_8h_source.md)

| Typedefs | |
| --- | --- |
| typedef void(\* | [sam0\_eic\_callback\_t](#a689981657e7012bca040dac40c5bf28f)) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pins, void \*data) |

| Enumerations | |
| --- | --- |
| enum | [sam0\_eic\_trigger](#a679adca86ca5da9a49b88bd3110f2f34) {     [SAM0\_EIC\_RISING](#a679adca86ca5da9a49b88bd3110f2f34a1c8d428daca3fb7b76bae9ecb5427511) , [SAM0\_EIC\_FALLING](#a679adca86ca5da9a49b88bd3110f2f34a7fb8fbeb7d3300080b1e54d656b990bc) , [SAM0\_EIC\_BOTH](#a679adca86ca5da9a49b88bd3110f2f34ad5a9871d1afcbd200a0b3e2e2b7e9871) , [SAM0\_EIC\_HIGH](#a679adca86ca5da9a49b88bd3110f2f34a61aac8fcb51758fd69b77c3b938d6486) ,     [SAM0\_EIC\_LOW](#a679adca86ca5da9a49b88bd3110f2f34a207804f632e291be19b237dde2fd15a9)   } |
|  | EIC trigger condition. [More...](#a679adca86ca5da9a49b88bd3110f2f34) |

| Functions | |
| --- | --- |
| int | [sam0\_eic\_acquire](#a6b6009bc8a688ac395ec579d52c25359) (int port, int pin, enum [sam0\_eic\_trigger](#a679adca86ca5da9a49b88bd3110f2f34) trigger, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) filter, [sam0\_eic\_callback\_t](#a689981657e7012bca040dac40c5bf28f) cb, void \*data) |
|  | Acquire an EIC interrupt for specific port and pin combination. |
| int | [sam0\_eic\_release](#aa6e652726d154e5cda1108aa31d60f26) (int port, int pin) |
|  | Release the EIC interrupt for a specific port and pin combination. |
| int | [sam0\_eic\_enable\_interrupt](#a7a65e580827b8e0d3f788cc1aaba7ea7) (int port, int pin) |
|  | Enable the EIC interrupt for a specific port and pin combination. |
| int | [sam0\_eic\_disable\_interrupt](#a5019df444a31531292fbf2fe5af160ef) (int port, int pin) |
|  | Disable the EIC interrupt for a specific port and pin combination. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [sam0\_eic\_interrupt\_pending](#a7dd3052cd7fb8074ad0b1233ecaa5708) (int port) |
|  | Test if there is an EIC interrupt pending for a port. |

## Typedef Documentation

## [◆ ](#a689981657e7012bca040dac40c5bf28f)sam0\_eic\_callback\_t

| typedef void(\* sam0\_eic\_callback\_t) ([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) pins, void \*data) |
| --- |

## Enumeration Type Documentation

## [◆ ](#a679adca86ca5da9a49b88bd3110f2f34)sam0\_eic\_trigger

| enum [sam0\_eic\_trigger](#a679adca86ca5da9a49b88bd3110f2f34) |
| --- |

EIC trigger condition.

| Enumerator | |
| --- | --- |
| SAM0\_EIC\_RISING |  |
| SAM0\_EIC\_FALLING |  |
| SAM0\_EIC\_BOTH |  |
| SAM0\_EIC\_HIGH |  |
| SAM0\_EIC\_LOW |  |

## Function Documentation

## [◆ ](#a6b6009bc8a688ac395ec579d52c25359)sam0\_eic\_acquire()

| int sam0\_eic\_acquire | ( | int | *port*, |
| --- | --- | --- | --- |
|  |  | int | *pin*, |
|  |  | enum [sam0\_eic\_trigger](#a679adca86ca5da9a49b88bd3110f2f34) | *trigger*, |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *filter*, |
|  |  | [sam0\_eic\_callback\_t](#a689981657e7012bca040dac40c5bf28f) | *cb*, |
|  |  | void \* | *data* ) |

Acquire an EIC interrupt for specific port and pin combination.

This acquires the EIC interrupt for a specific port and pin combination, or returns an error if the required line is not available. Only a single callback per port is supported and supplying a different one will change it for all lines on that port.

Parameters
:   | port | port index (A=0, etc) |
    | --- | --- |
    | pin | pin in the port |
    | trigger | trigger condition |
    | filter | enable filter |
    | cb | interrupt callback |
    | data | parameter to the interrupt callback |

## [◆ ](#a5019df444a31531292fbf2fe5af160ef)sam0\_eic\_disable\_interrupt()

| int sam0\_eic\_disable\_interrupt | ( | int | *port*, |
| --- | --- | --- | --- |
|  |  | int | *pin* ) |

Disable the EIC interrupt for a specific port and pin combination.

Parameters
:   | port | port index (A=0, etc) |
    | --- | --- |
    | pin | pin in the port |

## [◆ ](#a7a65e580827b8e0d3f788cc1aaba7ea7)sam0\_eic\_enable\_interrupt()

| int sam0\_eic\_enable\_interrupt | ( | int | *port*, |
| --- | --- | --- | --- |
|  |  | int | *pin* ) |

Enable the EIC interrupt for a specific port and pin combination.

Parameters
:   | port | port index (A=0, etc) |
    | --- | --- |
    | pin | pin in the port |

## [◆ ](#a7dd3052cd7fb8074ad0b1233ecaa5708)sam0\_eic\_interrupt\_pending()

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) sam0\_eic\_interrupt\_pending | ( | int | *port* | ) |  |
| --- | --- | --- | --- | --- | --- |

Test if there is an EIC interrupt pending for a port.

Parameters
:   | port | port index (A=0, etc) |
    | --- | --- |

## [◆ ](#aa6e652726d154e5cda1108aa31d60f26)sam0\_eic\_release()

| int sam0\_eic\_release | ( | int | *port*, |
| --- | --- | --- | --- |
|  |  | int | *pin* ) |

Release the EIC interrupt for a specific port and pin combination.

Release the EIC configuration for a specific port and pin combination. No effect if that combination does not currently hold the associated EIC line.

Parameters
:   | port | port index (A=0, etc) |
    | --- | --- |
    | pin | pin in the port |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [interrupt\_controller](dir_d4c0bd929525fabbb463a01ac157fd6b.md)
- [sam0\_eic.h](sam0__eic_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

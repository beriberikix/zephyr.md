---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structec__host__cmd__handler.html
original_path: doxygen/html/structec__host__cmd__handler.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ec\_host\_cmd\_handler Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [EC Host Command Interface](group__ec__host__cmd__interface.md)

Structure use for statically registering host command handlers.
[More...](#details)

`#include <[ec_host_cmd.h](ec__host__cmd_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [ec\_host\_cmd\_handler\_cb](group__ec__host__cmd__interface.md#ga027ae23ea11a0ec7711725d1b28125d7) | [handler](#aa87d559e625871f78023fcc015a02c82) |
|  | Callback routine to process commands that match *id*. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [id](#ad0aea63728aa9254e2a14d8cf0352b87) |
|  | The numerical command id used as the lookup for commands. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [version\_mask](#a2e4643dc7ca0ee4b8f7169b9156dadc6) |
|  | The bitfield of all versions that the *handler* supports, where each bit value represents that the *handler* supports that version. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [min\_rqt\_size](#aef233f030a30032e9dcde620c1953394) |
|  | The minimum *input\_buf\_size* enforced by the framework before passing to the handler. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [min\_rsp\_size](#a4777b0c23ddf568c36ca995886cf3248) |
|  | The minimum *output\_buf\_size* enforced by the framework before passing to the handler. |

## Detailed Description

Structure use for statically registering host command handlers.

## Field Documentation

## [◆ ](#aa87d559e625871f78023fcc015a02c82)handler

| [ec\_host\_cmd\_handler\_cb](group__ec__host__cmd__interface.md#ga027ae23ea11a0ec7711725d1b28125d7) ec\_host\_cmd\_handler::handler |
| --- |

Callback routine to process commands that match *id*.

## [◆ ](#ad0aea63728aa9254e2a14d8cf0352b87)id

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) ec\_host\_cmd\_handler::id |
| --- |

The numerical command id used as the lookup for commands.

## [◆ ](#aef233f030a30032e9dcde620c1953394)min\_rqt\_size

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) ec\_host\_cmd\_handler::min\_rqt\_size |
| --- |

The minimum *input\_buf\_size* enforced by the framework before passing to the handler.

## [◆ ](#a4777b0c23ddf568c36ca995886cf3248)min\_rsp\_size

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) ec\_host\_cmd\_handler::min\_rsp\_size |
| --- |

The minimum *output\_buf\_size* enforced by the framework before passing to the handler.

## [◆ ](#a2e4643dc7ca0ee4b8f7169b9156dadc6)version\_mask

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) ec\_host\_cmd\_handler::version\_mask |
| --- |

The bitfield of all versions that the *handler* supports, where each bit value represents that the *handler* supports that version.

E.g. [BIT(0)](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c "Unsigned integer with bit position n set (signed in assembly language).") corresponds to version 0.

---

The documentation for this struct was generated from the following file:

- zephyr/mgmt/ec\_host\_cmd/[ec\_host\_cmd.h](ec__host__cmd_8h_source.md)

- [ec\_host\_cmd\_handler](structec__host__cmd__handler.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

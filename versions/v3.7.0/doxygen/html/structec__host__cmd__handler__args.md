---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structec__host__cmd__handler__args.html
original_path: doxygen/html/structec__host__cmd__handler__args.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ec\_host\_cmd\_handler\_args Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [EC Host Command Interface](group__ec__host__cmd__interface.md)

Arguments passed into every installed host command handler.
[More...](#details)

`#include <[ec_host_cmd.h](ec__host__cmd_8h_source.md)>`

| Data Fields | |
| --- | --- |
| void \* | [reserved](#a8c7fcd1d310b0622f45458388462c9ef) |
|  | Reserved for compatibility. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [command](#a059b20824ece1ada2d53c7e73f49972d) |
|  | Command identifier. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [version](#ad346a4c196ee5e48c67640232a828745) |
|  | The version of the host command that is being requested. |
| const void \* | [input\_buf](#a364bda288790f65205f26310148d2888) |
|  | The incoming data that can be cast to the handlers request type. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [input\_buf\_size](#a7d6d622f7dd9e3b8faf928befa72f36a) |
|  | The number of valid bytes that can be read from *input\_buf*. |
| void \* | [output\_buf](#a1ac9d891b168b4db55a1829d72362ca5) |
|  | The data written to this buffer will be send to the host. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [output\_buf\_max](#ab3eaef25fd80d0ac38b8d2eb9e40ebd4) |
|  | Maximum number of bytes that can be written to the *output\_buf*. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [output\_buf\_size](#a1a6f9a7ba7faf810f7095b4c053dd3b2) |
|  | Number of bytes of *output\_buf* to send to the host. |

## Detailed Description

Arguments passed into every installed host command handler.

## Field Documentation

## [◆ ](#a059b20824ece1ada2d53c7e73f49972d)command

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) ec\_host\_cmd\_handler\_args::command |
| --- |

Command identifier.

## [◆ ](#a364bda288790f65205f26310148d2888)input\_buf

| const void\* ec\_host\_cmd\_handler\_args::input\_buf |
| --- |

The incoming data that can be cast to the handlers request type.

## [◆ ](#a7d6d622f7dd9e3b8faf928befa72f36a)input\_buf\_size

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) ec\_host\_cmd\_handler\_args::input\_buf\_size |
| --- |

The number of valid bytes that can be read from *input\_buf*.

## [◆ ](#a1ac9d891b168b4db55a1829d72362ca5)output\_buf

| void\* ec\_host\_cmd\_handler\_args::output\_buf |
| --- |

The data written to this buffer will be send to the host.

## [◆ ](#ab3eaef25fd80d0ac38b8d2eb9e40ebd4)output\_buf\_max

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) ec\_host\_cmd\_handler\_args::output\_buf\_max |
| --- |

Maximum number of bytes that can be written to the *output\_buf*.

## [◆ ](#a1a6f9a7ba7faf810f7095b4c053dd3b2)output\_buf\_size

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) ec\_host\_cmd\_handler\_args::output\_buf\_size |
| --- |

Number of bytes of *output\_buf* to send to the host.

## [◆ ](#a8c7fcd1d310b0622f45458388462c9ef)reserved

| void\* ec\_host\_cmd\_handler\_args::reserved |
| --- |

Reserved for compatibility.

## [◆ ](#ad346a4c196ee5e48c67640232a828745)version

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) ec\_host\_cmd\_handler\_args::version |
| --- |

The version of the host command that is being requested.

This will be a value that has been static registered as valid for the handler.

---

The documentation for this struct was generated from the following file:

- zephyr/mgmt/ec\_host\_cmd/[ec\_host\_cmd.h](ec__host__cmd_8h_source.md)

- [ec\_host\_cmd\_handler\_args](structec__host__cmd__handler__args.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

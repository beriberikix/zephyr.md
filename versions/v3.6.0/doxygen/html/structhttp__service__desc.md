---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structhttp__service__desc.html
original_path: doxygen/html/structhttp__service__desc.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

http\_service\_desc Struct Reference

`#include <[service.h](service_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const char \* | [host](#a421961e470a5ca82d9d4aa1f2a8d71a5) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \* | [port](#a30df63e2966f863762fe26b771206ff7) |
| void \* | [detail](#a94935033fe14aff5afb65dffffd42f94) |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [concurrent](#ab668b2e198c1202a9de44144b3c0de0b) |
| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) | [backlog](#af151d08745b99510d7c3edb64440523d) |
| struct [http\_resource\_desc](structhttp__resource__desc.md) \* | [res\_begin](#a3db5d3cbb7f9014301870263849ca84c) |
| struct [http\_resource\_desc](structhttp__resource__desc.md) \* | [res\_end](#a4c0b014ca8c46fe770b24c7af43d74f6) |

## Field Documentation

## [◆ ](#af151d08745b99510d7c3edb64440523d)backlog

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) http\_service\_desc::backlog |
| --- |

## [◆ ](#ab668b2e198c1202a9de44144b3c0de0b)concurrent

| [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) http\_service\_desc::concurrent |
| --- |

## [◆ ](#a94935033fe14aff5afb65dffffd42f94)detail

| void\* http\_service\_desc::detail |
| --- |

## [◆ ](#a421961e470a5ca82d9d4aa1f2a8d71a5)host

| const char\* http\_service\_desc::host |
| --- |

## [◆ ](#a30df63e2966f863762fe26b771206ff7)port

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)\* http\_service\_desc::port |
| --- |

## [◆ ](#a3db5d3cbb7f9014301870263849ca84c)res\_begin

| struct [http\_resource\_desc](structhttp__resource__desc.md)\* http\_service\_desc::res\_begin |
| --- |

## [◆ ](#a4c0b014ca8c46fe770b24c7af43d74f6)res\_end

| struct [http\_resource\_desc](structhttp__resource__desc.md)\* http\_service\_desc::res\_end |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/net/http/[service.h](service_8h_source.md)

- [http\_service\_desc](structhttp__service__desc.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

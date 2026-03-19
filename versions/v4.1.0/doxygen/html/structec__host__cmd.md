---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structec__host__cmd.html
original_path: doxygen/html/structec__host__cmd.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ec\_host\_cmd Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [EC Host Command Interface](group__ec__host__cmd__interface.md)

`#include <[ec_host_cmd.h](ec__host__cmd_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [ec\_host\_cmd\_rx\_ctx](structec__host__cmd__rx__ctx.md) | [rx\_ctx](#a1f5153ec8442ae8c70d4918ff21b908e) |
| struct [ec\_host\_cmd\_tx\_buf](structec__host__cmd__tx__buf.md) | [tx](#af1a3f483c1a7ddb88db187e406caa08d) |
| struct [ec\_host\_cmd\_backend](structec__host__cmd__backend.md) \* | [backend](#ad269f3223fc0885ba5c847b4443c993c) |
| struct k\_sem | [rx\_ready](#a465d588b50f0a881e7f1d8b761c4288f) |
|  | The backend gives rx\_ready (by calling the ec\_host\_cmd\_send\_receive function), when data in rx\_ctx are ready. |
| enum [ec\_host\_cmd\_status](group__ec__host__cmd__interface.md#ga9b0b87983dcc92ea55ebfa1aecf82a8f) | [rx\_status](#a0e50770725cd93b0923769b3b650b04d) |
|  | Status of the rx data checked in the ec\_host\_cmd\_send\_received function. |
| [ec\_host\_cmd\_user\_cb\_t](group__ec__host__cmd__interface.md#gaa6ea251ee113cc15fd085ef12b76a573) | [user\_cb](#ad2f10eda2e6c2743d9c3068bda4deb7c) |
|  | User callback after receiving a command. |
| void \* | [user\_data](#a7982f079e67180de58ebd0a6f0f5d7e0) |
| enum [ec\_host\_cmd\_state](group__ec__host__cmd__interface.md#gabf0f1243bf55cb70078f2a9fd0a755ec) | [state](#a444f295157c5ada6162aea803ff219e1) |

## Field Documentation

## [◆ ](#ad269f3223fc0885ba5c847b4443c993c)backend

| struct [ec\_host\_cmd\_backend](structec__host__cmd__backend.md)\* ec\_host\_cmd::backend |
| --- |

## [◆ ](#a1f5153ec8442ae8c70d4918ff21b908e)rx\_ctx

| struct [ec\_host\_cmd\_rx\_ctx](structec__host__cmd__rx__ctx.md) ec\_host\_cmd::rx\_ctx |
| --- |

## [◆ ](#a465d588b50f0a881e7f1d8b761c4288f)rx\_ready

| struct k\_sem ec\_host\_cmd::rx\_ready |
| --- |

The backend gives rx\_ready (by calling the ec\_host\_cmd\_send\_receive function), when data in rx\_ctx are ready.

The handler takes rx\_ready to read data in rx\_ctx.

## [◆ ](#a0e50770725cd93b0923769b3b650b04d)rx\_status

| enum [ec\_host\_cmd\_status](group__ec__host__cmd__interface.md#ga9b0b87983dcc92ea55ebfa1aecf82a8f) ec\_host\_cmd::rx\_status |
| --- |

Status of the rx data checked in the ec\_host\_cmd\_send\_received function.

## [◆ ](#a444f295157c5ada6162aea803ff219e1)state

| enum [ec\_host\_cmd\_state](group__ec__host__cmd__interface.md#gabf0f1243bf55cb70078f2a9fd0a755ec) ec\_host\_cmd::state |
| --- |

## [◆ ](#af1a3f483c1a7ddb88db187e406caa08d)tx

| struct [ec\_host\_cmd\_tx\_buf](structec__host__cmd__tx__buf.md) ec\_host\_cmd::tx |
| --- |

## [◆ ](#ad2f10eda2e6c2743d9c3068bda4deb7c)user\_cb

| [ec\_host\_cmd\_user\_cb\_t](group__ec__host__cmd__interface.md#gaa6ea251ee113cc15fd085ef12b76a573) ec\_host\_cmd::user\_cb |
| --- |

User callback after receiving a command.

It is called by the ec\_host\_cmd\_send\_received function.

## [◆ ](#a7982f079e67180de58ebd0a6f0f5d7e0)user\_data

| void\* ec\_host\_cmd::user\_data |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/mgmt/ec\_host\_cmd/[ec\_host\_cmd.h](ec__host__cmd_8h_source.md)

- [ec\_host\_cmd](structec__host__cmd.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

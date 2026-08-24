---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/structtisci__msg__rm__udmap__rx__ch__cfg.html
original_path: doxygen/html/structtisci__msg__rm__udmap__rx__ch__cfg.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

tisci\_msg\_rm\_udmap\_rx\_ch\_cfg Struct Reference

Configures a Navigator Subsystem UDMAP receive channel.
[More...](#details)

`#include <[zephyr/drivers/firmware/tisci/tisci.h](tisci_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [valid\_params](#a88fa4f4bf94a290a035419a65054b544) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [nav\_id](#a691a478fa65af24279638789433dca6f) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [index](#a459ca9cb93410be5747595a57d88c7ed) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [rx\_fetch\_size](#ad57a6d0dca932c95cff2a4675dc72990) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [rxcq\_qnum](#a554db2ab8742b2f15a6c7531638a6d74) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [rx\_priority](#a03ec736938d7b3eb05fcd56c62fd736a) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [rx\_qos](#a54f4136011d83df5441004dde0d5e696) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [rx\_orderid](#a9782a0a412413087ecf669beed77ff77) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [rx\_sched\_priority](#a4e9720567203889d41fdccb769d56025) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [flowid\_start](#abde08f01f02f26e1538cd82d9e87b19a) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [flowid\_cnt](#ac10643f49f4d685af2bf14bb7b9b90f0) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [rx\_pause\_on\_err](#ad008f77af3d4edbfeedb863ee2f8dcd0) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [rx\_atype](#a7a36a9e37b22229c6ec90528aa7f9a9c) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [rx\_chan\_type](#aecf4e3eaaa8b8c604504eb525d3e1a5f) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [rx\_ignore\_short](#ab1245dc9783e74cd3cb1fcb648714e76) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [rx\_ignore\_long](#a8e9b939089204b70469afedcb6c5ad8c) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [rx\_burst\_size](#a57c0675af1fdefd1c270d11183fa77d6) |

## Detailed Description

Configures a Navigator Subsystem UDMAP receive channel.

Configures a Navigator Subsystem UDMAP receive channel registers. See tisci\_msg\_rm\_udmap\_rx\_ch\_cfg\_req

## Field Documentation

## [◆ ](#ac10643f49f4d685af2bf14bb7b9b90f0)flowid\_cnt

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tisci\_msg\_rm\_udmap\_rx\_ch\_cfg::flowid\_cnt |
| --- |

## [◆ ](#abde08f01f02f26e1538cd82d9e87b19a)flowid\_start

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tisci\_msg\_rm\_udmap\_rx\_ch\_cfg::flowid\_start |
| --- |

## [◆ ](#a459ca9cb93410be5747595a57d88c7ed)index

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tisci\_msg\_rm\_udmap\_rx\_ch\_cfg::index |
| --- |

## [◆ ](#a691a478fa65af24279638789433dca6f)nav\_id

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tisci\_msg\_rm\_udmap\_rx\_ch\_cfg::nav\_id |
| --- |

## [◆ ](#a7a36a9e37b22229c6ec90528aa7f9a9c)rx\_atype

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) tisci\_msg\_rm\_udmap\_rx\_ch\_cfg::rx\_atype |
| --- |

## [◆ ](#a57c0675af1fdefd1c270d11183fa77d6)rx\_burst\_size

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) tisci\_msg\_rm\_udmap\_rx\_ch\_cfg::rx\_burst\_size |
| --- |

## [◆ ](#aecf4e3eaaa8b8c604504eb525d3e1a5f)rx\_chan\_type

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) tisci\_msg\_rm\_udmap\_rx\_ch\_cfg::rx\_chan\_type |
| --- |

## [◆ ](#ad57a6d0dca932c95cff2a4675dc72990)rx\_fetch\_size

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tisci\_msg\_rm\_udmap\_rx\_ch\_cfg::rx\_fetch\_size |
| --- |

## [◆ ](#a8e9b939089204b70469afedcb6c5ad8c)rx\_ignore\_long

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) tisci\_msg\_rm\_udmap\_rx\_ch\_cfg::rx\_ignore\_long |
| --- |

## [◆ ](#ab1245dc9783e74cd3cb1fcb648714e76)rx\_ignore\_short

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) tisci\_msg\_rm\_udmap\_rx\_ch\_cfg::rx\_ignore\_short |
| --- |

## [◆ ](#a9782a0a412413087ecf669beed77ff77)rx\_orderid

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) tisci\_msg\_rm\_udmap\_rx\_ch\_cfg::rx\_orderid |
| --- |

## [◆ ](#ad008f77af3d4edbfeedb863ee2f8dcd0)rx\_pause\_on\_err

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) tisci\_msg\_rm\_udmap\_rx\_ch\_cfg::rx\_pause\_on\_err |
| --- |

## [◆ ](#a03ec736938d7b3eb05fcd56c62fd736a)rx\_priority

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) tisci\_msg\_rm\_udmap\_rx\_ch\_cfg::rx\_priority |
| --- |

## [◆ ](#a54f4136011d83df5441004dde0d5e696)rx\_qos

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) tisci\_msg\_rm\_udmap\_rx\_ch\_cfg::rx\_qos |
| --- |

## [◆ ](#a4e9720567203889d41fdccb769d56025)rx\_sched\_priority

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) tisci\_msg\_rm\_udmap\_rx\_ch\_cfg::rx\_sched\_priority |
| --- |

## [◆ ](#a554db2ab8742b2f15a6c7531638a6d74)rxcq\_qnum

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tisci\_msg\_rm\_udmap\_rx\_ch\_cfg::rxcq\_qnum |
| --- |

## [◆ ](#a88fa4f4bf94a290a035419a65054b544)valid\_params

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) tisci\_msg\_rm\_udmap\_rx\_ch\_cfg::valid\_params |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/firmware/tisci/[tisci.h](tisci_8h_source.md)

- [tisci\_msg\_rm\_udmap\_rx\_ch\_cfg](structtisci__msg__rm__udmap__rx__ch__cfg.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structdns__resolve__context_1_1dns__pending__query.html
original_path: doxygen/html/structdns__resolve__context_1_1dns__pending__query.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

dns\_resolve\_context::dns\_pending\_query Struct Reference

Result callbacks.
[More...](#details)

`#include <[dns_resolve.h](dns__resolve_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [k\_work\_delayable](structk__work__delayable.md) | [timer](#a6f76b200b8c421399987be83b72b9230) |
|  | Timeout timer. |
| struct [dns\_resolve\_context](structdns__resolve__context.md) \* | [ctx](#a4260371a741b3c2e752848955eee5cae) |
|  | Back pointer to ctx, needed in timeout handler. |
| [dns\_resolve\_cb\_t](group__dns__resolve.md#gafe22d0ef90c581982561ef0c33d1f722) | [cb](#aacf4003ce035658038ae44773091f2d0) |
|  | Result callback. |
| void \* | [user\_data](#a6a1c93f3eab8f9aa55dbb26e704bb343) |
|  | User data. |
| [k\_timeout\_t](structk__timeout__t.md) | [timeout](#aa2b1f1db21ab4a05240ebb62512c24d5) |
|  | TX timeout. |
| const char \* | [query](#a106464bda8d56283b06251c37964906b) |
|  | String containing the thing to resolve like www.example.com. |
| enum [dns\_query\_type](group__dns__resolve.md#ga7169c5a920fb1b0d77910a6ab922e3f0) | [query\_type](#af5796eb469e2fe3bcebea2ad55a8fd78) |
|  | Query type. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [id](#a773e2ad2bedb2d1030df3590e9a14173) |
|  | DNS id of this query. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [query\_hash](#a168fea99e8c6760cab49611ceb5a6fc1) |
|  | Hash of the DNS name + query type we are querying. |

## Detailed Description

Result callbacks.

We have multiple callbacks here so that it is possible to do multiple queries at the same time.

Contents of this structure can be inspected and changed only when the lock is held.

## Field Documentation

## [◆ ](#aacf4003ce035658038ae44773091f2d0)cb

| [dns\_resolve\_cb\_t](group__dns__resolve.md#gafe22d0ef90c581982561ef0c33d1f722) dns\_resolve\_context::dns\_pending\_query::cb |
| --- |

Result callback.

A null value indicates the slot is not in use.

## [◆ ](#a4260371a741b3c2e752848955eee5cae)ctx

| struct [dns\_resolve\_context](structdns__resolve__context.md)\* dns\_resolve\_context::dns\_pending\_query::ctx |
| --- |

Back pointer to ctx, needed in timeout handler.

## [◆ ](#a773e2ad2bedb2d1030df3590e9a14173)id

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) dns\_resolve\_context::dns\_pending\_query::id |
| --- |

DNS id of this query.

## [◆ ](#a106464bda8d56283b06251c37964906b)query

| const char\* dns\_resolve\_context::dns\_pending\_query::query |
| --- |

String containing the thing to resolve like www.example.com.

This is set to a non-null value when the query is started, and is not used thereafter.

If the query completed at a point where the work item was still pending the pointer is cleared to indicate that the query is complete, but release of the query slot will be deferred until a request for a slot determines that the work item has been released.

## [◆ ](#a168fea99e8c6760cab49611ceb5a6fc1)query\_hash

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) dns\_resolve\_context::dns\_pending\_query::query\_hash |
| --- |

Hash of the DNS name + query type we are querying.

This hash is calculated so we can match the response that we are receiving. This is needed mainly for mDNS which is setting the DNS id to 0, which means that the id alone cannot be used to find correct pending query.

## [◆ ](#af5796eb469e2fe3bcebea2ad55a8fd78)query\_type

| enum [dns\_query\_type](group__dns__resolve.md#ga7169c5a920fb1b0d77910a6ab922e3f0) dns\_resolve\_context::dns\_pending\_query::query\_type |
| --- |

Query type.

## [◆ ](#aa2b1f1db21ab4a05240ebb62512c24d5)timeout

| [k\_timeout\_t](structk__timeout__t.md) dns\_resolve\_context::dns\_pending\_query::timeout |
| --- |

TX timeout.

## [◆ ](#a6f76b200b8c421399987be83b72b9230)timer

| struct [k\_work\_delayable](structk__work__delayable.md) dns\_resolve\_context::dns\_pending\_query::timer |
| --- |

Timeout timer.

## [◆ ](#a6a1c93f3eab8f9aa55dbb26e704bb343)user\_data

| void\* dns\_resolve\_context::dns\_pending\_query::user\_data |
| --- |

User data.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[dns\_resolve.h](dns__resolve_8h_source.md)

- [dns\_resolve\_context](structdns__resolve__context.md)
- [dns\_pending\_query](structdns__resolve__context_1_1dns__pending__query.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

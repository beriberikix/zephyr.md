---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/structtisci__msg__rm__udmap__tx__ch__cfg.html
original_path: doxygen/html/structtisci__msg__rm__udmap__tx__ch__cfg.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

tisci\_msg\_rm\_udmap\_tx\_ch\_cfg Struct Reference

Configures a Navigator Subsystem UDMAP transmit channel.
[More...](#details)

`#include <[zephyr/drivers/firmware/tisci/tisci.h](tisci_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [valid\_params](#acb243dd0b94ab38fa50ddd14a758b33a) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [nav\_id](#a646845b965fee520329a118ade711f02) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [index](#ab8327c9b3896c8294f47349572546e70) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [tx\_pause\_on\_err](#ad255f2c020bfc237f5f22a747e68c1b8) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [tx\_filt\_einfo](#a9d298e2ae456dcad3cbfdce595f0655c) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [tx\_filt\_pswords](#ab9a869848d253d09f9fafc91dc8958cc) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [tx\_atype](#a75147fe8091db6c41050ded22c9eefa3) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [tx\_chan\_type](#a14b9ea920df0ff044bd9cf45c2084f3a) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [tx\_supr\_tdpkt](#aaa18a6837a0271781164a353ce729623) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [tx\_fetch\_size](#afd02dd108fd620f1bc9d66fac5a3e775) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [tx\_credit\_count](#a90a701c601691c79cd37192fac02d052) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [txcq\_qnum](#a89f3ac8683240274b5bbc635e08b659f) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [tx\_priority](#aeaf51ae045dbc4079c02d61f13e487ed) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [tx\_qos](#af377d65e1fb43ed7fceda8a0665605d0) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [tx\_orderid](#ada34a3a63d1ed339a86804f906d4dbc5) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [fdepth](#ad8aec84ccd12e9f02c4cafac7eadb4a4) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [tx\_sched\_priority](#a01334fae8a1e94ffbbba28d9c59ed0b1) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [tx\_burst\_size](#a7e0bfdb950b1b285ddc0e58282bc224b) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [tx\_tdtype](#ab36b40f8989fa7cdc5419bc0e9dd5a68) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [extended\_ch\_type](#a37b6f2565ccdf51fcc09801a72fde7e4) |

## Detailed Description

Configures a Navigator Subsystem UDMAP transmit channel.

Configures a Navigator Subsystem UDMAP transmit channel registers. See tisci\_msg\_rm\_udmap\_tx\_ch\_cfg\_req

## Field Documentation

## [◆ ](#a37b6f2565ccdf51fcc09801a72fde7e4)extended\_ch\_type

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) tisci\_msg\_rm\_udmap\_tx\_ch\_cfg::extended\_ch\_type |
| --- |

## [◆ ](#ad8aec84ccd12e9f02c4cafac7eadb4a4)fdepth

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tisci\_msg\_rm\_udmap\_tx\_ch\_cfg::fdepth |
| --- |

## [◆ ](#ab8327c9b3896c8294f47349572546e70)index

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tisci\_msg\_rm\_udmap\_tx\_ch\_cfg::index |
| --- |

## [◆ ](#a646845b965fee520329a118ade711f02)nav\_id

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tisci\_msg\_rm\_udmap\_tx\_ch\_cfg::nav\_id |
| --- |

## [◆ ](#a75147fe8091db6c41050ded22c9eefa3)tx\_atype

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) tisci\_msg\_rm\_udmap\_tx\_ch\_cfg::tx\_atype |
| --- |

## [◆ ](#a7e0bfdb950b1b285ddc0e58282bc224b)tx\_burst\_size

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) tisci\_msg\_rm\_udmap\_tx\_ch\_cfg::tx\_burst\_size |
| --- |

## [◆ ](#a14b9ea920df0ff044bd9cf45c2084f3a)tx\_chan\_type

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) tisci\_msg\_rm\_udmap\_tx\_ch\_cfg::tx\_chan\_type |
| --- |

## [◆ ](#a90a701c601691c79cd37192fac02d052)tx\_credit\_count

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) tisci\_msg\_rm\_udmap\_tx\_ch\_cfg::tx\_credit\_count |
| --- |

## [◆ ](#afd02dd108fd620f1bc9d66fac5a3e775)tx\_fetch\_size

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tisci\_msg\_rm\_udmap\_tx\_ch\_cfg::tx\_fetch\_size |
| --- |

## [◆ ](#a9d298e2ae456dcad3cbfdce595f0655c)tx\_filt\_einfo

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) tisci\_msg\_rm\_udmap\_tx\_ch\_cfg::tx\_filt\_einfo |
| --- |

## [◆ ](#ab9a869848d253d09f9fafc91dc8958cc)tx\_filt\_pswords

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) tisci\_msg\_rm\_udmap\_tx\_ch\_cfg::tx\_filt\_pswords |
| --- |

## [◆ ](#ada34a3a63d1ed339a86804f906d4dbc5)tx\_orderid

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) tisci\_msg\_rm\_udmap\_tx\_ch\_cfg::tx\_orderid |
| --- |

## [◆ ](#ad255f2c020bfc237f5f22a747e68c1b8)tx\_pause\_on\_err

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) tisci\_msg\_rm\_udmap\_tx\_ch\_cfg::tx\_pause\_on\_err |
| --- |

## [◆ ](#aeaf51ae045dbc4079c02d61f13e487ed)tx\_priority

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) tisci\_msg\_rm\_udmap\_tx\_ch\_cfg::tx\_priority |
| --- |

## [◆ ](#af377d65e1fb43ed7fceda8a0665605d0)tx\_qos

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) tisci\_msg\_rm\_udmap\_tx\_ch\_cfg::tx\_qos |
| --- |

## [◆ ](#a01334fae8a1e94ffbbba28d9c59ed0b1)tx\_sched\_priority

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) tisci\_msg\_rm\_udmap\_tx\_ch\_cfg::tx\_sched\_priority |
| --- |

## [◆ ](#aaa18a6837a0271781164a353ce729623)tx\_supr\_tdpkt

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) tisci\_msg\_rm\_udmap\_tx\_ch\_cfg::tx\_supr\_tdpkt |
| --- |

## [◆ ](#ab36b40f8989fa7cdc5419bc0e9dd5a68)tx\_tdtype

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) tisci\_msg\_rm\_udmap\_tx\_ch\_cfg::tx\_tdtype |
| --- |

## [◆ ](#a89f3ac8683240274b5bbc635e08b659f)txcq\_qnum

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tisci\_msg\_rm\_udmap\_tx\_ch\_cfg::txcq\_qnum |
| --- |

## [◆ ](#acb243dd0b94ab38fa50ddd14a758b33a)valid\_params

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) tisci\_msg\_rm\_udmap\_tx\_ch\_cfg::valid\_params |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/firmware/tisci/[tisci.h](tisci_8h_source.md)

- [tisci\_msg\_rm\_udmap\_tx\_ch\_cfg](structtisci__msg__rm__udmap__tx__ch__cfg.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

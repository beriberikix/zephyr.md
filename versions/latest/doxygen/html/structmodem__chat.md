---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structmodem__chat.html
original_path: doxygen/html/structmodem__chat.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

modem\_chat Struct Reference

Chat instance internal context.
[More...](#details)

`#include <[chat.h](chat_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct modem\_pipe \* | [pipe](#a9bec3daf58728d27a554d228452a8fa9) |
| void \* | [user\_data](#a26d717e335b4b1ade0972458c11f42da) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [receive\_buf](#af2ac2cf3efac415af72b702a1ec62ae7) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [receive\_buf\_size](#a962b245335979eeb782410ba6429b4e6) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [receive\_buf\_len](#ae15c5238e6e04a4f94a27e779d3f2a30) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [work\_buf](#a5b3667c1e409fdc5382af75ad1329df9) [32] |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [work\_buf\_len](#a9acd26d97eec7c48482063a3c558c717) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [delimiter](#aa8d3d31dc6eaf676c03fad034597ad91) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [delimiter\_size](#a14104456f6e4b8c36b38eb232fb36996) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [delimiter\_match\_len](#ae5fe73d09b6fad3302e84ca841ad65ca) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \* | [filter](#adcb6a8d9fdb9b7c0e950d64ec4b0853c) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [filter\_size](#a199b2c9e9c6fd41e81ef6bca138b6328) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*\* | [argv](#ae7a2d23e34f95d3c3c5d5df15af1571a) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [argv\_size](#ac1c71497eb22137bc4a03877b6f30b37) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [argc](#ad08436ccb8308912a6d45b3b11cc0c59) |
| const struct [modem\_chat\_match](structmodem__chat__match.md) \* | [matches](#ac16520e4e7031bbc2162d29728eb86d2) [3] |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [matches\_size](#a249bc37382bddf11bfcabef834a19f2a) [3] |
| const struct [modem\_chat\_script](structmodem__chat__script.md) \* | [script](#a7c181f6c68809379d756080729e1e3a1) |
| const struct [modem\_chat\_script](structmodem__chat__script.md) \* | [pending\_script](#abff96c9a7bd215f20fece3d6f96899b5) |
| struct [k\_work](structk__work.md) | [script\_run\_work](#a44f303f7ec2aa304de5ba0e1249bff35) |
| struct [k\_work\_delayable](structk__work__delayable.md) | [script\_timeout\_work](#ada952e3176a7f2645ff7b64ca32cb29e) |
| struct [k\_work](structk__work.md) | [script\_abort\_work](#ae8df85a6e2c27f720e8f7f993e7d6a75) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [script\_chat\_it](#aa09d879afc7f69901799d564c3951c7b) |
| [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) | [script\_state](#af55e1bf861e72b497230c92b4a673f4c) |
| enum [modem\_chat\_script\_result](chat_8h.md#a4035be227ddec8424311575305647d3e) | [script\_result](#a8560fa2c2d26366ed27d8ca4620f30ff) |
| struct k\_sem | [script\_stopped\_sem](#aa365a6e40ec8de9e2a74c035dff0c203) |
| enum [modem\_chat\_script\_send\_state](chat_8h.md#a734cb1bcbbbf5c87551b20038e0608ae) | [script\_send\_state](#a9fc3fc3f5d2285d12ecad12e21e5be13) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [script\_send\_pos](#a36fb50970ebd8eb041506c913648be6c) |
| struct [k\_work](structk__work.md) | [script\_send\_work](#a5260f843646e401159fd5f13015e9db6) |
| struct [k\_work\_delayable](structk__work__delayable.md) | [script\_send\_timeout\_work](#a37ae5aeeaaeba6e50d7d9f0df6ff2870) |
| const struct [modem\_chat\_match](structmodem__chat__match.md) \* | [parse\_match](#a42d6fe9641db254459498d26b05ce152) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [parse\_match\_len](#ae14032ba980271ea758278d4bd8cca30) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [parse\_arg\_len](#a2e2555e463d6dffb5ed6531ad8a822ca) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [parse\_match\_type](#ae4063127d0a802801660f08a1f403121) |
| struct [k\_work](structk__work.md) | [receive\_work](#a4558d8dc063f0330bdb4d203e2af6907) |

## Detailed Description

Chat instance internal context.

Warning
:   Do not modify any members of this struct directly

## Field Documentation

## [◆ ](#ad08436ccb8308912a6d45b3b11cc0c59)argc

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) modem\_chat::argc |
| --- |

## [◆ ](#ae7a2d23e34f95d3c3c5d5df15af1571a)argv

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\*\* modem\_chat::argv |
| --- |

## [◆ ](#ac1c71497eb22137bc4a03877b6f30b37)argv\_size

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) modem\_chat::argv\_size |
| --- |

## [◆ ](#aa8d3d31dc6eaf676c03fad034597ad91)delimiter

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* modem\_chat::delimiter |
| --- |

## [◆ ](#ae5fe73d09b6fad3302e84ca841ad65ca)delimiter\_match\_len

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) modem\_chat::delimiter\_match\_len |
| --- |

## [◆ ](#a14104456f6e4b8c36b38eb232fb36996)delimiter\_size

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) modem\_chat::delimiter\_size |
| --- |

## [◆ ](#adcb6a8d9fdb9b7c0e950d64ec4b0853c)filter

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* modem\_chat::filter |
| --- |

## [◆ ](#a199b2c9e9c6fd41e81ef6bca138b6328)filter\_size

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) modem\_chat::filter\_size |
| --- |

## [◆ ](#ac16520e4e7031bbc2162d29728eb86d2)matches

| const struct [modem\_chat\_match](structmodem__chat__match.md)\* modem\_chat::matches[3] |
| --- |

## [◆ ](#a249bc37382bddf11bfcabef834a19f2a)matches\_size

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) modem\_chat::matches\_size[3] |
| --- |

## [◆ ](#a2e2555e463d6dffb5ed6531ad8a822ca)parse\_arg\_len

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) modem\_chat::parse\_arg\_len |
| --- |

## [◆ ](#a42d6fe9641db254459498d26b05ce152)parse\_match

| const struct [modem\_chat\_match](structmodem__chat__match.md)\* modem\_chat::parse\_match |
| --- |

## [◆ ](#ae14032ba980271ea758278d4bd8cca30)parse\_match\_len

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) modem\_chat::parse\_match\_len |
| --- |

## [◆ ](#ae4063127d0a802801660f08a1f403121)parse\_match\_type

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) modem\_chat::parse\_match\_type |
| --- |

## [◆ ](#abff96c9a7bd215f20fece3d6f96899b5)pending\_script

| const struct [modem\_chat\_script](structmodem__chat__script.md)\* modem\_chat::pending\_script |
| --- |

## [◆ ](#a9bec3daf58728d27a554d228452a8fa9)pipe

| struct modem\_pipe\* modem\_chat::pipe |
| --- |

## [◆ ](#af2ac2cf3efac415af72b702a1ec62ae7)receive\_buf

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)\* modem\_chat::receive\_buf |
| --- |

## [◆ ](#ae15c5238e6e04a4f94a27e779d3f2a30)receive\_buf\_len

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) modem\_chat::receive\_buf\_len |
| --- |

## [◆ ](#a962b245335979eeb782410ba6429b4e6)receive\_buf\_size

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) modem\_chat::receive\_buf\_size |
| --- |

## [◆ ](#a4558d8dc063f0330bdb4d203e2af6907)receive\_work

| struct [k\_work](structk__work.md) modem\_chat::receive\_work |
| --- |

## [◆ ](#a7c181f6c68809379d756080729e1e3a1)script

| const struct [modem\_chat\_script](structmodem__chat__script.md)\* modem\_chat::script |
| --- |

## [◆ ](#ae8df85a6e2c27f720e8f7f993e7d6a75)script\_abort\_work

| struct [k\_work](structk__work.md) modem\_chat::script\_abort\_work |
| --- |

## [◆ ](#aa09d879afc7f69901799d564c3951c7b)script\_chat\_it

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) modem\_chat::script\_chat\_it |
| --- |

## [◆ ](#a8560fa2c2d26366ed27d8ca4620f30ff)script\_result

| enum [modem\_chat\_script\_result](chat_8h.md#a4035be227ddec8424311575305647d3e) modem\_chat::script\_result |
| --- |

## [◆ ](#a44f303f7ec2aa304de5ba0e1249bff35)script\_run\_work

| struct [k\_work](structk__work.md) modem\_chat::script\_run\_work |
| --- |

## [◆ ](#a36fb50970ebd8eb041506c913648be6c)script\_send\_pos

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) modem\_chat::script\_send\_pos |
| --- |

## [◆ ](#a9fc3fc3f5d2285d12ecad12e21e5be13)script\_send\_state

| enum [modem\_chat\_script\_send\_state](chat_8h.md#a734cb1bcbbbf5c87551b20038e0608ae) modem\_chat::script\_send\_state |
| --- |

## [◆ ](#a37ae5aeeaaeba6e50d7d9f0df6ff2870)script\_send\_timeout\_work

| struct [k\_work\_delayable](structk__work__delayable.md) modem\_chat::script\_send\_timeout\_work |
| --- |

## [◆ ](#a5260f843646e401159fd5f13015e9db6)script\_send\_work

| struct [k\_work](structk__work.md) modem\_chat::script\_send\_work |
| --- |

## [◆ ](#af55e1bf861e72b497230c92b4a673f4c)script\_state

| [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) modem\_chat::script\_state |
| --- |

## [◆ ](#aa365a6e40ec8de9e2a74c035dff0c203)script\_stopped\_sem

| struct k\_sem modem\_chat::script\_stopped\_sem |
| --- |

## [◆ ](#ada952e3176a7f2645ff7b64ca32cb29e)script\_timeout\_work

| struct [k\_work\_delayable](structk__work__delayable.md) modem\_chat::script\_timeout\_work |
| --- |

## [◆ ](#a26d717e335b4b1ade0972458c11f42da)user\_data

| void\* modem\_chat::user\_data |
| --- |

## [◆ ](#a5b3667c1e409fdc5382af75ad1329df9)work\_buf

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) modem\_chat::work\_buf[32] |
| --- |

## [◆ ](#a9acd26d97eec7c48482063a3c558c717)work\_buf\_len

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) modem\_chat::work\_buf\_len |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/modem/[chat.h](chat_8h_source.md)

- [modem\_chat](structmodem__chat.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

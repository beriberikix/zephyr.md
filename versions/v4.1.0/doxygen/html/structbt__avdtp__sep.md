---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structbt__avdtp__sep.html
original_path: doxygen/html/structbt__avdtp__sep.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_avdtp\_sep Struct Reference

AVDTP Stream End Point.
[More...](#details)

`#include <[avdtp.h](avdtp_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [bt\_avdtp\_sep\_info](structbt__avdtp__sep__info.md) | [sep\_info](#a0258b35f0834479a2dccdcad9b3854b9) |
|  | Stream End Point information. |
| struct [bt\_l2cap\_br\_chan](structbt__l2cap__br__chan.md) | [chan](#a33e4959b5d7c5f53469ed59af4cae022) |
|  | Media Transport Channel. |
| void(\* | [media\_data\_cb](#aeec9eb785451c8da65725603058a2a14) )(struct [bt\_avdtp\_sep](structbt__avdtp__sep.md) \*sep, struct [net\_buf](structnet__buf.md) \*buf) |
|  | the endpoint media data |
| struct k\_sem | [sem\_lock](#acff70f1a2d29b987f57af88ac75afc3e) |
| struct bt\_avdtp \* | [session](#a5c1afb8231c42d39156023939583681a) |
|  | avdtp session |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [state](#a2405b59cc7ed23c9cb221a9a684dc386) |
|  | SEP state. |

## Detailed Description

AVDTP Stream End Point.

## Field Documentation

## [◆ ](#a33e4959b5d7c5f53469ed59af4cae022)chan

| struct [bt\_l2cap\_br\_chan](structbt__l2cap__br__chan.md) bt\_avdtp\_sep::chan |
| --- |

Media Transport Channel.

## [◆ ](#aeec9eb785451c8da65725603058a2a14)media\_data\_cb

| void(\* bt\_avdtp\_sep::media\_data\_cb) (struct [bt\_avdtp\_sep](structbt__avdtp__sep.md) \*sep, struct [net\_buf](structnet__buf.md) \*buf) |
| --- |

the endpoint media data

## [◆ ](#acff70f1a2d29b987f57af88ac75afc3e)sem\_lock

| struct k\_sem bt\_avdtp\_sep::sem\_lock |
| --- |

## [◆ ](#a0258b35f0834479a2dccdcad9b3854b9)sep\_info

| struct [bt\_avdtp\_sep\_info](structbt__avdtp__sep__info.md) bt\_avdtp\_sep::sep\_info |
| --- |

Stream End Point information.

## [◆ ](#a5c1afb8231c42d39156023939583681a)session

| struct bt\_avdtp\* bt\_avdtp\_sep::session |
| --- |

avdtp session

## [◆ ](#a2405b59cc7ed23c9cb221a9a684dc386)state

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) bt\_avdtp\_sep::state |
| --- |

SEP state.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/classic/[avdtp.h](avdtp_8h_source.md)

- [bt\_avdtp\_sep](structbt__avdtp__sep.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

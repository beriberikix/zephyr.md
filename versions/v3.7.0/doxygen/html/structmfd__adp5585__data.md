---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structmfd__adp5585__data.html
original_path: doxygen/html/structmfd__adp5585__data.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mfd\_adp5585\_data Struct Reference

`#include <[adp5585.h](adp5585_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [k\_work](structk__work.md) | [work](#aad6ae38b0cfe0b216f9a965718ae92bf) |
| struct k\_sem | [lock](#a87322b6acebc0c77b4d98ab8ee6b57e6) |
| const struct [device](structdevice.md) \* | [dev](#aa517e16739c65b8468df3ef26c3b7c06) |
| struct { |  |
| } | [child](#ac890b9075851d9b9b3a102043ba522ac) |
| struct [gpio\_callback](structgpio__callback.md) | [int\_gpio\_cb](#a22322bec62253aedbe8be191bf735e72) |

## Field Documentation

## [◆ ](#ac890b9075851d9b9b3a102043ba522ac)[struct]

| struct { ... } mfd\_adp5585\_data::child |
| --- |

## [◆ ](#aa517e16739c65b8468df3ef26c3b7c06)dev

| const struct [device](structdevice.md)\* mfd\_adp5585\_data::dev |
| --- |

## [◆ ](#a22322bec62253aedbe8be191bf735e72)int\_gpio\_cb

| struct [gpio\_callback](structgpio__callback.md) mfd\_adp5585\_data::int\_gpio\_cb |
| --- |

## [◆ ](#a87322b6acebc0c77b4d98ab8ee6b57e6)lock

| struct k\_sem mfd\_adp5585\_data::lock |
| --- |

## [◆ ](#aad6ae38b0cfe0b216f9a965718ae92bf)work

| struct [k\_work](structk__work.md) mfd\_adp5585\_data::work |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/mfd/[adp5585.h](adp5585_8h_source.md)

- [mfd\_adp5585\_data](structmfd__adp5585__data.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

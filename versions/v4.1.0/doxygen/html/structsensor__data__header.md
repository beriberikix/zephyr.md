---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structsensor__data__header.html
original_path: doxygen/html/structsensor__data__header.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sensor\_data\_header Struct Reference

`#include <[sensor_data_types.h](sensor__data__types_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [base\_timestamp\_ns](#a1db93386466e8e4778f448ae0d8ca556) |
|  | The closest timestamp for when the first frame was generated as attained by :c:func:[k\_uptime\_ticks](group__clock__apis.md#ga8f143af2ee4ad42d9f7817ef161cbd13 "Get system uptime, in system ticks."). |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [reading\_count](#ad31873d402a02842eb3098431591c151) |
|  | The number of elements in the 'readings' array. |

## Field Documentation

## [◆ ](#a1db93386466e8e4778f448ae0d8ca556)base\_timestamp\_ns

| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) sensor\_data\_header::base\_timestamp\_ns |
| --- |

The closest timestamp for when the first frame was generated as attained by :c:func:[k\_uptime\_ticks](group__clock__apis.md#ga8f143af2ee4ad42d9f7817ef161cbd13 "Get system uptime, in system ticks.").

## [◆ ](#ad31873d402a02842eb3098431591c151)reading\_count

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) sensor\_data\_header::reading\_count |
| --- |

The number of elements in the 'readings' array.

This must be at least 1

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[sensor\_data\_types.h](sensor__data__types_8h_source.md)

- [sensor\_data\_header](structsensor__data__header.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/structptp__clock__driver__api.html
original_path: doxygen/html/structptp__clock__driver__api.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ptp\_clock\_driver\_api Struct Reference

`#include <[ptp_clock.h](ptp__clock_8h_source.md)>`

| Data Fields | |
| --- | --- |
| int(\* | [set](#aba0ef94f2bfe3e3d7fa2d5cedd473ab2) )(const struct [device](structdevice.md) \*dev, struct [net\_ptp\_time](structnet__ptp__time.md) \*[tm](structtm.md)) |
| int(\* | [get](#a5f9cfa4f61efe4eeee9dccb6d1e396b4) )(const struct [device](structdevice.md) \*dev, struct [net\_ptp\_time](structnet__ptp__time.md) \*[tm](structtm.md)) |
| int(\* | [adjust](#a7177e1fb271aacbae2a081ef41eb585c) )(const struct [device](structdevice.md) \*dev, int increment) |
| int(\* | [rate\_adjust](#a8774b43b65403de8faec5606e024f9af) )(const struct [device](structdevice.md) \*dev, double ratio) |

## Field Documentation

## [◆ ](#a7177e1fb271aacbae2a081ef41eb585c)adjust

| int(\* ptp\_clock\_driver\_api::adjust) (const struct [device](structdevice.md) \*dev, int increment) |
| --- |

## [◆ ](#a5f9cfa4f61efe4eeee9dccb6d1e396b4)get

| int(\* ptp\_clock\_driver\_api::get) (const struct [device](structdevice.md) \*dev, struct [net\_ptp\_time](structnet__ptp__time.md) \*[tm](structtm.md)) |
| --- |

## [◆ ](#a8774b43b65403de8faec5606e024f9af)rate\_adjust

| int(\* ptp\_clock\_driver\_api::rate\_adjust) (const struct [device](structdevice.md) \*dev, double ratio) |
| --- |

## [◆ ](#aba0ef94f2bfe3e3d7fa2d5cedd473ab2)set

| int(\* ptp\_clock\_driver\_api::set) (const struct [device](structdevice.md) \*dev, struct [net\_ptp\_time](structnet__ptp__time.md) \*[tm](structtm.md)) |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[ptp\_clock.h](ptp__clock_8h_source.md)

- [ptp\_clock\_driver\_api](structptp__clock__driver__api.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

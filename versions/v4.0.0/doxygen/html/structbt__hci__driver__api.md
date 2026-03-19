---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structbt__hci__driver__api.html
original_path: doxygen/html/structbt__hci__driver__api.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_hci\_driver\_api Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Bluetooth HCI APIs](group__bt__hci__api.md)

`#include <[bluetooth.h](drivers_2bluetooth_8h_source.md)>`

| Data Fields | |
| --- | --- |
| int(\* | [open](#a5e324fbcb48110d45b3dfa3e63c149d9) )(const struct [device](structdevice.md) \*dev, [bt\_hci\_recv\_t](group__bt__hci__api.md#ga79b12569871b2b6c8420c245e9505aed) [recv](group__bsd__sockets.md#gae11da452beee536eac85d5f26e5cdd40)) |
| int(\* | [close](#a6ce182bca140ff9fb53953afa01acf75) )(const struct [device](structdevice.md) \*dev) |
| int(\* | [send](#ae8b1e9370b0f651eeed4b85bfabf13d1) )(const struct [device](structdevice.md) \*dev, struct [net\_buf](structnet__buf.md) \*buf) |

## Field Documentation

## [◆ ](#a6ce182bca140ff9fb53953afa01acf75)close

| int(\* bt\_hci\_driver\_api::close) (const struct [device](structdevice.md) \*dev) |
| --- |

## [◆ ](#a5e324fbcb48110d45b3dfa3e63c149d9)open

| int(\* bt\_hci\_driver\_api::open) (const struct [device](structdevice.md) \*dev, [bt\_hci\_recv\_t](group__bt__hci__api.md#ga79b12569871b2b6c8420c245e9505aed) [recv](group__bsd__sockets.md#gae11da452beee536eac85d5f26e5cdd40)) |
| --- |

## [◆ ](#ae8b1e9370b0f651eeed4b85bfabf13d1)send

| int(\* bt\_hci\_driver\_api::send) (const struct [device](structdevice.md) \*dev, struct [net\_buf](structnet__buf.md) \*buf) |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[bluetooth.h](drivers_2bluetooth_8h_source.md)

- [bt\_hci\_driver\_api](structbt__hci__driver__api.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structbt__cts__cb.html
original_path: doxygen/html/structbt__cts__cb.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_cts\_cb Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Current Time Service (CTS)](group__bt__cts.md)

Current Time Service callback structure.
[More...](#details)

`#include <[cts.h](cts_8h_source.md)>`

| Data Fields | |
| --- | --- |
| void(\* | [notification\_changed](#accf7eb6620ae0f4b9693d238ecdde5b3) )([bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enabled) |
|  | Current Time Service notifications changed. |
| int(\* | [cts\_time\_write](#a1dd6b251b07537e81c010f654721cbf4) )(struct [bt\_cts\_time\_format](structbt__cts__time__format.md) \*cts\_time) |
|  | The Current Time has been updated by a peer. |
| int(\* | [fill\_current\_cts\_time](#ae4a374f95870bfa21b8c1d87e832fe48) )(struct [bt\_cts\_time\_format](structbt__cts__time__format.md) \*cts\_time) |
|  | When current time Read request or notification is triggered, CTS uses this callback to retrieve current time information from application. |

## Detailed Description

Current Time Service callback structure.

## Field Documentation

## [◆ ](#a1dd6b251b07537e81c010f654721cbf4)cts\_time\_write

| int(\* bt\_cts\_cb::cts\_time\_write) (struct [bt\_cts\_time\_format](structbt__cts__time__format.md) \*cts\_time) |
| --- |

The Current Time has been updated by a peer.

It is the responsibility of the application to store the new time.

Parameters
:   | cts\_time | [IN] updated time |
    | --- | --- |

Returns
:   0 application has decoded it successfully
:   negative error codes on failure

## [◆ ](#ae4a374f95870bfa21b8c1d87e832fe48)fill\_current\_cts\_time

| int(\* bt\_cts\_cb::fill\_current\_cts\_time) (struct [bt\_cts\_time\_format](structbt__cts__time__format.md) \*cts\_time) |
| --- |

When current time Read request or notification is triggered, CTS uses this callback to retrieve current time information from application.

Application must implement it and provide cts formatted current time information

Note
:   this callback is mandatory

Parameters
:   | cts\_time | [IN] updated time |
    | --- | --- |

Returns
:   0 application has encoded it successfully
:   negative error codes on failure

## [◆ ](#accf7eb6620ae0f4b9693d238ecdde5b3)notification\_changed

| void(\* bt\_cts\_cb::notification\_changed) ([bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) enabled) |
| --- |

Current Time Service notifications changed.

Parameters
:   | enabled | True if notifications are enabled, false if disabled |
    | --- | --- |

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/services/[cts.h](cts_8h_source.md)

- [bt\_cts\_cb](structbt__cts__cb.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

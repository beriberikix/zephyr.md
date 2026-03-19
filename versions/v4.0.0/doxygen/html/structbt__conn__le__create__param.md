---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structbt__conn__le__create__param.html
original_path: doxygen/html/structbt__conn__le__create__param.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_conn\_le\_create\_param Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Connection management](group__bt__conn.md)

`#include <[conn.h](conn_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [options](#a4b1e26c0976d9c900b831c886c77b055) |
|  | Bit-field of create connection options. |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [interval](#a5cfae677f924534dc5bc7b38c457a7af) |
|  | Scan interval (N \* 0.625 ms). |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [window](#a339b99f65c5029ada6cdf453ab1f258e) |
|  | Scan window (N \* 0.625 ms). |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [interval\_coded](#a2bc978ac97435fe5f87c6e01692f2910) |
|  | Scan interval LE Coded PHY (N \* 0.625 MS). |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [window\_coded](#ae62491837d35d95e32016b793edf8c96) |
|  | Scan window LE Coded PHY (N \* 0.625 MS). |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [timeout](#a59f05bfb9468779d02f8d0beeb7a35c1) |
|  | Connection initiation timeout (N \* 10 MS). |

## Field Documentation

## [◆ ](#a5cfae677f924534dc5bc7b38c457a7af)interval

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_conn\_le\_create\_param::interval |
| --- |

Scan interval (N \* 0.625 ms).

Note
:   When

    ```
    CONFIG_BT_SCAN_AND_INITIATE_IN_PARALLEL
    ```

    is enabled and the application wants to scan and connect in parallel, the Bluetooth Controller may require the scan interval used for scanning and connection establishment to be equal to obtain the best performance.

## [◆ ](#a2bc978ac97435fe5f87c6e01692f2910)interval\_coded

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_conn\_le\_create\_param::interval\_coded |
| --- |

Scan interval LE Coded PHY (N \* 0.625 MS).

Set zero to use same as LE 1M PHY scan interval

## [◆ ](#a4b1e26c0976d9c900b831c886c77b055)options

| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) bt\_conn\_le\_create\_param::options |
| --- |

Bit-field of create connection options.

## [◆ ](#a59f05bfb9468779d02f8d0beeb7a35c1)timeout

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_conn\_le\_create\_param::timeout |
| --- |

Connection initiation timeout (N \* 10 MS).

Set zero to use the default

```
CONFIG_BT_CREATE_CONN_TIMEOUT
```

timeout.

Note
:   Unused in [bt\_conn\_le\_create\_auto](group__bt__conn.md#gaecfaf2cb44772511dbb585de8f76f09b "bt_conn_le_create_auto")

## [◆ ](#a339b99f65c5029ada6cdf453ab1f258e)window

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_conn\_le\_create\_param::window |
| --- |

Scan window (N \* 0.625 ms).

Note
:   When

    ```
    CONFIG_BT_SCAN_AND_INITIATE_IN_PARALLEL
    ```

    is enabled and the application wants to scan and connect in parallel, the Bluetooth Controller may require the scan window used for scanning and connection establishment to be equal to obtain the best performance.

## [◆ ](#ae62491837d35d95e32016b793edf8c96)window\_coded

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) bt\_conn\_le\_create\_param::window\_coded |
| --- |

Scan window LE Coded PHY (N \* 0.625 MS).

Set zero to use same as LE 1M PHY scan window.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/[conn.h](conn_8h_source.md)

- [bt\_conn\_le\_create\_param](structbt__conn__le__create__param.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

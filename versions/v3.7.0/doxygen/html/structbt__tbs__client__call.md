---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structbt__tbs__client__call.html
original_path: doxygen/html/structbt__tbs__client__call.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bt\_tbs\_client\_call Struct Reference

[Connectivity](group__connectivity.md) » [Bluetooth APIs](group__bluetooth.md) » [Telephone Bearer Service (TBS)](group__bt__tbs.md)

Struct to hold a call as the Telephone Bearer Service client.
[More...](#details)

`#include <[tbs.h](tbs_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [bt\_tbs\_client\_call\_state](structbt__tbs__client__call__state.md) | [call\_info](#a480279fea551db1bcb260de81edd6571) |
|  | Call information. |
| char \* | [remote\_uri](#af04f0576e786250526c12e1436a60c4e) |
|  | The remove URI. |

## Detailed Description

Struct to hold a call as the Telephone Bearer Service client.

## Field Documentation

## [◆ ](#a480279fea551db1bcb260de81edd6571)call\_info

| struct [bt\_tbs\_client\_call\_state](structbt__tbs__client__call__state.md) bt\_tbs\_client\_call::call\_info |
| --- |

Call information.

## [◆ ](#af04f0576e786250526c12e1436a60c4e)remote\_uri

| char\* bt\_tbs\_client\_call::remote\_uri |
| --- |

The remove URI.

---

The documentation for this struct was generated from the following file:

- zephyr/bluetooth/audio/[tbs.h](tbs_8h_source.md)

- [bt\_tbs\_client\_call](structbt__tbs__client__call.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

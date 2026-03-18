---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structwifi__ps__config.html
original_path: doxygen/html/structwifi__ps__config.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

wifi\_ps\_config Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Wi-Fi Management](group__wifi__mgmt.md)

Wi-Fi power save configuration.
[More...](#details)

`#include <[wifi_mgmt.h](wifi__mgmt_8h_source.md)>`

| Data Fields | |
| --- | --- |
| char | [num\_twt\_flows](#a9e83c10eaaa1d721cbc49b40aedb00df) |
|  | Number of TWT flows. |
| struct [wifi\_twt\_flow\_info](structwifi__twt__flow__info.md) | [twt\_flows](#ab7460f0f253b2d552e49e98e2c770967) [WIFI\_MAX\_TWT\_FLOWS] |
|  | TWT flow details. |
| struct [wifi\_ps\_params](structwifi__ps__params.md) | [ps\_params](#a357aafc2dedda37755b1cb1fc07fe5a6) |
|  | Power save configuration. |

## Detailed Description

Wi-Fi power save configuration.

## Field Documentation

## [◆ ](#a9e83c10eaaa1d721cbc49b40aedb00df)num\_twt\_flows

| char wifi\_ps\_config::num\_twt\_flows |
| --- |

Number of TWT flows.

## [◆ ](#a357aafc2dedda37755b1cb1fc07fe5a6)ps\_params

| struct [wifi\_ps\_params](structwifi__ps__params.md) wifi\_ps\_config::ps\_params |
| --- |

Power save configuration.

## [◆ ](#ab7460f0f253b2d552e49e98e2c770967)twt\_flows

| struct [wifi\_twt\_flow\_info](structwifi__twt__flow__info.md) wifi\_ps\_config::twt\_flows[WIFI\_MAX\_TWT\_FLOWS] |
| --- |

TWT flow details.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[wifi\_mgmt.h](wifi__mgmt_8h_source.md)

- [wifi\_ps\_config](structwifi__ps__config.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

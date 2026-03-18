---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/structnet__event__l4__hostname.html
original_path: doxygen/html/structnet__event__l4__hostname.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

net\_event\_l4\_hostname Struct Reference

[Connectivity](group__connectivity.md) » [Networking](group__networking.md) » [Network Management](group__net__mgmt.md)

Network Management event information structure Used to pass information on NET\_EVENT\_HOSTNAME\_CHANGED event when CONFIG\_NET\_MGMT\_EVENT\_INFO is enabled and event generator pass the information.
[More...](#details)

`#include <[net_event.h](net__event_8h_source.md)>`

| Data Fields | |
| --- | --- |
| char | [hostname](#a8e04c33dfb1c251a0deaa29081283245) [NET\_HOSTNAME\_SIZE] |
|  | New hostname. |

## Detailed Description

Network Management event information structure Used to pass information on NET\_EVENT\_HOSTNAME\_CHANGED event when CONFIG\_NET\_MGMT\_EVENT\_INFO is enabled and event generator pass the information.

## Field Documentation

## [◆ ](#a8e04c33dfb1c251a0deaa29081283245)hostname

| char net\_event\_l4\_hostname::hostname[NET\_HOSTNAME\_SIZE] |
| --- |

New hostname.

---

The documentation for this struct was generated from the following file:

- zephyr/net/[net\_event.h](net__event_8h_source.md)

- [net\_event\_l4\_hostname](structnet__event__l4__hostname.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/structtisci__msg__fwl__region__cfg.html
original_path: doxygen/html/structtisci__msg__fwl__region__cfg.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

tisci\_msg\_fwl\_region\_cfg Struct Reference

Request and Response for firewalls settings.
[More...](#details)

`#include <[zephyr/drivers/firmware/tisci/tisci.h](tisci_8h_source.md)>`

## Detailed Description

Request and Response for firewalls settings.

Parameters
:   | fwl\_id | Firewall ID in question |
    | --- | --- |
    | region | Region or channel number to set config info This field is unused in case of a simple firewall and must be initialized to zero. In case of a region based firewall, this field indicates the region in question. (index starting from 0) In case of a channel based firewall, this field indicates the channel in question (index starting from 0) |
    | n\_permission\_regs | Number of permission registers to set |
    | control | Contents of the firewall CONTROL register to set |
    | permissions | Contents of the firewall PERMISSION register to set |
    | start\_address | Contents of the firewall START\_ADDRESS register to set |
    | end\_address | Contents of the firewall END\_ADDRESS register to set |

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/firmware/tisci/[tisci.h](tisci_8h_source.md)

- [tisci\_msg\_fwl\_region\_cfg](structtisci__msg__fwl__region__cfg.md)
- Generated on  for Zephyr API Documentation by [![doxygen](https://docs.zephyrproject.org/4.2.0/doxygen/html/doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

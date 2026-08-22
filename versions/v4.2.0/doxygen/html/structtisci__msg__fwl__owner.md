---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/structtisci__msg__fwl__owner.html
original_path: doxygen/html/structtisci__msg__fwl__owner.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

tisci\_msg\_fwl\_owner Struct Reference

Request and Response for firewall owner change.
[More...](#details)

`#include <[zephyr/drivers/firmware/tisci/tisci.h](tisci_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [fwl\_id](#a370a1aff0233b53b035cbcd7b4c264b5) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [region](#a7ccaf9d3c1bd3639e8c170acd5d535a8) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [owner\_index](#a2010d9ee65f9a94e5477a0fc1f21774e) |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [owner\_privid](#a5e5e33a9a2f7c04022ce51fa1dcb8eef) |
| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) | [owner\_permission\_bits](#a31ec3f0e90fdb8cea887d67004b066a7) |

## Detailed Description

Request and Response for firewall owner change.

Parameters
:   | [fwl\_id](#a370a1aff0233b53b035cbcd7b4c264b5) | Firewall ID in question |
    | --- | --- |
    | [region](#a7ccaf9d3c1bd3639e8c170acd5d535a8) | Region or channel number to set config info This field is unused in case of a simple firewall and must be initialized to zero. In case of a region based firewall, this field indicates the region in question. (index starting from 0) In case of a channel based firewall, this field indicates the channel in question (index starting from 0) |
    | n\_permission\_regs | Number of permission registers <= 3 |
    | control | Control register value for this region |
    | [owner\_index](#a2010d9ee65f9a94e5477a0fc1f21774e) | New owner index to change to. Owner indexes are setup in DMSC firmware boot configuration data |
    | [owner\_privid](#a5e5e33a9a2f7c04022ce51fa1dcb8eef) | New owner priv-id, used to lookup owner\_index is not known, must be set to zero otherwise |
    | [owner\_permission\_bits](#a31ec3f0e90fdb8cea887d67004b066a7) | New owner permission bits |

## Field Documentation

## [◆ ](#a370a1aff0233b53b035cbcd7b4c264b5)fwl\_id

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tisci\_msg\_fwl\_owner::fwl\_id |
| --- |

## [◆ ](#a2010d9ee65f9a94e5477a0fc1f21774e)owner\_index

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) tisci\_msg\_fwl\_owner::owner\_index |
| --- |

## [◆ ](#a31ec3f0e90fdb8cea887d67004b066a7)owner\_permission\_bits

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tisci\_msg\_fwl\_owner::owner\_permission\_bits |
| --- |

## [◆ ](#a5e5e33a9a2f7c04022ce51fa1dcb8eef)owner\_privid

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) tisci\_msg\_fwl\_owner::owner\_privid |
| --- |

## [◆ ](#a7ccaf9d3c1bd3639e8c170acd5d535a8)region

| [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) tisci\_msg\_fwl\_owner::region |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/firmware/tisci/[tisci.h](tisci_8h_source.md)

- [tisci\_msg\_fwl\_owner](structtisci__msg__fwl__owner.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

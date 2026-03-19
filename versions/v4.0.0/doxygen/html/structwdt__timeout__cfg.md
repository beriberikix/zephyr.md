---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structwdt__timeout__cfg.html
original_path: doxygen/html/structwdt__timeout__cfg.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

wdt\_timeout\_cfg Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [Watchdog Interface](group__watchdog__interface.md)

Watchdog timeout configuration.
[More...](#details)

`#include <[watchdog.h](watchdog_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [wdt\_window](structwdt__window.md) | [window](#a7942c675aacd228e38ea3cde383aab41) |
|  | Timing parameters of watchdog timeout. |
| [wdt\_callback\_t](group__watchdog__interface.md#ga11a942c8e7ee7ceae87c4601dbea8486) | [callback](#a0a3bcc1a3f2785b44c0196a7d3223aa0) |
|  | Timeout callback (can be NULL). |
| struct [wdt\_timeout\_cfg](structwdt__timeout__cfg.md) \* | [next](#a325fe7146a922f5f266537307dba6c63) |
|  | Pointer to the next timeout configuration. |
| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) | [flags](#a71aa1ffb4f9937cce8197278cc0c61ee) |
|  | Flags (see [WDT\_FLAGS](group__watchdog__interface.md#WDT_FLAGS "WDT_FLAGS")). |

## Detailed Description

Watchdog timeout configuration.

## Field Documentation

## [◆ ](#a0a3bcc1a3f2785b44c0196a7d3223aa0)callback

| [wdt\_callback\_t](group__watchdog__interface.md#ga11a942c8e7ee7ceae87c4601dbea8486) wdt\_timeout\_cfg::callback |
| --- |

Timeout callback (can be NULL).

## [◆ ](#a71aa1ffb4f9937cce8197278cc0c61ee)flags

| [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) wdt\_timeout\_cfg::flags |
| --- |

Flags (see [WDT\_FLAGS](group__watchdog__interface.md#WDT_FLAGS "WDT_FLAGS")).

## [◆ ](#a325fe7146a922f5f266537307dba6c63)next

| struct [wdt\_timeout\_cfg](structwdt__timeout__cfg.md)\* wdt\_timeout\_cfg::next |
| --- |

Pointer to the next timeout configuration.

This field is only available if

```
CONFIG_WDT_MULTISTAGE
```

is enabled (watchdogs with staged timeouts functionality). Value must be NULL for single stage timeout.

## [◆ ](#a7942c675aacd228e38ea3cde383aab41)window

| struct [wdt\_window](structwdt__window.md) wdt\_timeout\_cfg::window |
| --- |

Timing parameters of watchdog timeout.

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[watchdog.h](watchdog_8h_source.md)

- [wdt\_timeout\_cfg](structwdt__timeout__cfg.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

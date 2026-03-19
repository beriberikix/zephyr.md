---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structentropy__driver__api.html
original_path: doxygen/html/structentropy__driver__api.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

entropy\_driver\_api Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [Entropy Interface](group__entropy__interface.md)

Entropy driver API structure.
[More...](#details)

`#include <[entropy.h](entropy_8h_source.md)>`

| Data Fields | |
| --- | --- |
| [entropy\_get\_entropy\_t](group__entropy__interface.md#ga661150c9482777f98cdee794e9164b28) | [get\_entropy](#a3fd7758ed4c71ba1d64939297d06faa3) |
| [entropy\_get\_entropy\_isr\_t](group__entropy__interface.md#gacaa273da74b4727ea49b25d1ccd9725c) | [get\_entropy\_isr](#ac0356f7fd4600377c6018414f056d766) |

## Detailed Description

Entropy driver API structure.

This is the mandatory API any Entropy driver needs to expose.

## Field Documentation

## [◆ ](#a3fd7758ed4c71ba1d64939297d06faa3)get\_entropy

| [entropy\_get\_entropy\_t](group__entropy__interface.md#ga661150c9482777f98cdee794e9164b28) entropy\_driver\_api::get\_entropy |
| --- |

## [◆ ](#ac0356f7fd4600377c6018414f056d766)get\_entropy\_isr

| [entropy\_get\_entropy\_isr\_t](group__entropy__interface.md#gacaa273da74b4727ea49b25d1ccd9725c) entropy\_driver\_api::get\_entropy\_isr |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[entropy.h](entropy_8h_source.md)

- [entropy\_driver\_api](structentropy__driver__api.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/structsigevent.html
original_path: doxygen/html/structsigevent.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sigevent Struct Reference

`#include <[signal.h](signal_8h_source.md)>`

| Data Fields | |
| --- | --- |
| void(\* | [sigev\_notify\_function](#ae3636bc03a98e9f92bf154dfefaa9b43) )(union [sigval](unionsigval.md) val) |
| pthread\_attr\_t \* | [sigev\_notify\_attributes](#a5a687d2092b237d76eb08e2d46a5115f) |
| union [sigval](unionsigval.md) | [sigev\_value](#a757af1e34b87e3f66bbc08c514017a2c) |
| int | [sigev\_notify](#aae9a19d879c38e0c4e8a9bf738c5081e) |
| int | [sigev\_signo](#a5c645ec1d12bb46efc3f4097c52b665d) |

## Field Documentation

## [◆ ](#aae9a19d879c38e0c4e8a9bf738c5081e)sigev\_notify

| int sigevent::sigev\_notify |
| --- |

## [◆ ](#a5a687d2092b237d76eb08e2d46a5115f)sigev\_notify\_attributes

| pthread\_attr\_t\* sigevent::sigev\_notify\_attributes |
| --- |

## [◆ ](#ae3636bc03a98e9f92bf154dfefaa9b43)sigev\_notify\_function

| void(\* sigevent::sigev\_notify\_function) (union [sigval](unionsigval.md) val) |
| --- |

## [◆ ](#a5c645ec1d12bb46efc3f4097c52b665d)sigev\_signo

| int sigevent::sigev\_signo |
| --- |

## [◆ ](#a757af1e34b87e3f66bbc08c514017a2c)sigev\_value

| union [sigval](unionsigval.md) sigevent::sigev\_value |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/posix/[signal.h](signal_8h_source.md)

- [sigevent](structsigevent.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

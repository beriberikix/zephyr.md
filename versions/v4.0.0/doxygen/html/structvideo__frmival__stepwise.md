---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structvideo__frmival__stepwise.html
original_path: doxygen/html/structvideo__frmival__stepwise.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

video\_frmival\_stepwise Struct Reference

[Device Driver APIs](group__io__interfaces.md) » [Video Interface](group__video__interface.md)

Video frame interval stepwise structure.
[More...](#details)

`#include <[video.h](video_8h_source.md)>`

| Data Fields | |
| --- | --- |
| struct [video\_frmival](structvideo__frmival.md) | [min](#aec892104241a9d4204c87af51765ee2f) |
|  | minimum frame interval in seconds |
| struct [video\_frmival](structvideo__frmival.md) | [max](#af1c5a40da9fe7ad30185464eccf5b438) |
|  | maximum frame interval in seconds |
| struct [video\_frmival](structvideo__frmival.md) | [step](#afc3c4e4fe3641952c4e6fc494fa85760) |
|  | frame interval step size in seconds |

## Detailed Description

Video frame interval stepwise structure.

Used to describe the video frame interval stepwise type.

## Field Documentation

## [◆ ](#af1c5a40da9fe7ad30185464eccf5b438)max

| struct [video\_frmival](structvideo__frmival.md) video\_frmival\_stepwise::max |
| --- |

maximum frame interval in seconds

## [◆ ](#aec892104241a9d4204c87af51765ee2f)min

| struct [video\_frmival](structvideo__frmival.md) video\_frmival\_stepwise::min |
| --- |

minimum frame interval in seconds

## [◆ ](#afc3c4e4fe3641952c4e6fc494fa85760)step

| struct [video\_frmival](structvideo__frmival.md) video\_frmival\_stepwise::step |
| --- |

frame interval step size in seconds

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/[video.h](video_8h_source.md)

- [video\_frmival\_stepwise](structvideo__frmival__stepwise.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

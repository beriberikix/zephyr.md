---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/haptics_8h.html
original_path: doxygen/html/haptics_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

haptics.h File Reference

`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <syscalls/haptics.h>`

[Go to the source code of this file.](haptics_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [haptics\_driver\_api](structhaptics__driver__api.md) |
|  | Haptic device API. [More...](structhaptics__driver__api.md#details) |

| Typedefs | |
| --- | --- |
| typedef int(\* | [haptics\_stop\_output\_t](group__haptics__interface.md#gae34e538c40e259967f5791cc5ebd2707)) (const struct [device](structdevice.md) \*dev) |
|  | Set the haptic device to stop output. |
| typedef int(\* | [haptics\_start\_output\_t](group__haptics__interface.md#gaa6c2ff4b8ed7ae83e4006eb735f61a46)) (const struct [device](structdevice.md) \*dev) |
|  | Set the haptic device to start output for a playback event. |

| Functions | |
| --- | --- |
| int | [haptics\_start\_output](group__haptics__interface.md#ga96e0b0fad35d6535adad7536a9411f44) (const struct [device](structdevice.md) \*dev) |
|  | Set the haptic device to start output for a playback event. |
| int | [haptics\_stop\_output](group__haptics__interface.md#ga42a5fc7e6b6247316cdf356573dbbb33) (const struct [device](structdevice.md) \*dev) |
|  | Set the haptic device to stop output for a playback event. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [haptics.h](haptics_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

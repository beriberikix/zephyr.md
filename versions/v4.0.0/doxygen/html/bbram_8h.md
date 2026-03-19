---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/bbram_8h.html
original_path: doxygen/html/bbram_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bbram.h File Reference

`#include <[errno.h](errno_8h_source.md)>`  
`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <zephyr/syscalls/bbram.h>`

[Go to the source code of this file.](bbram_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [bbram\_driver\_api](structbbram__driver__api.md) |

| Typedefs | |
| --- | --- |
| typedef int(\* | [bbram\_api\_check\_invalid\_t](group__bbram__interface.md#gac23658302662587043f3587080f798fe)) (const struct [device](structdevice.md) \*dev) |
|  | API template to check if the BBRAM is invalid. |
| typedef int(\* | [bbram\_api\_check\_standby\_power\_t](group__bbram__interface.md#ga99adefcb89ab80d8b5e24b8ffad8f43e)) (const struct [device](structdevice.md) \*dev) |
|  | API template to check for standby power failure. |
| typedef int(\* | [bbram\_api\_check\_power\_t](group__bbram__interface.md#gaa6edc8a61529edad90de2e6fff619fdf)) (const struct [device](structdevice.md) \*dev) |
|  | API template to check for V CC1 power failure. |
| typedef int(\* | [bbram\_api\_get\_size\_t](group__bbram__interface.md#gacfa586f705c520a6a05638a2e289fe50)) (const struct [device](structdevice.md) \*dev, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*size) |
|  | API template to check the size of the BBRAM. |
| typedef int(\* | [bbram\_api\_read\_t](group__bbram__interface.md#ga8b06a1b3bb9b524597804dd268904881)) (const struct [device](structdevice.md) \*dev, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) offset, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data) |
|  | API template to read from BBRAM. |
| typedef int(\* | [bbram\_api\_write\_t](group__bbram__interface.md#ga1b111ae421791b9544777c1bab5e2a02)) (const struct [device](structdevice.md) \*dev, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) offset, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data) |
|  | API template to write to BBRAM. |

| Functions | |
| --- | --- |
| int | [bbram\_check\_invalid](group__bbram__interface.md#ga7164969f308616696a9ab71a4d19b70b) (const struct [device](structdevice.md) \*dev) |
|  | Check if BBRAM is invalid. |
| int | [bbram\_check\_standby\_power](group__bbram__interface.md#ga948ed0a7d3824f950ad46b99ba3d86f4) (const struct [device](structdevice.md) \*dev) |
|  | Check for standby (Volt SBY) power failure. |
| int | [bbram\_check\_power](group__bbram__interface.md#ga8fc2a647bda90e96f866514300180a96) (const struct [device](structdevice.md) \*dev) |
|  | Check for V CC1 power failure. |
| int | [bbram\_get\_size](group__bbram__interface.md#gab6bdb4a1cba88ca645c256366a696bdd) (const struct [device](structdevice.md) \*dev, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) \*size) |
|  | Get the size of the BBRAM (in bytes). |
| int | [bbram\_read](group__bbram__interface.md#ga9ef786b0fbac3f8523be2bb87b7cff7b) (const struct [device](structdevice.md) \*dev, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) offset, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data) |
|  | Read bytes from BBRAM. |
| int | [bbram\_write](group__bbram__interface.md#ga51007eed4820aed341d20e4562607564) (const struct [device](structdevice.md) \*dev, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) offset, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) size, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data) |
|  | Write bytes to BBRAM. |
| int | [bbram\_emul\_set\_invalid](group__bbram__interface.md#gae2b89f8a44e38fe7df2219397bad139b) (const struct [device](structdevice.md) \*dev, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) is\_invalid) |
|  | Set the emulated BBRAM driver's invalid state. |
| int | [bbram\_emul\_set\_standby\_power\_state](group__bbram__interface.md#ga08a2c565ba0ec6ac5894a718a652eec2) (const struct [device](structdevice.md) \*dev, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) failure) |
|  | Set the emulated BBRAM driver's standby power state. |
| int | [bbram\_emul\_set\_power\_state](group__bbram__interface.md#gadc0243187b853832b08af36c9baf9cb0) (const struct [device](structdevice.md) \*dev, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) failure) |
|  | Set the emulated BBRAM driver's power state. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [bbram.h](bbram_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/emul__bbram_8h.html
original_path: doxygen/html/emul__bbram_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

emul\_bbram.h File Reference

`#include <[zephyr/drivers/emul.h](drivers_2emul_8h_source.md)>`  
`#include <[stdint.h](stdint_8h_source.md)>`

[Go to the source code of this file.](emul__bbram_8h_source.md)

| Functions | |
| --- | --- |
| static int | [emul\_bbram\_backend\_set\_data](group__bbram__emulator__backend.md#gaeff1fa9acd765323778c42a4c3424c0b) (const struct [emul](structemul.md) \*target, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) offset, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) count, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data) |
|  | Set the expected data in the bbram region. |
| static int | [emul\_bbram\_backend\_get\_data](group__bbram__emulator__backend.md#ga92942f1ebe6905ad3cfe389824af5914) (const struct [emul](structemul.md) \*target, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) offset, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) count, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data) |
|  | Get the expected data in the bbram region. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [emul\_bbram.h](emul__bbram_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

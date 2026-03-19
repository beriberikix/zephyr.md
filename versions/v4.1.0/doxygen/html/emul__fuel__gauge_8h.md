---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/emul__fuel__gauge_8h.html
original_path: doxygen/html/emul__fuel__gauge_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

emul\_fuel\_gauge.h File Reference

Backend APIs for the fuel gauge emulators.
[More...](#details)

`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <[zephyr/drivers/emul.h](drivers_2emul_8h_source.md)>`  
`#include <[zephyr/drivers/fuel_gauge.h](fuel__gauge_8h_source.md)>`  
`#include <zephyr/syscalls/emul_fuel_gauge.h>`

[Go to the source code of this file.](emul__fuel__gauge_8h_source.md)

| Functions | |
| --- | --- |
| int | [emul\_fuel\_gauge\_set\_battery\_charging](group__fuel__gauge__emulator__backend.md#gab6493138c35191a58e6f28c24b97715e) (const struct [emul](structemul.md) \*target, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) uV, int uA) |
|  | Set charging for fuel gauge associated battery. |
| int | [emul\_fuel\_gauge\_is\_battery\_cutoff](group__fuel__gauge__emulator__backend.md#gaf8326331c7470b41aa542f828b20a828) (const struct [emul](structemul.md) \*target, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) \*cutoff) |
|  | Check if the battery has been cut off. |

## Detailed Description

Backend APIs for the fuel gauge emulators.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [emul\_fuel\_gauge.h](emul__fuel__gauge_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

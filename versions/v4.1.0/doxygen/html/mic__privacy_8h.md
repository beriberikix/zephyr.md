---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/mic__privacy_8h.html
original_path: doxygen/html/mic__privacy_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mic\_privacy.h File Reference

`#include <[stdint.h](stdint_8h_source.md)>`  
`#include <[errno.h](errno_8h_source.md)>`  
`#include <[stdbool.h](stdbool_8h_source.md)>`  
`#include <[zephyr/kernel.h](kernel_8h_source.md)>`  
`#include <[zephyr/spinlock.h](spinlock_8h_source.md)>`  
`#include <[zephyr/devicetree.h](devicetree_8h_source.md)>`

[Go to the source code of this file.](mic__privacy_8h_source.md)

| Data Structures | |
| --- | --- |
| union | [mic\_privacy\_mask](unionmic__privacy__mask.md) |
| struct | [intel\_adsp\_mic\_priv\_data](structintel__adsp__mic__priv__data.md) |
| struct | [intel\_adsp\_mic\_priv\_cfg](structintel__adsp__mic__priv__cfg.md) |
| struct | [mic\_privacy\_api\_funcs](structmic__privacy__api__funcs.md) |

| Enumerations | |
| --- | --- |
| enum | [mic\_privacy\_policy](#acbabb5c150f29668a23379bcb2180931) { [MIC\_PRIVACY\_DISABLED](#acbabb5c150f29668a23379bcb2180931a6d9216a6396136add2267a39d3b0cfe4) = 0 , [MIC\_PRIVACY\_HW\_MANAGED](#acbabb5c150f29668a23379bcb2180931a0ac8b17e6006dafa7516b5ebfd9d3d0f) = 1 , [MIC\_PRIVACY\_FW\_MANAGED](#acbabb5c150f29668a23379bcb2180931a1abc8c704d5bc13bbda18dbef6b9da5c) = 2 , [MIC\_PRIVACY\_FORCE\_MIC\_DISABLED](#acbabb5c150f29668a23379bcb2180931a7d76f1a96d342f4c7c769d3fc5fcac90) = 3 } |

## Enumeration Type Documentation

## [◆ ](#acbabb5c150f29668a23379bcb2180931)mic\_privacy\_policy

| enum [mic\_privacy\_policy](#acbabb5c150f29668a23379bcb2180931) |
| --- |

| Enumerator | |
| --- | --- |
| MIC\_PRIVACY\_DISABLED |  |
| MIC\_PRIVACY\_HW\_MANAGED |  |
| MIC\_PRIVACY\_FW\_MANAGED |  |
| MIC\_PRIVACY\_FORCE\_MIC\_DISABLED |  |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [mic\_privacy](dir_2e06c65c52133b8e4ff4bf7424ae25af.md)
- [intel](dir_493819a1cd457399897f0d97609f1fe6.md)
- [mic\_privacy.h](mic__privacy_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

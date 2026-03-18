---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/include_2zephyr_2arch_2arm_2cortex__m_2cpu_8h.html
original_path: doxygen/html/include_2zephyr_2arch_2arm_2cortex__m_2cpu_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

cpu.h File Reference

`#include <[stdint.h](stdint_8h_source.md)>`

[Go to the source code of this file.](include_2zephyr_2arch_2arm_2cortex__m_2cpu_8h_source.md)

| Macros | |
| --- | --- |
| #define | [CPACR\_CP10\_Pos](#a65fa7b1d26e122d7466d09d023dd03f5)   20U |
| #define | [CPACR\_CP10\_Msk](#aae47418d3f6f6596d74427d671db4568)   (3UL << [CPACR\_CP10\_Pos](#a65fa7b1d26e122d7466d09d023dd03f5)) |
| #define | [CPACR\_CP10\_NO\_ACCESS](#ab98d9a7803e01c9419a1b3db46ea1add)   (0UL << [CPACR\_CP10\_Pos](#a65fa7b1d26e122d7466d09d023dd03f5)) |
| #define | [CPACR\_CP10\_PRIV\_ACCESS](#aae2814998733c5960397fe122e1fd171)   (1UL << [CPACR\_CP10\_Pos](#a65fa7b1d26e122d7466d09d023dd03f5)) |
| #define | [CPACR\_CP10\_RESERVED](#a92b527c3d4f14132baac8726ab4df091)   (2UL << [CPACR\_CP10\_Pos](#a65fa7b1d26e122d7466d09d023dd03f5)) |
| #define | [CPACR\_CP10\_FULL\_ACCESS](#a9206df98746982fe6644162f551d7dfa)   (3UL << [CPACR\_CP10\_Pos](#a65fa7b1d26e122d7466d09d023dd03f5)) |
| #define | [CPACR\_CP11\_Pos](#aedc603d4d2e20473426cf237efdf0a0f)   22U |
| #define | [CPACR\_CP11\_Msk](#a48424c4ebf99120abe4887ca5f6445eb)   (3UL << [CPACR\_CP11\_Pos](#aedc603d4d2e20473426cf237efdf0a0f)) |
| #define | [CPACR\_CP11\_NO\_ACCESS](#a8994c5fdf0730b06c7a11846151eaa5f)   (0UL << [CPACR\_CP11\_Pos](#aedc603d4d2e20473426cf237efdf0a0f)) |
| #define | [CPACR\_CP11\_PRIV\_ACCESS](#abcb053930af36f899c8d079fa80cbb6a)   (1UL << [CPACR\_CP11\_Pos](#aedc603d4d2e20473426cf237efdf0a0f)) |
| #define | [CPACR\_CP11\_RESERVED](#a8318babac72e1f7ee52b60cbf0c5975d)   (2UL << [CPACR\_CP11\_Pos](#aedc603d4d2e20473426cf237efdf0a0f)) |
| #define | [CPACR\_CP11\_FULL\_ACCESS](#a45e50725e2027dda6cbc5ca350d5d177)   (3UL << [CPACR\_CP11\_Pos](#aedc603d4d2e20473426cf237efdf0a0f)) |

## Macro Definition Documentation

## [◆ ](#a9206df98746982fe6644162f551d7dfa)CPACR\_CP10\_FULL\_ACCESS

| #define CPACR\_CP10\_FULL\_ACCESS   (3UL << [CPACR\_CP10\_Pos](#a65fa7b1d26e122d7466d09d023dd03f5)) |
| --- |

## [◆ ](#aae47418d3f6f6596d74427d671db4568)CPACR\_CP10\_Msk

| #define CPACR\_CP10\_Msk   (3UL << [CPACR\_CP10\_Pos](#a65fa7b1d26e122d7466d09d023dd03f5)) |
| --- |

## [◆ ](#ab98d9a7803e01c9419a1b3db46ea1add)CPACR\_CP10\_NO\_ACCESS

| #define CPACR\_CP10\_NO\_ACCESS   (0UL << [CPACR\_CP10\_Pos](#a65fa7b1d26e122d7466d09d023dd03f5)) |
| --- |

## [◆ ](#a65fa7b1d26e122d7466d09d023dd03f5)CPACR\_CP10\_Pos

| #define CPACR\_CP10\_Pos   20U |
| --- |

## [◆ ](#aae2814998733c5960397fe122e1fd171)CPACR\_CP10\_PRIV\_ACCESS

| #define CPACR\_CP10\_PRIV\_ACCESS   (1UL << [CPACR\_CP10\_Pos](#a65fa7b1d26e122d7466d09d023dd03f5)) |
| --- |

## [◆ ](#a92b527c3d4f14132baac8726ab4df091)CPACR\_CP10\_RESERVED

| #define CPACR\_CP10\_RESERVED   (2UL << [CPACR\_CP10\_Pos](#a65fa7b1d26e122d7466d09d023dd03f5)) |
| --- |

## [◆ ](#a45e50725e2027dda6cbc5ca350d5d177)CPACR\_CP11\_FULL\_ACCESS

| #define CPACR\_CP11\_FULL\_ACCESS   (3UL << [CPACR\_CP11\_Pos](#aedc603d4d2e20473426cf237efdf0a0f)) |
| --- |

## [◆ ](#a48424c4ebf99120abe4887ca5f6445eb)CPACR\_CP11\_Msk

| #define CPACR\_CP11\_Msk   (3UL << [CPACR\_CP11\_Pos](#aedc603d4d2e20473426cf237efdf0a0f)) |
| --- |

## [◆ ](#a8994c5fdf0730b06c7a11846151eaa5f)CPACR\_CP11\_NO\_ACCESS

| #define CPACR\_CP11\_NO\_ACCESS   (0UL << [CPACR\_CP11\_Pos](#aedc603d4d2e20473426cf237efdf0a0f)) |
| --- |

## [◆ ](#aedc603d4d2e20473426cf237efdf0a0f)CPACR\_CP11\_Pos

| #define CPACR\_CP11\_Pos   22U |
| --- |

## [◆ ](#abcb053930af36f899c8d079fa80cbb6a)CPACR\_CP11\_PRIV\_ACCESS

| #define CPACR\_CP11\_PRIV\_ACCESS   (1UL << [CPACR\_CP11\_Pos](#aedc603d4d2e20473426cf237efdf0a0f)) |
| --- |

## [◆ ](#a8318babac72e1f7ee52b60cbf0c5975d)CPACR\_CP11\_RESERVED

| #define CPACR\_CP11\_RESERVED   (2UL << [CPACR\_CP11\_Pos](#aedc603d4d2e20473426cf237efdf0a0f)) |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [arch](dir_1a8d0ab52d1a59023360721fe35b1360.md)
- [arm](dir_e988120edb98a906db9f63ecbd85c0b4.md)
- [cortex\_m](dir_d27032cbfb87610ee5132d2bc57d6588.md)
- [cpu.h](include_2zephyr_2arch_2arm_2cortex__m_2cpu_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

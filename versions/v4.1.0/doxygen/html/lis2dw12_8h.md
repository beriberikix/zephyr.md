---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/lis2dw12_8h.html
original_path: doxygen/html/lis2dw12_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

lis2dw12.h File Reference

[Go to the source code of this file.](lis2dw12_8h_source.md)

| Macros | |
| --- | --- |
| #define | [LIS2DW12\_DT\_LP\_M1](#a0c03f55d1b6ebbf1d48e0c34d9122a74)   0 |
| #define | [LIS2DW12\_DT\_LP\_M2](#aeb6d34d3c11a1f3e7dc2cfe5f7405aae)   1 |
| #define | [LIS2DW12\_DT\_LP\_M3](#ab9ab746af6c8dfa384671ee313c7eea4)   2 |
| #define | [LIS2DW12\_DT\_LP\_M4](#ada20bc2633adb3ae955c2f709d727154)   3 |
| #define | [LIS2DW12\_DT\_HP\_MODE](#a0307502b4dee186f1945636c713eee4d)   4 |
| #define | [LIS2DW12\_DT\_FILTER\_BW\_ODR\_DIV\_2](#a88efe563d0f4d704773886d7670bea31)   0 |
| #define | [LIS2DW12\_DT\_FILTER\_BW\_ODR\_DIV\_4](#a4433ccc00389f58d30b9998b11915848)   1 |
| #define | [LIS2DW12\_DT\_FILTER\_BW\_ODR\_DIV\_10](#aad4197948abbd4587f6c9810f34e0c49)   2 |
| #define | [LIS2DW12\_DT\_FILTER\_BW\_ODR\_DIV\_20](#a9972d8b7618f39c9ddff273ecd80616a)   3 |
| #define | [LIS2DW12\_DT\_SINGLE\_TAP](#a71fc2ff7108bd85a86fd82c0ff002c18)   0 |
| #define | [LIS2DW12\_DT\_SINGLE\_DOUBLE\_TAP](#a4011203a9d243f9650cecab3d9ecf34d)   1 |
| #define | [LIS2DW12\_DT\_FF\_THRESHOLD\_156\_mg](#ac0420687b2a5ef0b886534b183d9b2f7)   0 |
| #define | [LIS2DW12\_DT\_FF\_THRESHOLD\_219\_mg](#a6afc0cf0328630c3bcdaf4cc579d8988)   1 |
| #define | [LIS2DW12\_DT\_FF\_THRESHOLD\_250\_mg](#a25b0e004ef448952083e417b0c77f97d)   2 |
| #define | [LIS2DW12\_DT\_FF\_THRESHOLD\_312\_mg](#a5ab3d56ad2ab84179316f3706780d716)   3 |
| #define | [LIS2DW12\_DT\_FF\_THRESHOLD\_344\_mg](#a429524e40340eb36610b7c0b4a449298)   4 |
| #define | [LIS2DW12\_DT\_FF\_THRESHOLD\_406\_mg](#a9a7a1520051a5b6107e6e0adbfb1d837)   5 |
| #define | [LIS2DW12\_DT\_FF\_THRESHOLD\_469\_mg](#ac336d6955333fc41ce21b9d68dfde4e5)   6 |
| #define | [LIS2DW12\_DT\_FF\_THRESHOLD\_500\_mg](#a7de449940954836ff3c48ef192662760)   7 |
| #define | [LIS2DW12\_DT\_WAKEUP\_1\_ODR](#a1bcffaa1b8439f626164b736be17f9db)   0 |
| #define | [LIS2DW12\_DT\_WAKEUP\_2\_ODR](#a53457e3a0d24bf3599ff779f3a559fb4)   1 |
| #define | [LIS2DW12\_DT\_WAKEUP\_3\_ODR](#a580dd3e03a377fce36db7916c254b52a)   2 |
| #define | [LIS2DW12\_DT\_WAKEUP\_4\_ODR](#aae58921652443e8f7757b38ade589c49)   3 |
| #define | [LIS2DW12\_DT\_SLEEP\_0\_ODR](#aa9df8cef65e33e117a8de9eb2df745c3)   0 |
| #define | [LIS2DW12\_DT\_SLEEP\_1\_ODR](#af43f42617789c1482e1ddf1d9abd7c3d)   1 |
| #define | [LIS2DW12\_DT\_SLEEP\_2\_ODR](#a6c76600bf9baff0483d5865ba98aa75e)   2 |
| #define | [LIS2DW12\_DT\_SLEEP\_3\_ODR](#af294baab225caba1e4931abfee9660b8)   3 |
| #define | [LIS2DW12\_DT\_SLEEP\_4\_ODR](#ac45de707e5c1ee485b5cdd95ce3332af)   4 |
| #define | [LIS2DW12\_DT\_SLEEP\_5\_ODR](#a904ec47239d01ac05218bee5fa2f4235)   5 |
| #define | [LIS2DW12\_DT\_SLEEP\_6\_ODR](#a552a71243df2cfe6dcc6f9ca5a4208c9)   6 |
| #define | [LIS2DW12\_DT\_SLEEP\_7\_ODR](#a72ced204873bfce192b6bcfc9d823ffc)   7 |
| #define | [LIS2DW12\_DT\_SLEEP\_8\_ODR](#a9078b4d1fa77dd53871ddbc7715b3f0c)   8 |
| #define | [LIS2DW12\_DT\_SLEEP\_9\_ODR](#a979e47f3dda9c72b92d87bb3fc5b3e4f)   9 |
| #define | [LIS2DW12\_DT\_SLEEP\_10\_ODR](#a15982beb9fce8268a056fb2f088f6724)   10 |
| #define | [LIS2DW12\_DT\_SLEEP\_11\_ODR](#ad3546f54d5eee5d7d9cb9318a6104a9c)   11 |
| #define | [LIS2DW12\_DT\_SLEEP\_12\_ODR](#a97614b907ca69fd13f0e8a9b61e15904)   12 |
| #define | [LIS2DW12\_DT\_SLEEP\_13\_ODR](#abff45bcd009134ee4da471e9e915584a)   13 |
| #define | [LIS2DW12\_DT\_SLEEP\_14\_ODR](#a8ba46d92426bf168d6b9da5acee6668f)   14 |
| #define | [LIS2DW12\_DT\_SLEEP\_15\_ODR](#a39ddac85ed26346de4272157ce2533a8)   15 |

## Macro Definition Documentation

## [◆ ](#ac0420687b2a5ef0b886534b183d9b2f7)LIS2DW12\_DT\_FF\_THRESHOLD\_156\_mg

| #define LIS2DW12\_DT\_FF\_THRESHOLD\_156\_mg   0 |
| --- |

## [◆ ](#a6afc0cf0328630c3bcdaf4cc579d8988)LIS2DW12\_DT\_FF\_THRESHOLD\_219\_mg

| #define LIS2DW12\_DT\_FF\_THRESHOLD\_219\_mg   1 |
| --- |

## [◆ ](#a25b0e004ef448952083e417b0c77f97d)LIS2DW12\_DT\_FF\_THRESHOLD\_250\_mg

| #define LIS2DW12\_DT\_FF\_THRESHOLD\_250\_mg   2 |
| --- |

## [◆ ](#a5ab3d56ad2ab84179316f3706780d716)LIS2DW12\_DT\_FF\_THRESHOLD\_312\_mg

| #define LIS2DW12\_DT\_FF\_THRESHOLD\_312\_mg   3 |
| --- |

## [◆ ](#a429524e40340eb36610b7c0b4a449298)LIS2DW12\_DT\_FF\_THRESHOLD\_344\_mg

| #define LIS2DW12\_DT\_FF\_THRESHOLD\_344\_mg   4 |
| --- |

## [◆ ](#a9a7a1520051a5b6107e6e0adbfb1d837)LIS2DW12\_DT\_FF\_THRESHOLD\_406\_mg

| #define LIS2DW12\_DT\_FF\_THRESHOLD\_406\_mg   5 |
| --- |

## [◆ ](#ac336d6955333fc41ce21b9d68dfde4e5)LIS2DW12\_DT\_FF\_THRESHOLD\_469\_mg

| #define LIS2DW12\_DT\_FF\_THRESHOLD\_469\_mg   6 |
| --- |

## [◆ ](#a7de449940954836ff3c48ef192662760)LIS2DW12\_DT\_FF\_THRESHOLD\_500\_mg

| #define LIS2DW12\_DT\_FF\_THRESHOLD\_500\_mg   7 |
| --- |

## [◆ ](#aad4197948abbd4587f6c9810f34e0c49)LIS2DW12\_DT\_FILTER\_BW\_ODR\_DIV\_10

| #define LIS2DW12\_DT\_FILTER\_BW\_ODR\_DIV\_10   2 |
| --- |

## [◆ ](#a88efe563d0f4d704773886d7670bea31)LIS2DW12\_DT\_FILTER\_BW\_ODR\_DIV\_2

| #define LIS2DW12\_DT\_FILTER\_BW\_ODR\_DIV\_2   0 |
| --- |

## [◆ ](#a9972d8b7618f39c9ddff273ecd80616a)LIS2DW12\_DT\_FILTER\_BW\_ODR\_DIV\_20

| #define LIS2DW12\_DT\_FILTER\_BW\_ODR\_DIV\_20   3 |
| --- |

## [◆ ](#a4433ccc00389f58d30b9998b11915848)LIS2DW12\_DT\_FILTER\_BW\_ODR\_DIV\_4

| #define LIS2DW12\_DT\_FILTER\_BW\_ODR\_DIV\_4   1 |
| --- |

## [◆ ](#a0307502b4dee186f1945636c713eee4d)LIS2DW12\_DT\_HP\_MODE

| #define LIS2DW12\_DT\_HP\_MODE   4 |
| --- |

## [◆ ](#a0c03f55d1b6ebbf1d48e0c34d9122a74)LIS2DW12\_DT\_LP\_M1

| #define LIS2DW12\_DT\_LP\_M1   0 |
| --- |

## [◆ ](#aeb6d34d3c11a1f3e7dc2cfe5f7405aae)LIS2DW12\_DT\_LP\_M2

| #define LIS2DW12\_DT\_LP\_M2   1 |
| --- |

## [◆ ](#ab9ab746af6c8dfa384671ee313c7eea4)LIS2DW12\_DT\_LP\_M3

| #define LIS2DW12\_DT\_LP\_M3   2 |
| --- |

## [◆ ](#ada20bc2633adb3ae955c2f709d727154)LIS2DW12\_DT\_LP\_M4

| #define LIS2DW12\_DT\_LP\_M4   3 |
| --- |

## [◆ ](#a4011203a9d243f9650cecab3d9ecf34d)LIS2DW12\_DT\_SINGLE\_DOUBLE\_TAP

| #define LIS2DW12\_DT\_SINGLE\_DOUBLE\_TAP   1 |
| --- |

## [◆ ](#a71fc2ff7108bd85a86fd82c0ff002c18)LIS2DW12\_DT\_SINGLE\_TAP

| #define LIS2DW12\_DT\_SINGLE\_TAP   0 |
| --- |

## [◆ ](#aa9df8cef65e33e117a8de9eb2df745c3)LIS2DW12\_DT\_SLEEP\_0\_ODR

| #define LIS2DW12\_DT\_SLEEP\_0\_ODR   0 |
| --- |

## [◆ ](#a15982beb9fce8268a056fb2f088f6724)LIS2DW12\_DT\_SLEEP\_10\_ODR

| #define LIS2DW12\_DT\_SLEEP\_10\_ODR   10 |
| --- |

## [◆ ](#ad3546f54d5eee5d7d9cb9318a6104a9c)LIS2DW12\_DT\_SLEEP\_11\_ODR

| #define LIS2DW12\_DT\_SLEEP\_11\_ODR   11 |
| --- |

## [◆ ](#a97614b907ca69fd13f0e8a9b61e15904)LIS2DW12\_DT\_SLEEP\_12\_ODR

| #define LIS2DW12\_DT\_SLEEP\_12\_ODR   12 |
| --- |

## [◆ ](#abff45bcd009134ee4da471e9e915584a)LIS2DW12\_DT\_SLEEP\_13\_ODR

| #define LIS2DW12\_DT\_SLEEP\_13\_ODR   13 |
| --- |

## [◆ ](#a8ba46d92426bf168d6b9da5acee6668f)LIS2DW12\_DT\_SLEEP\_14\_ODR

| #define LIS2DW12\_DT\_SLEEP\_14\_ODR   14 |
| --- |

## [◆ ](#a39ddac85ed26346de4272157ce2533a8)LIS2DW12\_DT\_SLEEP\_15\_ODR

| #define LIS2DW12\_DT\_SLEEP\_15\_ODR   15 |
| --- |

## [◆ ](#af43f42617789c1482e1ddf1d9abd7c3d)LIS2DW12\_DT\_SLEEP\_1\_ODR

| #define LIS2DW12\_DT\_SLEEP\_1\_ODR   1 |
| --- |

## [◆ ](#a6c76600bf9baff0483d5865ba98aa75e)LIS2DW12\_DT\_SLEEP\_2\_ODR

| #define LIS2DW12\_DT\_SLEEP\_2\_ODR   2 |
| --- |

## [◆ ](#af294baab225caba1e4931abfee9660b8)LIS2DW12\_DT\_SLEEP\_3\_ODR

| #define LIS2DW12\_DT\_SLEEP\_3\_ODR   3 |
| --- |

## [◆ ](#ac45de707e5c1ee485b5cdd95ce3332af)LIS2DW12\_DT\_SLEEP\_4\_ODR

| #define LIS2DW12\_DT\_SLEEP\_4\_ODR   4 |
| --- |

## [◆ ](#a904ec47239d01ac05218bee5fa2f4235)LIS2DW12\_DT\_SLEEP\_5\_ODR

| #define LIS2DW12\_DT\_SLEEP\_5\_ODR   5 |
| --- |

## [◆ ](#a552a71243df2cfe6dcc6f9ca5a4208c9)LIS2DW12\_DT\_SLEEP\_6\_ODR

| #define LIS2DW12\_DT\_SLEEP\_6\_ODR   6 |
| --- |

## [◆ ](#a72ced204873bfce192b6bcfc9d823ffc)LIS2DW12\_DT\_SLEEP\_7\_ODR

| #define LIS2DW12\_DT\_SLEEP\_7\_ODR   7 |
| --- |

## [◆ ](#a9078b4d1fa77dd53871ddbc7715b3f0c)LIS2DW12\_DT\_SLEEP\_8\_ODR

| #define LIS2DW12\_DT\_SLEEP\_8\_ODR   8 |
| --- |

## [◆ ](#a979e47f3dda9c72b92d87bb3fc5b3e4f)LIS2DW12\_DT\_SLEEP\_9\_ODR

| #define LIS2DW12\_DT\_SLEEP\_9\_ODR   9 |
| --- |

## [◆ ](#a1bcffaa1b8439f626164b736be17f9db)LIS2DW12\_DT\_WAKEUP\_1\_ODR

| #define LIS2DW12\_DT\_WAKEUP\_1\_ODR   0 |
| --- |

## [◆ ](#a53457e3a0d24bf3599ff779f3a559fb4)LIS2DW12\_DT\_WAKEUP\_2\_ODR

| #define LIS2DW12\_DT\_WAKEUP\_2\_ODR   1 |
| --- |

## [◆ ](#a580dd3e03a377fce36db7916c254b52a)LIS2DW12\_DT\_WAKEUP\_3\_ODR

| #define LIS2DW12\_DT\_WAKEUP\_3\_ODR   2 |
| --- |

## [◆ ](#aae58921652443e8f7757b38ade589c49)LIS2DW12\_DT\_WAKEUP\_4\_ODR

| #define LIS2DW12\_DT\_WAKEUP\_4\_ODR   3 |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [sensor](dir_c9b2d7ff2bbb57ff9b1854f820609711.md)
- [lis2dw12.h](lis2dw12_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

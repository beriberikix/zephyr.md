---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/nrf__lpcomp_8h.html
original_path: doxygen/html/nrf__lpcomp_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

nrf\_lpcomp.h File Reference

`#include <[zephyr/drivers/comparator.h](comparator_8h_source.md)>`

[Go to the source code of this file.](nrf__lpcomp_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [comp\_nrf\_lpcomp\_config](structcomp__nrf__lpcomp__config.md) |
|  | Configuration structure. [More...](structcomp__nrf__lpcomp__config.md#details) |

| Enumerations | |
| --- | --- |
| enum | [comp\_nrf\_lpcomp\_psel](#af1c88d0e254866b05c344b50a2574582) {     [COMP\_NRF\_LPCOMP\_PSEL\_AIN0](#af1c88d0e254866b05c344b50a2574582afdfa8c7afaedabfa6d66379d717c8230) , [COMP\_NRF\_LPCOMP\_PSEL\_AIN1](#af1c88d0e254866b05c344b50a2574582aff42e45ad33b6be0acb2b2db5f5517d8) , [COMP\_NRF\_LPCOMP\_PSEL\_AIN2](#af1c88d0e254866b05c344b50a2574582a9e485565e0f600538314af0b140ee8ed) , [COMP\_NRF\_LPCOMP\_PSEL\_AIN3](#af1c88d0e254866b05c344b50a2574582a93ec605b4475653e3eee896ed9de6791) ,     [COMP\_NRF\_LPCOMP\_PSEL\_AIN4](#af1c88d0e254866b05c344b50a2574582aa40f5844c344870a65db0768516d821d) , [COMP\_NRF\_LPCOMP\_PSEL\_AIN5](#af1c88d0e254866b05c344b50a2574582a550f58b7541368c722af8dfe575f49a0) , [COMP\_NRF\_LPCOMP\_PSEL\_AIN6](#af1c88d0e254866b05c344b50a2574582a0032da62c7b68dc91cfab011838a23bd) , [COMP\_NRF\_LPCOMP\_PSEL\_AIN7](#af1c88d0e254866b05c344b50a2574582aab8c5a2ccbb98de807f020d4b47eb35e)   } |
|  | Positive input selection. [More...](#af1c88d0e254866b05c344b50a2574582) |
| enum | [comp\_nrf\_lpcomp\_extrefsel](#ab150e9043eca4b0b4ce7ace4317e1b21) { [COMP\_NRF\_LPCOMP\_EXTREFSEL\_AIN0](#ab150e9043eca4b0b4ce7ace4317e1b21a5a95781545b3b3cfbbe22f4313199df2) , [COMP\_NRF\_LPCOMP\_EXTREFSEL\_AIN1](#ab150e9043eca4b0b4ce7ace4317e1b21a1581658dd7f77da5278119959f93af4a) } |
|  | External reference selection. [More...](#ab150e9043eca4b0b4ce7ace4317e1b21) |
| enum | [comp\_nrf\_lpcomp\_refsel](#ae42326afcd4f5435480f80d382266a04) {     [COMP\_NRF\_LPCOMP\_REFSEL\_VDD\_1\_8](#ae42326afcd4f5435480f80d382266a04a99627f00ae3182014da516333f64705f) , [COMP\_NRF\_LPCOMP\_REFSEL\_VDD\_2\_8](#ae42326afcd4f5435480f80d382266a04a3c10840415f3aed4d0b8414a6decf56d) , [COMP\_NRF\_LPCOMP\_REFSEL\_VDD\_3\_8](#ae42326afcd4f5435480f80d382266a04a25c009efcddd2e84417d115b5f4e346e) , [COMP\_NRF\_LPCOMP\_REFSEL\_VDD\_4\_8](#ae42326afcd4f5435480f80d382266a04a848e512c3223a019f6ec59612616fe33) ,     [COMP\_NRF\_LPCOMP\_REFSEL\_VDD\_5\_8](#ae42326afcd4f5435480f80d382266a04a295352a4ecb28f6288efe33fd0c49526) , [COMP\_NRF\_LPCOMP\_REFSEL\_VDD\_6\_8](#ae42326afcd4f5435480f80d382266a04a624b842d3ef6e8fa172412fc3a06dd1a) , [COMP\_NRF\_LPCOMP\_REFSEL\_VDD\_7\_8](#ae42326afcd4f5435480f80d382266a04a2b1cd929103b9af8ef372472078efb76) , [COMP\_NRF\_LPCOMP\_REFSEL\_VDD\_1\_16](#ae42326afcd4f5435480f80d382266a04acd4c60e604696b7d24028ad9e98d77f3) ,     [COMP\_NRF\_LPCOMP\_REFSEL\_VDD\_3\_16](#ae42326afcd4f5435480f80d382266a04a3b3760b0298de0fcb94812f98433ba16) , [COMP\_NRF\_LPCOMP\_REFSEL\_VDD\_5\_16](#ae42326afcd4f5435480f80d382266a04a94a97a641eaa3dc25b09d00dda8fb137) , [COMP\_NRF\_LPCOMP\_REFSEL\_VDD\_7\_16](#ae42326afcd4f5435480f80d382266a04a98def2c5d100c1c51c697203606b66dd) , [COMP\_NRF\_LPCOMP\_REFSEL\_VDD\_9\_16](#ae42326afcd4f5435480f80d382266a04aa62402dda42b69bd974de3f19aa4a509) ,     [COMP\_NRF\_LPCOMP\_REFSEL\_VDD\_11\_16](#ae42326afcd4f5435480f80d382266a04a9913bfd70d57767e295ced6e7287a7bb) , [COMP\_NRF\_LPCOMP\_REFSEL\_VDD\_13\_16](#ae42326afcd4f5435480f80d382266a04a930ce822163d6654cda439e43fbbaab1) , [COMP\_NRF\_LPCOMP\_REFSEL\_VDD\_15\_16](#ae42326afcd4f5435480f80d382266a04aade5263dc54bd126f9a761e0188b13f7) , [COMP\_NRF\_LPCOMP\_REFSEL\_AREF](#ae42326afcd4f5435480f80d382266a04abf717bfb0610352e60d4f4fc45a370b1)   } |
|  | Reference selection. [More...](#ae42326afcd4f5435480f80d382266a04) |

| Functions | |
| --- | --- |
| int | [comp\_nrf\_lpcomp\_configure](#aff748ac1a1a8c13796b81ef789b4c7f2) (const struct [device](structdevice.md) \*dev, const struct [comp\_nrf\_lpcomp\_config](structcomp__nrf__lpcomp__config.md) \*config) |
|  | Configure comparator. |

## Enumeration Type Documentation

## [◆ ](#ab150e9043eca4b0b4ce7ace4317e1b21)comp\_nrf\_lpcomp\_extrefsel

| enum [comp\_nrf\_lpcomp\_extrefsel](#ab150e9043eca4b0b4ce7ace4317e1b21) |
| --- |

External reference selection.

| Enumerator | |
| --- | --- |
| COMP\_NRF\_LPCOMP\_EXTREFSEL\_AIN0 | AIN0 external input. |
| COMP\_NRF\_LPCOMP\_EXTREFSEL\_AIN1 | AIN1 external input. |

## [◆ ](#af1c88d0e254866b05c344b50a2574582)comp\_nrf\_lpcomp\_psel

| enum [comp\_nrf\_lpcomp\_psel](#af1c88d0e254866b05c344b50a2574582) |
| --- |

Positive input selection.

| Enumerator | |
| --- | --- |
| COMP\_NRF\_LPCOMP\_PSEL\_AIN0 | AIN0 external input. |
| COMP\_NRF\_LPCOMP\_PSEL\_AIN1 | AIN1 external input. |
| COMP\_NRF\_LPCOMP\_PSEL\_AIN2 | AIN2 external input. |
| COMP\_NRF\_LPCOMP\_PSEL\_AIN3 | AIN3 external input. |
| COMP\_NRF\_LPCOMP\_PSEL\_AIN4 | AIN4 external input. |
| COMP\_NRF\_LPCOMP\_PSEL\_AIN5 | AIN5 external input. |
| COMP\_NRF\_LPCOMP\_PSEL\_AIN6 | AIN6 external input. |
| COMP\_NRF\_LPCOMP\_PSEL\_AIN7 | AIN7 external input. |

## [◆ ](#ae42326afcd4f5435480f80d382266a04)comp\_nrf\_lpcomp\_refsel

| enum [comp\_nrf\_lpcomp\_refsel](#ae42326afcd4f5435480f80d382266a04) |
| --- |

Reference selection.

| Enumerator | |
| --- | --- |
| COMP\_NRF\_LPCOMP\_REFSEL\_VDD\_1\_8 | Use (VDD \* (1/8)) as reference. |
| COMP\_NRF\_LPCOMP\_REFSEL\_VDD\_2\_8 | Use (VDD \* (2/8)) as reference. |
| COMP\_NRF\_LPCOMP\_REFSEL\_VDD\_3\_8 | Use (VDD \* (3/8)) as reference. |
| COMP\_NRF\_LPCOMP\_REFSEL\_VDD\_4\_8 | Use (VDD \* (4/8)) as reference. |
| COMP\_NRF\_LPCOMP\_REFSEL\_VDD\_5\_8 | Use (VDD \* (5/8)) as reference. |
| COMP\_NRF\_LPCOMP\_REFSEL\_VDD\_6\_8 | Use (VDD \* (6/8)) as reference. |
| COMP\_NRF\_LPCOMP\_REFSEL\_VDD\_7\_8 | Use (VDD \* (7/8)) as reference. |
| COMP\_NRF\_LPCOMP\_REFSEL\_VDD\_1\_16 | Use (VDD \* (1/16)) as reference. |
| COMP\_NRF\_LPCOMP\_REFSEL\_VDD\_3\_16 | Use (VDD \* (3/16)) as reference. |
| COMP\_NRF\_LPCOMP\_REFSEL\_VDD\_5\_16 | Use (VDD \* (5/16)) as reference. |
| COMP\_NRF\_LPCOMP\_REFSEL\_VDD\_7\_16 | Use (VDD \* (7/16)) as reference. |
| COMP\_NRF\_LPCOMP\_REFSEL\_VDD\_9\_16 | Use (VDD \* (9/16)) as reference. |
| COMP\_NRF\_LPCOMP\_REFSEL\_VDD\_11\_16 | Use (VDD \* (11/16)) as reference. |
| COMP\_NRF\_LPCOMP\_REFSEL\_VDD\_13\_16 | Use (VDD \* (13/16)) as reference. |
| COMP\_NRF\_LPCOMP\_REFSEL\_VDD\_15\_16 | Use (VDD \* (15/16)) as reference. |
| COMP\_NRF\_LPCOMP\_REFSEL\_AREF | Use external analog reference. |

## Function Documentation

## [◆ ](#aff748ac1a1a8c13796b81ef789b4c7f2)comp\_nrf\_lpcomp\_configure()

| int comp\_nrf\_lpcomp\_configure | ( | const struct [device](structdevice.md) \* | *dev*, |
| --- | --- | --- | --- |
|  |  | const struct [comp\_nrf\_lpcomp\_config](structcomp__nrf__lpcomp__config.md) \* | *config* ) |

Configure comparator.

Parameters
:   | dev | Comparator device instance |
    | --- | --- |
    | config | Configuration |

Return values
:   | 0 | if successful |
    | --- | --- |
    | negative | errno-code otherwise |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [comparator](dir_25be445c737a80f4854b3956f06e1693.md)
- [nrf\_lpcomp.h](nrf__lpcomp_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

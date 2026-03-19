---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/esp32c2__clock_8h.html
original_path: doxygen/html/esp32c2__clock_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

esp32c2\_clock.h File Reference

[Go to the source code of this file.](esp32c2__clock_8h_source.md)

| Macros | |
| --- | --- |
| #define | [ESP32\_CPU\_CLK\_SRC\_XTAL](#a44ee3670c3168dd0ffbc79a563a7f074)   0U |
| #define | [ESP32\_CPU\_CLK\_SRC\_PLL](#a7a723b6353a23b55ef44d720297fe26f)   1U |
| #define | [ESP32\_CLK\_SRC\_RC\_FAST](#a1962dad90f737a51fcc70cea1931b236)   2U |
| #define | [ESP32\_CLK\_CPU\_PLL\_40M](#aa61a2254926bfec49b2eb959f307ff30)   40000000 |
| #define | [ESP32\_CLK\_CPU\_PLL\_60M](#af817a387d83b343413616ee4eaa73bc4)   60000000 |
| #define | [ESP32\_CLK\_CPU\_PLL\_80M](#a61275f95111fb2a6bdbe446c0228f877)   80000000 |
| #define | [ESP32\_CLK\_CPU\_PLL\_120M](#a31d4aba38136e01b31ff34c81b08256e)   120000000 |
| #define | [ESP32\_CLK\_CPU\_RC\_FAST\_FREQ](#ab779f427209fda571ec4d229b8ef8bfc)   8750000 |
| #define | [ESP32\_CLK\_XTAL\_26M](#a06efe791ed749209eb07de5066c6eddc)   26000000 |
| #define | [ESP32\_CLK\_XTAL\_32M](#aeb5c606e77a85fa858ab7af6061c7949)   32000000 |
| #define | [ESP32\_CLK\_XTAL\_40M](#a6afe38f9f9c44a1bd2e5279163523a98)   40000000 |
| #define | [ESP32\_RTC\_FAST\_CLK\_SRC\_XTAL\_D2](#a725193bf445b7f8f2c1058a6735ca476)   0 |
| #define | [ESP32\_RTC\_FAST\_CLK\_SRC\_RC\_FAST](#aae48d9f1288771e11c11d6177ecf3af7)   1 |
| #define | [ESP32\_RTC\_SLOW\_CLK\_SRC\_RC\_SLOW](#ad1d90df80dee3040dbe8c968cd774443)   0 |
| #define | [ESP32\_RTC\_SLOW\_CLK\_SRC\_OSC\_SLOW](#a0c9ed1e9c69731554227e93ddd086e9e)   1 |
| #define | [ESP32\_RTC\_SLOW\_CLK\_SRC\_RC\_FAST\_D256](#aaec50946dbdaabaf2199e795a389634e)   2 |
| #define | [ESP32\_RTC\_SLOW\_CLK\_SRC\_RC\_SLOW\_FREQ](#af5cdcfa17e680ceda2f90e375eded6e6)   136000 |
| #define | [ESP32\_RTC\_SLOW\_CLK\_SRC\_OSC\_SLOW\_FREQ](#ab3d6d4b49e506dac9b7812b9abd30a82)   32768 |
| #define | [ESP32\_RTC\_SLOW\_CLK\_SRC\_RC\_FAST\_D256\_FREQ](#a8531ee06161cae4ea8516d00825c32c8)   68359 |
| #define | [ESP32\_LEDC\_MODULE](#a60f4f5ee56d788f2161b52ebbc2aa510)   0 |
| #define | [ESP32\_UART0\_MODULE](#a9708d046fbadfb7ccbc5df3e0ae57844)   1 |
| #define | [ESP32\_UART1\_MODULE](#a480803130ef80df04527f4dd12525d48)   2 |
| #define | [ESP32\_I2C0\_MODULE](#a7331ffa2ec41896d05f1f86c4d30f758)   3 |
| #define | [ESP32\_TIMG0\_MODULE](#a88ae2c1bafdc6e78258ada5cbb9368f9)   4 |
| #define | [ESP32\_TIMG1\_MODULE](#a251462caa49fc6fe0ae1c8fe99a87caa)   5 /\* No timg1 on esp32c2, TODO: IDF-3825 \*/ |
| #define | [ESP32\_UHCI0\_MODULE](#af5ef985d4eaf1ffe565e2662493178c6)   6 |
| #define | [ESP32\_SPI\_MODULE](#a5652d0e2b1fc766dde13b84294d4576b)   7 /\* SPI1 \*/ |
| #define | [ESP32\_SPI2\_MODULE](#a5e5283c23811e9c4f30980f1d865773b)   8 /\* SPI2 \*/ |
| #define | [ESP32\_RNG\_MODULE](#ad5423ca02819aab6b3fe63c11b3cf998)   9 |
| #define | [ESP32\_WIFI\_MODULE](#a4013c1fc7538bf46d5c1771f837a8b21)   10 |
| #define | [ESP32\_BT\_MODULE](#ad180ebcea5567ce6c3145998f3761584)   11 |
| #define | [ESP32\_WIFI\_BT\_COMMON\_MODULE](#aba1295479849f8b4dc44245e330e3020)   12 |
| #define | [ESP32\_BT\_BASEBAND\_MODULE](#a653e6d1f91c532b3ba313be27a97c2af)   13 |
| #define | [ESP32\_BT\_LC\_MODULE](#a8e27f45346390d8909f9424f13280b76)   14 |
| #define | [ESP32\_AES\_MODULE](#a290ac6ab6c5de2e8d84a911e389e1cfc)   15 |
| #define | [ESP32\_SHA\_MODULE](#a683dd8814bf170018b63b57268c0fde9)   16 |
| #define | [ESP32\_ECC\_MODULE](#a27bd450bf21c8b7502d1f32d9536129f)   17 |
| #define | [ESP32\_GDMA\_MODULE](#a701fec66fac239e66a19389ea153ff75)   18 |
| #define | [ESP32\_SYSTIMER\_MODULE](#aaf8e1de1e86906ba539863b9009ebe37)   19 |
| #define | [ESP32\_SARADC\_MODULE](#abe244da38fbe794e93094feef9b188fe)   20 |
| #define | [ESP32\_TEMPSENSOR\_MODULE](#a488d6d32cf66e81a27f0999f837fe39a)   21 |
| #define | [ESP32\_MODEM\_RPA\_MODULE](#a65f83f03cf7bdda167c25d3bb283f99b)   22 |
| #define | [ESP32\_MODULE\_MAX](#ac380a7ff843ee465763a355cb01ef295)   23 |

## Macro Definition Documentation

## [◆ ](#a290ac6ab6c5de2e8d84a911e389e1cfc)ESP32\_AES\_MODULE

| #define ESP32\_AES\_MODULE   15 |
| --- |

## [◆ ](#a653e6d1f91c532b3ba313be27a97c2af)ESP32\_BT\_BASEBAND\_MODULE

| #define ESP32\_BT\_BASEBAND\_MODULE   13 |
| --- |

## [◆ ](#a8e27f45346390d8909f9424f13280b76)ESP32\_BT\_LC\_MODULE

| #define ESP32\_BT\_LC\_MODULE   14 |
| --- |

## [◆ ](#ad180ebcea5567ce6c3145998f3761584)ESP32\_BT\_MODULE

| #define ESP32\_BT\_MODULE   11 |
| --- |

## [◆ ](#a31d4aba38136e01b31ff34c81b08256e)ESP32\_CLK\_CPU\_PLL\_120M

| #define ESP32\_CLK\_CPU\_PLL\_120M   120000000 |
| --- |

## [◆ ](#aa61a2254926bfec49b2eb959f307ff30)ESP32\_CLK\_CPU\_PLL\_40M

| #define ESP32\_CLK\_CPU\_PLL\_40M   40000000 |
| --- |

## [◆ ](#af817a387d83b343413616ee4eaa73bc4)ESP32\_CLK\_CPU\_PLL\_60M

| #define ESP32\_CLK\_CPU\_PLL\_60M   60000000 |
| --- |

## [◆ ](#a61275f95111fb2a6bdbe446c0228f877)ESP32\_CLK\_CPU\_PLL\_80M

| #define ESP32\_CLK\_CPU\_PLL\_80M   80000000 |
| --- |

## [◆ ](#ab779f427209fda571ec4d229b8ef8bfc)ESP32\_CLK\_CPU\_RC\_FAST\_FREQ

| #define ESP32\_CLK\_CPU\_RC\_FAST\_FREQ   8750000 |
| --- |

## [◆ ](#a1962dad90f737a51fcc70cea1931b236)ESP32\_CLK\_SRC\_RC\_FAST

| #define ESP32\_CLK\_SRC\_RC\_FAST   2U |
| --- |

## [◆ ](#a06efe791ed749209eb07de5066c6eddc)ESP32\_CLK\_XTAL\_26M

| #define ESP32\_CLK\_XTAL\_26M   26000000 |
| --- |

## [◆ ](#aeb5c606e77a85fa858ab7af6061c7949)ESP32\_CLK\_XTAL\_32M

| #define ESP32\_CLK\_XTAL\_32M   32000000 |
| --- |

## [◆ ](#a6afe38f9f9c44a1bd2e5279163523a98)ESP32\_CLK\_XTAL\_40M

| #define ESP32\_CLK\_XTAL\_40M   40000000 |
| --- |

## [◆ ](#a7a723b6353a23b55ef44d720297fe26f)ESP32\_CPU\_CLK\_SRC\_PLL

| #define ESP32\_CPU\_CLK\_SRC\_PLL   1U |
| --- |

## [◆ ](#a44ee3670c3168dd0ffbc79a563a7f074)ESP32\_CPU\_CLK\_SRC\_XTAL

| #define ESP32\_CPU\_CLK\_SRC\_XTAL   0U |
| --- |

## [◆ ](#a27bd450bf21c8b7502d1f32d9536129f)ESP32\_ECC\_MODULE

| #define ESP32\_ECC\_MODULE   17 |
| --- |

## [◆ ](#a701fec66fac239e66a19389ea153ff75)ESP32\_GDMA\_MODULE

| #define ESP32\_GDMA\_MODULE   18 |
| --- |

## [◆ ](#a7331ffa2ec41896d05f1f86c4d30f758)ESP32\_I2C0\_MODULE

| #define ESP32\_I2C0\_MODULE   3 |
| --- |

## [◆ ](#a60f4f5ee56d788f2161b52ebbc2aa510)ESP32\_LEDC\_MODULE

| #define ESP32\_LEDC\_MODULE   0 |
| --- |

## [◆ ](#a65f83f03cf7bdda167c25d3bb283f99b)ESP32\_MODEM\_RPA\_MODULE

| #define ESP32\_MODEM\_RPA\_MODULE   22 |
| --- |

## [◆ ](#ac380a7ff843ee465763a355cb01ef295)ESP32\_MODULE\_MAX

| #define ESP32\_MODULE\_MAX   23 |
| --- |

## [◆ ](#ad5423ca02819aab6b3fe63c11b3cf998)ESP32\_RNG\_MODULE

| #define ESP32\_RNG\_MODULE   9 |
| --- |

## [◆ ](#aae48d9f1288771e11c11d6177ecf3af7)ESP32\_RTC\_FAST\_CLK\_SRC\_RC\_FAST

| #define ESP32\_RTC\_FAST\_CLK\_SRC\_RC\_FAST   1 |
| --- |

## [◆ ](#a725193bf445b7f8f2c1058a6735ca476)ESP32\_RTC\_FAST\_CLK\_SRC\_XTAL\_D2

| #define ESP32\_RTC\_FAST\_CLK\_SRC\_XTAL\_D2   0 |
| --- |

## [◆ ](#a0c9ed1e9c69731554227e93ddd086e9e)ESP32\_RTC\_SLOW\_CLK\_SRC\_OSC\_SLOW

| #define ESP32\_RTC\_SLOW\_CLK\_SRC\_OSC\_SLOW   1 |
| --- |

## [◆ ](#ab3d6d4b49e506dac9b7812b9abd30a82)ESP32\_RTC\_SLOW\_CLK\_SRC\_OSC\_SLOW\_FREQ

| #define ESP32\_RTC\_SLOW\_CLK\_SRC\_OSC\_SLOW\_FREQ   32768 |
| --- |

## [◆ ](#aaec50946dbdaabaf2199e795a389634e)ESP32\_RTC\_SLOW\_CLK\_SRC\_RC\_FAST\_D256

| #define ESP32\_RTC\_SLOW\_CLK\_SRC\_RC\_FAST\_D256   2 |
| --- |

## [◆ ](#a8531ee06161cae4ea8516d00825c32c8)ESP32\_RTC\_SLOW\_CLK\_SRC\_RC\_FAST\_D256\_FREQ

| #define ESP32\_RTC\_SLOW\_CLK\_SRC\_RC\_FAST\_D256\_FREQ   68359 |
| --- |

## [◆ ](#ad1d90df80dee3040dbe8c968cd774443)ESP32\_RTC\_SLOW\_CLK\_SRC\_RC\_SLOW

| #define ESP32\_RTC\_SLOW\_CLK\_SRC\_RC\_SLOW   0 |
| --- |

## [◆ ](#af5cdcfa17e680ceda2f90e375eded6e6)ESP32\_RTC\_SLOW\_CLK\_SRC\_RC\_SLOW\_FREQ

| #define ESP32\_RTC\_SLOW\_CLK\_SRC\_RC\_SLOW\_FREQ   136000 |
| --- |

## [◆ ](#abe244da38fbe794e93094feef9b188fe)ESP32\_SARADC\_MODULE

| #define ESP32\_SARADC\_MODULE   20 |
| --- |

## [◆ ](#a683dd8814bf170018b63b57268c0fde9)ESP32\_SHA\_MODULE

| #define ESP32\_SHA\_MODULE   16 |
| --- |

## [◆ ](#a5e5283c23811e9c4f30980f1d865773b)ESP32\_SPI2\_MODULE

| #define ESP32\_SPI2\_MODULE   8 /\* SPI2 \*/ |
| --- |

## [◆ ](#a5652d0e2b1fc766dde13b84294d4576b)ESP32\_SPI\_MODULE

| #define ESP32\_SPI\_MODULE   7 /\* SPI1 \*/ |
| --- |

## [◆ ](#aaf8e1de1e86906ba539863b9009ebe37)ESP32\_SYSTIMER\_MODULE

| #define ESP32\_SYSTIMER\_MODULE   19 |
| --- |

## [◆ ](#a488d6d32cf66e81a27f0999f837fe39a)ESP32\_TEMPSENSOR\_MODULE

| #define ESP32\_TEMPSENSOR\_MODULE   21 |
| --- |

## [◆ ](#a88ae2c1bafdc6e78258ada5cbb9368f9)ESP32\_TIMG0\_MODULE

| #define ESP32\_TIMG0\_MODULE   4 |
| --- |

## [◆ ](#a251462caa49fc6fe0ae1c8fe99a87caa)ESP32\_TIMG1\_MODULE

| #define ESP32\_TIMG1\_MODULE   5 /\* No timg1 on esp32c2, TODO: IDF-3825 \*/ |
| --- |

## [◆ ](#a9708d046fbadfb7ccbc5df3e0ae57844)ESP32\_UART0\_MODULE

| #define ESP32\_UART0\_MODULE   1 |
| --- |

## [◆ ](#a480803130ef80df04527f4dd12525d48)ESP32\_UART1\_MODULE

| #define ESP32\_UART1\_MODULE   2 |
| --- |

## [◆ ](#af5ef985d4eaf1ffe565e2662493178c6)ESP32\_UHCI0\_MODULE

| #define ESP32\_UHCI0\_MODULE   6 |
| --- |

## [◆ ](#aba1295479849f8b4dc44245e330e3020)ESP32\_WIFI\_BT\_COMMON\_MODULE

| #define ESP32\_WIFI\_BT\_COMMON\_MODULE   12 |
| --- |

## [◆ ](#a4013c1fc7538bf46d5c1771f837a8b21)ESP32\_WIFI\_MODULE

| #define ESP32\_WIFI\_MODULE   10 |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [clock](dir_6e9992ac75fd0b7a50e889108957c907.md)
- [esp32c2\_clock.h](esp32c2__clock_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

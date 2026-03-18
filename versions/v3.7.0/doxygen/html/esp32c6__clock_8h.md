---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/esp32c6__clock_8h.html
original_path: doxygen/html/esp32c6__clock_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

esp32c6\_clock.h File Reference

[Go to the source code of this file.](esp32c6__clock_8h_source.md)

| Macros | |
| --- | --- |
| #define | [ESP32\_CPU\_CLK\_SRC\_XTAL](#a44ee3670c3168dd0ffbc79a563a7f074)   0U |
| #define | [ESP32\_CPU\_CLK\_SRC\_PLL](#a7a723b6353a23b55ef44d720297fe26f)   1U |
| #define | [ESP32\_CLK\_SRC\_RC\_FAST](#a1962dad90f737a51fcc70cea1931b236)   2U |
| #define | [ESP32\_CLK\_CPU\_PLL\_80M](#a61275f95111fb2a6bdbe446c0228f877)   80000000 |
| #define | [ESP32\_CLK\_CPU\_PLL\_160M](#ad80a59287e6a2f3771fd448982be9555)   160000000 |
| #define | [ESP32\_CLK\_CPU\_RC\_FAST\_FREQ](#ab779f427209fda571ec4d229b8ef8bfc)   17500000 |
| #define | [ESP32\_CLK\_XTAL\_32M](#aeb5c606e77a85fa858ab7af6061c7949)   32000000 |
| #define | [ESP32\_CLK\_XTAL\_40M](#a6afe38f9f9c44a1bd2e5279163523a98)   40000000 |
| #define | [ESP32\_RTC\_FAST\_CLK\_SRC\_RC\_FAST](#aae48d9f1288771e11c11d6177ecf3af7)   0 |
| #define | [ESP32\_RTC\_FAST\_CLK\_SRC\_XTAL\_D2](#a725193bf445b7f8f2c1058a6735ca476)   1 |
| #define | [ESP32\_RTC\_SLOW\_CLK\_SRC\_RC\_SLOW](#ad1d90df80dee3040dbe8c968cd774443)   0 |
| #define | [ESP32\_RTC\_SLOW\_CLK\_SRC\_XTAL32K](#aeaccf7695cab85cd7523c6ebc21704c4)   1 |
| #define | [ESP32\_RTC\_SLOW\_CLK\_SRC\_RC32K](#ad2816af571c412c39237c7e2f5f18c04)   2 |
| #define | [ESP32\_RTC\_SLOW\_CLK\_32K\_EXT\_OSC](#aa5d6a46de7da027832aa02489c062069)   9 |
| #define | [ESP32\_RTC\_SLOW\_CLK\_SRC\_RC\_SLOW\_FREQ](#af5cdcfa17e680ceda2f90e375eded6e6)   136000 |
| #define | [ESP32\_RTC\_SLOW\_CLK\_SRC\_XTAL32K\_FREQ](#ab63ec0973bfb87f7f09c5614ab66deb8)   32768 |
| #define | [ESP32\_RTC\_SLOW\_CLK\_SRC\_RC32K\_FREQ](#a3b18cdc509424e2249c7f4c3f1d93107)   32768 |
| #define | [ESP32\_LEDC\_MODULE](#a60f4f5ee56d788f2161b52ebbc2aa510)   0 |
| #define | [ESP32\_UART0\_MODULE](#a9708d046fbadfb7ccbc5df3e0ae57844)   1 |
| #define | [ESP32\_UART1\_MODULE](#a480803130ef80df04527f4dd12525d48)   2 |
| #define | [ESP32\_USB\_MODULE](#afcf8170a750f4dc35326010b52f4e082)   3 |
| #define | [ESP32\_I2C0\_MODULE](#a7331ffa2ec41896d05f1f86c4d30f758)   4 |
| #define | [ESP32\_I2S1\_MODULE](#a1cc05bfada949af9e9265abaadb1b6bc)   5 |
| #define | [ESP32\_TIMG0\_MODULE](#a88ae2c1bafdc6e78258ada5cbb9368f9)   6 |
| #define | [ESP32\_TIMG1\_MODULE](#a251462caa49fc6fe0ae1c8fe99a87caa)   7 |
| #define | [ESP32\_UHCI0\_MODULE](#af5ef985d4eaf1ffe565e2662493178c6)   8 |
| #define | [ESP32\_RMT\_MODULE](#a4a2d8ca15cd619022c02f97842d54159)   9 |
| #define | [ESP32\_PCNT\_MODULE](#ac0d8fb4397baaac7ff45dee8f4e1cb7c)   10 |
| #define | [ESP32\_SPI\_MODULE](#a5652d0e2b1fc766dde13b84294d4576b)   11 |
| #define | [ESP32\_SPI2\_MODULE](#a5e5283c23811e9c4f30980f1d865773b)   12 |
| #define | [ESP32\_TWAI0\_MODULE](#ad6847f96f663ae04ca4d2c324b793d16)   13 |
| #define | [ESP32\_TWAI1\_MODULE](#a0f0617f973ff3de27881f36957cd7cf2)   14 |
| #define | [ESP32\_RNG\_MODULE](#ad5423ca02819aab6b3fe63c11b3cf998)   15 |
| #define | [ESP32\_RSA\_MODULE](#a5261565b59c0a5b75794014b80692b33)   16 |
| #define | [ESP32\_AES\_MODULE](#a290ac6ab6c5de2e8d84a911e389e1cfc)   17 |
| #define | [ESP32\_SHA\_MODULE](#a683dd8814bf170018b63b57268c0fde9)   18 |
| #define | [ESP32\_ECC\_MODULE](#a27bd450bf21c8b7502d1f32d9536129f)   19 |
| #define | [ESP32\_HMAC\_MODULE](#ae17c59442b576d1b9aade6019850e6f8)   20 |
| #define | [ESP32\_DS\_MODULE](#aaea0a7a0e789019e4ddfd38365e83688)   21 |
| #define | [ESP32\_SDIO\_SLAVE\_MODULE](#a83b43d5f4d6373a5bb437de5ee5c091f)   22 |
| #define | [ESP32\_GDMA\_MODULE](#a701fec66fac239e66a19389ea153ff75)   23 |
| #define | [ESP32\_MCPWM0\_MODULE](#a13e722b2a08b3ea2da2ba3b40d794697)   24 |
| #define | [ESP32\_ETM\_MODULE](#a991c820648c7ef77b5aff2cecefee45d)   25 |
| #define | [ESP32\_PARLIO\_MODULE](#ada34a774bc3ec003c91cfe7c89939763)   26 |
| #define | [ESP32\_SYSTIMER\_MODULE](#aaf8e1de1e86906ba539863b9009ebe37)   27 |
| #define | [ESP32\_SARADC\_MODULE](#abe244da38fbe794e93094feef9b188fe)   28 |
| #define | [ESP32\_TEMPSENSOR\_MODULE](#a488d6d32cf66e81a27f0999f837fe39a)   29 |
| #define | [ESP32\_REGDMA\_MODULE](#a4a2832234309c8525ce7ce35a05ae41f)   30 |
| #define | [ESP32\_LP\_I2C0\_MODULE](#a5ccf92c28d468d746c24d34453ff1caa)   31 |
| #define | [ESP32\_WIFI\_MODULE](#a4013c1fc7538bf46d5c1771f837a8b21)   32 |
| #define | [ESP32\_BT\_MODULE](#ad180ebcea5567ce6c3145998f3761584)   33 |
| #define | [ESP32\_IEEE802154\_MODULE](#adf10ec1f34cbc43fb1e896da892c677d)   34 |
| #define | [ESP32\_COEX\_MODULE](#afe4f89e4a6712cc76536ea1b6a769a2d)   35 |
| #define | [ESP32\_PHY\_MODULE](#ae77d17fb45b7464a1ae16cc8e95ad6a2)   36 |
| #define | [ESP32\_MODULE\_MAX](#ac380a7ff843ee465763a355cb01ef295)   37 |

## Macro Definition Documentation

## [◆ ](#a290ac6ab6c5de2e8d84a911e389e1cfc)ESP32\_AES\_MODULE

| #define ESP32\_AES\_MODULE   17 |
| --- |

## [◆ ](#ad180ebcea5567ce6c3145998f3761584)ESP32\_BT\_MODULE

| #define ESP32\_BT\_MODULE   33 |
| --- |

## [◆ ](#ad80a59287e6a2f3771fd448982be9555)ESP32\_CLK\_CPU\_PLL\_160M

| #define ESP32\_CLK\_CPU\_PLL\_160M   160000000 |
| --- |

## [◆ ](#a61275f95111fb2a6bdbe446c0228f877)ESP32\_CLK\_CPU\_PLL\_80M

| #define ESP32\_CLK\_CPU\_PLL\_80M   80000000 |
| --- |

## [◆ ](#ab779f427209fda571ec4d229b8ef8bfc)ESP32\_CLK\_CPU\_RC\_FAST\_FREQ

| #define ESP32\_CLK\_CPU\_RC\_FAST\_FREQ   17500000 |
| --- |

## [◆ ](#a1962dad90f737a51fcc70cea1931b236)ESP32\_CLK\_SRC\_RC\_FAST

| #define ESP32\_CLK\_SRC\_RC\_FAST   2U |
| --- |

## [◆ ](#aeb5c606e77a85fa858ab7af6061c7949)ESP32\_CLK\_XTAL\_32M

| #define ESP32\_CLK\_XTAL\_32M   32000000 |
| --- |

## [◆ ](#a6afe38f9f9c44a1bd2e5279163523a98)ESP32\_CLK\_XTAL\_40M

| #define ESP32\_CLK\_XTAL\_40M   40000000 |
| --- |

## [◆ ](#afe4f89e4a6712cc76536ea1b6a769a2d)ESP32\_COEX\_MODULE

| #define ESP32\_COEX\_MODULE   35 |
| --- |

## [◆ ](#a7a723b6353a23b55ef44d720297fe26f)ESP32\_CPU\_CLK\_SRC\_PLL

| #define ESP32\_CPU\_CLK\_SRC\_PLL   1U |
| --- |

## [◆ ](#a44ee3670c3168dd0ffbc79a563a7f074)ESP32\_CPU\_CLK\_SRC\_XTAL

| #define ESP32\_CPU\_CLK\_SRC\_XTAL   0U |
| --- |

## [◆ ](#aaea0a7a0e789019e4ddfd38365e83688)ESP32\_DS\_MODULE

| #define ESP32\_DS\_MODULE   21 |
| --- |

## [◆ ](#a27bd450bf21c8b7502d1f32d9536129f)ESP32\_ECC\_MODULE

| #define ESP32\_ECC\_MODULE   19 |
| --- |

## [◆ ](#a991c820648c7ef77b5aff2cecefee45d)ESP32\_ETM\_MODULE

| #define ESP32\_ETM\_MODULE   25 |
| --- |

## [◆ ](#a701fec66fac239e66a19389ea153ff75)ESP32\_GDMA\_MODULE

| #define ESP32\_GDMA\_MODULE   23 |
| --- |

## [◆ ](#ae17c59442b576d1b9aade6019850e6f8)ESP32\_HMAC\_MODULE

| #define ESP32\_HMAC\_MODULE   20 |
| --- |

## [◆ ](#a7331ffa2ec41896d05f1f86c4d30f758)ESP32\_I2C0\_MODULE

| #define ESP32\_I2C0\_MODULE   4 |
| --- |

## [◆ ](#a1cc05bfada949af9e9265abaadb1b6bc)ESP32\_I2S1\_MODULE

| #define ESP32\_I2S1\_MODULE   5 |
| --- |

## [◆ ](#adf10ec1f34cbc43fb1e896da892c677d)ESP32\_IEEE802154\_MODULE

| #define ESP32\_IEEE802154\_MODULE   34 |
| --- |

## [◆ ](#a60f4f5ee56d788f2161b52ebbc2aa510)ESP32\_LEDC\_MODULE

| #define ESP32\_LEDC\_MODULE   0 |
| --- |

## [◆ ](#a5ccf92c28d468d746c24d34453ff1caa)ESP32\_LP\_I2C0\_MODULE

| #define ESP32\_LP\_I2C0\_MODULE   31 |
| --- |

## [◆ ](#a13e722b2a08b3ea2da2ba3b40d794697)ESP32\_MCPWM0\_MODULE

| #define ESP32\_MCPWM0\_MODULE   24 |
| --- |

## [◆ ](#ac380a7ff843ee465763a355cb01ef295)ESP32\_MODULE\_MAX

| #define ESP32\_MODULE\_MAX   37 |
| --- |

## [◆ ](#ada34a774bc3ec003c91cfe7c89939763)ESP32\_PARLIO\_MODULE

| #define ESP32\_PARLIO\_MODULE   26 |
| --- |

## [◆ ](#ac0d8fb4397baaac7ff45dee8f4e1cb7c)ESP32\_PCNT\_MODULE

| #define ESP32\_PCNT\_MODULE   10 |
| --- |

## [◆ ](#ae77d17fb45b7464a1ae16cc8e95ad6a2)ESP32\_PHY\_MODULE

| #define ESP32\_PHY\_MODULE   36 |
| --- |

## [◆ ](#a4a2832234309c8525ce7ce35a05ae41f)ESP32\_REGDMA\_MODULE

| #define ESP32\_REGDMA\_MODULE   30 |
| --- |

## [◆ ](#a4a2d8ca15cd619022c02f97842d54159)ESP32\_RMT\_MODULE

| #define ESP32\_RMT\_MODULE   9 |
| --- |

## [◆ ](#ad5423ca02819aab6b3fe63c11b3cf998)ESP32\_RNG\_MODULE

| #define ESP32\_RNG\_MODULE   15 |
| --- |

## [◆ ](#a5261565b59c0a5b75794014b80692b33)ESP32\_RSA\_MODULE

| #define ESP32\_RSA\_MODULE   16 |
| --- |

## [◆ ](#aae48d9f1288771e11c11d6177ecf3af7)ESP32\_RTC\_FAST\_CLK\_SRC\_RC\_FAST

| #define ESP32\_RTC\_FAST\_CLK\_SRC\_RC\_FAST   0 |
| --- |

## [◆ ](#a725193bf445b7f8f2c1058a6735ca476)ESP32\_RTC\_FAST\_CLK\_SRC\_XTAL\_D2

| #define ESP32\_RTC\_FAST\_CLK\_SRC\_XTAL\_D2   1 |
| --- |

## [◆ ](#aa5d6a46de7da027832aa02489c062069)ESP32\_RTC\_SLOW\_CLK\_32K\_EXT\_OSC

| #define ESP32\_RTC\_SLOW\_CLK\_32K\_EXT\_OSC   9 |
| --- |

## [◆ ](#ad2816af571c412c39237c7e2f5f18c04)ESP32\_RTC\_SLOW\_CLK\_SRC\_RC32K

| #define ESP32\_RTC\_SLOW\_CLK\_SRC\_RC32K   2 |
| --- |

## [◆ ](#a3b18cdc509424e2249c7f4c3f1d93107)ESP32\_RTC\_SLOW\_CLK\_SRC\_RC32K\_FREQ

| #define ESP32\_RTC\_SLOW\_CLK\_SRC\_RC32K\_FREQ   32768 |
| --- |

## [◆ ](#ad1d90df80dee3040dbe8c968cd774443)ESP32\_RTC\_SLOW\_CLK\_SRC\_RC\_SLOW

| #define ESP32\_RTC\_SLOW\_CLK\_SRC\_RC\_SLOW   0 |
| --- |

## [◆ ](#af5cdcfa17e680ceda2f90e375eded6e6)ESP32\_RTC\_SLOW\_CLK\_SRC\_RC\_SLOW\_FREQ

| #define ESP32\_RTC\_SLOW\_CLK\_SRC\_RC\_SLOW\_FREQ   136000 |
| --- |

## [◆ ](#aeaccf7695cab85cd7523c6ebc21704c4)ESP32\_RTC\_SLOW\_CLK\_SRC\_XTAL32K

| #define ESP32\_RTC\_SLOW\_CLK\_SRC\_XTAL32K   1 |
| --- |

## [◆ ](#ab63ec0973bfb87f7f09c5614ab66deb8)ESP32\_RTC\_SLOW\_CLK\_SRC\_XTAL32K\_FREQ

| #define ESP32\_RTC\_SLOW\_CLK\_SRC\_XTAL32K\_FREQ   32768 |
| --- |

## [◆ ](#abe244da38fbe794e93094feef9b188fe)ESP32\_SARADC\_MODULE

| #define ESP32\_SARADC\_MODULE   28 |
| --- |

## [◆ ](#a83b43d5f4d6373a5bb437de5ee5c091f)ESP32\_SDIO\_SLAVE\_MODULE

| #define ESP32\_SDIO\_SLAVE\_MODULE   22 |
| --- |

## [◆ ](#a683dd8814bf170018b63b57268c0fde9)ESP32\_SHA\_MODULE

| #define ESP32\_SHA\_MODULE   18 |
| --- |

## [◆ ](#a5e5283c23811e9c4f30980f1d865773b)ESP32\_SPI2\_MODULE

| #define ESP32\_SPI2\_MODULE   12 |
| --- |

## [◆ ](#a5652d0e2b1fc766dde13b84294d4576b)ESP32\_SPI\_MODULE

| #define ESP32\_SPI\_MODULE   11 |
| --- |

## [◆ ](#aaf8e1de1e86906ba539863b9009ebe37)ESP32\_SYSTIMER\_MODULE

| #define ESP32\_SYSTIMER\_MODULE   27 |
| --- |

## [◆ ](#a488d6d32cf66e81a27f0999f837fe39a)ESP32\_TEMPSENSOR\_MODULE

| #define ESP32\_TEMPSENSOR\_MODULE   29 |
| --- |

## [◆ ](#a88ae2c1bafdc6e78258ada5cbb9368f9)ESP32\_TIMG0\_MODULE

| #define ESP32\_TIMG0\_MODULE   6 |
| --- |

## [◆ ](#a251462caa49fc6fe0ae1c8fe99a87caa)ESP32\_TIMG1\_MODULE

| #define ESP32\_TIMG1\_MODULE   7 |
| --- |

## [◆ ](#ad6847f96f663ae04ca4d2c324b793d16)ESP32\_TWAI0\_MODULE

| #define ESP32\_TWAI0\_MODULE   13 |
| --- |

## [◆ ](#a0f0617f973ff3de27881f36957cd7cf2)ESP32\_TWAI1\_MODULE

| #define ESP32\_TWAI1\_MODULE   14 |
| --- |

## [◆ ](#a9708d046fbadfb7ccbc5df3e0ae57844)ESP32\_UART0\_MODULE

| #define ESP32\_UART0\_MODULE   1 |
| --- |

## [◆ ](#a480803130ef80df04527f4dd12525d48)ESP32\_UART1\_MODULE

| #define ESP32\_UART1\_MODULE   2 |
| --- |

## [◆ ](#af5ef985d4eaf1ffe565e2662493178c6)ESP32\_UHCI0\_MODULE

| #define ESP32\_UHCI0\_MODULE   8 |
| --- |

## [◆ ](#afcf8170a750f4dc35326010b52f4e082)ESP32\_USB\_MODULE

| #define ESP32\_USB\_MODULE   3 |
| --- |

## [◆ ](#a4013c1fc7538bf46d5c1771f837a8b21)ESP32\_WIFI\_MODULE

| #define ESP32\_WIFI\_MODULE   32 |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [clock](dir_6e9992ac75fd0b7a50e889108957c907.md)
- [esp32c6\_clock.h](esp32c6__clock_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/esp32c3__clock_8h.html
original_path: doxygen/html/esp32c3__clock_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

esp32c3\_clock.h File Reference

[Go to the source code of this file.](esp32c3__clock_8h_source.md)

| Macros | |
| --- | --- |
| #define | [ESP32\_CLK\_SRC\_XTAL](#afca77320ca383abd16c3da3dd9f5475b)   0U |
| #define | [ESP32\_CLK\_SRC\_PLL](#a2b6410b41a6a9b646ed1030e8626a8f8)   1U |
| #define | [ESP32\_CLK\_SRC\_RTC8M](#a4de6bcb9ee3b5c6dfc4887528999af77)   2U |
| #define | [ESP32\_CLK\_SRC\_APLL](#a9d8f8be2dbba1b9cfc31e2188868b025)   3U |
| #define | [ESP32\_CLK\_CPU\_80M](#a7ef1aa6b333059931611dd948b93e147)   80000000 |
| #define | [ESP32\_CLK\_CPU\_160M](#a4ce7aae7fa038527cc1892e94762ddf5)   160000000 |
| #define | [ESP32\_CLK\_XTAL\_32M](#aeb5c606e77a85fa858ab7af6061c7949)   0U |
| #define | [ESP32\_CLK\_XTAL\_40M](#a6afe38f9f9c44a1bd2e5279163523a98)   1U |
| #define | [ESP32\_RTC\_FAST\_CLK\_FREQ\_8M](#a7545a9269b1a9db19e45913f77e93ae1)   8500000U |
| #define | [ESP32\_RTC\_FAST\_CLK\_FREQ\_APPROX](#accb6c4420081f80615e07a97606c6b62)   [ESP32\_RTC\_FAST\_CLK\_FREQ\_8M](#a7545a9269b1a9db19e45913f77e93ae1) |
| #define | [ESP32\_RTC\_SLOW\_CLK\_FREQ\_90K](#ac1907007a9016544d3a8a84b350c2f0f)   90000U |
| #define | [ESP32\_RTC\_SLOW\_CLK\_FREQ\_8MD256](#a995e21929ecfb57c86d7ca1b1cf8e010)   ([ESP32\_RTC\_FAST\_CLK\_FREQ\_APPROX](#accb6c4420081f80615e07a97606c6b62) / 256) |
| #define | [ESP32\_RTC\_SLOW\_CLK\_FREQ\_32K](#ac977efbcfd0b8665b9362b40af6657e8)   32768U |
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
| #define | [ESP32\_SPI\_MODULE](#a5652d0e2b1fc766dde13b84294d4576b)   10 |
| #define | [ESP32\_SPI2\_MODULE](#a5e5283c23811e9c4f30980f1d865773b)   11 |
| #define | [ESP32\_TWAI\_MODULE](#aba65cf1082c8422cc1e91c710bb702cc)   12 |
| #define | [ESP32\_RNG\_MODULE](#ad5423ca02819aab6b3fe63c11b3cf998)   13 |
| #define | [ESP32\_WIFI\_MODULE](#a4013c1fc7538bf46d5c1771f837a8b21)   14 |
| #define | [ESP32\_BT\_MODULE](#ad180ebcea5567ce6c3145998f3761584)   15 |
| #define | [ESP32\_WIFI\_BT\_COMMON\_MODULE](#aba1295479849f8b4dc44245e330e3020)   16 |
| #define | [ESP32\_BT\_BASEBAND\_MODULE](#a653e6d1f91c532b3ba313be27a97c2af)   17 |
| #define | [ESP32\_BT\_LC\_MODULE](#a8e27f45346390d8909f9424f13280b76)   18 |
| #define | [ESP32\_RSA\_MODULE](#a5261565b59c0a5b75794014b80692b33)   19 |
| #define | [ESP32\_AES\_MODULE](#a290ac6ab6c5de2e8d84a911e389e1cfc)   20 |
| #define | [ESP32\_SHA\_MODULE](#a683dd8814bf170018b63b57268c0fde9)   21 |
| #define | [ESP32\_HMAC\_MODULE](#ae17c59442b576d1b9aade6019850e6f8)   22 |
| #define | [ESP32\_DS\_MODULE](#aaea0a7a0e789019e4ddfd38365e83688)   23 |
| #define | [ESP32\_GDMA\_MODULE](#a701fec66fac239e66a19389ea153ff75)   24 |
| #define | [ESP32\_SYSTIMER\_MODULE](#aaf8e1de1e86906ba539863b9009ebe37)   25 |
| #define | [ESP32\_SARADC\_MODULE](#abe244da38fbe794e93094feef9b188fe)   26 |
| #define | [ESP32\_MODULE\_MAX](#ac380a7ff843ee465763a355cb01ef295)   27 |

## Macro Definition Documentation

## [◆ ](#a290ac6ab6c5de2e8d84a911e389e1cfc)ESP32\_AES\_MODULE

| #define ESP32\_AES\_MODULE   20 |
| --- |

## [◆ ](#a653e6d1f91c532b3ba313be27a97c2af)ESP32\_BT\_BASEBAND\_MODULE

| #define ESP32\_BT\_BASEBAND\_MODULE   17 |
| --- |

## [◆ ](#a8e27f45346390d8909f9424f13280b76)ESP32\_BT\_LC\_MODULE

| #define ESP32\_BT\_LC\_MODULE   18 |
| --- |

## [◆ ](#ad180ebcea5567ce6c3145998f3761584)ESP32\_BT\_MODULE

| #define ESP32\_BT\_MODULE   15 |
| --- |

## [◆ ](#a4ce7aae7fa038527cc1892e94762ddf5)ESP32\_CLK\_CPU\_160M

| #define ESP32\_CLK\_CPU\_160M   160000000 |
| --- |

## [◆ ](#a7ef1aa6b333059931611dd948b93e147)ESP32\_CLK\_CPU\_80M

| #define ESP32\_CLK\_CPU\_80M   80000000 |
| --- |

## [◆ ](#a9d8f8be2dbba1b9cfc31e2188868b025)ESP32\_CLK\_SRC\_APLL

| #define ESP32\_CLK\_SRC\_APLL   3U |
| --- |

## [◆ ](#a2b6410b41a6a9b646ed1030e8626a8f8)ESP32\_CLK\_SRC\_PLL

| #define ESP32\_CLK\_SRC\_PLL   1U |
| --- |

## [◆ ](#a4de6bcb9ee3b5c6dfc4887528999af77)ESP32\_CLK\_SRC\_RTC8M

| #define ESP32\_CLK\_SRC\_RTC8M   2U |
| --- |

## [◆ ](#afca77320ca383abd16c3da3dd9f5475b)ESP32\_CLK\_SRC\_XTAL

| #define ESP32\_CLK\_SRC\_XTAL   0U |
| --- |

## [◆ ](#aeb5c606e77a85fa858ab7af6061c7949)ESP32\_CLK\_XTAL\_32M

| #define ESP32\_CLK\_XTAL\_32M   0U |
| --- |

## [◆ ](#a6afe38f9f9c44a1bd2e5279163523a98)ESP32\_CLK\_XTAL\_40M

| #define ESP32\_CLK\_XTAL\_40M   1U |
| --- |

## [◆ ](#aaea0a7a0e789019e4ddfd38365e83688)ESP32\_DS\_MODULE

| #define ESP32\_DS\_MODULE   23 |
| --- |

## [◆ ](#a701fec66fac239e66a19389ea153ff75)ESP32\_GDMA\_MODULE

| #define ESP32\_GDMA\_MODULE   24 |
| --- |

## [◆ ](#ae17c59442b576d1b9aade6019850e6f8)ESP32\_HMAC\_MODULE

| #define ESP32\_HMAC\_MODULE   22 |
| --- |

## [◆ ](#a7331ffa2ec41896d05f1f86c4d30f758)ESP32\_I2C0\_MODULE

| #define ESP32\_I2C0\_MODULE   4 |
| --- |

## [◆ ](#a1cc05bfada949af9e9265abaadb1b6bc)ESP32\_I2S1\_MODULE

| #define ESP32\_I2S1\_MODULE   5 |
| --- |

## [◆ ](#a60f4f5ee56d788f2161b52ebbc2aa510)ESP32\_LEDC\_MODULE

| #define ESP32\_LEDC\_MODULE   0 |
| --- |

## [◆ ](#ac380a7ff843ee465763a355cb01ef295)ESP32\_MODULE\_MAX

| #define ESP32\_MODULE\_MAX   27 |
| --- |

## [◆ ](#a4a2d8ca15cd619022c02f97842d54159)ESP32\_RMT\_MODULE

| #define ESP32\_RMT\_MODULE   9 |
| --- |

## [◆ ](#ad5423ca02819aab6b3fe63c11b3cf998)ESP32\_RNG\_MODULE

| #define ESP32\_RNG\_MODULE   13 |
| --- |

## [◆ ](#a5261565b59c0a5b75794014b80692b33)ESP32\_RSA\_MODULE

| #define ESP32\_RSA\_MODULE   19 |
| --- |

## [◆ ](#a7545a9269b1a9db19e45913f77e93ae1)ESP32\_RTC\_FAST\_CLK\_FREQ\_8M

| #define ESP32\_RTC\_FAST\_CLK\_FREQ\_8M   8500000U |
| --- |

## [◆ ](#accb6c4420081f80615e07a97606c6b62)ESP32\_RTC\_FAST\_CLK\_FREQ\_APPROX

| #define ESP32\_RTC\_FAST\_CLK\_FREQ\_APPROX   [ESP32\_RTC\_FAST\_CLK\_FREQ\_8M](#a7545a9269b1a9db19e45913f77e93ae1) |
| --- |

## [◆ ](#ac977efbcfd0b8665b9362b40af6657e8)ESP32\_RTC\_SLOW\_CLK\_FREQ\_32K

| #define ESP32\_RTC\_SLOW\_CLK\_FREQ\_32K   32768U |
| --- |

## [◆ ](#a995e21929ecfb57c86d7ca1b1cf8e010)ESP32\_RTC\_SLOW\_CLK\_FREQ\_8MD256

| #define ESP32\_RTC\_SLOW\_CLK\_FREQ\_8MD256   ([ESP32\_RTC\_FAST\_CLK\_FREQ\_APPROX](#accb6c4420081f80615e07a97606c6b62) / 256) |
| --- |

## [◆ ](#ac1907007a9016544d3a8a84b350c2f0f)ESP32\_RTC\_SLOW\_CLK\_FREQ\_90K

| #define ESP32\_RTC\_SLOW\_CLK\_FREQ\_90K   90000U |
| --- |

## [◆ ](#abe244da38fbe794e93094feef9b188fe)ESP32\_SARADC\_MODULE

| #define ESP32\_SARADC\_MODULE   26 |
| --- |

## [◆ ](#a683dd8814bf170018b63b57268c0fde9)ESP32\_SHA\_MODULE

| #define ESP32\_SHA\_MODULE   21 |
| --- |

## [◆ ](#a5e5283c23811e9c4f30980f1d865773b)ESP32\_SPI2\_MODULE

| #define ESP32\_SPI2\_MODULE   11 |
| --- |

## [◆ ](#a5652d0e2b1fc766dde13b84294d4576b)ESP32\_SPI\_MODULE

| #define ESP32\_SPI\_MODULE   10 |
| --- |

## [◆ ](#aaf8e1de1e86906ba539863b9009ebe37)ESP32\_SYSTIMER\_MODULE

| #define ESP32\_SYSTIMER\_MODULE   25 |
| --- |

## [◆ ](#a88ae2c1bafdc6e78258ada5cbb9368f9)ESP32\_TIMG0\_MODULE

| #define ESP32\_TIMG0\_MODULE   6 |
| --- |

## [◆ ](#a251462caa49fc6fe0ae1c8fe99a87caa)ESP32\_TIMG1\_MODULE

| #define ESP32\_TIMG1\_MODULE   7 |
| --- |

## [◆ ](#aba65cf1082c8422cc1e91c710bb702cc)ESP32\_TWAI\_MODULE

| #define ESP32\_TWAI\_MODULE   12 |
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

## [◆ ](#aba1295479849f8b4dc44245e330e3020)ESP32\_WIFI\_BT\_COMMON\_MODULE

| #define ESP32\_WIFI\_BT\_COMMON\_MODULE   16 |
| --- |

## [◆ ](#a4013c1fc7538bf46d5c1771f837a8b21)ESP32\_WIFI\_MODULE

| #define ESP32\_WIFI\_MODULE   14 |
| --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [dt-bindings](dir_2e4d86f9d28357ce2f99093c0845149c.md)
- [clock](dir_6e9992ac75fd0b7a50e889108957c907.md)
- [esp32c3\_clock.h](esp32c3__clock_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

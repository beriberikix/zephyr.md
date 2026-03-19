---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/nrf__lpcomp_8h_source.html
original_path: doxygen/html/nrf__lpcomp_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

nrf\_lpcomp.h

[Go to the documentation of this file.](nrf__lpcomp_8h.md)

1/\*

2 \* Copyright (c) 2024 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_COMP\_NRF\_LPCOMP\_H\_

8#define ZEPHYR\_INCLUDE\_DRIVERS\_COMP\_NRF\_LPCOMP\_H\_

9

10#include <[zephyr/drivers/comparator.h](comparator_8h.md)>

11

12#ifdef \_\_cplusplus

13extern "C" {

14#endif

15

[ 17](nrf__lpcomp_8h.md#af1c88d0e254866b05c344b50a2574582)enum [comp\_nrf\_lpcomp\_psel](nrf__lpcomp_8h.md#af1c88d0e254866b05c344b50a2574582) {

[ 19](nrf__lpcomp_8h.md#af1c88d0e254866b05c344b50a2574582afdfa8c7afaedabfa6d66379d717c8230) [COMP\_NRF\_LPCOMP\_PSEL\_AIN0](nrf__lpcomp_8h.md#af1c88d0e254866b05c344b50a2574582afdfa8c7afaedabfa6d66379d717c8230),

[ 21](nrf__lpcomp_8h.md#af1c88d0e254866b05c344b50a2574582aff42e45ad33b6be0acb2b2db5f5517d8) [COMP\_NRF\_LPCOMP\_PSEL\_AIN1](nrf__lpcomp_8h.md#af1c88d0e254866b05c344b50a2574582aff42e45ad33b6be0acb2b2db5f5517d8),

[ 23](nrf__lpcomp_8h.md#af1c88d0e254866b05c344b50a2574582a9e485565e0f600538314af0b140ee8ed) [COMP\_NRF\_LPCOMP\_PSEL\_AIN2](nrf__lpcomp_8h.md#af1c88d0e254866b05c344b50a2574582a9e485565e0f600538314af0b140ee8ed),

[ 25](nrf__lpcomp_8h.md#af1c88d0e254866b05c344b50a2574582a93ec605b4475653e3eee896ed9de6791) [COMP\_NRF\_LPCOMP\_PSEL\_AIN3](nrf__lpcomp_8h.md#af1c88d0e254866b05c344b50a2574582a93ec605b4475653e3eee896ed9de6791),

[ 27](nrf__lpcomp_8h.md#af1c88d0e254866b05c344b50a2574582aa40f5844c344870a65db0768516d821d) [COMP\_NRF\_LPCOMP\_PSEL\_AIN4](nrf__lpcomp_8h.md#af1c88d0e254866b05c344b50a2574582aa40f5844c344870a65db0768516d821d),

[ 29](nrf__lpcomp_8h.md#af1c88d0e254866b05c344b50a2574582a550f58b7541368c722af8dfe575f49a0) [COMP\_NRF\_LPCOMP\_PSEL\_AIN5](nrf__lpcomp_8h.md#af1c88d0e254866b05c344b50a2574582a550f58b7541368c722af8dfe575f49a0),

[ 31](nrf__lpcomp_8h.md#af1c88d0e254866b05c344b50a2574582a0032da62c7b68dc91cfab011838a23bd) [COMP\_NRF\_LPCOMP\_PSEL\_AIN6](nrf__lpcomp_8h.md#af1c88d0e254866b05c344b50a2574582a0032da62c7b68dc91cfab011838a23bd),

[ 33](nrf__lpcomp_8h.md#af1c88d0e254866b05c344b50a2574582aab8c5a2ccbb98de807f020d4b47eb35e) [COMP\_NRF\_LPCOMP\_PSEL\_AIN7](nrf__lpcomp_8h.md#af1c88d0e254866b05c344b50a2574582aab8c5a2ccbb98de807f020d4b47eb35e),

34};

35

[ 37](nrf__lpcomp_8h.md#ab150e9043eca4b0b4ce7ace4317e1b21)enum [comp\_nrf\_lpcomp\_extrefsel](nrf__lpcomp_8h.md#ab150e9043eca4b0b4ce7ace4317e1b21) {

[ 39](nrf__lpcomp_8h.md#ab150e9043eca4b0b4ce7ace4317e1b21a5a95781545b3b3cfbbe22f4313199df2) [COMP\_NRF\_LPCOMP\_EXTREFSEL\_AIN0](nrf__lpcomp_8h.md#ab150e9043eca4b0b4ce7ace4317e1b21a5a95781545b3b3cfbbe22f4313199df2),

[ 41](nrf__lpcomp_8h.md#ab150e9043eca4b0b4ce7ace4317e1b21a1581658dd7f77da5278119959f93af4a) [COMP\_NRF\_LPCOMP\_EXTREFSEL\_AIN1](nrf__lpcomp_8h.md#ab150e9043eca4b0b4ce7ace4317e1b21a1581658dd7f77da5278119959f93af4a),

42};

43

[ 45](nrf__lpcomp_8h.md#ae42326afcd4f5435480f80d382266a04)enum [comp\_nrf\_lpcomp\_refsel](nrf__lpcomp_8h.md#ae42326afcd4f5435480f80d382266a04) {

[ 47](nrf__lpcomp_8h.md#ae42326afcd4f5435480f80d382266a04a99627f00ae3182014da516333f64705f) [COMP\_NRF\_LPCOMP\_REFSEL\_VDD\_1\_8](nrf__lpcomp_8h.md#ae42326afcd4f5435480f80d382266a04a99627f00ae3182014da516333f64705f),

[ 49](nrf__lpcomp_8h.md#ae42326afcd4f5435480f80d382266a04a3c10840415f3aed4d0b8414a6decf56d) [COMP\_NRF\_LPCOMP\_REFSEL\_VDD\_2\_8](nrf__lpcomp_8h.md#ae42326afcd4f5435480f80d382266a04a3c10840415f3aed4d0b8414a6decf56d),

[ 51](nrf__lpcomp_8h.md#ae42326afcd4f5435480f80d382266a04a25c009efcddd2e84417d115b5f4e346e) [COMP\_NRF\_LPCOMP\_REFSEL\_VDD\_3\_8](nrf__lpcomp_8h.md#ae42326afcd4f5435480f80d382266a04a25c009efcddd2e84417d115b5f4e346e),

[ 53](nrf__lpcomp_8h.md#ae42326afcd4f5435480f80d382266a04a848e512c3223a019f6ec59612616fe33) [COMP\_NRF\_LPCOMP\_REFSEL\_VDD\_4\_8](nrf__lpcomp_8h.md#ae42326afcd4f5435480f80d382266a04a848e512c3223a019f6ec59612616fe33),

[ 55](nrf__lpcomp_8h.md#ae42326afcd4f5435480f80d382266a04a295352a4ecb28f6288efe33fd0c49526) [COMP\_NRF\_LPCOMP\_REFSEL\_VDD\_5\_8](nrf__lpcomp_8h.md#ae42326afcd4f5435480f80d382266a04a295352a4ecb28f6288efe33fd0c49526),

[ 57](nrf__lpcomp_8h.md#ae42326afcd4f5435480f80d382266a04a624b842d3ef6e8fa172412fc3a06dd1a) [COMP\_NRF\_LPCOMP\_REFSEL\_VDD\_6\_8](nrf__lpcomp_8h.md#ae42326afcd4f5435480f80d382266a04a624b842d3ef6e8fa172412fc3a06dd1a),

[ 59](nrf__lpcomp_8h.md#ae42326afcd4f5435480f80d382266a04a2b1cd929103b9af8ef372472078efb76) [COMP\_NRF\_LPCOMP\_REFSEL\_VDD\_7\_8](nrf__lpcomp_8h.md#ae42326afcd4f5435480f80d382266a04a2b1cd929103b9af8ef372472078efb76),

[ 61](nrf__lpcomp_8h.md#ae42326afcd4f5435480f80d382266a04acd4c60e604696b7d24028ad9e98d77f3) [COMP\_NRF\_LPCOMP\_REFSEL\_VDD\_1\_16](nrf__lpcomp_8h.md#ae42326afcd4f5435480f80d382266a04acd4c60e604696b7d24028ad9e98d77f3),

[ 63](nrf__lpcomp_8h.md#ae42326afcd4f5435480f80d382266a04a3b3760b0298de0fcb94812f98433ba16) [COMP\_NRF\_LPCOMP\_REFSEL\_VDD\_3\_16](nrf__lpcomp_8h.md#ae42326afcd4f5435480f80d382266a04a3b3760b0298de0fcb94812f98433ba16),

[ 65](nrf__lpcomp_8h.md#ae42326afcd4f5435480f80d382266a04a94a97a641eaa3dc25b09d00dda8fb137) [COMP\_NRF\_LPCOMP\_REFSEL\_VDD\_5\_16](nrf__lpcomp_8h.md#ae42326afcd4f5435480f80d382266a04a94a97a641eaa3dc25b09d00dda8fb137),

[ 67](nrf__lpcomp_8h.md#ae42326afcd4f5435480f80d382266a04a98def2c5d100c1c51c697203606b66dd) [COMP\_NRF\_LPCOMP\_REFSEL\_VDD\_7\_16](nrf__lpcomp_8h.md#ae42326afcd4f5435480f80d382266a04a98def2c5d100c1c51c697203606b66dd),

[ 69](nrf__lpcomp_8h.md#ae42326afcd4f5435480f80d382266a04aa62402dda42b69bd974de3f19aa4a509) [COMP\_NRF\_LPCOMP\_REFSEL\_VDD\_9\_16](nrf__lpcomp_8h.md#ae42326afcd4f5435480f80d382266a04aa62402dda42b69bd974de3f19aa4a509),

[ 71](nrf__lpcomp_8h.md#ae42326afcd4f5435480f80d382266a04a9913bfd70d57767e295ced6e7287a7bb) [COMP\_NRF\_LPCOMP\_REFSEL\_VDD\_11\_16](nrf__lpcomp_8h.md#ae42326afcd4f5435480f80d382266a04a9913bfd70d57767e295ced6e7287a7bb),

[ 73](nrf__lpcomp_8h.md#ae42326afcd4f5435480f80d382266a04a930ce822163d6654cda439e43fbbaab1) [COMP\_NRF\_LPCOMP\_REFSEL\_VDD\_13\_16](nrf__lpcomp_8h.md#ae42326afcd4f5435480f80d382266a04a930ce822163d6654cda439e43fbbaab1),

[ 75](nrf__lpcomp_8h.md#ae42326afcd4f5435480f80d382266a04aade5263dc54bd126f9a761e0188b13f7) [COMP\_NRF\_LPCOMP\_REFSEL\_VDD\_15\_16](nrf__lpcomp_8h.md#ae42326afcd4f5435480f80d382266a04aade5263dc54bd126f9a761e0188b13f7),

[ 77](nrf__lpcomp_8h.md#ae42326afcd4f5435480f80d382266a04abf717bfb0610352e60d4f4fc45a370b1) [COMP\_NRF\_LPCOMP\_REFSEL\_AREF](nrf__lpcomp_8h.md#ae42326afcd4f5435480f80d382266a04abf717bfb0610352e60d4f4fc45a370b1),

78};

79

[ 85](structcomp__nrf__lpcomp__config.md)struct [comp\_nrf\_lpcomp\_config](structcomp__nrf__lpcomp__config.md) {

[ 87](structcomp__nrf__lpcomp__config.md#aa39efb6f9cb0ad0720d04cefb4ba0513) enum [comp\_nrf\_lpcomp\_psel](nrf__lpcomp_8h.md#af1c88d0e254866b05c344b50a2574582) [psel](structcomp__nrf__lpcomp__config.md#aa39efb6f9cb0ad0720d04cefb4ba0513);

[ 89](structcomp__nrf__lpcomp__config.md#a4b69733d3fc9a20f9958a027d3898ec3) enum [comp\_nrf\_lpcomp\_extrefsel](nrf__lpcomp_8h.md#ab150e9043eca4b0b4ce7ace4317e1b21) [extrefsel](structcomp__nrf__lpcomp__config.md#a4b69733d3fc9a20f9958a027d3898ec3);

[ 91](structcomp__nrf__lpcomp__config.md#ad1022de6c772909a4f8c3d90e0748fe7) enum [comp\_nrf\_lpcomp\_refsel](nrf__lpcomp_8h.md#ae42326afcd4f5435480f80d382266a04) [refsel](structcomp__nrf__lpcomp__config.md#ad1022de6c772909a4f8c3d90e0748fe7);

[ 93](structcomp__nrf__lpcomp__config.md#ac561f00056c9faabb61a4a67b628f963) bool [enable\_hyst](structcomp__nrf__lpcomp__config.md#ac561f00056c9faabb61a4a67b628f963);

94};

95

[ 105](nrf__lpcomp_8h.md#aff748ac1a1a8c13796b81ef789b4c7f2)int [comp\_nrf\_lpcomp\_configure](nrf__lpcomp_8h.md#aff748ac1a1a8c13796b81ef789b4c7f2)(const struct [device](structdevice.md) \*dev,

106 const struct [comp\_nrf\_lpcomp\_config](structcomp__nrf__lpcomp__config.md) \*config);

107

108#ifdef \_\_cplusplus

109}

110#endif

111

112#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_COMP\_NRF\_LPCOMP\_H\_ \*/

[comparator.h](comparator_8h.md)

[comp\_nrf\_lpcomp\_extrefsel](nrf__lpcomp_8h.md#ab150e9043eca4b0b4ce7ace4317e1b21)

comp\_nrf\_lpcomp\_extrefsel

External reference selection.

**Definition** nrf\_lpcomp.h:37

[COMP\_NRF\_LPCOMP\_EXTREFSEL\_AIN1](nrf__lpcomp_8h.md#ab150e9043eca4b0b4ce7ace4317e1b21a1581658dd7f77da5278119959f93af4a)

@ COMP\_NRF\_LPCOMP\_EXTREFSEL\_AIN1

AIN1 external input.

**Definition** nrf\_lpcomp.h:41

[COMP\_NRF\_LPCOMP\_EXTREFSEL\_AIN0](nrf__lpcomp_8h.md#ab150e9043eca4b0b4ce7ace4317e1b21a5a95781545b3b3cfbbe22f4313199df2)

@ COMP\_NRF\_LPCOMP\_EXTREFSEL\_AIN0

AIN0 external input.

**Definition** nrf\_lpcomp.h:39

[comp\_nrf\_lpcomp\_refsel](nrf__lpcomp_8h.md#ae42326afcd4f5435480f80d382266a04)

comp\_nrf\_lpcomp\_refsel

Reference selection.

**Definition** nrf\_lpcomp.h:45

[COMP\_NRF\_LPCOMP\_REFSEL\_VDD\_3\_8](nrf__lpcomp_8h.md#ae42326afcd4f5435480f80d382266a04a25c009efcddd2e84417d115b5f4e346e)

@ COMP\_NRF\_LPCOMP\_REFSEL\_VDD\_3\_8

Use (VDD \* (3/8)) as reference.

**Definition** nrf\_lpcomp.h:51

[COMP\_NRF\_LPCOMP\_REFSEL\_VDD\_5\_8](nrf__lpcomp_8h.md#ae42326afcd4f5435480f80d382266a04a295352a4ecb28f6288efe33fd0c49526)

@ COMP\_NRF\_LPCOMP\_REFSEL\_VDD\_5\_8

Use (VDD \* (5/8)) as reference.

**Definition** nrf\_lpcomp.h:55

[COMP\_NRF\_LPCOMP\_REFSEL\_VDD\_7\_8](nrf__lpcomp_8h.md#ae42326afcd4f5435480f80d382266a04a2b1cd929103b9af8ef372472078efb76)

@ COMP\_NRF\_LPCOMP\_REFSEL\_VDD\_7\_8

Use (VDD \* (7/8)) as reference.

**Definition** nrf\_lpcomp.h:59

[COMP\_NRF\_LPCOMP\_REFSEL\_VDD\_3\_16](nrf__lpcomp_8h.md#ae42326afcd4f5435480f80d382266a04a3b3760b0298de0fcb94812f98433ba16)

@ COMP\_NRF\_LPCOMP\_REFSEL\_VDD\_3\_16

Use (VDD \* (3/16)) as reference.

**Definition** nrf\_lpcomp.h:63

[COMP\_NRF\_LPCOMP\_REFSEL\_VDD\_2\_8](nrf__lpcomp_8h.md#ae42326afcd4f5435480f80d382266a04a3c10840415f3aed4d0b8414a6decf56d)

@ COMP\_NRF\_LPCOMP\_REFSEL\_VDD\_2\_8

Use (VDD \* (2/8)) as reference.

**Definition** nrf\_lpcomp.h:49

[COMP\_NRF\_LPCOMP\_REFSEL\_VDD\_6\_8](nrf__lpcomp_8h.md#ae42326afcd4f5435480f80d382266a04a624b842d3ef6e8fa172412fc3a06dd1a)

@ COMP\_NRF\_LPCOMP\_REFSEL\_VDD\_6\_8

Use (VDD \* (6/8)) as reference.

**Definition** nrf\_lpcomp.h:57

[COMP\_NRF\_LPCOMP\_REFSEL\_VDD\_4\_8](nrf__lpcomp_8h.md#ae42326afcd4f5435480f80d382266a04a848e512c3223a019f6ec59612616fe33)

@ COMP\_NRF\_LPCOMP\_REFSEL\_VDD\_4\_8

Use (VDD \* (4/8)) as reference.

**Definition** nrf\_lpcomp.h:53

[COMP\_NRF\_LPCOMP\_REFSEL\_VDD\_13\_16](nrf__lpcomp_8h.md#ae42326afcd4f5435480f80d382266a04a930ce822163d6654cda439e43fbbaab1)

@ COMP\_NRF\_LPCOMP\_REFSEL\_VDD\_13\_16

Use (VDD \* (13/16)) as reference.

**Definition** nrf\_lpcomp.h:73

[COMP\_NRF\_LPCOMP\_REFSEL\_VDD\_5\_16](nrf__lpcomp_8h.md#ae42326afcd4f5435480f80d382266a04a94a97a641eaa3dc25b09d00dda8fb137)

@ COMP\_NRF\_LPCOMP\_REFSEL\_VDD\_5\_16

Use (VDD \* (5/16)) as reference.

**Definition** nrf\_lpcomp.h:65

[COMP\_NRF\_LPCOMP\_REFSEL\_VDD\_7\_16](nrf__lpcomp_8h.md#ae42326afcd4f5435480f80d382266a04a98def2c5d100c1c51c697203606b66dd)

@ COMP\_NRF\_LPCOMP\_REFSEL\_VDD\_7\_16

Use (VDD \* (7/16)) as reference.

**Definition** nrf\_lpcomp.h:67

[COMP\_NRF\_LPCOMP\_REFSEL\_VDD\_11\_16](nrf__lpcomp_8h.md#ae42326afcd4f5435480f80d382266a04a9913bfd70d57767e295ced6e7287a7bb)

@ COMP\_NRF\_LPCOMP\_REFSEL\_VDD\_11\_16

Use (VDD \* (11/16)) as reference.

**Definition** nrf\_lpcomp.h:71

[COMP\_NRF\_LPCOMP\_REFSEL\_VDD\_1\_8](nrf__lpcomp_8h.md#ae42326afcd4f5435480f80d382266a04a99627f00ae3182014da516333f64705f)

@ COMP\_NRF\_LPCOMP\_REFSEL\_VDD\_1\_8

Use (VDD \* (1/8)) as reference.

**Definition** nrf\_lpcomp.h:47

[COMP\_NRF\_LPCOMP\_REFSEL\_VDD\_9\_16](nrf__lpcomp_8h.md#ae42326afcd4f5435480f80d382266a04aa62402dda42b69bd974de3f19aa4a509)

@ COMP\_NRF\_LPCOMP\_REFSEL\_VDD\_9\_16

Use (VDD \* (9/16)) as reference.

**Definition** nrf\_lpcomp.h:69

[COMP\_NRF\_LPCOMP\_REFSEL\_VDD\_15\_16](nrf__lpcomp_8h.md#ae42326afcd4f5435480f80d382266a04aade5263dc54bd126f9a761e0188b13f7)

@ COMP\_NRF\_LPCOMP\_REFSEL\_VDD\_15\_16

Use (VDD \* (15/16)) as reference.

**Definition** nrf\_lpcomp.h:75

[COMP\_NRF\_LPCOMP\_REFSEL\_AREF](nrf__lpcomp_8h.md#ae42326afcd4f5435480f80d382266a04abf717bfb0610352e60d4f4fc45a370b1)

@ COMP\_NRF\_LPCOMP\_REFSEL\_AREF

Use external analog reference.

**Definition** nrf\_lpcomp.h:77

[COMP\_NRF\_LPCOMP\_REFSEL\_VDD\_1\_16](nrf__lpcomp_8h.md#ae42326afcd4f5435480f80d382266a04acd4c60e604696b7d24028ad9e98d77f3)

@ COMP\_NRF\_LPCOMP\_REFSEL\_VDD\_1\_16

Use (VDD \* (1/16)) as reference.

**Definition** nrf\_lpcomp.h:61

[comp\_nrf\_lpcomp\_psel](nrf__lpcomp_8h.md#af1c88d0e254866b05c344b50a2574582)

comp\_nrf\_lpcomp\_psel

Positive input selection.

**Definition** nrf\_lpcomp.h:17

[COMP\_NRF\_LPCOMP\_PSEL\_AIN6](nrf__lpcomp_8h.md#af1c88d0e254866b05c344b50a2574582a0032da62c7b68dc91cfab011838a23bd)

@ COMP\_NRF\_LPCOMP\_PSEL\_AIN6

AIN6 external input.

**Definition** nrf\_lpcomp.h:31

[COMP\_NRF\_LPCOMP\_PSEL\_AIN5](nrf__lpcomp_8h.md#af1c88d0e254866b05c344b50a2574582a550f58b7541368c722af8dfe575f49a0)

@ COMP\_NRF\_LPCOMP\_PSEL\_AIN5

AIN5 external input.

**Definition** nrf\_lpcomp.h:29

[COMP\_NRF\_LPCOMP\_PSEL\_AIN3](nrf__lpcomp_8h.md#af1c88d0e254866b05c344b50a2574582a93ec605b4475653e3eee896ed9de6791)

@ COMP\_NRF\_LPCOMP\_PSEL\_AIN3

AIN3 external input.

**Definition** nrf\_lpcomp.h:25

[COMP\_NRF\_LPCOMP\_PSEL\_AIN2](nrf__lpcomp_8h.md#af1c88d0e254866b05c344b50a2574582a9e485565e0f600538314af0b140ee8ed)

@ COMP\_NRF\_LPCOMP\_PSEL\_AIN2

AIN2 external input.

**Definition** nrf\_lpcomp.h:23

[COMP\_NRF\_LPCOMP\_PSEL\_AIN4](nrf__lpcomp_8h.md#af1c88d0e254866b05c344b50a2574582aa40f5844c344870a65db0768516d821d)

@ COMP\_NRF\_LPCOMP\_PSEL\_AIN4

AIN4 external input.

**Definition** nrf\_lpcomp.h:27

[COMP\_NRF\_LPCOMP\_PSEL\_AIN7](nrf__lpcomp_8h.md#af1c88d0e254866b05c344b50a2574582aab8c5a2ccbb98de807f020d4b47eb35e)

@ COMP\_NRF\_LPCOMP\_PSEL\_AIN7

AIN7 external input.

**Definition** nrf\_lpcomp.h:33

[COMP\_NRF\_LPCOMP\_PSEL\_AIN0](nrf__lpcomp_8h.md#af1c88d0e254866b05c344b50a2574582afdfa8c7afaedabfa6d66379d717c8230)

@ COMP\_NRF\_LPCOMP\_PSEL\_AIN0

AIN0 external input.

**Definition** nrf\_lpcomp.h:19

[COMP\_NRF\_LPCOMP\_PSEL\_AIN1](nrf__lpcomp_8h.md#af1c88d0e254866b05c344b50a2574582aff42e45ad33b6be0acb2b2db5f5517d8)

@ COMP\_NRF\_LPCOMP\_PSEL\_AIN1

AIN1 external input.

**Definition** nrf\_lpcomp.h:21

[comp\_nrf\_lpcomp\_configure](nrf__lpcomp_8h.md#aff748ac1a1a8c13796b81ef789b4c7f2)

int comp\_nrf\_lpcomp\_configure(const struct device \*dev, const struct comp\_nrf\_lpcomp\_config \*config)

Configure comparator.

[comp\_nrf\_lpcomp\_config](structcomp__nrf__lpcomp__config.md)

Configuration structure.

**Definition** nrf\_lpcomp.h:85

[comp\_nrf\_lpcomp\_config::extrefsel](structcomp__nrf__lpcomp__config.md#a4b69733d3fc9a20f9958a027d3898ec3)

enum comp\_nrf\_lpcomp\_extrefsel extrefsel

External reference selection.

**Definition** nrf\_lpcomp.h:89

[comp\_nrf\_lpcomp\_config::psel](structcomp__nrf__lpcomp__config.md#aa39efb6f9cb0ad0720d04cefb4ba0513)

enum comp\_nrf\_lpcomp\_psel psel

Positive input selection.

**Definition** nrf\_lpcomp.h:87

[comp\_nrf\_lpcomp\_config::enable\_hyst](structcomp__nrf__lpcomp__config.md#ac561f00056c9faabb61a4a67b628f963)

bool enable\_hyst

Hysteresis configuration.

**Definition** nrf\_lpcomp.h:93

[comp\_nrf\_lpcomp\_config::refsel](structcomp__nrf__lpcomp__config.md#ad1022de6c772909a4f8c3d90e0748fe7)

enum comp\_nrf\_lpcomp\_refsel refsel

Reference selection.

**Definition** nrf\_lpcomp.h:91

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:453

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [comparator](dir_25be445c737a80f4854b3956f06e1693.md)
- [nrf\_lpcomp.h](nrf__lpcomp_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/mic__privacy_8h_source.html
original_path: doxygen/html/mic__privacy_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

mic\_privacy.h

[Go to the documentation of this file.](mic__privacy_8h.md)

1/\*

2 \* Copyright (c) 2025 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef \_\_ZEPHYR\_INCLUDE\_MIC\_PRIVACY\_H\_\_

8#define \_\_ZEPHYR\_INCLUDE\_MIC\_PRIVACY\_H\_\_

9

10#include <[stdint.h](stdint_8h.md)>

11#include <[errno.h](errno_8h.md)>

12#include <[stdbool.h](stdbool_8h.md)>

13#include <[stdint.h](stdint_8h.md)>

14#include <[zephyr/kernel.h](kernel_8h.md)>

15#include <[zephyr/spinlock.h](spinlock_8h.md)>

16#include <[zephyr/devicetree.h](devicetree_8h.md)>

17

[ 18](mic__privacy_8h.md#acbabb5c150f29668a23379bcb2180931)enum [mic\_privacy\_policy](mic__privacy_8h.md#acbabb5c150f29668a23379bcb2180931) {

[ 19](mic__privacy_8h.md#acbabb5c150f29668a23379bcb2180931a6d9216a6396136add2267a39d3b0cfe4) [MIC\_PRIVACY\_DISABLED](mic__privacy_8h.md#acbabb5c150f29668a23379bcb2180931a6d9216a6396136add2267a39d3b0cfe4) = 0,

[ 20](mic__privacy_8h.md#acbabb5c150f29668a23379bcb2180931a0ac8b17e6006dafa7516b5ebfd9d3d0f) [MIC\_PRIVACY\_HW\_MANAGED](mic__privacy_8h.md#acbabb5c150f29668a23379bcb2180931a0ac8b17e6006dafa7516b5ebfd9d3d0f) = 1,

[ 21](mic__privacy_8h.md#acbabb5c150f29668a23379bcb2180931a1abc8c704d5bc13bbda18dbef6b9da5c) [MIC\_PRIVACY\_FW\_MANAGED](mic__privacy_8h.md#acbabb5c150f29668a23379bcb2180931a1abc8c704d5bc13bbda18dbef6b9da5c) = 2,

[ 22](mic__privacy_8h.md#acbabb5c150f29668a23379bcb2180931a7d76f1a96d342f4c7c769d3fc5fcac90) [MIC\_PRIVACY\_FORCE\_MIC\_DISABLED](mic__privacy_8h.md#acbabb5c150f29668a23379bcb2180931a7d76f1a96d342f4c7c769d3fc5fcac90) = 3,

23};

24

25/\* has to match HW register definition

26 \* (DZLS bit field in DFMICPVCP register)

27 \*/

[ 28](unionmic__privacy__mask.md)union [mic\_privacy\_mask](unionmic__privacy__mask.md) {

[ 29](unionmic__privacy__mask.md#a9ca8420acd33e12b2454457d4e626c03) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [value](unionmic__privacy__mask.md#a9ca8420acd33e12b2454457d4e626c03);

30 struct {

[ 31](unionmic__privacy__mask.md#a7803afbf97e48fa202cbb40e96777437) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [sndw](unionmic__privacy__mask.md#a7803afbf97e48fa202cbb40e96777437):7;

[ 32](unionmic__privacy__mask.md#a074ae40d422faa6a338454ca5072c978) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [dmic](unionmic__privacy__mask.md#a074ae40d422faa6a338454ca5072c978):1;

33 };

34};

35

[ 36](structintel__adsp__mic__priv__data.md)struct [intel\_adsp\_mic\_priv\_data](structintel__adsp__mic__priv__data.md) {

[ 37](structintel__adsp__mic__priv__data.md#a35c90e6b6980e1015acb521b90f4992e) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [rsvd](structintel__adsp__mic__priv__data.md#a35c90e6b6980e1015acb521b90f4992e);

38};

39

[ 40](structintel__adsp__mic__priv__cfg.md)struct [intel\_adsp\_mic\_priv\_cfg](structintel__adsp__mic__priv__cfg.md) {

[ 41](structintel__adsp__mic__priv__cfg.md#ad3b2a9026031e758618cf97dbb66c006) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [base](structintel__adsp__mic__priv__cfg.md#ad3b2a9026031e758618cf97dbb66c006);

[ 42](structintel__adsp__mic__priv__cfg.md#abbd9d8fbdef2f213c6d7fd05d087358c) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [regblock\_size](structintel__adsp__mic__priv__cfg.md#abbd9d8fbdef2f213c6d7fd05d087358c);

43};

44

[ 45](structmic__privacy__api__funcs.md)struct [mic\_privacy\_api\_funcs](structmic__privacy__api__funcs.md) {

[ 46](structmic__privacy__api__funcs.md#a67548968f088126881ef11f7317e5036) void (\*[enable\_fw\_managed\_irq](structmic__privacy__api__funcs.md#a67548968f088126881ef11f7317e5036))(bool [enable\_irq](4_2lib__helpers_8h.md#a9519288643c3060570256bc125cbbeaf), const void \*fn);

[ 47](structmic__privacy__api__funcs.md#a294e4cd3bb23ccb23f7143b6a9e4dba5) void (\*[clear\_fw\_managed\_irq](structmic__privacy__api__funcs.md#a294e4cd3bb23ccb23f7143b6a9e4dba5))();

[ 48](structmic__privacy__api__funcs.md#afc87beb092fa02c06dcd84125ccc305a) void (\*[enable\_dmic\_irq](structmic__privacy__api__funcs.md#afc87beb092fa02c06dcd84125ccc305a))(bool [enable\_irq](4_2lib__helpers_8h.md#a9519288643c3060570256bc125cbbeaf), const void \*fn);

[ 49](structmic__privacy__api__funcs.md#a8cd74fd6817c3f5bfa0fc7697765d357) [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) (\*[get\_dmic\_irq\_status](structmic__privacy__api__funcs.md#a8cd74fd6817c3f5bfa0fc7697765d357))(void);

[ 50](structmic__privacy__api__funcs.md#ae68b97acf6ec4f5812275ee682bdf96d) void (\*[clear\_dmic\_irq\_status](structmic__privacy__api__funcs.md#ae68b97acf6ec4f5812275ee682bdf96d))(void);

51 enum [mic\_privacy\_policy](mic__privacy_8h.md#acbabb5c150f29668a23379bcb2180931) (\*[get\_policy](structmic__privacy__api__funcs.md#a558346b619a67f3f05b20cf62a7993ef))();

[ 52](structmic__privacy__api__funcs.md#ad03e41de9d08b1cdd77abd6d40f14baf) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) (\*[get\_privacy\_policy\_register\_raw\_value](structmic__privacy__api__funcs.md#ad03e41de9d08b1cdd77abd6d40f14baf))();

[ 53](structmic__privacy__api__funcs.md#a1ee80c505a6a7d7bdf34c228acfc3b87) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) (\*[get\_dma\_data\_zeroing\_wait\_time](structmic__privacy__api__funcs.md#a1ee80c505a6a7d7bdf34c228acfc3b87))();

[ 54](structmic__privacy__api__funcs.md#a73ea5882b8af5f4a738913c1c16a3aaf) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) (\*[get\_dma\_data\_zeroing\_link\_select](structmic__privacy__api__funcs.md#a73ea5882b8af5f4a738913c1c16a3aaf))();

[ 55](structmic__privacy__api__funcs.md#a3e365ecf294cf653d0439d5d6d7d6ed5) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) (\*[get\_dmic\_mic\_disable\_status](structmic__privacy__api__funcs.md#a3e365ecf294cf653d0439d5d6d7d6ed5))(void);

[ 56](structmic__privacy__api__funcs.md#abedb0ba2dbb1d9ba639aab636308747f) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) (\*[get\_fw\_managed\_mic\_disable\_status](structmic__privacy__api__funcs.md#abedb0ba2dbb1d9ba639aab636308747f))();

[ 57](structmic__privacy__api__funcs.md#a9b827a1b6b817d5e5ec19ffa94b531f0) void (\*[set\_fw\_managed\_mode](structmic__privacy__api__funcs.md#a9b827a1b6b817d5e5ec19ffa94b531f0))(bool is\_fw\_managed\_enabled);

[ 58](structmic__privacy__api__funcs.md#a6f21bade6b6041322cba6995f9140d6b) void (\*[set\_fw\_mic\_disable\_status](structmic__privacy__api__funcs.md#a6f21bade6b6041322cba6995f9140d6b))(bool fw\_mic\_disable\_status);

[ 59](structmic__privacy__api__funcs.md#ac60beb8b72089feab7267c265d4bfe5d) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) (\*[get\_fw\_mic\_disable\_status](structmic__privacy__api__funcs.md#ac60beb8b72089feab7267c265d4bfe5d))();

60};

61

62#endif

[enable\_irq](4_2lib__helpers_8h.md#a9519288643c3060570256bc125cbbeaf)

static ALWAYS\_INLINE void enable\_irq(void)

**Definition** lib\_helpers.h:132

[devicetree.h](devicetree_8h.md)

Devicetree main header.

[errno.h](errno_8h.md)

System error numbers.

[kernel.h](kernel_8h.md)

Public kernel APIs.

[mic\_privacy\_policy](mic__privacy_8h.md#acbabb5c150f29668a23379bcb2180931)

mic\_privacy\_policy

**Definition** mic\_privacy.h:18

[MIC\_PRIVACY\_HW\_MANAGED](mic__privacy_8h.md#acbabb5c150f29668a23379bcb2180931a0ac8b17e6006dafa7516b5ebfd9d3d0f)

@ MIC\_PRIVACY\_HW\_MANAGED

**Definition** mic\_privacy.h:20

[MIC\_PRIVACY\_FW\_MANAGED](mic__privacy_8h.md#acbabb5c150f29668a23379bcb2180931a1abc8c704d5bc13bbda18dbef6b9da5c)

@ MIC\_PRIVACY\_FW\_MANAGED

**Definition** mic\_privacy.h:21

[MIC\_PRIVACY\_DISABLED](mic__privacy_8h.md#acbabb5c150f29668a23379bcb2180931a6d9216a6396136add2267a39d3b0cfe4)

@ MIC\_PRIVACY\_DISABLED

**Definition** mic\_privacy.h:19

[MIC\_PRIVACY\_FORCE\_MIC\_DISABLED](mic__privacy_8h.md#acbabb5c150f29668a23379bcb2180931a7d76f1a96d342f4c7c769d3fc5fcac90)

@ MIC\_PRIVACY\_FORCE\_MIC\_DISABLED

**Definition** mic\_privacy.h:22

[spinlock.h](spinlock_8h.md)

Public interface for spinlocks.

[stdbool.h](stdbool_8h.md)

[bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)

#define bool

**Definition** stdbool.h:13

[stdint.h](stdint_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[intel\_adsp\_mic\_priv\_cfg](structintel__adsp__mic__priv__cfg.md)

**Definition** mic\_privacy.h:40

[intel\_adsp\_mic\_priv\_cfg::regblock\_size](structintel__adsp__mic__priv__cfg.md#abbd9d8fbdef2f213c6d7fd05d087358c)

uint32\_t regblock\_size

**Definition** mic\_privacy.h:42

[intel\_adsp\_mic\_priv\_cfg::base](structintel__adsp__mic__priv__cfg.md#ad3b2a9026031e758618cf97dbb66c006)

uint32\_t base

**Definition** mic\_privacy.h:41

[intel\_adsp\_mic\_priv\_data](structintel__adsp__mic__priv__data.md)

**Definition** mic\_privacy.h:36

[intel\_adsp\_mic\_priv\_data::rsvd](structintel__adsp__mic__priv__data.md#a35c90e6b6980e1015acb521b90f4992e)

uint8\_t rsvd

**Definition** mic\_privacy.h:37

[mic\_privacy\_api\_funcs](structmic__privacy__api__funcs.md)

**Definition** mic\_privacy.h:45

[mic\_privacy\_api\_funcs::get\_dma\_data\_zeroing\_wait\_time](structmic__privacy__api__funcs.md#a1ee80c505a6a7d7bdf34c228acfc3b87)

uint32\_t(\* get\_dma\_data\_zeroing\_wait\_time)()

**Definition** mic\_privacy.h:53

[mic\_privacy\_api\_funcs::clear\_fw\_managed\_irq](structmic__privacy__api__funcs.md#a294e4cd3bb23ccb23f7143b6a9e4dba5)

void(\* clear\_fw\_managed\_irq)()

**Definition** mic\_privacy.h:47

[mic\_privacy\_api\_funcs::get\_dmic\_mic\_disable\_status](structmic__privacy__api__funcs.md#a3e365ecf294cf653d0439d5d6d7d6ed5)

uint32\_t(\* get\_dmic\_mic\_disable\_status)(void)

**Definition** mic\_privacy.h:55

[mic\_privacy\_api\_funcs::get\_policy](structmic__privacy__api__funcs.md#a558346b619a67f3f05b20cf62a7993ef)

enum mic\_privacy\_policy(\* get\_policy)()

**Definition** mic\_privacy.h:51

[mic\_privacy\_api\_funcs::enable\_fw\_managed\_irq](structmic__privacy__api__funcs.md#a67548968f088126881ef11f7317e5036)

void(\* enable\_fw\_managed\_irq)(bool enable\_irq, const void \*fn)

**Definition** mic\_privacy.h:46

[mic\_privacy\_api\_funcs::set\_fw\_mic\_disable\_status](structmic__privacy__api__funcs.md#a6f21bade6b6041322cba6995f9140d6b)

void(\* set\_fw\_mic\_disable\_status)(bool fw\_mic\_disable\_status)

**Definition** mic\_privacy.h:58

[mic\_privacy\_api\_funcs::get\_dma\_data\_zeroing\_link\_select](structmic__privacy__api__funcs.md#a73ea5882b8af5f4a738913c1c16a3aaf)

uint32\_t(\* get\_dma\_data\_zeroing\_link\_select)()

**Definition** mic\_privacy.h:54

[mic\_privacy\_api\_funcs::get\_dmic\_irq\_status](structmic__privacy__api__funcs.md#a8cd74fd6817c3f5bfa0fc7697765d357)

bool(\* get\_dmic\_irq\_status)(void)

**Definition** mic\_privacy.h:49

[mic\_privacy\_api\_funcs::set\_fw\_managed\_mode](structmic__privacy__api__funcs.md#a9b827a1b6b817d5e5ec19ffa94b531f0)

void(\* set\_fw\_managed\_mode)(bool is\_fw\_managed\_enabled)

**Definition** mic\_privacy.h:57

[mic\_privacy\_api\_funcs::get\_fw\_managed\_mic\_disable\_status](structmic__privacy__api__funcs.md#abedb0ba2dbb1d9ba639aab636308747f)

uint32\_t(\* get\_fw\_managed\_mic\_disable\_status)()

**Definition** mic\_privacy.h:56

[mic\_privacy\_api\_funcs::get\_fw\_mic\_disable\_status](structmic__privacy__api__funcs.md#ac60beb8b72089feab7267c265d4bfe5d)

uint32\_t(\* get\_fw\_mic\_disable\_status)()

**Definition** mic\_privacy.h:59

[mic\_privacy\_api\_funcs::get\_privacy\_policy\_register\_raw\_value](structmic__privacy__api__funcs.md#ad03e41de9d08b1cdd77abd6d40f14baf)

uint32\_t(\* get\_privacy\_policy\_register\_raw\_value)()

**Definition** mic\_privacy.h:52

[mic\_privacy\_api\_funcs::clear\_dmic\_irq\_status](structmic__privacy__api__funcs.md#ae68b97acf6ec4f5812275ee682bdf96d)

void(\* clear\_dmic\_irq\_status)(void)

**Definition** mic\_privacy.h:50

[mic\_privacy\_api\_funcs::enable\_dmic\_irq](structmic__privacy__api__funcs.md#afc87beb092fa02c06dcd84125ccc305a)

void(\* enable\_dmic\_irq)(bool enable\_irq, const void \*fn)

**Definition** mic\_privacy.h:48

[mic\_privacy\_mask](unionmic__privacy__mask.md)

**Definition** mic\_privacy.h:28

[mic\_privacy\_mask::dmic](unionmic__privacy__mask.md#a074ae40d422faa6a338454ca5072c978)

uint32\_t dmic

**Definition** mic\_privacy.h:32

[mic\_privacy\_mask::sndw](unionmic__privacy__mask.md#a7803afbf97e48fa202cbb40e96777437)

uint32\_t sndw

**Definition** mic\_privacy.h:31

[mic\_privacy\_mask::value](unionmic__privacy__mask.md#a9ca8420acd33e12b2454457d4e626c03)

uint32\_t value

**Definition** mic\_privacy.h:29

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [mic\_privacy](dir_2e06c65c52133b8e4ff4bf7424ae25af.md)
- [intel](dir_493819a1cd457399897f0d97609f1fe6.md)
- [mic\_privacy.h](mic__privacy_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

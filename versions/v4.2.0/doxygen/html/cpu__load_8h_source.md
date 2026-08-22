---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/cpu__load_8h_source.html
original_path: doxygen/html/cpu__load_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

cpu\_load.h

[Go to the documentation of this file.](cpu__load_8h.md)

1/\*

2 \* Copyright (c) 2024, Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DEBUG\_CPU\_LOAD\_H\_

8#define ZEPHYR\_INCLUDE\_DEBUG\_CPU\_LOAD\_H\_

9

10#include <[stdbool.h](stdbool_8h.md)>

11#include <[stdint.h](stdint_8h.md)>

12

13#ifdef \_\_cplusplus

14extern "C" {

15#endif

16

24

[ 26](group__cpu__load.md#ga28a73232eb45cdf6ce057e1e4c84190d)void [cpu\_load\_on\_enter\_idle](group__cpu__load.md#ga28a73232eb45cdf6ce057e1e4c84190d)(void);

27

[ 29](group__cpu__load.md#ga8a8c97914a72b6eb5a7e1862710a0c6d)void [cpu\_load\_on\_exit\_idle](group__cpu__load.md#ga8a8c97914a72b6eb5a7e1862710a0c6d)(void);

30

[ 42](group__cpu__load.md#gaf44501a292aeef7749b68c706b34119f)int [cpu\_load\_get](group__cpu__load.md#gaf44501a292aeef7749b68c706b34119f)(bool reset);

43

[ 50](group__cpu__load.md#gabc95920fb1a666b1496618cf5afbfbff)void [cpu\_load\_log\_control](group__cpu__load.md#gabc95920fb1a666b1496618cf5afbfbff)(bool enable);

51

52/\* Optional callback for cpu\_load\_cb\_reg

53 \*

54 \* This will be called from the k\_timer expiry\_fn used for periodic logging.

55 \* CONFIG\_CPU\_LOAD\_LOG\_PERIODICALLY must be configured to a positive value.

56 \* Time spent in this callback must be kept to a minimum.

57 \*/

[ 58](group__cpu__load.md#ga83f2e3099de11b8e6b66395ae69f394a)typedef void (\*[cpu\_load\_cb\_t](group__cpu__load.md#ga83f2e3099de11b8e6b66395ae69f394a))([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) percent);

59

[ 69](group__cpu__load.md#gaec80c70d8dd6ea130edde48618ed2463)int [cpu\_load\_cb\_reg](group__cpu__load.md#gaec80c70d8dd6ea130edde48618ed2463)([cpu\_load\_cb\_t](group__cpu__load.md#ga83f2e3099de11b8e6b66395ae69f394a) cb, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) threshold\_percent);

70

74

75#ifdef \_\_cplusplus

76}

77#endif

78

79

80#endif /\* ZEPHYR\_INCLUDE\_DEBUG\_CPU\_LOAD\_H\_ \*/

[cpu\_load\_on\_enter\_idle](group__cpu__load.md#ga28a73232eb45cdf6ce057e1e4c84190d)

void cpu\_load\_on\_enter\_idle(void)

Hook called by the application specific hook on entering CPU idle.

[cpu\_load\_cb\_t](group__cpu__load.md#ga83f2e3099de11b8e6b66395ae69f394a)

void(\* cpu\_load\_cb\_t)(uint8\_t percent)

**Definition** cpu\_load.h:58

[cpu\_load\_on\_exit\_idle](group__cpu__load.md#ga8a8c97914a72b6eb5a7e1862710a0c6d)

void cpu\_load\_on\_exit\_idle(void)

Hook called by the application specific hook on exiting CPU idle.

[cpu\_load\_log\_control](group__cpu__load.md#gabc95920fb1a666b1496618cf5afbfbff)

void cpu\_load\_log\_control(bool enable)

Control periodic CPU statistics report.

[cpu\_load\_cb\_reg](group__cpu__load.md#gaec80c70d8dd6ea130edde48618ed2463)

int cpu\_load\_cb\_reg(cpu\_load\_cb\_t cb, uint8\_t threshold\_percent)

Optional registration of callback when load is greater or equal to the threshold.

[cpu\_load\_get](group__cpu__load.md#gaf44501a292aeef7749b68c706b34119f)

int cpu\_load\_get(bool reset)

Get CPU load.

[stdbool.h](stdbool_8h.md)

[stdint.h](stdint_8h.md)

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [debug](dir_44aa0acd5660d74ea205f18be43003ca.md)
- [cpu\_load.h](cpu__load_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

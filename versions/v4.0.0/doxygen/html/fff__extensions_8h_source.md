---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/fff__extensions_8h_source.html
original_path: doxygen/html/fff__extensions_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

fff\_extensions.h

[Go to the documentation of this file.](fff__extensions_8h.md)

1/\*

2 \* Copyright(c) 2023 Legrand North America, LLC.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

12

13#ifndef ZEPHYR\_SUBSYS\_TESTSUITE\_INCLUDE\_ZEPHYR\_FFF\_EXTENSIONS\_H\_

14#define ZEPHYR\_SUBSYS\_TESTSUITE\_INCLUDE\_ZEPHYR\_FFF\_EXTENSIONS\_H\_

15

16#include <[zephyr/fff.h](fff_8h.md)>

17#include <[zephyr/sys/util.h](sys_2util_8h.md)> /\* for CONTAINER\_OF \*/

18

28

29

78

[ 79](group__fff__extensions.md#ga4a4e81f6291e0bfbe7f60e0a03c2e9b1)#define RETURN\_HANDLED\_CONTEXT(FUNCNAME, \

80 CONTEXTTYPE, RESULTFIELD, CONTEXTPTRNAME, HANDLERBODY) \

81 if (FUNCNAME##\_fake.return\_val\_seq\_len) { \

82 CONTEXTTYPE \* const contexts = \

83 CONTAINER\_OF(FUNCNAME##\_fake.return\_val\_seq, \

84 CONTEXTTYPE, RESULTFIELD); \

85 size\_t const seq\_idx = (FUNCNAME##\_fake.return\_val\_seq\_idx < \

86 FUNCNAME##\_fake.return\_val\_seq\_len) ? \

87 FUNCNAME##\_fake.return\_val\_seq\_idx++ :\

88 FUNCNAME##\_fake.return\_val\_seq\_idx - 1;\

89 CONTEXTTYPE \* const CONTEXTPTRNAME = &contexts[seq\_idx]; \

90 HANDLERBODY; \

91 } \

92 return FUNCNAME##\_fake.return\_val

93

97

98#endif /\* ZEPHYR\_SUBSYS\_TESTSUITE\_INCLUDE\_ZEPHYR\_FFF\_EXTENSIONS\_H\_ \*/

[fff.h](fff_8h.md)

[util.h](sys_2util_8h.md)

Misc utilities.

- [subsys](dir_c85cb826952b1679a37b077c3741c8c1.md)
- [testsuite](dir_1abba8fd2d51532ae0fc663391fcb2bd.md)
- [include](dir_d5cd24c9babba9527629083c466f69cc.md)
- [zephyr](dir_91e5ce9bd56815b1bd388aa667b3762f.md)
- [fff\_extensions.h](fff__extensions_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/ztest__assert_8h.html
original_path: doxygen/html/ztest__assert_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ztest\_assert.h File Reference

Zephyr testing framework assertion macros.
[More...](#details)

`#include <stdarg.h>`  
`#include <[stdbool.h](stdbool_8h_source.md)>`  
`#include <[stdio.h](stdio_8h_source.md)>`  
`#include <[string.h](string_8h_source.md)>`  
`#include <[zephyr/ztest.h](ztest_8h_source.md)>`

[Go to the source code of this file.](ztest__assert_8h_source.md)

| Macros | |
| --- | --- |
| #define | [zassert](group__ztest__assert.md#ga0911ad9e94cdf1fe011d21316683ee7f)(cond, default\_msg, ...) |
| #define | [zassume](group__ztest__assert.md#ga5a4319eec770be532f34acb86e022c48)(cond, default\_msg, ...) |
| #define | [zexpect](group__ztest__assert.md#ga7bd837a8164123e3a06795b9f87a308d)(cond, default\_msg, ...) |
| #define | [zassert\_unreachable](group__ztest__assert.md#ga300684a6b56e73e2cad6fd7458541129)(...) |
|  | Assert that this function call won't be reached. |
| #define | [zassert\_true](group__ztest__assert.md#gaeebddde19012223e3d5e853a1dac3ac5)(cond, ...) |
|  | Assert that *cond* is true. |
| #define | [zassert\_false](group__ztest__assert.md#ga7330d1794fb961e07ee40294019dead0)(cond, ...) |
|  | Assert that *cond* is false. |
| #define | [zassert\_ok](group__ztest__assert.md#gade40e2ec78ec813739e7725524fae7f0)(cond, ...) |
|  | Assert that *cond* is 0 (success). |
| #define | [zassert\_not\_ok](group__ztest__assert.md#gafe0e2609f77906ab0caddc31448a4fc8)(cond, ...) |
|  | Assert that *cond* is not 0 (failure). |
| #define | [zassert\_is\_null](group__ztest__assert.md#gac0839891fd8bb7313b98551465e04c19)(ptr, ...) |
|  | Assert that *ptr* is NULL. |
| #define | [zassert\_not\_null](group__ztest__assert.md#ga849adad4afe893a7ae3dc2fbe750dc00)(ptr, ...) |
|  | Assert that *ptr* is not NULL. |
| #define | [zassert\_equal](group__ztest__assert.md#gacd075c7ee4dc2d64701bd3098a31b673)(a, b, ...) |
|  | Assert that *a* equals *b*. |
| #define | [zassert\_not\_equal](group__ztest__assert.md#ga43f306bf33d5e837b8927df16b82a363)(a, b, ...) |
|  | Assert that *a* does not equal *b*. |
| #define | [zassert\_equal\_ptr](group__ztest__assert.md#gabf20273fcba9cc45939a9f7db77f0bfc)(a, b, ...) |
|  | Assert that *a* equals *b*. |
| #define | [zassert\_within](group__ztest__assert.md#gacc930af1a66e8533c5eca9526e198b4b)(a, b, [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417), ...) |
|  | Assert that *a* is within *b* with delta *d*. |
| #define | [zassert\_between\_inclusive](group__ztest__assert.md#ga2b6b41de3e4856b21458febab3261b91)(a, l, u, ...) |
|  | Assert that *a* is greater than or equal to *l* and less than or equal to *u*. |
| #define | [zassert\_mem\_equal](group__ztest__assert.md#gabbfcf6345172387326d35b5d0e2bb051)(...) |
|  | Assert that 2 memory buffers have the same contents. |
| #define | [zassert\_mem\_equal\_\_](group__ztest__assert.md#ga30e5fefa185944d3e949d4023c2eea27)(buf, exp, size, ...) |
|  | Internal assert that 2 memory buffers have the same contents. |
| #define | [zassert\_str\_equal](group__ztest__assert.md#ga382017945a8c409e885cad8d0909b197)(s1, s2, ...) |
|  | Assert that 2 strings have the same contents. |
| #define | [zassume\_true](group__ztest__assume.md#ga6f5778ed8c1205126f7dcafb6eb26905)(cond, ...) |
|  | Assume that *cond* is true. |
| #define | [zassume\_false](group__ztest__assume.md#ga5acf4256e5af3afaed06da7400dc3ad5)(cond, ...) |
|  | Assume that *cond* is false. |
| #define | [zassume\_ok](group__ztest__assume.md#ga9c6d1c701dd2d50027bf5e24b7567ae4)(cond, ...) |
|  | Assume that *cond* is 0 (success). |
| #define | [zassume\_not\_ok](group__ztest__assume.md#ga539831d2f42cc991a8295b388ec12846)(cond, ...) |
|  | Assume that *cond* is not 0 (failure). |
| #define | [zassume\_is\_null](group__ztest__assume.md#ga3c5b1814deb5974e8ba0af961b516fa0)(ptr, ...) |
|  | Assume that *ptr* is NULL. |
| #define | [zassume\_not\_null](group__ztest__assume.md#ga24f4144edf5cef493c88872c7d56900e)(ptr, ...) |
|  | Assume that *ptr* is not NULL. |
| #define | [zassume\_equal](group__ztest__assume.md#ga88c2a3153568a6f621b88dd6ceeb48d6)(a, b, ...) |
|  | Assume that *a* equals *b*. |
| #define | [zassume\_not\_equal](group__ztest__assume.md#ga0d90bb874c3135ffee870a4b61607853)(a, b, ...) |
|  | Assume that *a* does not equal *b*. |
| #define | [zassume\_equal\_ptr](group__ztest__assume.md#ga78d6fbbf5eb13b32a5164053811b6cca)(a, b, ...) |
|  | Assume that *a* equals *b*. |
| #define | [zassume\_within](group__ztest__assume.md#gad808c91e07e6c27b2e28ec7e04e03854)(a, b, [d](asm-macro-32-bit-gnu_8h.md#abaebda2ebe87111969af89be8895e417), ...) |
|  | Assume that *a* is within *b* with delta *d*. |
| #define | [zassume\_between\_inclusive](group__ztest__assume.md#gacff02eeba8dd334b3727dbe2036617e3)(a, l, u, ...) |
|  | Assume that *a* is greater than or equal to *l* and less than or equal to *u*. |
| #define | [zassume\_mem\_equal](group__ztest__assume.md#ga62be45256399530167745e71226e4a37)(...) |
|  | Assume that 2 memory buffers have the same contents. |
| #define | [zassume\_mem\_equal\_\_](group__ztest__assume.md#gaaed6045f194ead4ffe1dd72a6fa5175d)(buf, exp, size, ...) |
|  | Internal assume that 2 memory buffers have the same contents. |
| #define | [zassume\_str\_equal](group__ztest__assume.md#ga33a9cd37d321f1a421a1328e67b04788)(s1, s2, ...) |
|  | Assumes that 2 strings have the same contents. |
| #define | [zexpect\_true](group__ztest__expect.md#gaef66b2764b6086dfbe8cbc933a8cfdc3)(cond, ...) |
|  | Expect that *cond* is true, otherwise mark test as failed but continue its execution. |
| #define | [zexpect\_false](group__ztest__expect.md#ga619bd320e39799414383a228dc2d8299)(cond, ...) |
|  | Expect that *cond* is false, otherwise mark test as failed but continue its execution. |
| #define | [zexpect\_ok](group__ztest__expect.md#gaab325ee22058252c6a1c3243f3226657)(cond, ...) |
|  | Expect that *cond* is 0 (success), otherwise mark test as failed but continue its execution. |
| #define | [zexpect\_not\_ok](group__ztest__expect.md#gabde5406775f05d5fcd135eb926969004)(cond, ...) |
|  | Expect that *cond* is not 0 (failure), otherwise mark test as failed but continue its execution. |
| #define | [zexpect\_is\_null](group__ztest__expect.md#ga10b2c904f1c68b816eae2ad53e2b9f90)(ptr, ...) |
|  | Expect that *ptr* is NULL, otherwise mark test as failed but continue its execution. |
| #define | [zexpect\_not\_null](group__ztest__expect.md#gaa51053fe2a07c6417db7952d7a594798)(ptr, ...) |
|  | Expect that *ptr* is not NULL, otherwise mark test as failed but continue its execution. |
| #define | [zexpect\_equal](group__ztest__expect.md#ga5ba65dbf95c204ed60694c5757db247f)(a, b, ...) |
|  | Expect that *a* equals *b*, otherwise mark test as failed but continue its execution. |
| #define | [zexpect\_not\_equal](group__ztest__expect.md#ga31d83ab89828a03aebe0d0dc003f5232)(a, b, ...) |
|  | Expect that *a* does not equal *b*, otherwise mark test as failed but continue its execution. |
| #define | [zexpect\_equal\_ptr](group__ztest__expect.md#gabf791d13c5781fc2215289d6dd925b3e)(a, b, ...) |
|  | Expect that *a* equals *b*, otherwise mark test as failed but continue its execution. |
| #define | [zexpect\_within](group__ztest__expect.md#ga907afb07269bbc444a3d8ffee46839b5)(a, b, delta, ...) |
|  | Expect that *a* is within *b* with delta *d*, otherwise mark test as failed but continue its execution. |
| #define | [zexpect\_between\_inclusive](group__ztest__expect.md#gac37ebea6a9c71e3666a4911ceea5c913)(a, lower, upper, ...) |
|  | Expect that *a* is greater than or equal to *l* and less than or equal to *u*, otherwise mark test as failed but continue its execution. |
| #define | [zexpect\_mem\_equal](group__ztest__expect.md#gaee52264e5f92a606a2a85f5fbb0a85fb)(buf, exp, size, ...) |
|  | Expect that 2 memory buffers have the same contents, otherwise mark test as failed but continue its execution. |
| #define | [zexpect\_str\_equal](group__ztest__expect.md#gacd5ef284610ca2027fc2e892243dfd38)(s1, s2, ...) |
|  | Expect that 2 strings have the same contents, otherwise mark test as failed but continue its execution. |

| Functions | |
| --- | --- |
| const char \* | [ztest\_relative\_filename](#a06a081e3d716be7e024973cbf305c14b) (const char \*file) |
| void | [ztest\_test\_fail](#acd6eb423f54dce8544f7c3b1618c0374) (void) |
| void | [ztest\_test\_skip](#ada3b1fcfa71db1bf7787c03ff45256d5) (void) |
| void | [ztest\_test\_expect\_fail](#a5c6bb493c88f7426a827889526dc0772) (void) |
| void | [ztest\_skip\_failed\_assumption](#a17537c79021fbc12e56b72ccec4b99c5) (void) |

## Detailed Description

Zephyr testing framework assertion macros.

## Function Documentation

## [◆ ](#a06a081e3d716be7e024973cbf305c14b)ztest\_relative\_filename()

| const char \* ztest\_relative\_filename | ( | const char \* | *file* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a17537c79021fbc12e56b72ccec4b99c5)ztest\_skip\_failed\_assumption()

| void ztest\_skip\_failed\_assumption | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a5c6bb493c88f7426a827889526dc0772)ztest\_test\_expect\_fail()

| void ztest\_test\_expect\_fail | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#acd6eb423f54dce8544f7c3b1618c0374)ztest\_test\_fail()

| void ztest\_test\_fail | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#ada3b1fcfa71db1bf7787c03ff45256d5)ztest\_test\_skip()

| void ztest\_test\_skip | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

- [subsys](dir_c85cb826952b1679a37b077c3741c8c1.md)
- [testsuite](dir_1abba8fd2d51532ae0fc663391fcb2bd.md)
- [ztest](dir_baac9b2eb462986e22d73d5689d3a238.md)
- [include](dir_c3f97f6cb043cb2f48a1d98a4dc6b6bd.md)
- [zephyr](dir_7f004fc53e18f085dec56f1200601760.md)
- [ztest\_assert.h](ztest__assert_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

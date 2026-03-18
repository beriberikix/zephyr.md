---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/tc__util_8h.html
original_path: doxygen/html/tc__util_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

tc\_util.h File Reference

`#include <[zephyr/kernel.h](include_2zephyr_2kernel_8h_source.md)>`  
`#include <[string.h](string_8h_source.md)>`  
`#include <[zephyr/sys/printk.h](printk_8h_source.md)>`

[Go to the source code of this file.](tc__util_8h_source.md)

| Macros | |
| --- | --- |
| #define | [PRINT\_DATA](#aec98e66470b575771ed484118095b692)(fmt, ...) |
| #define | [TC\_STR\_HELPER](#a91250f31fc327df207018b9c66493677)(x) |
| #define | [TC\_STR](#acd142b5f39b0d6fe5216440432ef2c72)(x) |
| #define | [TC\_PRINT\_RUNID](#a82cdb6d03f070075b576cbe1dab5e71a)   do {} while (0) |
|  | Report a Run ID. |
| #define | [PRINT\_LINE](#af72c5654279b3d1e227e8dec30411944) |
| #define | [TASK\_STACK\_SIZE](#a5486258f1f34d3baeda92a74b63c27c3)   (1024 \* 2) |
| #define | [FMT\_ERROR](#a8e446c4d4b1517a80c371ca370c56ac3)   "%s - %[s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d)@%d. " |
| #define | [TC\_PASS](#afb66a88e5d1e781aeb5aa9739a8fe868)   0 |
| #define | [TC\_FAIL](#a196c300c18de32c79d757131b579a3a5)   1 |
| #define | [TC\_SKIP](#abafb6d8cf1e1a3bb2247d5384d1d5461)   2 |
| #define | [TC\_FLAKY](#ac0108c70de44b3186c7ead1c1430b3d1)   3 |
| #define | [TC\_PASS\_STR](#a991995992ef5c23b7c6cf7138b394437)   "PASS" |
| #define | [TC\_FAIL\_STR](#ac5103b154fa450c478c2bf3f520cb8ff)   "FAIL" |
| #define | [TC\_SKIP\_STR](#a586f060684ebfc5db4105a30370a41d0)   "SKIP" |
| #define | [TC\_FLAKY\_STR](#a584cf09eac3d2fa3758924cb843cdbf5)   "FLAKY" |
| #define | [TC\_ERROR](#a6fcd0e6c5448a9198cdaed1e88e86e1b)(fmt, ...) |
| #define | [TC\_PRINT](#a31562104efbbaec65655dc0b661c0164)(fmt, ...) |
| #define | [TC\_SUMMARY\_PRINT](#a21b72e847828bb33f121df1f49d6049b)(fmt, ...) |
| #define | [TC\_START\_PRINT](#a84a358e0dffa73ee8008c082863b0019)(name) |
| #define | [TC\_START](#aa090341b412763239ae09ba1f7a52b3e)(name) |
| #define | [TC\_END](#a8efc6e62889487dc919facca8ec42ecf)(result, fmt, ...) |
| #define | [TC\_END\_PRINT](#a257c3ffdd1721ca67ec44f6b9e8d9641)(result, fmt, ...) |
| #define | [TC\_END\_RESULT](#a51a8593a108ecdec4e29cbe2169d3a6b)(result) |
| #define | [TC\_END\_RESULT\_CUSTOM](#ada1b9d646eb10dd40f23667a19a57714)(result, func) |
| #define | [TC\_SUITE\_PRINT](#a342b3d937894dfa380580b96b73664a4)(fmt, ...) |
| #define | [TC\_SUITE\_START](#a175563de07188c1cc549cf88b0e78575)(name) |
| #define | [TC\_SUITE\_END](#af972f5db041628380c3f8a66c1513bdc)(name, result) |
| #define | [TC\_END\_POST](#a4aa57b8a67f3d67de8aec48a268a12ae)(result) |
| #define | [TC\_END\_REPORT](#a3a7161b4346dd5e84a4a86d6ebdc0b9e)(result) |
| #define | [TC\_CMD\_DEFINE](#aeae77e3905136ee851f1907cae75b9d9)(name) |
| #define | [TC\_CMD\_ITEM](#a44c72e8abf49266ead1bd1c97121e76b)(name) |

| Functions | |
| --- | --- |
| static const char \* | [TC\_RESULT\_TO\_STR](#a9e2302e8d62cfefe7df86e62489efe29) (int result) |
| static void | [get\_start\_time\_cyc](#a497dd92db8a77681994baee1ba3f0847) (void) |
| static void | [get\_test\_duration\_ms](#ab6f8f2a5ffd8240715e1eef0dfd27907) (void) |
| static void | [print\_nothing](#a30c304c5caa2145085e83fdbd5fa24e4) (const char \*fmt,...) |

| Variables | |
| --- | --- |
| static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [tc\_start\_time](#ad3aec479c61df7656ae28f68aa4dc4a5) |
| static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [tc\_spend\_time](#a9bb8eafa6af5b875097421ba21a8dfc8) |

## Macro Definition Documentation

## [◆ ](#a8e446c4d4b1517a80c371ca370c56ac3)FMT\_ERROR

| #define FMT\_ERROR   "%s - %[s](asm-macro-32-bit-gnu_8h.md#a53a876d393ad3ed42cfeb2173695978d)@%d. " |
| --- |

## [◆ ](#aec98e66470b575771ed484118095b692)PRINT\_DATA

| #define PRINT\_DATA | ( |  | *fmt*, |
| --- | --- | --- | --- |
|  |  |  | ... ) |

**Value:**

[printk](printk_8h.md#a768a7dff8592b69f327a08f96b00fa54)(fmt, ##\_\_VA\_ARGS\_\_)

[printk](printk_8h.md#a768a7dff8592b69f327a08f96b00fa54)

static void printk(const char \*fmt,...)

Print kernel debugging message.

**Definition** printk.h:51

## [◆ ](#af72c5654279b3d1e227e8dec30411944)PRINT\_LINE

| #define PRINT\_LINE |
| --- |

**Value:**

[PRINT\_DATA](#aec98e66470b575771ed484118095b692)( \

"============================================================" \

"=======\n")

[PRINT\_DATA](#aec98e66470b575771ed484118095b692)

#define PRINT\_DATA(fmt,...)

**Definition** tc\_util.h:25

## [◆ ](#a5486258f1f34d3baeda92a74b63c27c3)TASK\_STACK\_SIZE

| #define TASK\_STACK\_SIZE   (1024 \* 2) |
| --- |

## [◆ ](#aeae77e3905136ee851f1907cae75b9d9)TC\_CMD\_DEFINE

| #define TC\_CMD\_DEFINE | ( |  | *name* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

int cmd\_##name(int argc, char \*argv[]) \

{ \

TC\_START(\_\_func\_\_); \

name(); \

TC\_END\_RESULT([TC\_PASS](#afb66a88e5d1e781aeb5aa9739a8fe868)); \

return 0; \

}

[TC\_PASS](#afb66a88e5d1e781aeb5aa9739a8fe868)

#define TC\_PASS

**Definition** tc\_util.h:67

## [◆ ](#a44c72e8abf49266ead1bd1c97121e76b)TC\_CMD\_ITEM

| #define TC\_CMD\_ITEM | ( |  | *name* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

{[STRINGIFY](common_8h.md#a4689212d5a549893cabb9d7782eecfb6)(name), cmd\_##name, "none"}

[STRINGIFY](common_8h.md#a4689212d5a549893cabb9d7782eecfb6)

#define STRINGIFY(s)

**Definition** common.h:134

## [◆ ](#a8efc6e62889487dc919facca8ec42ecf)TC\_END

| #define TC\_END | ( |  | *result*, |
| --- | --- | --- | --- |
|  |  |  | *fmt*, |
|  |  |  | ... ) |

**Value:**

[PRINT\_DATA](#aec98e66470b575771ed484118095b692)(fmt, ##\_\_VA\_ARGS\_\_)

## [◆ ](#a4aa57b8a67f3d67de8aec48a268a12ae)TC\_END\_POST

| #define TC\_END\_POST | ( |  | *result* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a257c3ffdd1721ca67ec44f6b9e8d9641)TC\_END\_PRINT

| #define TC\_END\_PRINT | ( |  | *result*, |
| --- | --- | --- | --- |
|  |  |  | *fmt*, |
|  |  |  | ... ) |

**Value:**

[print\_nothing](#a30c304c5caa2145085e83fdbd5fa24e4)(fmt)

[print\_nothing](#a30c304c5caa2145085e83fdbd5fa24e4)

static void print\_nothing(const char \*fmt,...)

**Definition** tc\_util.h:124

## [◆ ](#a3a7161b4346dd5e84a4a86d6ebdc0b9e)TC\_END\_REPORT

| #define TC\_END\_REPORT | ( |  | *result* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

do { \

[PRINT\_LINE](#af72c5654279b3d1e227e8dec30411944); \

[TC\_PRINT\_RUNID](#a82cdb6d03f070075b576cbe1dab5e71a); \

TC\_END(result, \

"PROJECT EXECUTION %s\n", \

(result) == [TC\_PASS](#afb66a88e5d1e781aeb5aa9739a8fe868) ? "SUCCESSFUL" : "FAILED"); \

TC\_END\_POST(result); \

} while (0)

[TC\_PRINT\_RUNID](#a82cdb6d03f070075b576cbe1dab5e71a)

#define TC\_PRINT\_RUNID

Report a Run ID.

**Definition** tc\_util.h:52

[PRINT\_LINE](#af72c5654279b3d1e227e8dec30411944)

#define PRINT\_LINE

**Definition** tc\_util.h:56

## [◆ ](#a51a8593a108ecdec4e29cbe2169d3a6b)TC\_END\_RESULT

| #define TC\_END\_RESULT | ( |  | *result* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

Z\_TC\_END\_RESULT((result), \_\_func\_\_)

## [◆ ](#ada1b9d646eb10dd40f23667a19a57714)TC\_END\_RESULT\_CUSTOM

| #define TC\_END\_RESULT\_CUSTOM | ( |  | *result*, |
| --- | --- | --- | --- |
|  |  |  | *func* ) |

**Value:**

Z\_TC\_END\_RESULT((result), func)

## [◆ ](#a6fcd0e6c5448a9198cdaed1e88e86e1b)TC\_ERROR

| #define TC\_ERROR | ( |  | *fmt*, |
| --- | --- | --- | --- |
|  |  |  | ... ) |

**Value:**

do { \

PRINT\_DATA([FMT\_ERROR](#a8e446c4d4b1517a80c371ca370c56ac3), "FAIL", \_\_func\_\_, \_\_LINE\_\_); \

PRINT\_DATA(fmt, ##\_\_VA\_ARGS\_\_); \

} while (0)

[FMT\_ERROR](#a8e446c4d4b1517a80c371ca370c56ac3)

#define FMT\_ERROR

**Definition** tc\_util.h:65

## [◆ ](#a196c300c18de32c79d757131b579a3a5)TC\_FAIL

| #define TC\_FAIL   1 |
| --- |

## [◆ ](#ac5103b154fa450c478c2bf3f520cb8ff)TC\_FAIL\_STR

| #define TC\_FAIL\_STR   "FAIL" |
| --- |

## [◆ ](#ac0108c70de44b3186c7ead1c1430b3d1)TC\_FLAKY

| #define TC\_FLAKY   3 |
| --- |

## [◆ ](#a584cf09eac3d2fa3758924cb843cdbf5)TC\_FLAKY\_STR

| #define TC\_FLAKY\_STR   "FLAKY" |
| --- |

## [◆ ](#afb66a88e5d1e781aeb5aa9739a8fe868)TC\_PASS

| #define TC\_PASS   0 |
| --- |

## [◆ ](#a991995992ef5c23b7c6cf7138b394437)TC\_PASS\_STR

| #define TC\_PASS\_STR   "PASS" |
| --- |

## [◆ ](#a31562104efbbaec65655dc0b661c0164)TC\_PRINT

| #define TC\_PRINT | ( |  | *fmt*, |
| --- | --- | --- | --- |
|  |  |  | ... ) |

**Value:**

[print\_nothing](#a30c304c5caa2145085e83fdbd5fa24e4)(fmt, ##\_\_VA\_ARGS\_\_)

## [◆ ](#a82cdb6d03f070075b576cbe1dab5e71a)TC\_PRINT\_RUNID

| #define TC\_PRINT\_RUNID   do {} while (0) |
| --- |

Report a Run ID.

When the CPP symbol `TC_RUNID` is defined (for example, from the compile environment), print the defined string RunID:
<TC\_RUNID> when called ([TC\_END\_REPORT()](#a3a7161b4346dd5e84a4a86d6ebdc0b9e) will also call it).

This is used mainly when automating the execution and running of multiple test cases, to verify that the expected image is being executed (as sometimes the targets fail to flash or reset properly).

TC\_RUNID is any string, that will be converted to a string literal.

## [◆ ](#abafb6d8cf1e1a3bb2247d5384d1d5461)TC\_SKIP

| #define TC\_SKIP   2 |
| --- |

## [◆ ](#a586f060684ebfc5db4105a30370a41d0)TC\_SKIP\_STR

| #define TC\_SKIP\_STR   "SKIP" |
| --- |

## [◆ ](#aa090341b412763239ae09ba1f7a52b3e)TC\_START

| #define TC\_START | ( |  | *name* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

do { \

TC\_START\_PRINT(name); \

} while (0)

## [◆ ](#a84a358e0dffa73ee8008c082863b0019)TC\_START\_PRINT

| #define TC\_START\_PRINT | ( |  | *name* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[print\_nothing](#a30c304c5caa2145085e83fdbd5fa24e4)(name)

## [◆ ](#acd142b5f39b0d6fe5216440432ef2c72)TC\_STR

| #define TC\_STR | ( |  | *x* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

[TC\_STR\_HELPER](#a91250f31fc327df207018b9c66493677)(x)

[TC\_STR\_HELPER](#a91250f31fc327df207018b9c66493677)

#define TC\_STR\_HELPER(x)

**Definition** tc\_util.h:47

## [◆ ](#a91250f31fc327df207018b9c66493677)TC\_STR\_HELPER

| #define TC\_STR\_HELPER | ( |  | *x* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

#x

## [◆ ](#af972f5db041628380c3f8a66c1513bdc)TC\_SUITE\_END

| #define TC\_SUITE\_END | ( |  | *name*, |
| --- | --- | --- | --- |
|  |  |  | *result* ) |

**Value:**

do { \

if (result != [TC\_FAIL](#a196c300c18de32c79d757131b579a3a5)) { \

TC\_SUITE\_PRINT("TESTSUITE %s succeeded\n", name); \

} else { \

TC\_SUITE\_PRINT("TESTSUITE %s failed.\n", name); \

} \

} while (0)

[TC\_FAIL](#a196c300c18de32c79d757131b579a3a5)

#define TC\_FAIL

**Definition** tc\_util.h:68

## [◆ ](#a342b3d937894dfa380580b96b73664a4)TC\_SUITE\_PRINT

| #define TC\_SUITE\_PRINT | ( |  | *fmt*, |
| --- | --- | --- | --- |
|  |  |  | ... ) |

**Value:**

[PRINT\_DATA](#aec98e66470b575771ed484118095b692)(fmt, ##\_\_VA\_ARGS\_\_)

## [◆ ](#a175563de07188c1cc549cf88b0e78575)TC\_SUITE\_START

| #define TC\_SUITE\_START | ( |  | *name* | ) |  |
| --- | --- | --- | --- | --- | --- |

**Value:**

do { \

TC\_SUITE\_PRINT("Running TESTSUITE %s\n", name); \

[PRINT\_LINE](#af72c5654279b3d1e227e8dec30411944); \

} while (0)

## [◆ ](#a21b72e847828bb33f121df1f49d6049b)TC\_SUMMARY\_PRINT

| #define TC\_SUMMARY\_PRINT | ( |  | *fmt*, |
| --- | --- | --- | --- |
|  |  |  | ... ) |

**Value:**

[PRINT\_DATA](#aec98e66470b575771ed484118095b692)(fmt, ##\_\_VA\_ARGS\_\_)

## Function Documentation

## [◆ ](#a497dd92db8a77681994baee1ba3f0847)get\_start\_time\_cyc()

| | void get\_start\_time\_cyc | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#ab6f8f2a5ffd8240715e1eef0dfd27907)get\_test\_duration\_ms()

| | void get\_test\_duration\_ms | ( | void |  | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a30c304c5caa2145085e83fdbd5fa24e4)print\_nothing()

| | void print\_nothing | ( | const char \* | *fmt*, | | --- | --- | --- | --- | |  |  |  | *...* ) | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

## [◆ ](#a9e2302e8d62cfefe7df86e62489efe29)TC\_RESULT\_TO\_STR()

| | const char \* TC\_RESULT\_TO\_STR | ( | int | *result* | ) |  | | --- | --- | --- | --- | --- | --- | | inlinestatic |
| --- | --- | --- | --- | --- | --- | --- | --- |

## Variable Documentation

## [◆ ](#a9bb8eafa6af5b875097421ba21a8dfc8)tc\_spend\_time

| | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) tc\_spend\_time | | --- | | static |
| --- | --- | --- |

## [◆ ](#ad3aec479c61df7656ae28f68aa4dc4a5)tc\_start\_time

| | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) tc\_start\_time | | --- | | static |
| --- | --- | --- |

- [subsys](dir_c85cb826952b1679a37b077c3741c8c1.md)
- [testsuite](dir_1abba8fd2d51532ae0fc663391fcb2bd.md)
- [include](dir_d5cd24c9babba9527629083c466f69cc.md)
- [zephyr](dir_91e5ce9bd56815b1bd388aa667b3762f.md)
- [tc\_util.h](tc__util_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

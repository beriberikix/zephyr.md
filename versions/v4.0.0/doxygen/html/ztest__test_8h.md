---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/ztest__test_8h.html
original_path: doxygen/html/ztest__test_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ztest\_test.h File Reference

Zephyr testing framework \_test.
[More...](#details)

`#include <[zephyr/app_memory/app_memdomain.h](app__memdomain_8h_source.md)>`  
`#include <[zephyr/init.h](init_8h_source.md)>`  
`#include <[zephyr/sys/iterable_sections.h](sys_2iterable__sections_8h_source.md)>`  
`#include <[stdbool.h](stdbool_8h_source.md)>`  
`#include <zephyr/syscalls/ztest_test.h>`

[Go to the source code of this file.](ztest__test_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [ztest\_expected\_result\_entry](structztest__expected__result__entry.md) |
|  | A single expectation entry allowing tests to fail/skip and be considered passing. [More...](structztest__expected__result__entry.md#details) |
| struct | [ztest\_unit\_test](structztest__unit__test.md) |
| struct | [ztest\_suite\_stats](structztest__suite__stats.md) |
|  | Stats about a ztest suite. [More...](structztest__suite__stats.md#details) |
| struct | [ztest\_unit\_test\_stats](structztest__unit__test__stats.md) |
| struct | [ztest\_suite\_node](structztest__suite__node.md) |
|  | A single node of test suite. [More...](structztest__suite__node.md#details) |
| struct | [ztest\_arch\_api](structztest__arch__api.md) |
|  | Structure for architecture specific APIs. [More...](structztest__arch__api.md#details) |

| Macros | |
| --- | --- |
| #define | [ZTEST\_EXPECT\_FAIL](group__ztest__test.md#gaeaa5b96855dd45e015b9556212f8945a)(\_suite\_name, \_test\_name) |
|  | Expect a test to fail (mark it passing if it failed). |
| #define | [ZTEST\_EXPECT\_SKIP](group__ztest__test.md#gacb6f06920e522b9a9f6e7a98f0620f38)(\_suite\_name, \_test\_name) |
|  | Expect a test to skip (mark it passing if it failed). |
| #define | [ZTEST\_TEST\_COUNT](group__ztest__test.md#ga8777ca60bd21cc128f64833bd7921b9c)   (\_ztest\_unit\_test\_list\_end - \_ztest\_unit\_test\_list\_start) |
|  | Number of registered unit tests. |
| #define | [ZTEST\_SUITE\_COUNT](group__ztest__test.md#ga678b4ae96879c029e6e567a326bbf027)   (\_ztest\_suite\_node\_list\_end - \_ztest\_suite\_node\_list\_start) |
|  | Number of registered test suites. |
| #define | [ZTEST\_SUITE](group__ztest__test.md#gaef8892743e2d47c983efcb61beeedeb3)(SUITE\_NAME, PREDICATE, setup\_fn, before\_fn, after\_fn, teardown\_fn) |
|  | Create and register a ztest suite. |
| #define | [ZTEST\_DMEM](group__ztest__test.md#ga2c7d0aa85e7f320d582395c5ded90133)   [K\_APP\_DMEM](group__mem__domain__apis__app.md#gace571a7f6ee313a732976cc863b5d0e6)([ztest\_mem\_partition](group__ztest__test.md#ga3adced2fdda96833e6b1ecbf3d61d446)) |
|  | Make data section used by Ztest userspace accessible. |
| #define | [ZTEST\_BMEM](group__ztest__test.md#gac3de5965061b1164a8033712c9094e23)   [K\_APP\_BMEM](group__mem__domain__apis__app.md#ga8fd691f9c9007ec80432c19f7ce84881)([ztest\_mem\_partition](group__ztest__test.md#ga3adced2fdda96833e6b1ecbf3d61d446)) |
|  | Make bss section used by Ztest userspace accessible. |
| #define | [ZTEST\_SECTION](group__ztest__test.md#ga44777f5011728bbff63fe3639c1b4aa8)   [K\_APP\_DMEM\_SECTION](group__mem__domain__apis__app.md#ga81962bb530118ffa13fccdf99f973787)([ztest\_mem\_partition](group__ztest__test.md#ga3adced2fdda96833e6b1ecbf3d61d446)) |
|  | Ztest data section for accessing data from userspace. |
| #define | [ZTEST\_P](group__ztest__test.md#gab80e25231b291b2c2b32e6049a52d34c)(suite, fn) |
| #define | [ZTEST](group__ztest__test.md#gac25858f76ea667d07de422a3b489cb15)(suite, fn) |
|  | Create and register a new unit test. |
| #define | [ZTEST\_USER](group__ztest__test.md#ga7121acc7ee00646cacefa773ff9631c8)(suite, fn) |
|  | Define a test function that should run as a user thread. |
| #define | [ZTEST\_F](group__ztest__test.md#gacd3ab522e0e5c8a270e86b0cb6bd81b2)(suite, fn) |
|  | Define a test function. |
| #define | [ZTEST\_USER\_F](group__ztest__test.md#ga12ccce144e577cac6ba763982ad14def)(suite, fn) |
|  | Define a test function that should run as a user thread. |
| #define | [ZTEST\_RULE](group__ztest__test.md#ga2a0a5e3b6e8fa1c9a03e7600895d875f)(name, before\_each\_fn, after\_each\_fn) |
|  | Define a test rule that will run before/after each unit test. |
| #define | [ztest\_run\_test\_suite](group__ztest__test.md#gac2ac069e393ea7480e78e85ed93238be)(suite, shuffle, suite\_iter, case\_iter, param) |
|  | Run the specified test suite. |

| Typedefs | |
| --- | --- |
| typedef void \*(\* | [ztest\_suite\_setup\_t](group__ztest__test.md#ga0063907dd70b9eb817ea472162693ee4)) (void) |
|  | Setup function to run before running this suite. |
| typedef void(\* | [ztest\_suite\_before\_t](group__ztest__test.md#gac8a204832c267fed047e7707b65be74d)) (void \*fixture) |
|  | Function to run before each test in this suite. |
| typedef void(\* | [ztest\_suite\_after\_t](group__ztest__test.md#ga0f9eeb8ddae455c1e7cc7a388a7b013c)) (void \*fixture) |
|  | Function to run after each test in this suite. |
| typedef void(\* | [ztest\_suite\_teardown\_t](group__ztest__test.md#ga7769b894fdac5283ac949ce8fceea0dd)) (void \*fixture) |
|  | Teardown function to run after running this suite. |
| typedef [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b)(\* | [ztest\_suite\_predicate\_t](group__ztest__test.md#gad5323aa82773dac33cf0930e9524420c)) (const void \*global\_state) |
|  | An optional predicate function to determine if the test should run. |
| typedef void(\* | [ztest\_rule\_cb](group__ztest__test.md#ga2090c493018a95112b89c5f83b5d8162)) (const struct [ztest\_unit\_test](structztest__unit__test.md) \*test, void \*data) |
|  | Test rule callback function signature. |

| Enumerations | |
| --- | --- |
| enum | [ztest\_expected\_result](group__ztest__test.md#gaf4dfaad1b5f1059e87f406979769aa26) { [ZTEST\_EXPECTED\_RESULT\_FAIL](group__ztest__test.md#ggaf4dfaad1b5f1059e87f406979769aa26a4d372c4fae4866c909e666173fa5be1d) = 0 , [ZTEST\_EXPECTED\_RESULT\_SKIP](group__ztest__test.md#ggaf4dfaad1b5f1059e87f406979769aa26a66f3e9393dbe9ca2607187a209e29b8a) } |
|  | The expected result of a test. [More...](group__ztest__test.md#gaf4dfaad1b5f1059e87f406979769aa26) |
| enum | [ztest\_result](group__ztest__test.md#gac2842295307e7286d256bb179be60b02) {     [ZTEST\_RESULT\_PENDING](group__ztest__test.md#ggac2842295307e7286d256bb179be60b02a8dac9ba9321cd8d0a3a61b52cbdb4cfc) , [ZTEST\_RESULT\_PASS](group__ztest__test.md#ggac2842295307e7286d256bb179be60b02a92cec4e702d9d4502e02f76c7071211e) , [ZTEST\_RESULT\_FAIL](group__ztest__test.md#ggac2842295307e7286d256bb179be60b02aa29639fb74516d8d112b9dade2422888) , [ZTEST\_RESULT\_SKIP](group__ztest__test.md#ggac2842295307e7286d256bb179be60b02a07327a99dd9daf709d9a28a5ea8316c4) ,     [ZTEST\_RESULT\_SUITE\_SKIP](group__ztest__test.md#ggac2842295307e7286d256bb179be60b02af5927209b63a89467df81ad9de245b5e) , [ZTEST\_RESULT\_SUITE\_FAIL](group__ztest__test.md#ggac2842295307e7286d256bb179be60b02ac09ff18a766e298ede6f7746f4704c55)   } |
|  | The result of the current running test. [More...](group__ztest__test.md#gac2842295307e7286d256bb179be60b02) |
| enum | [ztest\_phase](group__ztest__test.md#ga5dde8913cf45656bca8a48c825a95d59) {     [TEST\_PHASE\_SETUP](group__ztest__test.md#gga5dde8913cf45656bca8a48c825a95d59aa5a6af32f1f4bac30640934e1eb3b0bf) , [TEST\_PHASE\_BEFORE](group__ztest__test.md#gga5dde8913cf45656bca8a48c825a95d59a78c54591383696b200d6a4582619b765) , [TEST\_PHASE\_TEST](group__ztest__test.md#gga5dde8913cf45656bca8a48c825a95d59a1dc3378deb96d78130b2ecc0cd966bd1) , [TEST\_PHASE\_AFTER](group__ztest__test.md#gga5dde8913cf45656bca8a48c825a95d59a46c899f020982afc47164237a36a1663) ,     [TEST\_PHASE\_TEARDOWN](group__ztest__test.md#gga5dde8913cf45656bca8a48c825a95d59aaf847259cdce47813e155c3523e36901) , [TEST\_PHASE\_FRAMEWORK](group__ztest__test.md#gga5dde8913cf45656bca8a48c825a95d59ad5efde89d69e093341de2a6a823e3971)   } |
|  | Each enum member represents a distinct phase of execution for the test binary. [More...](group__ztest__test.md#ga5dde8913cf45656bca8a48c825a95d59) |

| Functions | |
| --- | --- |
| void | [ztest\_run\_all](group__ztest__test.md#gac6b1f8b820cd682094b7aaeebdaa106e) (const void \*[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90), [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) shuffle, int suite\_iter, int case\_iter) |
|  | Default entry point for running or listing registered unit tests. |
| int | [ztest\_run\_test\_suites](group__ztest__test.md#gaafb3cba3a9637839952b2db2486ab88c) (const void \*[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90), [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) shuffle, int suite\_iter, int case\_iter) |
|  | Run the registered unit tests which return true from their predicate function. |
| void | [ztest\_verify\_all\_test\_suites\_ran](group__ztest__test.md#ga349fda278dff713debfd2a3b94b8b1eb) (void) |
|  | Fails the test if any of the registered tests did not run. |
| void | [ztest\_test\_fail](group__ztest__test.md#gacd6eb423f54dce8544f7c3b1618c0374) (void) |
|  | Fail the currently running test. |
| void | [ztest\_test\_pass](group__ztest__test.md#ga085d30a04102ebb8c3f2206020723ee0) (void) |
|  | Pass the currently running test. |
| void | [ztest\_test\_skip](group__ztest__test.md#gada3b1fcfa71db1bf7787c03ff45256d5) (void) |
|  | Skip the current test. |
| void | [ztest\_skip\_failed\_assumption](group__ztest__test.md#ga17537c79021fbc12e56b72ccec4b99c5) (void) |
| void | [ztest\_simple\_1cpu\_before](group__ztest__test.md#gac7ddc33b5a0d11e2ffa0a564019c5e3d) (void \*data) |
|  | A 'before' function to use in test suites that just need to start 1cpu. |
| void | [ztest\_simple\_1cpu\_after](group__ztest__test.md#gaa53486873430dd8fa978745d8a1d0686) (void \*data) |
|  | A 'after' function to use in test suites that just need to stop 1cpu. |
| void | [sys\_clock\_tick\_set](#a846fcbfbda9794cba2dcf1c34bd9be1b) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) tick) |

| Variables | |
| --- | --- |
| struct [k\_mem\_partition](structk__mem__partition.md) | [ztest\_mem\_partition](group__ztest__test.md#ga3adced2fdda96833e6b1ecbf3d61d446) |

## Detailed Description

Zephyr testing framework \_test.

## Function Documentation

## [◆ ](#a846fcbfbda9794cba2dcf1c34bd9be1b)sys\_clock\_tick\_set()

| void sys\_clock\_tick\_set | ( | [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | *tick* | ) |  |
| --- | --- | --- | --- | --- | --- |

- [subsys](dir_c85cb826952b1679a37b077c3741c8c1.md)
- [testsuite](dir_1abba8fd2d51532ae0fc663391fcb2bd.md)
- [ztest](dir_baac9b2eb462986e22d73d5689d3a238.md)
- [include](dir_c3f97f6cb043cb2f48a1d98a4dc6b6bd.md)
- [zephyr](dir_7f004fc53e18f085dec56f1200601760.md)
- [ztest\_test.h](ztest__test_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

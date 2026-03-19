---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/group__timeutil__unit__apis.html
original_path: doxygen/html/group__timeutil__unit__apis.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

Time Units Helpers

[Utilities](group__utilities.md) » [Time Utility APIs](group__timeutil__apis.md)

Various helper APIs for converting between time units.
[More...](#details)

| Macros | |
| --- | --- |
| #define | [SYS\_FOREVER\_MS](#ga9f9c4c41f62c7578a30209475201efed)   (-1) |
|  | System-wide macro to denote "forever" in milliseconds. |
| #define | [SYS\_FOREVER\_US](#gad8743aaa97d3b2650908020ffb76ef0e)   (-1) |
|  | System-wide macro to denote "forever" in microseconds. |
| #define | [SYS\_TIMEOUT\_MS](#ga6504e9e6fe4955e0bc31eccd4cfc01b7)(ms) |
|  | System-wide macro to convert milliseconds to kernel timeouts. |
| #define | [TIME\_CONSTEXPR](#ga387f15169fe1c0c58745548eceae1556) |
| #define | [sys\_clock\_hw\_cycles\_per\_sec](#gafe3ef19636d5002350794fa01b480d16)() |
|  | Get the system timer frequency. |
| #define | [k\_sec\_to\_cyc\_floor32](#ga38efeb3c71b28e98c6f18f63a2c59334)(t) |
|  | Convert seconds to hardware cycles. |
| #define | [k\_sec\_to\_cyc\_floor64](#gaa9b2ed48e2b68d509a4eee305cdcd2fe)(t) |
|  | Convert seconds to hardware cycles. |
| #define | [k\_sec\_to\_cyc\_near32](#ga5a6ec23bd5644867f211eb5f47d81a3e)(t) |
|  | Convert seconds to hardware cycles. |
| #define | [k\_sec\_to\_cyc\_near64](#gab1722b870ef8c9ed1084f104974c83a3)(t) |
|  | Convert seconds to hardware cycles. |
| #define | [k\_sec\_to\_cyc\_ceil32](#ga197fe61819a3c51802f080187a39f2d5)(t) |
|  | Convert seconds to hardware cycles. |
| #define | [k\_sec\_to\_cyc\_ceil64](#ga363ec5ce8d2365d25107e4c630222a9a)(t) |
|  | Convert seconds to hardware cycles. |
| #define | [k\_sec\_to\_ticks\_floor32](#gab6a57f08409edf9fba80837c3da34fb8)(t) |
|  | Convert seconds to ticks. |
| #define | [k\_sec\_to\_ticks\_floor64](#gafee9fc110890fba84640acac74af6717)(t) |
|  | Convert seconds to ticks. |
| #define | [k\_sec\_to\_ticks\_near32](#ga4fbbf706ce9a69ab8b2b09bd3b0d4a3e)(t) |
|  | Convert seconds to ticks. |
| #define | [k\_sec\_to\_ticks\_near64](#gafbdfa2986e27ea95b0347319e8a23c68)(t) |
|  | Convert seconds to ticks. |
| #define | [k\_sec\_to\_ticks\_ceil32](#ga20d46aec38239513826d5d5259b5836c)(t) |
|  | Convert seconds to ticks. |
| #define | [k\_sec\_to\_ticks\_ceil64](#gad382b2d98f84705c4c4e7a775bb549e8)(t) |
|  | Convert seconds to ticks. |
| #define | [k\_ms\_to\_cyc\_floor32](#ga2d60494645102034a7864ab0235bbfe4)(t) |
|  | Convert milliseconds to hardware cycles. |
| #define | [k\_ms\_to\_cyc\_floor64](#ga4d3e1ec8eed229a08072aea744d40bba)(t) |
|  | Convert milliseconds to hardware cycles. |
| #define | [k\_ms\_to\_cyc\_near32](#ga8a0d31e998f1a19a3ee8200c173eb7c9)(t) |
|  | Convert milliseconds to hardware cycles. |
| #define | [k\_ms\_to\_cyc\_near64](#gab2bcf34a4899619fcf083819a078a09e)(t) |
|  | Convert milliseconds to hardware cycles. |
| #define | [k\_ms\_to\_cyc\_ceil32](#gab4636150867df2c4e918c12ec2e9bc5f)(t) |
|  | Convert milliseconds to hardware cycles. |
| #define | [k\_ms\_to\_cyc\_ceil64](#ga82829fc9e99658faf91e5925c9545c9f)(t) |
|  | Convert milliseconds to hardware cycles. |
| #define | [k\_ms\_to\_ticks\_floor32](#gaf41d7ca19e5bb47824374698ce409ea1)(t) |
|  | Convert milliseconds to ticks. |
| #define | [k\_ms\_to\_ticks\_floor64](#gaa6ea6977308dfd2f092ba0ac4e779a31)(t) |
|  | Convert milliseconds to ticks. |
| #define | [k\_ms\_to\_ticks\_near32](#ga0a61385f187c7c2a0f5288b17873b3db)(t) |
|  | Convert milliseconds to ticks. |
| #define | [k\_ms\_to\_ticks\_near64](#gab2f6dd223151224cd9fa0491f196c1f6)(t) |
|  | Convert milliseconds to ticks. |
| #define | [k\_ms\_to\_ticks\_ceil32](#gac74a319bcb69cc714818413ae15af7a2)(t) |
|  | Convert milliseconds to ticks. |
| #define | [k\_ms\_to\_ticks\_ceil64](#gaa623d51d51b18a2e54b20d36d2f81c42)(t) |
|  | Convert milliseconds to ticks. |
| #define | [k\_us\_to\_cyc\_floor32](#ga66c1ea8197e7adc01c837163e0aa4b62)(t) |
|  | Convert microseconds to hardware cycles. |
| #define | [k\_us\_to\_cyc\_floor64](#gac78731d5891b2389dc227608decf28dd)(t) |
|  | Convert microseconds to hardware cycles. |
| #define | [k\_us\_to\_cyc\_near32](#ga01dabb87e1a4864e47fcd39cc4bce869)(t) |
|  | Convert microseconds to hardware cycles. |
| #define | [k\_us\_to\_cyc\_near64](#ga49a64e1f11cf450fdd770d67617cbe23)(t) |
|  | Convert microseconds to hardware cycles. |
| #define | [k\_us\_to\_cyc\_ceil32](#ga689a3f97643be5362c8c70c6d9d81051)(t) |
|  | Convert microseconds to hardware cycles. |
| #define | [k\_us\_to\_cyc\_ceil64](#ga2f65f04acc1daf019470beb04f16e276)(t) |
|  | Convert microseconds to hardware cycles. |
| #define | [k\_us\_to\_ticks\_floor32](#ga96f32803affb56c366cbab5967c6b76c)(t) |
|  | Convert microseconds to ticks. |
| #define | [k\_us\_to\_ticks\_floor64](#gaf6b4fb83131e5a52d9be875e5466d022)(t) |
|  | Convert microseconds to ticks. |
| #define | [k\_us\_to\_ticks\_near32](#ga5b0286cc82370178c852c3fa290eb61d)(t) |
|  | Convert microseconds to ticks. |
| #define | [k\_us\_to\_ticks\_near64](#gaf2aae5316fcb5e99f4a77b99a5db27f9)(t) |
|  | Convert microseconds to ticks. |
| #define | [k\_us\_to\_ticks\_ceil32](#ga950ac5ce654ec92e0af61e000de884a7)(t) |
|  | Convert microseconds to ticks. |
| #define | [k\_us\_to\_ticks\_ceil64](#ga1a977f93dc94ce9db54b3c9fdf9ba2f9)(t) |
|  | Convert microseconds to ticks. |
| #define | [k\_ns\_to\_cyc\_floor32](#ga46013e42990cfa561da06fb2bffaa261)(t) |
|  | Convert nanoseconds to hardware cycles. |
| #define | [k\_ns\_to\_cyc\_floor64](#gafc4ff458df5f4d1f221bcf0799d25335)(t) |
|  | Convert nanoseconds to hardware cycles. |
| #define | [k\_ns\_to\_cyc\_near32](#gac8e586ebc94174ccdabf6f49dd0251e6)(t) |
|  | Convert nanoseconds to hardware cycles. |
| #define | [k\_ns\_to\_cyc\_near64](#gae6ec742a39a72b0a3dd7bc3da4a98403)(t) |
|  | Convert nanoseconds to hardware cycles. |
| #define | [k\_ns\_to\_cyc\_ceil32](#ga928ace6a14c0c2eb6aaa027f545601a7)(t) |
|  | Convert nanoseconds to hardware cycles. |
| #define | [k\_ns\_to\_cyc\_ceil64](#ga82264e42744defb8acf69caa8612e476)(t) |
|  | Convert nanoseconds to hardware cycles. |
| #define | [k\_ns\_to\_ticks\_floor32](#ga4b0a61273dfbebd9273c0dc71ea74c65)(t) |
|  | Convert nanoseconds to ticks. |
| #define | [k\_ns\_to\_ticks\_floor64](#ga6089738092396227384c2dbb2510e002)(t) |
|  | Convert nanoseconds to ticks. |
| #define | [k\_ns\_to\_ticks\_near32](#ga308b172f1fb6e1452c14db444ad7e75e)(t) |
|  | Convert nanoseconds to ticks. |
| #define | [k\_ns\_to\_ticks\_near64](#ga50c08351970ea8e62a0509b68898901a)(t) |
|  | Convert nanoseconds to ticks. |
| #define | [k\_ns\_to\_ticks\_ceil32](#gad958afbd9f86f94ccd5c9569e7587fad)(t) |
|  | Convert nanoseconds to ticks. |
| #define | [k\_ns\_to\_ticks\_ceil64](#ga1078f0f8764f7bad744cfb1ffd675c70)(t) |
|  | Convert nanoseconds to ticks. |
| #define | [k\_cyc\_to\_sec\_floor32](#ga7a83cefe2d1e0828c6cdf949d4be9674)(t) |
|  | Convert hardware cycles to seconds. |
| #define | [k\_cyc\_to\_sec\_floor64](#gadb48b4c005c8e4f1a30f018192fe4ae5)(t) |
|  | Convert hardware cycles to seconds. |
| #define | [k\_cyc\_to\_sec\_near32](#ga41d9d97ae4abc59eb235626682b767c9)(t) |
|  | Convert hardware cycles to seconds. |
| #define | [k\_cyc\_to\_sec\_near64](#ga8dccd0c590fb4c2c399b0e0a120a5753)(t) |
|  | Convert hardware cycles to seconds. |
| #define | [k\_cyc\_to\_sec\_ceil32](#gaeaf83a64009e2a834b0d65ead788e856)(t) |
|  | Convert hardware cycles to seconds. |
| #define | [k\_cyc\_to\_sec\_ceil64](#ga2c64ffb238dd5047413d394b39900d61)(t) |
|  | Convert hardware cycles to seconds. |
| #define | [k\_cyc\_to\_ms\_floor32](#ga5f9f903e6e4eba5415cae3f337d565ed)(t) |
|  | Convert hardware cycles to milliseconds. |
| #define | [k\_cyc\_to\_ms\_floor64](#gaeaa9339beec5b82b924302bbc57923f6)(t) |
|  | Convert hardware cycles to milliseconds. |
| #define | [k\_cyc\_to\_ms\_near32](#gaba2f18bc00740fb0411371d2d2f3d949)(t) |
|  | Convert hardware cycles to milliseconds. |
| #define | [k\_cyc\_to\_ms\_near64](#ga217f0b8bf86a24654419c3ccfd6e7822)(t) |
|  | Convert hardware cycles to milliseconds. |
| #define | [k\_cyc\_to\_ms\_ceil32](#ga40bf11b01ba76673c67569e8d1e55d92)(t) |
|  | Convert hardware cycles to milliseconds. |
| #define | [k\_cyc\_to\_ms\_ceil64](#gaf85474dc07ce8165379415f4977aa44f)(t) |
|  | Convert hardware cycles to milliseconds. |
| #define | [k\_cyc\_to\_us\_floor32](#ga86392f2bddfbb7c895c08becf9c8c485)(t) |
|  | Convert hardware cycles to microseconds. |
| #define | [k\_cyc\_to\_us\_floor64](#gad3376aa7ab36b6b7f5a1f9c9977cee4a)(t) |
|  | Convert hardware cycles to microseconds. |
| #define | [k\_cyc\_to\_us\_near32](#ga1314249a8a404f00c8a03d6c77e0c752)(t) |
|  | Convert hardware cycles to microseconds. |
| #define | [k\_cyc\_to\_us\_near64](#ga869ccaf50e83712d0bafe0f8e238fc61)(t) |
|  | Convert hardware cycles to microseconds. |
| #define | [k\_cyc\_to\_us\_ceil32](#ga051fbec0b352b4fb3116544c8c33250a)(t) |
|  | Convert hardware cycles to microseconds. |
| #define | [k\_cyc\_to\_us\_ceil64](#ga90b09be4536f6877f67a60b3c33f5299)(t) |
|  | Convert hardware cycles to microseconds. |
| #define | [k\_cyc\_to\_ns\_floor32](#ga775c4d72bd0ecb9a6ad947f34c479754)(t) |
|  | Convert hardware cycles to nanoseconds. |
| #define | [k\_cyc\_to\_ns\_floor64](#ga665d5fc98ffe8bd1cf78ca994f58724a)(t) |
|  | Convert hardware cycles to nanoseconds. |
| #define | [k\_cyc\_to\_ns\_near32](#gabd5378a62e480fc1b79b3326c8f02d5f)(t) |
|  | Convert hardware cycles to nanoseconds. |
| #define | [k\_cyc\_to\_ns\_near64](#gad36269d0d63bee37e09da46cfe516c8c)(t) |
|  | Convert hardware cycles to nanoseconds. |
| #define | [k\_cyc\_to\_ns\_ceil32](#ga19526c845440ed793068fa8d8d5088ff)(t) |
|  | Convert hardware cycles to nanoseconds. |
| #define | [k\_cyc\_to\_ns\_ceil64](#gab2889da75f359d248a6eb61fdc3d53c0)(t) |
|  | Convert hardware cycles to nanoseconds. |
| #define | [k\_cyc\_to\_ticks\_floor32](#ga2efd0e2611cbeb696778eb73cf24b7ee)(t) |
|  | Convert hardware cycles to ticks. |
| #define | [k\_cyc\_to\_ticks\_floor64](#gaad0256d9429dfa5c5a194f1419691cfc)(t) |
|  | Convert hardware cycles to ticks. |
| #define | [k\_cyc\_to\_ticks\_near32](#ga4601ea99148307043d2d47a2e9fccb8e)(t) |
|  | Convert hardware cycles to ticks. |
| #define | [k\_cyc\_to\_ticks\_near64](#gafa97757f07a5048d67d6eca4a72cf39c)(t) |
|  | Convert hardware cycles to ticks. |
| #define | [k\_cyc\_to\_ticks\_ceil32](#gae7653e92b9b44accaa9ee2764237f595)(t) |
|  | Convert hardware cycles to ticks. |
| #define | [k\_cyc\_to\_ticks\_ceil64](#ga0fa410ff13d0cd467d160c1c14cf24a6)(t) |
|  | Convert hardware cycles to ticks. |
| #define | [k\_ticks\_to\_sec\_floor32](#ga824ffc9857fa2d4bccb3a9f4a56b8f18)(t) |
|  | Convert ticks to seconds. |
| #define | [k\_ticks\_to\_sec\_floor64](#ga6e9ef943c78cbb5963d8eece896b6189)(t) |
|  | Convert ticks to seconds. |
| #define | [k\_ticks\_to\_sec\_near32](#ga15284161d40816f06b2bbf4cd03a0fed)(t) |
|  | Convert ticks to seconds. |
| #define | [k\_ticks\_to\_sec\_near64](#gab6b9b6d752ec3c8b69d9f27ca5f7b85e)(t) |
|  | Convert ticks to seconds. |
| #define | [k\_ticks\_to\_sec\_ceil32](#ga3986215ef060ab2ff9cc7c576eb05b01)(t) |
|  | Convert ticks to seconds. |
| #define | [k\_ticks\_to\_sec\_ceil64](#ga02493c454fbbbf6787b036ca7f739073)(t) |
|  | Convert ticks to seconds. |
| #define | [k\_ticks\_to\_ms\_floor32](#ga6ecf0ab60ac29c60d6a6b66a45c86664)(t) |
|  | Convert ticks to milliseconds. |
| #define | [k\_ticks\_to\_ms\_floor64](#gac417ab53d5d493d95e24e7f777f8a4e0)(t) |
|  | Convert ticks to milliseconds. |
| #define | [k\_ticks\_to\_ms\_near32](#ga8f1133f69f154d593fc127d2b00931c8)(t) |
|  | Convert ticks to milliseconds. |
| #define | [k\_ticks\_to\_ms\_near64](#gac3578501567233a7576c61cfd6cf28cb)(t) |
|  | Convert ticks to milliseconds. |
| #define | [k\_ticks\_to\_ms\_ceil32](#ga3f2c3cf86ef1d243b43f29958a108088)(t) |
|  | Convert ticks to milliseconds. |
| #define | [k\_ticks\_to\_ms\_ceil64](#gabee58122304820b36d601268eb4598e2)(t) |
|  | Convert ticks to milliseconds. |
| #define | [k\_ticks\_to\_us\_floor32](#ga86767fd65071fc7c57f25434386caeed)(t) |
|  | Convert ticks to microseconds. |
| #define | [k\_ticks\_to\_us\_floor64](#ga27cac5d9974320ef12c6bcacdae8b47c)(t) |
|  | Convert ticks to microseconds. |
| #define | [k\_ticks\_to\_us\_near32](#ga328649dd1ec1fae9c69eb3a75709a9f2)(t) |
|  | Convert ticks to microseconds. |
| #define | [k\_ticks\_to\_us\_near64](#ga5735cb347e01fa391368d2fb54d6d965)(t) |
|  | Convert ticks to microseconds. |
| #define | [k\_ticks\_to\_us\_ceil32](#gadd968c2033d548c03072e46c895375bc)(t) |
|  | Convert ticks to microseconds. |
| #define | [k\_ticks\_to\_us\_ceil64](#gad1c6d9e60835c6c00960778395cdbacc)(t) |
|  | Convert ticks to microseconds. |
| #define | [k\_ticks\_to\_ns\_floor32](#ga5c2a1ae6f66fcf22971c40301e78be8a)(t) |
|  | Convert ticks to nanoseconds. |
| #define | [k\_ticks\_to\_ns\_floor64](#ga8c8c4d713c5716e5b0d41b014b394edf)(t) |
|  | Convert ticks to nanoseconds. |
| #define | [k\_ticks\_to\_ns\_near32](#ga26c20d96c08dc26d4664f3d66507e0bb)(t) |
|  | Convert ticks to nanoseconds. |
| #define | [k\_ticks\_to\_ns\_near64](#ga3b0a2f92a3d61be64d4b80101129bc83)(t) |
|  | Convert ticks to nanoseconds. |
| #define | [k\_ticks\_to\_ns\_ceil32](#gae28b7099ffbda7617f4049cd730921f8)(t) |
|  | Convert ticks to nanoseconds. |
| #define | [k\_ticks\_to\_ns\_ceil64](#ga0221878e17c689e7f40940a201c4fdd7)(t) |
|  | Convert ticks to nanoseconds. |
| #define | [k\_ticks\_to\_cyc\_floor32](#ga629a18a817e4b0240dc6bc9018d8809a)(t) |
|  | Convert ticks to hardware cycles. |
| #define | [k\_ticks\_to\_cyc\_floor64](#ga5593c0751ec707a63ce25aed1567b2de)(t) |
|  | Convert ticks to hardware cycles. |
| #define | [k\_ticks\_to\_cyc\_near32](#gaf8d7352f4d2325ddb3aec3111cc8e124)(t) |
|  | Convert ticks to hardware cycles. |
| #define | [k\_ticks\_to\_cyc\_near64](#ga7eed234908b9db5236de6c7543f40da1)(t) |
|  | Convert ticks to hardware cycles. |
| #define | [k\_ticks\_to\_cyc\_ceil32](#ga00f31f894f66dde999714fe0cbab2178)(t) |
|  | Convert ticks to hardware cycles. |
| #define | [k\_ticks\_to\_cyc\_ceil64](#ga4fa97b6aa81457142fc82cc73ef6c7a5)(t) |
|  | Convert ticks to hardware cycles. |

## Detailed Description

Various helper APIs for converting between time units.

## Macro Definition Documentation

## [◆ ](#ga40bf11b01ba76673c67569e8d1e55d92)k\_cyc\_to\_ms\_ceil32

| #define k\_cyc\_to\_ms\_ceil32 | ( |  | *t* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[time_units.h](time__units_8h.md)>`

**Value:**

z\_tmcvt\_32(t, Z\_HZ\_cyc, Z\_HZ\_ms, Z\_CCYC, true, false)

Convert hardware cycles to milliseconds.

32 bits. Rounds up.

Converts time values in hardware cycles to milliseconds. Computes result in 32 bit precision. Rounds up to the next highest output unit.

Warning
:   Generated. Do not edit. See above.

Parameters
:   | t | Source time in hardware cycles. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) |
    | --- | --- |

Returns
:   The converted time value in milliseconds. [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

## [◆ ](#gaf85474dc07ce8165379415f4977aa44f)k\_cyc\_to\_ms\_ceil64

| #define k\_cyc\_to\_ms\_ceil64 | ( |  | *t* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[time_units.h](time__units_8h.md)>`

**Value:**

z\_tmcvt\_64(t, Z\_HZ\_cyc, Z\_HZ\_ms, Z\_CCYC, true, false)

Convert hardware cycles to milliseconds.

64 bits. Rounds up.

Converts time values in hardware cycles to milliseconds. Computes result in 64 bit precision. Rounds up to the next highest output unit.

Warning
:   Generated. Do not edit. See above.

Parameters
:   | t | Source time in hardware cycles. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) |
    | --- | --- |

Returns
:   The converted time value in milliseconds. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

## [◆ ](#ga5f9f903e6e4eba5415cae3f337d565ed)k\_cyc\_to\_ms\_floor32

| #define k\_cyc\_to\_ms\_floor32 | ( |  | *t* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[time_units.h](time__units_8h.md)>`

**Value:**

z\_tmcvt\_32(t, Z\_HZ\_cyc, Z\_HZ\_ms, Z\_CCYC, false, false)

Convert hardware cycles to milliseconds.

32 bits. Truncates.

Converts time values in hardware cycles to milliseconds. Computes result in 32 bit precision. Truncates to the next lowest output unit.

Warning
:   Generated. Do not edit. See above.

Parameters
:   | t | Source time in hardware cycles. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) |
    | --- | --- |

Returns
:   The converted time value in milliseconds. [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

## [◆ ](#gaeaa9339beec5b82b924302bbc57923f6)k\_cyc\_to\_ms\_floor64

| #define k\_cyc\_to\_ms\_floor64 | ( |  | *t* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[time_units.h](time__units_8h.md)>`

**Value:**

z\_tmcvt\_64(t, Z\_HZ\_cyc, Z\_HZ\_ms, Z\_CCYC, false, false)

Convert hardware cycles to milliseconds.

64 bits. Truncates.

Converts time values in hardware cycles to milliseconds. Computes result in 64 bit precision. Truncates to the next lowest output unit.

Warning
:   Generated. Do not edit. See above.

Parameters
:   | t | Source time in hardware cycles. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) |
    | --- | --- |

Returns
:   The converted time value in milliseconds. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

## [◆ ](#gaba2f18bc00740fb0411371d2d2f3d949)k\_cyc\_to\_ms\_near32

| #define k\_cyc\_to\_ms\_near32 | ( |  | *t* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[time_units.h](time__units_8h.md)>`

**Value:**

z\_tmcvt\_32(t, Z\_HZ\_cyc, Z\_HZ\_ms, Z\_CCYC, false, true)

Convert hardware cycles to milliseconds.

32 bits. Round nearest.

Converts time values in hardware cycles to milliseconds. Computes result in 32 bit precision. Rounds to the nearest output unit.

Warning
:   Generated. Do not edit. See above.

Parameters
:   | t | Source time in hardware cycles. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) |
    | --- | --- |

Returns
:   The converted time value in milliseconds. [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

## [◆ ](#ga217f0b8bf86a24654419c3ccfd6e7822)k\_cyc\_to\_ms\_near64

| #define k\_cyc\_to\_ms\_near64 | ( |  | *t* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[time_units.h](time__units_8h.md)>`

**Value:**

z\_tmcvt\_64(t, Z\_HZ\_cyc, Z\_HZ\_ms, Z\_CCYC, false, true)

Convert hardware cycles to milliseconds.

64 bits. Round nearest.

Converts time values in hardware cycles to milliseconds. Computes result in 64 bit precision. Rounds to the nearest output unit.

Warning
:   Generated. Do not edit. See above.

Parameters
:   | t | Source time in hardware cycles. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) |
    | --- | --- |

Returns
:   The converted time value in milliseconds. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

## [◆ ](#ga19526c845440ed793068fa8d8d5088ff)k\_cyc\_to\_ns\_ceil32

| #define k\_cyc\_to\_ns\_ceil32 | ( |  | *t* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[time_units.h](time__units_8h.md)>`

**Value:**

z\_tmcvt\_32(t, Z\_HZ\_cyc, Z\_HZ\_ns, Z\_CCYC, true, false)

Convert hardware cycles to nanoseconds.

32 bits. Rounds up.

Converts time values in hardware cycles to nanoseconds. Computes result in 32 bit precision. Rounds up to the next highest output unit.

Warning
:   Generated. Do not edit. See above.

Parameters
:   | t | Source time in hardware cycles. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) |
    | --- | --- |

Returns
:   The converted time value in nanoseconds. [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

## [◆ ](#gab2889da75f359d248a6eb61fdc3d53c0)k\_cyc\_to\_ns\_ceil64

| #define k\_cyc\_to\_ns\_ceil64 | ( |  | *t* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[time_units.h](time__units_8h.md)>`

**Value:**

z\_tmcvt\_64(t, Z\_HZ\_cyc, Z\_HZ\_ns, Z\_CCYC, true, false)

Convert hardware cycles to nanoseconds.

64 bits. Rounds up.

Converts time values in hardware cycles to nanoseconds. Computes result in 64 bit precision. Rounds up to the next highest output unit.

Warning
:   Generated. Do not edit. See above.

Parameters
:   | t | Source time in hardware cycles. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) |
    | --- | --- |

Returns
:   The converted time value in nanoseconds. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

## [◆ ](#ga775c4d72bd0ecb9a6ad947f34c479754)k\_cyc\_to\_ns\_floor32

| #define k\_cyc\_to\_ns\_floor32 | ( |  | *t* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[time_units.h](time__units_8h.md)>`

**Value:**

z\_tmcvt\_32(t, Z\_HZ\_cyc, Z\_HZ\_ns, Z\_CCYC, false, false)

Convert hardware cycles to nanoseconds.

32 bits. Truncates.

Converts time values in hardware cycles to nanoseconds. Computes result in 32 bit precision. Truncates to the next lowest output unit.

Warning
:   Generated. Do not edit. See above.

Parameters
:   | t | Source time in hardware cycles. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) |
    | --- | --- |

Returns
:   The converted time value in nanoseconds. [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

## [◆ ](#ga665d5fc98ffe8bd1cf78ca994f58724a)k\_cyc\_to\_ns\_floor64

| #define k\_cyc\_to\_ns\_floor64 | ( |  | *t* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[time_units.h](time__units_8h.md)>`

**Value:**

z\_tmcvt\_64(t, Z\_HZ\_cyc, Z\_HZ\_ns, Z\_CCYC, false, false)

Convert hardware cycles to nanoseconds.

64 bits. Truncates.

Converts time values in hardware cycles to nanoseconds. Computes result in 64 bit precision. Truncates to the next lowest output unit.

Warning
:   Generated. Do not edit. See above.

Parameters
:   | t | Source time in hardware cycles. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) |
    | --- | --- |

Returns
:   The converted time value in nanoseconds. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

## [◆ ](#gabd5378a62e480fc1b79b3326c8f02d5f)k\_cyc\_to\_ns\_near32

| #define k\_cyc\_to\_ns\_near32 | ( |  | *t* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[time_units.h](time__units_8h.md)>`

**Value:**

z\_tmcvt\_32(t, Z\_HZ\_cyc, Z\_HZ\_ns, Z\_CCYC, false, true)

Convert hardware cycles to nanoseconds.

32 bits. Round nearest.

Converts time values in hardware cycles to nanoseconds. Computes result in 32 bit precision. Rounds to the nearest output unit.

Warning
:   Generated. Do not edit. See above.

Parameters
:   | t | Source time in hardware cycles. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) |
    | --- | --- |

Returns
:   The converted time value in nanoseconds. [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

## [◆ ](#gad36269d0d63bee37e09da46cfe516c8c)k\_cyc\_to\_ns\_near64

| #define k\_cyc\_to\_ns\_near64 | ( |  | *t* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[time_units.h](time__units_8h.md)>`

**Value:**

z\_tmcvt\_64(t, Z\_HZ\_cyc, Z\_HZ\_ns, Z\_CCYC, false, true)

Convert hardware cycles to nanoseconds.

64 bits. Round nearest.

Converts time values in hardware cycles to nanoseconds. Computes result in 64 bit precision. Rounds to the nearest output unit.

Warning
:   Generated. Do not edit. See above.

Parameters
:   | t | Source time in hardware cycles. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) |
    | --- | --- |

Returns
:   The converted time value in nanoseconds. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

## [◆ ](#gaeaf83a64009e2a834b0d65ead788e856)k\_cyc\_to\_sec\_ceil32

| #define k\_cyc\_to\_sec\_ceil32 | ( |  | *t* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[time_units.h](time__units_8h.md)>`

**Value:**

z\_tmcvt\_32(t, Z\_HZ\_cyc, Z\_HZ\_sec, Z\_CCYC, true, false)

Convert hardware cycles to seconds.

32 bits. Rounds up.

Converts time values in hardware cycles to seconds. Computes result in 32 bit precision. Rounds up to the next highest output unit.

Warning
:   Generated. Do not edit. See above.

Parameters
:   | t | Source time in hardware cycles. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) |
    | --- | --- |

Returns
:   The converted time value in seconds. [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

## [◆ ](#ga2c64ffb238dd5047413d394b39900d61)k\_cyc\_to\_sec\_ceil64

| #define k\_cyc\_to\_sec\_ceil64 | ( |  | *t* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[time_units.h](time__units_8h.md)>`

**Value:**

z\_tmcvt\_64(t, Z\_HZ\_cyc, Z\_HZ\_sec, Z\_CCYC, true, false)

Convert hardware cycles to seconds.

64 bits. Rounds up.

Converts time values in hardware cycles to seconds. Computes result in 64 bit precision. Rounds up to the next highest output unit.

Warning
:   Generated. Do not edit. See above.

Parameters
:   | t | Source time in hardware cycles. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) |
    | --- | --- |

Returns
:   The converted time value in seconds. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

## [◆ ](#ga7a83cefe2d1e0828c6cdf949d4be9674)k\_cyc\_to\_sec\_floor32

| #define k\_cyc\_to\_sec\_floor32 | ( |  | *t* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[time_units.h](time__units_8h.md)>`

**Value:**

z\_tmcvt\_32(t, Z\_HZ\_cyc, Z\_HZ\_sec, Z\_CCYC, false, false)

Convert hardware cycles to seconds.

32 bits. Truncates.

Converts time values in hardware cycles to seconds. Computes result in 32 bit precision. Truncates to the next lowest output unit.

Warning
:   Generated. Do not edit. See above.

Parameters
:   | t | Source time in hardware cycles. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) |
    | --- | --- |

Returns
:   The converted time value in seconds. [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

## [◆ ](#gadb48b4c005c8e4f1a30f018192fe4ae5)k\_cyc\_to\_sec\_floor64

| #define k\_cyc\_to\_sec\_floor64 | ( |  | *t* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[time_units.h](time__units_8h.md)>`

**Value:**

z\_tmcvt\_64(t, Z\_HZ\_cyc, Z\_HZ\_sec, Z\_CCYC, false, false)

Convert hardware cycles to seconds.

64 bits. Truncates.

Converts time values in hardware cycles to seconds. Computes result in 64 bit precision. Truncates to the next lowest output unit.

Warning
:   Generated. Do not edit. See above.

Parameters
:   | t | Source time in hardware cycles. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) |
    | --- | --- |

Returns
:   The converted time value in seconds. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

## [◆ ](#ga41d9d97ae4abc59eb235626682b767c9)k\_cyc\_to\_sec\_near32

| #define k\_cyc\_to\_sec\_near32 | ( |  | *t* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[time_units.h](time__units_8h.md)>`

**Value:**

z\_tmcvt\_32(t, Z\_HZ\_cyc, Z\_HZ\_sec, Z\_CCYC, false, true)

Convert hardware cycles to seconds.

32 bits. Round nearest.

Converts time values in hardware cycles to seconds. Computes result in 32 bit precision. Rounds to the nearest output unit.

Warning
:   Generated. Do not edit. See above.

Parameters
:   | t | Source time in hardware cycles. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) |
    | --- | --- |

Returns
:   The converted time value in seconds. [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

## [◆ ](#ga8dccd0c590fb4c2c399b0e0a120a5753)k\_cyc\_to\_sec\_near64

| #define k\_cyc\_to\_sec\_near64 | ( |  | *t* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[time_units.h](time__units_8h.md)>`

**Value:**

z\_tmcvt\_64(t, Z\_HZ\_cyc, Z\_HZ\_sec, Z\_CCYC, false, true)

Convert hardware cycles to seconds.

64 bits. Round nearest.

Converts time values in hardware cycles to seconds. Computes result in 64 bit precision. Rounds to the nearest output unit.

Warning
:   Generated. Do not edit. See above.

Parameters
:   | t | Source time in hardware cycles. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) |
    | --- | --- |

Returns
:   The converted time value in seconds. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

## [◆ ](#gae7653e92b9b44accaa9ee2764237f595)k\_cyc\_to\_ticks\_ceil32

| #define k\_cyc\_to\_ticks\_ceil32 | ( |  | *t* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[time_units.h](time__units_8h.md)>`

**Value:**

z\_tmcvt\_32(t, Z\_HZ\_cyc, Z\_HZ\_ticks, Z\_CCYC, true, false)

Convert hardware cycles to ticks.

32 bits. Rounds up.

Converts time values in hardware cycles to ticks. Computes result in 32 bit precision. Rounds up to the next highest output unit.

Warning
:   Generated. Do not edit. See above.

Parameters
:   | t | Source time in hardware cycles. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) |
    | --- | --- |

Returns
:   The converted time value in ticks. [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

## [◆ ](#ga0fa410ff13d0cd467d160c1c14cf24a6)k\_cyc\_to\_ticks\_ceil64

| #define k\_cyc\_to\_ticks\_ceil64 | ( |  | *t* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[time_units.h](time__units_8h.md)>`

**Value:**

z\_tmcvt\_64(t, Z\_HZ\_cyc, Z\_HZ\_ticks, Z\_CCYC, true, false)

Convert hardware cycles to ticks.

64 bits. Rounds up.

Converts time values in hardware cycles to ticks. Computes result in 64 bit precision. Rounds up to the next highest output unit.

Warning
:   Generated. Do not edit. See above.

Parameters
:   | t | Source time in hardware cycles. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) |
    | --- | --- |

Returns
:   The converted time value in ticks. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

## [◆ ](#ga2efd0e2611cbeb696778eb73cf24b7ee)k\_cyc\_to\_ticks\_floor32

| #define k\_cyc\_to\_ticks\_floor32 | ( |  | *t* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[time_units.h](time__units_8h.md)>`

**Value:**

z\_tmcvt\_32(t, Z\_HZ\_cyc, Z\_HZ\_ticks, Z\_CCYC, false, false)

Convert hardware cycles to ticks.

32 bits. Truncates.

Converts time values in hardware cycles to ticks. Computes result in 32 bit precision. Truncates to the next lowest output unit.

Warning
:   Generated. Do not edit. See above.

Parameters
:   | t | Source time in hardware cycles. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) |
    | --- | --- |

Returns
:   The converted time value in ticks. [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

## [◆ ](#gaad0256d9429dfa5c5a194f1419691cfc)k\_cyc\_to\_ticks\_floor64

| #define k\_cyc\_to\_ticks\_floor64 | ( |  | *t* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[time_units.h](time__units_8h.md)>`

**Value:**

z\_tmcvt\_64(t, Z\_HZ\_cyc, Z\_HZ\_ticks, Z\_CCYC, false, false)

Convert hardware cycles to ticks.

64 bits. Truncates.

Converts time values in hardware cycles to ticks. Computes result in 64 bit precision. Truncates to the next lowest output unit.

Warning
:   Generated. Do not edit. See above.

Parameters
:   | t | Source time in hardware cycles. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) |
    | --- | --- |

Returns
:   The converted time value in ticks. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

## [◆ ](#ga4601ea99148307043d2d47a2e9fccb8e)k\_cyc\_to\_ticks\_near32

| #define k\_cyc\_to\_ticks\_near32 | ( |  | *t* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[time_units.h](time__units_8h.md)>`

**Value:**

z\_tmcvt\_32(t, Z\_HZ\_cyc, Z\_HZ\_ticks, Z\_CCYC, false, true)

Convert hardware cycles to ticks.

32 bits. Round nearest.

Converts time values in hardware cycles to ticks. Computes result in 32 bit precision. Rounds to the nearest output unit.

Warning
:   Generated. Do not edit. See above.

Parameters
:   | t | Source time in hardware cycles. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) |
    | --- | --- |

Returns
:   The converted time value in ticks. [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

## [◆ ](#gafa97757f07a5048d67d6eca4a72cf39c)k\_cyc\_to\_ticks\_near64

| #define k\_cyc\_to\_ticks\_near64 | ( |  | *t* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[time_units.h](time__units_8h.md)>`

**Value:**

z\_tmcvt\_64(t, Z\_HZ\_cyc, Z\_HZ\_ticks, Z\_CCYC, false, true)

Convert hardware cycles to ticks.

64 bits. Round nearest.

Converts time values in hardware cycles to ticks. Computes result in 64 bit precision. Rounds to the nearest output unit.

Warning
:   Generated. Do not edit. See above.

Parameters
:   | t | Source time in hardware cycles. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) |
    | --- | --- |

Returns
:   The converted time value in ticks. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

## [◆ ](#ga051fbec0b352b4fb3116544c8c33250a)k\_cyc\_to\_us\_ceil32

| #define k\_cyc\_to\_us\_ceil32 | ( |  | *t* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[time_units.h](time__units_8h.md)>`

**Value:**

z\_tmcvt\_32(t, Z\_HZ\_cyc, Z\_HZ\_us, Z\_CCYC, true, false)

Convert hardware cycles to microseconds.

32 bits. Rounds up.

Converts time values in hardware cycles to microseconds. Computes result in 32 bit precision. Rounds up to the next highest output unit.

Warning
:   Generated. Do not edit. See above.

Parameters
:   | t | Source time in hardware cycles. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) |
    | --- | --- |

Returns
:   The converted time value in microseconds. [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

## [◆ ](#ga90b09be4536f6877f67a60b3c33f5299)k\_cyc\_to\_us\_ceil64

| #define k\_cyc\_to\_us\_ceil64 | ( |  | *t* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[time_units.h](time__units_8h.md)>`

**Value:**

z\_tmcvt\_64(t, Z\_HZ\_cyc, Z\_HZ\_us, Z\_CCYC, true, false)

Convert hardware cycles to microseconds.

64 bits. Rounds up.

Converts time values in hardware cycles to microseconds. Computes result in 64 bit precision. Rounds up to the next highest output unit.

Warning
:   Generated. Do not edit. See above.

Parameters
:   | t | Source time in hardware cycles. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) |
    | --- | --- |

Returns
:   The converted time value in microseconds. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

## [◆ ](#ga86392f2bddfbb7c895c08becf9c8c485)k\_cyc\_to\_us\_floor32

| #define k\_cyc\_to\_us\_floor32 | ( |  | *t* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[time_units.h](time__units_8h.md)>`

**Value:**

z\_tmcvt\_32(t, Z\_HZ\_cyc, Z\_HZ\_us, Z\_CCYC, false, false)

Convert hardware cycles to microseconds.

32 bits. Truncates.

Converts time values in hardware cycles to microseconds. Computes result in 32 bit precision. Truncates to the next lowest output unit.

Warning
:   Generated. Do not edit. See above.

Parameters
:   | t | Source time in hardware cycles. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) |
    | --- | --- |

Returns
:   The converted time value in microseconds. [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

## [◆ ](#gad3376aa7ab36b6b7f5a1f9c9977cee4a)k\_cyc\_to\_us\_floor64

| #define k\_cyc\_to\_us\_floor64 | ( |  | *t* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[time_units.h](time__units_8h.md)>`

**Value:**

z\_tmcvt\_64(t, Z\_HZ\_cyc, Z\_HZ\_us, Z\_CCYC, false, false)

Convert hardware cycles to microseconds.

64 bits. Truncates.

Converts time values in hardware cycles to microseconds. Computes result in 64 bit precision. Truncates to the next lowest output unit.

Warning
:   Generated. Do not edit. See above.

Parameters
:   | t | Source time in hardware cycles. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) |
    | --- | --- |

Returns
:   The converted time value in microseconds. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

## [◆ ](#ga1314249a8a404f00c8a03d6c77e0c752)k\_cyc\_to\_us\_near32

| #define k\_cyc\_to\_us\_near32 | ( |  | *t* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[time_units.h](time__units_8h.md)>`

**Value:**

z\_tmcvt\_32(t, Z\_HZ\_cyc, Z\_HZ\_us, Z\_CCYC, false, true)

Convert hardware cycles to microseconds.

32 bits. Round nearest.

Converts time values in hardware cycles to microseconds. Computes result in 32 bit precision. Rounds to the nearest output unit.

Warning
:   Generated. Do not edit. See above.

Parameters
:   | t | Source time in hardware cycles. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) |
    | --- | --- |

Returns
:   The converted time value in microseconds. [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

## [◆ ](#ga869ccaf50e83712d0bafe0f8e238fc61)k\_cyc\_to\_us\_near64

| #define k\_cyc\_to\_us\_near64 | ( |  | *t* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[time_units.h](time__units_8h.md)>`

**Value:**

z\_tmcvt\_64(t, Z\_HZ\_cyc, Z\_HZ\_us, Z\_CCYC, false, true)

Convert hardware cycles to microseconds.

64 bits. Round nearest.

Converts time values in hardware cycles to microseconds. Computes result in 64 bit precision. Rounds to the nearest output unit.

Warning
:   Generated. Do not edit. See above.

Parameters
:   | t | Source time in hardware cycles. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) |
    | --- | --- |

Returns
:   The converted time value in microseconds. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

## [◆ ](#gab4636150867df2c4e918c12ec2e9bc5f)k\_ms\_to\_cyc\_ceil32

| #define k\_ms\_to\_cyc\_ceil32 | ( |  | *t* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[time_units.h](time__units_8h.md)>`

**Value:**

z\_tmcvt\_32(t, Z\_HZ\_ms, Z\_HZ\_cyc, Z\_CCYC, true, false)

Convert milliseconds to hardware cycles.

32 bits. Rounds up.

Converts time values in milliseconds to hardware cycles. Computes result in 32 bit precision. Rounds up to the next highest output unit.

Warning
:   Generated. Do not edit. See above.

Parameters
:   | t | Source time in milliseconds. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) |
    | --- | --- |

Returns
:   The converted time value in hardware cycles. [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

## [◆ ](#ga82829fc9e99658faf91e5925c9545c9f)k\_ms\_to\_cyc\_ceil64

| #define k\_ms\_to\_cyc\_ceil64 | ( |  | *t* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[time_units.h](time__units_8h.md)>`

**Value:**

z\_tmcvt\_64(t, Z\_HZ\_ms, Z\_HZ\_cyc, Z\_CCYC, true, false)

Convert milliseconds to hardware cycles.

64 bits. Rounds up.

Converts time values in milliseconds to hardware cycles. Computes result in 64 bit precision. Rounds up to the next highest output unit.

Warning
:   Generated. Do not edit. See above.

Parameters
:   | t | Source time in milliseconds. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) |
    | --- | --- |

Returns
:   The converted time value in hardware cycles. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

## [◆ ](#ga2d60494645102034a7864ab0235bbfe4)k\_ms\_to\_cyc\_floor32

| #define k\_ms\_to\_cyc\_floor32 | ( |  | *t* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[time_units.h](time__units_8h.md)>`

**Value:**

z\_tmcvt\_32(t, Z\_HZ\_ms, Z\_HZ\_cyc, Z\_CCYC, false, false)

Convert milliseconds to hardware cycles.

32 bits. Truncates.

Converts time values in milliseconds to hardware cycles. Computes result in 32 bit precision. Truncates to the next lowest output unit.

Warning
:   Generated. Do not edit. See above.

Parameters
:   | t | Source time in milliseconds. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) |
    | --- | --- |

Returns
:   The converted time value in hardware cycles. [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

## [◆ ](#ga4d3e1ec8eed229a08072aea744d40bba)k\_ms\_to\_cyc\_floor64

| #define k\_ms\_to\_cyc\_floor64 | ( |  | *t* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[time_units.h](time__units_8h.md)>`

**Value:**

z\_tmcvt\_64(t, Z\_HZ\_ms, Z\_HZ\_cyc, Z\_CCYC, false, false)

Convert milliseconds to hardware cycles.

64 bits. Truncates.

Converts time values in milliseconds to hardware cycles. Computes result in 64 bit precision. Truncates to the next lowest output unit.

Warning
:   Generated. Do not edit. See above.

Parameters
:   | t | Source time in milliseconds. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) |
    | --- | --- |

Returns
:   The converted time value in hardware cycles. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

## [◆ ](#ga8a0d31e998f1a19a3ee8200c173eb7c9)k\_ms\_to\_cyc\_near32

| #define k\_ms\_to\_cyc\_near32 | ( |  | *t* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[time_units.h](time__units_8h.md)>`

**Value:**

z\_tmcvt\_32(t, Z\_HZ\_ms, Z\_HZ\_cyc, Z\_CCYC, false, true)

Convert milliseconds to hardware cycles.

32 bits. Round nearest.

Converts time values in milliseconds to hardware cycles. Computes result in 32 bit precision. Rounds to the nearest output unit.

Warning
:   Generated. Do not edit. See above.

Parameters
:   | t | Source time in milliseconds. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) |
    | --- | --- |

Returns
:   The converted time value in hardware cycles. [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

## [◆ ](#gab2bcf34a4899619fcf083819a078a09e)k\_ms\_to\_cyc\_near64

| #define k\_ms\_to\_cyc\_near64 | ( |  | *t* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[time_units.h](time__units_8h.md)>`

**Value:**

z\_tmcvt\_64(t, Z\_HZ\_ms, Z\_HZ\_cyc, Z\_CCYC, false, true)

Convert milliseconds to hardware cycles.

64 bits. Round nearest.

Converts time values in milliseconds to hardware cycles. Computes result in 64 bit precision. Rounds to the nearest output unit.

Warning
:   Generated. Do not edit. See above.

Parameters
:   | t | Source time in milliseconds. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) |
    | --- | --- |

Returns
:   The converted time value in hardware cycles. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

## [◆ ](#gac74a319bcb69cc714818413ae15af7a2)k\_ms\_to\_ticks\_ceil32

| #define k\_ms\_to\_ticks\_ceil32 | ( |  | *t* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[time_units.h](time__units_8h.md)>`

**Value:**

z\_tmcvt\_32(t, Z\_HZ\_ms, Z\_HZ\_ticks, true, true, false)

Convert milliseconds to ticks.

32 bits. Rounds up.

Converts time values in milliseconds to ticks. Computes result in 32 bit precision. Rounds up to the next highest output unit.

Warning
:   Generated. Do not edit. See above.

Parameters
:   | t | Source time in milliseconds. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) |
    | --- | --- |

Returns
:   The converted time value in ticks. [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

## [◆ ](#gaa623d51d51b18a2e54b20d36d2f81c42)k\_ms\_to\_ticks\_ceil64

| #define k\_ms\_to\_ticks\_ceil64 | ( |  | *t* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[time_units.h](time__units_8h.md)>`

**Value:**

z\_tmcvt\_64(t, Z\_HZ\_ms, Z\_HZ\_ticks, true, true, false)

Convert milliseconds to ticks.

64 bits. Rounds up.

Converts time values in milliseconds to ticks. Computes result in 64 bit precision. Rounds up to the next highest output unit.

Warning
:   Generated. Do not edit. See above.

Parameters
:   | t | Source time in milliseconds. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) |
    | --- | --- |

Returns
:   The converted time value in ticks. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

## [◆ ](#gaf41d7ca19e5bb47824374698ce409ea1)k\_ms\_to\_ticks\_floor32

| #define k\_ms\_to\_ticks\_floor32 | ( |  | *t* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[time_units.h](time__units_8h.md)>`

**Value:**

z\_tmcvt\_32(t, Z\_HZ\_ms, Z\_HZ\_ticks, true, false, false)

Convert milliseconds to ticks.

32 bits. Truncates.

Converts time values in milliseconds to ticks. Computes result in 32 bit precision. Truncates to the next lowest output unit.

Warning
:   Generated. Do not edit. See above.

Parameters
:   | t | Source time in milliseconds. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) |
    | --- | --- |

Returns
:   The converted time value in ticks. [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

## [◆ ](#gaa6ea6977308dfd2f092ba0ac4e779a31)k\_ms\_to\_ticks\_floor64

| #define k\_ms\_to\_ticks\_floor64 | ( |  | *t* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[time_units.h](time__units_8h.md)>`

**Value:**

z\_tmcvt\_64(t, Z\_HZ\_ms, Z\_HZ\_ticks, true, false, false)

Convert milliseconds to ticks.

64 bits. Truncates.

Converts time values in milliseconds to ticks. Computes result in 64 bit precision. Truncates to the next lowest output unit.

Warning
:   Generated. Do not edit. See above.

Parameters
:   | t | Source time in milliseconds. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) |
    | --- | --- |

Returns
:   The converted time value in ticks. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

## [◆ ](#ga0a61385f187c7c2a0f5288b17873b3db)k\_ms\_to\_ticks\_near32

| #define k\_ms\_to\_ticks\_near32 | ( |  | *t* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[time_units.h](time__units_8h.md)>`

**Value:**

z\_tmcvt\_32(t, Z\_HZ\_ms, Z\_HZ\_ticks, true, false, true)

Convert milliseconds to ticks.

32 bits. Round nearest.

Converts time values in milliseconds to ticks. Computes result in 32 bit precision. Rounds to the nearest output unit.

Warning
:   Generated. Do not edit. See above.

Parameters
:   | t | Source time in milliseconds. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) |
    | --- | --- |

Returns
:   The converted time value in ticks. [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

## [◆ ](#gab2f6dd223151224cd9fa0491f196c1f6)k\_ms\_to\_ticks\_near64

| #define k\_ms\_to\_ticks\_near64 | ( |  | *t* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[time_units.h](time__units_8h.md)>`

**Value:**

z\_tmcvt\_64(t, Z\_HZ\_ms, Z\_HZ\_ticks, true, false, true)

Convert milliseconds to ticks.

64 bits. Round nearest.

Converts time values in milliseconds to ticks. Computes result in 64 bit precision. Rounds to the nearest output unit.

Warning
:   Generated. Do not edit. See above.

Parameters
:   | t | Source time in milliseconds. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) |
    | --- | --- |

Returns
:   The converted time value in ticks. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

## [◆ ](#ga928ace6a14c0c2eb6aaa027f545601a7)k\_ns\_to\_cyc\_ceil32

| #define k\_ns\_to\_cyc\_ceil32 | ( |  | *t* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[time_units.h](time__units_8h.md)>`

**Value:**

z\_tmcvt\_32(t, Z\_HZ\_ns, Z\_HZ\_cyc, Z\_CCYC, true, false)

Convert nanoseconds to hardware cycles.

32 bits. Rounds up.

Converts time values in nanoseconds to hardware cycles. Computes result in 32 bit precision. Rounds up to the next highest output unit.

Warning
:   Generated. Do not edit. See above.

Parameters
:   | t | Source time in nanoseconds. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) |
    | --- | --- |

Returns
:   The converted time value in hardware cycles. [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

## [◆ ](#ga82264e42744defb8acf69caa8612e476)k\_ns\_to\_cyc\_ceil64

| #define k\_ns\_to\_cyc\_ceil64 | ( |  | *t* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[time_units.h](time__units_8h.md)>`

**Value:**

z\_tmcvt\_64(t, Z\_HZ\_ns, Z\_HZ\_cyc, Z\_CCYC, true, false)

Convert nanoseconds to hardware cycles.

64 bits. Rounds up.

Converts time values in nanoseconds to hardware cycles. Computes result in 64 bit precision. Rounds up to the next highest output unit.

Warning
:   Generated. Do not edit. See above.

Parameters
:   | t | Source time in nanoseconds. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) |
    | --- | --- |

Returns
:   The converted time value in hardware cycles. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

## [◆ ](#ga46013e42990cfa561da06fb2bffaa261)k\_ns\_to\_cyc\_floor32

| #define k\_ns\_to\_cyc\_floor32 | ( |  | *t* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[time_units.h](time__units_8h.md)>`

**Value:**

z\_tmcvt\_32(t, Z\_HZ\_ns, Z\_HZ\_cyc, Z\_CCYC, false, false)

Convert nanoseconds to hardware cycles.

32 bits. Truncates.

Converts time values in nanoseconds to hardware cycles. Computes result in 32 bit precision. Truncates to the next lowest output unit.

Warning
:   Generated. Do not edit. See above.

Parameters
:   | t | Source time in nanoseconds. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) |
    | --- | --- |

Returns
:   The converted time value in hardware cycles. [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

## [◆ ](#gafc4ff458df5f4d1f221bcf0799d25335)k\_ns\_to\_cyc\_floor64

| #define k\_ns\_to\_cyc\_floor64 | ( |  | *t* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[time_units.h](time__units_8h.md)>`

**Value:**

z\_tmcvt\_64(t, Z\_HZ\_ns, Z\_HZ\_cyc, Z\_CCYC, false, false)

Convert nanoseconds to hardware cycles.

64 bits. Truncates.

Converts time values in nanoseconds to hardware cycles. Computes result in 64 bit precision. Truncates to the next lowest output unit.

Warning
:   Generated. Do not edit. See above.

Parameters
:   | t | Source time in nanoseconds. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) |
    | --- | --- |

Returns
:   The converted time value in hardware cycles. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

## [◆ ](#gac8e586ebc94174ccdabf6f49dd0251e6)k\_ns\_to\_cyc\_near32

| #define k\_ns\_to\_cyc\_near32 | ( |  | *t* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[time_units.h](time__units_8h.md)>`

**Value:**

z\_tmcvt\_32(t, Z\_HZ\_ns, Z\_HZ\_cyc, Z\_CCYC, false, true)

Convert nanoseconds to hardware cycles.

32 bits. Round nearest.

Converts time values in nanoseconds to hardware cycles. Computes result in 32 bit precision. Rounds to the nearest output unit.

Warning
:   Generated. Do not edit. See above.

Parameters
:   | t | Source time in nanoseconds. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) |
    | --- | --- |

Returns
:   The converted time value in hardware cycles. [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

## [◆ ](#gae6ec742a39a72b0a3dd7bc3da4a98403)k\_ns\_to\_cyc\_near64

| #define k\_ns\_to\_cyc\_near64 | ( |  | *t* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[time_units.h](time__units_8h.md)>`

**Value:**

z\_tmcvt\_64(t, Z\_HZ\_ns, Z\_HZ\_cyc, Z\_CCYC, false, true)

Convert nanoseconds to hardware cycles.

64 bits. Round nearest.

Converts time values in nanoseconds to hardware cycles. Computes result in 64 bit precision. Rounds to the nearest output unit.

Warning
:   Generated. Do not edit. See above.

Parameters
:   | t | Source time in nanoseconds. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) |
    | --- | --- |

Returns
:   The converted time value in hardware cycles. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

## [◆ ](#gad958afbd9f86f94ccd5c9569e7587fad)k\_ns\_to\_ticks\_ceil32

| #define k\_ns\_to\_ticks\_ceil32 | ( |  | *t* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[time_units.h](time__units_8h.md)>`

**Value:**

z\_tmcvt\_32(t, Z\_HZ\_ns, Z\_HZ\_ticks, true, true, false)

Convert nanoseconds to ticks.

32 bits. Rounds up.

Converts time values in nanoseconds to ticks. Computes result in 32 bit precision. Rounds up to the next highest output unit.

Warning
:   Generated. Do not edit. See above.

Parameters
:   | t | Source time in nanoseconds. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) |
    | --- | --- |

Returns
:   The converted time value in ticks. [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

## [◆ ](#ga1078f0f8764f7bad744cfb1ffd675c70)k\_ns\_to\_ticks\_ceil64

| #define k\_ns\_to\_ticks\_ceil64 | ( |  | *t* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[time_units.h](time__units_8h.md)>`

**Value:**

z\_tmcvt\_64(t, Z\_HZ\_ns, Z\_HZ\_ticks, true, true, false)

Convert nanoseconds to ticks.

64 bits. Rounds up.

Converts time values in nanoseconds to ticks. Computes result in 64 bit precision. Rounds up to the next highest output unit.

Warning
:   Generated. Do not edit. See above.

Parameters
:   | t | Source time in nanoseconds. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) |
    | --- | --- |

Returns
:   The converted time value in ticks. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

## [◆ ](#ga4b0a61273dfbebd9273c0dc71ea74c65)k\_ns\_to\_ticks\_floor32

| #define k\_ns\_to\_ticks\_floor32 | ( |  | *t* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[time_units.h](time__units_8h.md)>`

**Value:**

z\_tmcvt\_32(t, Z\_HZ\_ns, Z\_HZ\_ticks, true, false, false)

Convert nanoseconds to ticks.

32 bits. Truncates.

Converts time values in nanoseconds to ticks. Computes result in 32 bit precision. Truncates to the next lowest output unit.

Warning
:   Generated. Do not edit. See above.

Parameters
:   | t | Source time in nanoseconds. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) |
    | --- | --- |

Returns
:   The converted time value in ticks. [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

## [◆ ](#ga6089738092396227384c2dbb2510e002)k\_ns\_to\_ticks\_floor64

| #define k\_ns\_to\_ticks\_floor64 | ( |  | *t* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[time_units.h](time__units_8h.md)>`

**Value:**

z\_tmcvt\_64(t, Z\_HZ\_ns, Z\_HZ\_ticks, true, false, false)

Convert nanoseconds to ticks.

64 bits. Truncates.

Converts time values in nanoseconds to ticks. Computes result in 64 bit precision. Truncates to the next lowest output unit.

Warning
:   Generated. Do not edit. See above.

Parameters
:   | t | Source time in nanoseconds. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) |
    | --- | --- |

Returns
:   The converted time value in ticks. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

## [◆ ](#ga308b172f1fb6e1452c14db444ad7e75e)k\_ns\_to\_ticks\_near32

| #define k\_ns\_to\_ticks\_near32 | ( |  | *t* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[time_units.h](time__units_8h.md)>`

**Value:**

z\_tmcvt\_32(t, Z\_HZ\_ns, Z\_HZ\_ticks, true, false, true)

Convert nanoseconds to ticks.

32 bits. Round nearest.

Converts time values in nanoseconds to ticks. Computes result in 32 bit precision. Rounds to the nearest output unit.

Warning
:   Generated. Do not edit. See above.

Parameters
:   | t | Source time in nanoseconds. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) |
    | --- | --- |

Returns
:   The converted time value in ticks. [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

## [◆ ](#ga50c08351970ea8e62a0509b68898901a)k\_ns\_to\_ticks\_near64

| #define k\_ns\_to\_ticks\_near64 | ( |  | *t* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[time_units.h](time__units_8h.md)>`

**Value:**

z\_tmcvt\_64(t, Z\_HZ\_ns, Z\_HZ\_ticks, true, false, true)

Convert nanoseconds to ticks.

64 bits. Round nearest.

Converts time values in nanoseconds to ticks. Computes result in 64 bit precision. Rounds to the nearest output unit.

Warning
:   Generated. Do not edit. See above.

Parameters
:   | t | Source time in nanoseconds. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) |
    | --- | --- |

Returns
:   The converted time value in ticks. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

## [◆ ](#ga197fe61819a3c51802f080187a39f2d5)k\_sec\_to\_cyc\_ceil32

| #define k\_sec\_to\_cyc\_ceil32 | ( |  | *t* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[time_units.h](time__units_8h.md)>`

**Value:**

z\_tmcvt\_32(t, Z\_HZ\_sec, Z\_HZ\_cyc, Z\_CCYC, true, false)

Convert seconds to hardware cycles.

32 bits. Rounds up.

Converts time values in seconds to hardware cycles. Computes result in 32 bit precision. Rounds up to the next highest output unit.

Warning
:   Generated. Do not edit. See above.

Parameters
:   | t | Source time in seconds. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) |
    | --- | --- |

Returns
:   The converted time value in hardware cycles. [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

## [◆ ](#ga363ec5ce8d2365d25107e4c630222a9a)k\_sec\_to\_cyc\_ceil64

| #define k\_sec\_to\_cyc\_ceil64 | ( |  | *t* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[time_units.h](time__units_8h.md)>`

**Value:**

z\_tmcvt\_64(t, Z\_HZ\_sec, Z\_HZ\_cyc, Z\_CCYC, true, false)

Convert seconds to hardware cycles.

64 bits. Rounds up.

Converts time values in seconds to hardware cycles. Computes result in 64 bit precision. Rounds up to the next highest output unit.

Warning
:   Generated. Do not edit. See above.

Parameters
:   | t | Source time in seconds. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) |
    | --- | --- |

Returns
:   The converted time value in hardware cycles. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

## [◆ ](#ga38efeb3c71b28e98c6f18f63a2c59334)k\_sec\_to\_cyc\_floor32

| #define k\_sec\_to\_cyc\_floor32 | ( |  | *t* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[time_units.h](time__units_8h.md)>`

**Value:**

z\_tmcvt\_32(t, Z\_HZ\_sec, Z\_HZ\_cyc, Z\_CCYC, false, false)

Convert seconds to hardware cycles.

32 bits. Truncates.

Converts time values in seconds to hardware cycles. Computes result in 32 bit precision. Truncates to the next lowest output unit.

Warning
:   Generated. Do not edit. See above.

Parameters
:   | t | Source time in seconds. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) |
    | --- | --- |

Returns
:   The converted time value in hardware cycles. [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

## [◆ ](#gaa9b2ed48e2b68d509a4eee305cdcd2fe)k\_sec\_to\_cyc\_floor64

| #define k\_sec\_to\_cyc\_floor64 | ( |  | *t* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[time_units.h](time__units_8h.md)>`

**Value:**

z\_tmcvt\_64(t, Z\_HZ\_sec, Z\_HZ\_cyc, Z\_CCYC, false, false)

Convert seconds to hardware cycles.

64 bits. Truncates.

Converts time values in seconds to hardware cycles. Computes result in 64 bit precision. Truncates to the next lowest output unit.

Warning
:   Generated. Do not edit. See above.

Parameters
:   | t | Source time in seconds. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) |
    | --- | --- |

Returns
:   The converted time value in hardware cycles. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

## [◆ ](#ga5a6ec23bd5644867f211eb5f47d81a3e)k\_sec\_to\_cyc\_near32

| #define k\_sec\_to\_cyc\_near32 | ( |  | *t* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[time_units.h](time__units_8h.md)>`

**Value:**

z\_tmcvt\_32(t, Z\_HZ\_sec, Z\_HZ\_cyc, Z\_CCYC, false, true)

Convert seconds to hardware cycles.

32 bits. Round nearest.

Converts time values in seconds to hardware cycles. Computes result in 32 bit precision. Rounds to the nearest output unit.

Warning
:   Generated. Do not edit. See above.

Parameters
:   | t | Source time in seconds. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) |
    | --- | --- |

Returns
:   The converted time value in hardware cycles. [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

## [◆ ](#gab1722b870ef8c9ed1084f104974c83a3)k\_sec\_to\_cyc\_near64

| #define k\_sec\_to\_cyc\_near64 | ( |  | *t* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[time_units.h](time__units_8h.md)>`

**Value:**

z\_tmcvt\_64(t, Z\_HZ\_sec, Z\_HZ\_cyc, Z\_CCYC, false, true)

Convert seconds to hardware cycles.

64 bits. Round nearest.

Converts time values in seconds to hardware cycles. Computes result in 64 bit precision. Rounds to the nearest output unit.

Warning
:   Generated. Do not edit. See above.

Parameters
:   | t | Source time in seconds. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) |
    | --- | --- |

Returns
:   The converted time value in hardware cycles. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

## [◆ ](#ga20d46aec38239513826d5d5259b5836c)k\_sec\_to\_ticks\_ceil32

| #define k\_sec\_to\_ticks\_ceil32 | ( |  | *t* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[time_units.h](time__units_8h.md)>`

**Value:**

z\_tmcvt\_32(t, Z\_HZ\_sec, Z\_HZ\_ticks, true, true, false)

Convert seconds to ticks.

32 bits. Rounds up.

Converts time values in seconds to ticks. Computes result in 32 bit precision. Rounds up to the next highest output unit.

Warning
:   Generated. Do not edit. See above.

Parameters
:   | t | Source time in seconds. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) |
    | --- | --- |

Returns
:   The converted time value in ticks. [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

## [◆ ](#gad382b2d98f84705c4c4e7a775bb549e8)k\_sec\_to\_ticks\_ceil64

| #define k\_sec\_to\_ticks\_ceil64 | ( |  | *t* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[time_units.h](time__units_8h.md)>`

**Value:**

z\_tmcvt\_64(t, Z\_HZ\_sec, Z\_HZ\_ticks, true, true, false)

Convert seconds to ticks.

64 bits. Rounds up.

Converts time values in seconds to ticks. Computes result in 64 bit precision. Rounds up to the next highest output unit.

Warning
:   Generated. Do not edit. See above.

Parameters
:   | t | Source time in seconds. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) |
    | --- | --- |

Returns
:   The converted time value in ticks. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

## [◆ ](#gab6a57f08409edf9fba80837c3da34fb8)k\_sec\_to\_ticks\_floor32

| #define k\_sec\_to\_ticks\_floor32 | ( |  | *t* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[time_units.h](time__units_8h.md)>`

**Value:**

z\_tmcvt\_32(t, Z\_HZ\_sec, Z\_HZ\_ticks, true, false, false)

Convert seconds to ticks.

32 bits. Truncates.

Converts time values in seconds to ticks. Computes result in 32 bit precision. Truncates to the next lowest output unit.

Warning
:   Generated. Do not edit. See above.

Parameters
:   | t | Source time in seconds. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) |
    | --- | --- |

Returns
:   The converted time value in ticks. [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

## [◆ ](#gafee9fc110890fba84640acac74af6717)k\_sec\_to\_ticks\_floor64

| #define k\_sec\_to\_ticks\_floor64 | ( |  | *t* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[time_units.h](time__units_8h.md)>`

**Value:**

z\_tmcvt\_64(t, Z\_HZ\_sec, Z\_HZ\_ticks, true, false, false)

Convert seconds to ticks.

64 bits. Truncates.

Converts time values in seconds to ticks. Computes result in 64 bit precision. Truncates to the next lowest output unit.

Warning
:   Generated. Do not edit. See above.

Parameters
:   | t | Source time in seconds. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) |
    | --- | --- |

Returns
:   The converted time value in ticks. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

## [◆ ](#ga4fbbf706ce9a69ab8b2b09bd3b0d4a3e)k\_sec\_to\_ticks\_near32

| #define k\_sec\_to\_ticks\_near32 | ( |  | *t* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[time_units.h](time__units_8h.md)>`

**Value:**

z\_tmcvt\_32(t, Z\_HZ\_sec, Z\_HZ\_ticks, true, false, true)

Convert seconds to ticks.

32 bits. Round nearest.

Converts time values in seconds to ticks. Computes result in 32 bit precision. Rounds to the nearest output unit.

Warning
:   Generated. Do not edit. See above.

Parameters
:   | t | Source time in seconds. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) |
    | --- | --- |

Returns
:   The converted time value in ticks. [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

## [◆ ](#gafbdfa2986e27ea95b0347319e8a23c68)k\_sec\_to\_ticks\_near64

| #define k\_sec\_to\_ticks\_near64 | ( |  | *t* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[time_units.h](time__units_8h.md)>`

**Value:**

z\_tmcvt\_64(t, Z\_HZ\_sec, Z\_HZ\_ticks, true, false, true)

Convert seconds to ticks.

64 bits. Round nearest.

Converts time values in seconds to ticks. Computes result in 64 bit precision. Rounds to the nearest output unit.

Warning
:   Generated. Do not edit. See above.

Parameters
:   | t | Source time in seconds. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) |
    | --- | --- |

Returns
:   The converted time value in ticks. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

## [◆ ](#ga00f31f894f66dde999714fe0cbab2178)k\_ticks\_to\_cyc\_ceil32

| #define k\_ticks\_to\_cyc\_ceil32 | ( |  | *t* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[time_units.h](time__units_8h.md)>`

**Value:**

z\_tmcvt\_32(t, Z\_HZ\_ticks, Z\_HZ\_cyc, Z\_CCYC, true, false)

Convert ticks to hardware cycles.

32 bits. Rounds up.

Converts time values in ticks to hardware cycles. Computes result in 32 bit precision. Rounds up to the next highest output unit.

Warning
:   Generated. Do not edit. See above.

Parameters
:   | t | Source time in ticks. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) |
    | --- | --- |

Returns
:   The converted time value in hardware cycles. [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

## [◆ ](#ga4fa97b6aa81457142fc82cc73ef6c7a5)k\_ticks\_to\_cyc\_ceil64

| #define k\_ticks\_to\_cyc\_ceil64 | ( |  | *t* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[time_units.h](time__units_8h.md)>`

**Value:**

z\_tmcvt\_64(t, Z\_HZ\_ticks, Z\_HZ\_cyc, Z\_CCYC, true, false)

Convert ticks to hardware cycles.

64 bits. Rounds up.

Converts time values in ticks to hardware cycles. Computes result in 64 bit precision. Rounds up to the next highest output unit.

Warning
:   Generated. Do not edit. See above.

Parameters
:   | t | Source time in ticks. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) |
    | --- | --- |

Returns
:   The converted time value in hardware cycles. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

## [◆ ](#ga629a18a817e4b0240dc6bc9018d8809a)k\_ticks\_to\_cyc\_floor32

| #define k\_ticks\_to\_cyc\_floor32 | ( |  | *t* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[time_units.h](time__units_8h.md)>`

**Value:**

z\_tmcvt\_32(t, Z\_HZ\_ticks, Z\_HZ\_cyc, Z\_CCYC, false, false)

Convert ticks to hardware cycles.

32 bits. Truncates.

Converts time values in ticks to hardware cycles. Computes result in 32 bit precision. Truncates to the next lowest output unit.

Warning
:   Generated. Do not edit. See above.

Parameters
:   | t | Source time in ticks. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) |
    | --- | --- |

Returns
:   The converted time value in hardware cycles. [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

## [◆ ](#ga5593c0751ec707a63ce25aed1567b2de)k\_ticks\_to\_cyc\_floor64

| #define k\_ticks\_to\_cyc\_floor64 | ( |  | *t* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[time_units.h](time__units_8h.md)>`

**Value:**

z\_tmcvt\_64(t, Z\_HZ\_ticks, Z\_HZ\_cyc, Z\_CCYC, false, false)

Convert ticks to hardware cycles.

64 bits. Truncates.

Converts time values in ticks to hardware cycles. Computes result in 64 bit precision. Truncates to the next lowest output unit.

Warning
:   Generated. Do not edit. See above.

Parameters
:   | t | Source time in ticks. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) |
    | --- | --- |

Returns
:   The converted time value in hardware cycles. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

## [◆ ](#gaf8d7352f4d2325ddb3aec3111cc8e124)k\_ticks\_to\_cyc\_near32

| #define k\_ticks\_to\_cyc\_near32 | ( |  | *t* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[time_units.h](time__units_8h.md)>`

**Value:**

z\_tmcvt\_32(t, Z\_HZ\_ticks, Z\_HZ\_cyc, Z\_CCYC, false, true)

Convert ticks to hardware cycles.

32 bits. Round nearest.

Converts time values in ticks to hardware cycles. Computes result in 32 bit precision. Rounds to the nearest output unit.

Warning
:   Generated. Do not edit. See above.

Parameters
:   | t | Source time in ticks. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) |
    | --- | --- |

Returns
:   The converted time value in hardware cycles. [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

## [◆ ](#ga7eed234908b9db5236de6c7543f40da1)k\_ticks\_to\_cyc\_near64

| #define k\_ticks\_to\_cyc\_near64 | ( |  | *t* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[time_units.h](time__units_8h.md)>`

**Value:**

z\_tmcvt\_64(t, Z\_HZ\_ticks, Z\_HZ\_cyc, Z\_CCYC, false, true)

Convert ticks to hardware cycles.

64 bits. Round nearest.

Converts time values in ticks to hardware cycles. Computes result in 64 bit precision. Rounds to the nearest output unit.

Warning
:   Generated. Do not edit. See above.

Parameters
:   | t | Source time in ticks. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) |
    | --- | --- |

Returns
:   The converted time value in hardware cycles. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

## [◆ ](#ga3f2c3cf86ef1d243b43f29958a108088)k\_ticks\_to\_ms\_ceil32

| #define k\_ticks\_to\_ms\_ceil32 | ( |  | *t* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[time_units.h](time__units_8h.md)>`

**Value:**

z\_tmcvt\_32(t, Z\_HZ\_ticks, Z\_HZ\_ms, true, true, false)

Convert ticks to milliseconds.

32 bits. Rounds up.

Converts time values in ticks to milliseconds. Computes result in 32 bit precision. Rounds up to the next highest output unit.

Warning
:   Generated. Do not edit. See above.

Parameters
:   | t | Source time in ticks. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) |
    | --- | --- |

Returns
:   The converted time value in milliseconds. [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

## [◆ ](#gabee58122304820b36d601268eb4598e2)k\_ticks\_to\_ms\_ceil64

| #define k\_ticks\_to\_ms\_ceil64 | ( |  | *t* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[time_units.h](time__units_8h.md)>`

**Value:**

z\_tmcvt\_64(t, Z\_HZ\_ticks, Z\_HZ\_ms, true, true, false)

Convert ticks to milliseconds.

64 bits. Rounds up.

Converts time values in ticks to milliseconds. Computes result in 64 bit precision. Rounds up to the next highest output unit.

Warning
:   Generated. Do not edit. See above.

Parameters
:   | t | Source time in ticks. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) |
    | --- | --- |

Returns
:   The converted time value in milliseconds. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

## [◆ ](#ga6ecf0ab60ac29c60d6a6b66a45c86664)k\_ticks\_to\_ms\_floor32

| #define k\_ticks\_to\_ms\_floor32 | ( |  | *t* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[time_units.h](time__units_8h.md)>`

**Value:**

z\_tmcvt\_32(t, Z\_HZ\_ticks, Z\_HZ\_ms, true, false, false)

Convert ticks to milliseconds.

32 bits. Truncates.

Converts time values in ticks to milliseconds. Computes result in 32 bit precision. Truncates to the next lowest output unit.

Warning
:   Generated. Do not edit. See above.

Parameters
:   | t | Source time in ticks. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) |
    | --- | --- |

Returns
:   The converted time value in milliseconds. [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

## [◆ ](#gac417ab53d5d493d95e24e7f777f8a4e0)k\_ticks\_to\_ms\_floor64

| #define k\_ticks\_to\_ms\_floor64 | ( |  | *t* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[time_units.h](time__units_8h.md)>`

**Value:**

z\_tmcvt\_64(t, Z\_HZ\_ticks, Z\_HZ\_ms, true, false, false)

Convert ticks to milliseconds.

64 bits. Truncates.

Converts time values in ticks to milliseconds. Computes result in 64 bit precision. Truncates to the next lowest output unit.

Warning
:   Generated. Do not edit. See above.

Parameters
:   | t | Source time in ticks. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) |
    | --- | --- |

Returns
:   The converted time value in milliseconds. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

## [◆ ](#ga8f1133f69f154d593fc127d2b00931c8)k\_ticks\_to\_ms\_near32

| #define k\_ticks\_to\_ms\_near32 | ( |  | *t* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[time_units.h](time__units_8h.md)>`

**Value:**

z\_tmcvt\_32(t, Z\_HZ\_ticks, Z\_HZ\_ms, true, false, true)

Convert ticks to milliseconds.

32 bits. Round nearest.

Converts time values in ticks to milliseconds. Computes result in 32 bit precision. Rounds to the nearest output unit.

Warning
:   Generated. Do not edit. See above.

Parameters
:   | t | Source time in ticks. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) |
    | --- | --- |

Returns
:   The converted time value in milliseconds. [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

## [◆ ](#gac3578501567233a7576c61cfd6cf28cb)k\_ticks\_to\_ms\_near64

| #define k\_ticks\_to\_ms\_near64 | ( |  | *t* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[time_units.h](time__units_8h.md)>`

**Value:**

z\_tmcvt\_64(t, Z\_HZ\_ticks, Z\_HZ\_ms, true, false, true)

Convert ticks to milliseconds.

64 bits. Round nearest.

Converts time values in ticks to milliseconds. Computes result in 64 bit precision. Rounds to the nearest output unit.

Warning
:   Generated. Do not edit. See above.

Parameters
:   | t | Source time in ticks. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) |
    | --- | --- |

Returns
:   The converted time value in milliseconds. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

## [◆ ](#gae28b7099ffbda7617f4049cd730921f8)k\_ticks\_to\_ns\_ceil32

| #define k\_ticks\_to\_ns\_ceil32 | ( |  | *t* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[time_units.h](time__units_8h.md)>`

**Value:**

z\_tmcvt\_32(t, Z\_HZ\_ticks, Z\_HZ\_ns, true, true, false)

Convert ticks to nanoseconds.

32 bits. Rounds up.

Converts time values in ticks to nanoseconds. Computes result in 32 bit precision. Rounds up to the next highest output unit.

Warning
:   Generated. Do not edit. See above.

Parameters
:   | t | Source time in ticks. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) |
    | --- | --- |

Returns
:   The converted time value in nanoseconds. [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

## [◆ ](#ga0221878e17c689e7f40940a201c4fdd7)k\_ticks\_to\_ns\_ceil64

| #define k\_ticks\_to\_ns\_ceil64 | ( |  | *t* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[time_units.h](time__units_8h.md)>`

**Value:**

z\_tmcvt\_64(t, Z\_HZ\_ticks, Z\_HZ\_ns, true, true, false)

Convert ticks to nanoseconds.

64 bits. Rounds up.

Converts time values in ticks to nanoseconds. Computes result in 64 bit precision. Rounds up to the next highest output unit.

Warning
:   Generated. Do not edit. See above.

Parameters
:   | t | Source time in ticks. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) |
    | --- | --- |

Returns
:   The converted time value in nanoseconds. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

## [◆ ](#ga5c2a1ae6f66fcf22971c40301e78be8a)k\_ticks\_to\_ns\_floor32

| #define k\_ticks\_to\_ns\_floor32 | ( |  | *t* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[time_units.h](time__units_8h.md)>`

**Value:**

z\_tmcvt\_32(t, Z\_HZ\_ticks, Z\_HZ\_ns, true, false, false)

Convert ticks to nanoseconds.

32 bits. Truncates.

Converts time values in ticks to nanoseconds. Computes result in 32 bit precision. Truncates to the next lowest output unit.

Warning
:   Generated. Do not edit. See above.

Parameters
:   | t | Source time in ticks. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) |
    | --- | --- |

Returns
:   The converted time value in nanoseconds. [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

## [◆ ](#ga8c8c4d713c5716e5b0d41b014b394edf)k\_ticks\_to\_ns\_floor64

| #define k\_ticks\_to\_ns\_floor64 | ( |  | *t* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[time_units.h](time__units_8h.md)>`

**Value:**

z\_tmcvt\_64(t, Z\_HZ\_ticks, Z\_HZ\_ns, true, false, false)

Convert ticks to nanoseconds.

64 bits. Truncates.

Converts time values in ticks to nanoseconds. Computes result in 64 bit precision. Truncates to the next lowest output unit.

Warning
:   Generated. Do not edit. See above.

Parameters
:   | t | Source time in ticks. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) |
    | --- | --- |

Returns
:   The converted time value in nanoseconds. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

## [◆ ](#ga26c20d96c08dc26d4664f3d66507e0bb)k\_ticks\_to\_ns\_near32

| #define k\_ticks\_to\_ns\_near32 | ( |  | *t* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[time_units.h](time__units_8h.md)>`

**Value:**

z\_tmcvt\_32(t, Z\_HZ\_ticks, Z\_HZ\_ns, true, false, true)

Convert ticks to nanoseconds.

32 bits. Round nearest.

Converts time values in ticks to nanoseconds. Computes result in 32 bit precision. Rounds to the nearest output unit.

Warning
:   Generated. Do not edit. See above.

Parameters
:   | t | Source time in ticks. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) |
    | --- | --- |

Returns
:   The converted time value in nanoseconds. [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

## [◆ ](#ga3b0a2f92a3d61be64d4b80101129bc83)k\_ticks\_to\_ns\_near64

| #define k\_ticks\_to\_ns\_near64 | ( |  | *t* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[time_units.h](time__units_8h.md)>`

**Value:**

z\_tmcvt\_64(t, Z\_HZ\_ticks, Z\_HZ\_ns, true, false, true)

Convert ticks to nanoseconds.

64 bits. Round nearest.

Converts time values in ticks to nanoseconds. Computes result in 64 bit precision. Rounds to the nearest output unit.

Warning
:   Generated. Do not edit. See above.

Parameters
:   | t | Source time in ticks. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) |
    | --- | --- |

Returns
:   The converted time value in nanoseconds. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

## [◆ ](#ga3986215ef060ab2ff9cc7c576eb05b01)k\_ticks\_to\_sec\_ceil32

| #define k\_ticks\_to\_sec\_ceil32 | ( |  | *t* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[time_units.h](time__units_8h.md)>`

**Value:**

z\_tmcvt\_32(t, Z\_HZ\_ticks, Z\_HZ\_sec, true, true, false)

Convert ticks to seconds.

32 bits. Rounds up.

Converts time values in ticks to seconds. Computes result in 32 bit precision. Rounds up to the next highest output unit.

Warning
:   Generated. Do not edit. See above.

Parameters
:   | t | Source time in ticks. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) |
    | --- | --- |

Returns
:   The converted time value in seconds. [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

## [◆ ](#ga02493c454fbbbf6787b036ca7f739073)k\_ticks\_to\_sec\_ceil64

| #define k\_ticks\_to\_sec\_ceil64 | ( |  | *t* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[time_units.h](time__units_8h.md)>`

**Value:**

z\_tmcvt\_64(t, Z\_HZ\_ticks, Z\_HZ\_sec, true, true, false)

Convert ticks to seconds.

64 bits. Rounds up.

Converts time values in ticks to seconds. Computes result in 64 bit precision. Rounds up to the next highest output unit.

Warning
:   Generated. Do not edit. See above.

Parameters
:   | t | Source time in ticks. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) |
    | --- | --- |

Returns
:   The converted time value in seconds. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

## [◆ ](#ga824ffc9857fa2d4bccb3a9f4a56b8f18)k\_ticks\_to\_sec\_floor32

| #define k\_ticks\_to\_sec\_floor32 | ( |  | *t* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[time_units.h](time__units_8h.md)>`

**Value:**

z\_tmcvt\_32(t, Z\_HZ\_ticks, Z\_HZ\_sec, true, false, false)

Convert ticks to seconds.

32 bits. Truncates.

Converts time values in ticks to seconds. Computes result in 32 bit precision. Truncates to the next lowest output unit.

Warning
:   Generated. Do not edit. See above.

Parameters
:   | t | Source time in ticks. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) |
    | --- | --- |

Returns
:   The converted time value in seconds. [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

## [◆ ](#ga6e9ef943c78cbb5963d8eece896b6189)k\_ticks\_to\_sec\_floor64

| #define k\_ticks\_to\_sec\_floor64 | ( |  | *t* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[time_units.h](time__units_8h.md)>`

**Value:**

z\_tmcvt\_64(t, Z\_HZ\_ticks, Z\_HZ\_sec, true, false, false)

Convert ticks to seconds.

64 bits. Truncates.

Converts time values in ticks to seconds. Computes result in 64 bit precision. Truncates to the next lowest output unit.

Warning
:   Generated. Do not edit. See above.

Parameters
:   | t | Source time in ticks. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) |
    | --- | --- |

Returns
:   The converted time value in seconds. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

## [◆ ](#ga15284161d40816f06b2bbf4cd03a0fed)k\_ticks\_to\_sec\_near32

| #define k\_ticks\_to\_sec\_near32 | ( |  | *t* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[time_units.h](time__units_8h.md)>`

**Value:**

z\_tmcvt\_32(t, Z\_HZ\_ticks, Z\_HZ\_sec, true, false, true)

Convert ticks to seconds.

32 bits. Round nearest.

Converts time values in ticks to seconds. Computes result in 32 bit precision. Rounds to the nearest output unit.

Warning
:   Generated. Do not edit. See above.

Parameters
:   | t | Source time in ticks. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) |
    | --- | --- |

Returns
:   The converted time value in seconds. [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

## [◆ ](#gab6b9b6d752ec3c8b69d9f27ca5f7b85e)k\_ticks\_to\_sec\_near64

| #define k\_ticks\_to\_sec\_near64 | ( |  | *t* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[time_units.h](time__units_8h.md)>`

**Value:**

z\_tmcvt\_64(t, Z\_HZ\_ticks, Z\_HZ\_sec, true, false, true)

Convert ticks to seconds.

64 bits. Round nearest.

Converts time values in ticks to seconds. Computes result in 64 bit precision. Rounds to the nearest output unit.

Warning
:   Generated. Do not edit. See above.

Parameters
:   | t | Source time in ticks. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) |
    | --- | --- |

Returns
:   The converted time value in seconds. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

## [◆ ](#gadd968c2033d548c03072e46c895375bc)k\_ticks\_to\_us\_ceil32

| #define k\_ticks\_to\_us\_ceil32 | ( |  | *t* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[time_units.h](time__units_8h.md)>`

**Value:**

z\_tmcvt\_32(t, Z\_HZ\_ticks, Z\_HZ\_us, true, true, false)

Convert ticks to microseconds.

32 bits. Rounds up.

Converts time values in ticks to microseconds. Computes result in 32 bit precision. Rounds up to the next highest output unit.

Warning
:   Generated. Do not edit. See above.

Parameters
:   | t | Source time in ticks. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) |
    | --- | --- |

Returns
:   The converted time value in microseconds. [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

## [◆ ](#gad1c6d9e60835c6c00960778395cdbacc)k\_ticks\_to\_us\_ceil64

| #define k\_ticks\_to\_us\_ceil64 | ( |  | *t* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[time_units.h](time__units_8h.md)>`

**Value:**

z\_tmcvt\_64(t, Z\_HZ\_ticks, Z\_HZ\_us, true, true, false)

Convert ticks to microseconds.

64 bits. Rounds up.

Converts time values in ticks to microseconds. Computes result in 64 bit precision. Rounds up to the next highest output unit.

Warning
:   Generated. Do not edit. See above.

Parameters
:   | t | Source time in ticks. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) |
    | --- | --- |

Returns
:   The converted time value in microseconds. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

## [◆ ](#ga86767fd65071fc7c57f25434386caeed)k\_ticks\_to\_us\_floor32

| #define k\_ticks\_to\_us\_floor32 | ( |  | *t* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[time_units.h](time__units_8h.md)>`

**Value:**

z\_tmcvt\_32(t, Z\_HZ\_ticks, Z\_HZ\_us, true, false, false)

Convert ticks to microseconds.

32 bits. Truncates.

Converts time values in ticks to microseconds. Computes result in 32 bit precision. Truncates to the next lowest output unit.

Warning
:   Generated. Do not edit. See above.

Parameters
:   | t | Source time in ticks. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) |
    | --- | --- |

Returns
:   The converted time value in microseconds. [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

## [◆ ](#ga27cac5d9974320ef12c6bcacdae8b47c)k\_ticks\_to\_us\_floor64

| #define k\_ticks\_to\_us\_floor64 | ( |  | *t* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[time_units.h](time__units_8h.md)>`

**Value:**

z\_tmcvt\_64(t, Z\_HZ\_ticks, Z\_HZ\_us, true, false, false)

Convert ticks to microseconds.

64 bits. Truncates.

Converts time values in ticks to microseconds. Computes result in 64 bit precision. Truncates to the next lowest output unit.

Warning
:   Generated. Do not edit. See above.

Parameters
:   | t | Source time in ticks. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) |
    | --- | --- |

Returns
:   The converted time value in microseconds. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

## [◆ ](#ga328649dd1ec1fae9c69eb3a75709a9f2)k\_ticks\_to\_us\_near32

| #define k\_ticks\_to\_us\_near32 | ( |  | *t* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[time_units.h](time__units_8h.md)>`

**Value:**

z\_tmcvt\_32(t, Z\_HZ\_ticks, Z\_HZ\_us, true, false, true)

Convert ticks to microseconds.

32 bits. Round nearest.

Converts time values in ticks to microseconds. Computes result in 32 bit precision. Rounds to the nearest output unit.

Warning
:   Generated. Do not edit. See above.

Parameters
:   | t | Source time in ticks. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) |
    | --- | --- |

Returns
:   The converted time value in microseconds. [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

## [◆ ](#ga5735cb347e01fa391368d2fb54d6d965)k\_ticks\_to\_us\_near64

| #define k\_ticks\_to\_us\_near64 | ( |  | *t* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[time_units.h](time__units_8h.md)>`

**Value:**

z\_tmcvt\_64(t, Z\_HZ\_ticks, Z\_HZ\_us, true, false, true)

Convert ticks to microseconds.

64 bits. Round nearest.

Converts time values in ticks to microseconds. Computes result in 64 bit precision. Rounds to the nearest output unit.

Warning
:   Generated. Do not edit. See above.

Parameters
:   | t | Source time in ticks. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) |
    | --- | --- |

Returns
:   The converted time value in microseconds. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

## [◆ ](#ga689a3f97643be5362c8c70c6d9d81051)k\_us\_to\_cyc\_ceil32

| #define k\_us\_to\_cyc\_ceil32 | ( |  | *t* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[time_units.h](time__units_8h.md)>`

**Value:**

z\_tmcvt\_32(t, Z\_HZ\_us, Z\_HZ\_cyc, Z\_CCYC, true, false)

Convert microseconds to hardware cycles.

32 bits. Rounds up.

Converts time values in microseconds to hardware cycles. Computes result in 32 bit precision. Rounds up to the next highest output unit.

Warning
:   Generated. Do not edit. See above.

Parameters
:   | t | Source time in microseconds. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) |
    | --- | --- |

Returns
:   The converted time value in hardware cycles. [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

## [◆ ](#ga2f65f04acc1daf019470beb04f16e276)k\_us\_to\_cyc\_ceil64

| #define k\_us\_to\_cyc\_ceil64 | ( |  | *t* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[time_units.h](time__units_8h.md)>`

**Value:**

z\_tmcvt\_64(t, Z\_HZ\_us, Z\_HZ\_cyc, Z\_CCYC, true, false)

Convert microseconds to hardware cycles.

64 bits. Rounds up.

Converts time values in microseconds to hardware cycles. Computes result in 64 bit precision. Rounds up to the next highest output unit.

Warning
:   Generated. Do not edit. See above.

Parameters
:   | t | Source time in microseconds. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) |
    | --- | --- |

Returns
:   The converted time value in hardware cycles. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

## [◆ ](#ga66c1ea8197e7adc01c837163e0aa4b62)k\_us\_to\_cyc\_floor32

| #define k\_us\_to\_cyc\_floor32 | ( |  | *t* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[time_units.h](time__units_8h.md)>`

**Value:**

z\_tmcvt\_32(t, Z\_HZ\_us, Z\_HZ\_cyc, Z\_CCYC, false, false)

Convert microseconds to hardware cycles.

32 bits. Truncates.

Converts time values in microseconds to hardware cycles. Computes result in 32 bit precision. Truncates to the next lowest output unit.

Warning
:   Generated. Do not edit. See above.

Parameters
:   | t | Source time in microseconds. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) |
    | --- | --- |

Returns
:   The converted time value in hardware cycles. [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

## [◆ ](#gac78731d5891b2389dc227608decf28dd)k\_us\_to\_cyc\_floor64

| #define k\_us\_to\_cyc\_floor64 | ( |  | *t* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[time_units.h](time__units_8h.md)>`

**Value:**

z\_tmcvt\_64(t, Z\_HZ\_us, Z\_HZ\_cyc, Z\_CCYC, false, false)

Convert microseconds to hardware cycles.

64 bits. Truncates.

Converts time values in microseconds to hardware cycles. Computes result in 64 bit precision. Truncates to the next lowest output unit.

Warning
:   Generated. Do not edit. See above.

Parameters
:   | t | Source time in microseconds. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) |
    | --- | --- |

Returns
:   The converted time value in hardware cycles. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

## [◆ ](#ga01dabb87e1a4864e47fcd39cc4bce869)k\_us\_to\_cyc\_near32

| #define k\_us\_to\_cyc\_near32 | ( |  | *t* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[time_units.h](time__units_8h.md)>`

**Value:**

z\_tmcvt\_32(t, Z\_HZ\_us, Z\_HZ\_cyc, Z\_CCYC, false, true)

Convert microseconds to hardware cycles.

32 bits. Round nearest.

Converts time values in microseconds to hardware cycles. Computes result in 32 bit precision. Rounds to the nearest output unit.

Warning
:   Generated. Do not edit. See above.

Parameters
:   | t | Source time in microseconds. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) |
    | --- | --- |

Returns
:   The converted time value in hardware cycles. [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

## [◆ ](#ga49a64e1f11cf450fdd770d67617cbe23)k\_us\_to\_cyc\_near64

| #define k\_us\_to\_cyc\_near64 | ( |  | *t* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[time_units.h](time__units_8h.md)>`

**Value:**

z\_tmcvt\_64(t, Z\_HZ\_us, Z\_HZ\_cyc, Z\_CCYC, false, true)

Convert microseconds to hardware cycles.

64 bits. Round nearest.

Converts time values in microseconds to hardware cycles. Computes result in 64 bit precision. Rounds to the nearest output unit.

Warning
:   Generated. Do not edit. See above.

Parameters
:   | t | Source time in microseconds. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) |
    | --- | --- |

Returns
:   The converted time value in hardware cycles. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

## [◆ ](#ga950ac5ce654ec92e0af61e000de884a7)k\_us\_to\_ticks\_ceil32

| #define k\_us\_to\_ticks\_ceil32 | ( |  | *t* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[time_units.h](time__units_8h.md)>`

**Value:**

z\_tmcvt\_32(t, Z\_HZ\_us, Z\_HZ\_ticks, true, true, false)

Convert microseconds to ticks.

32 bits. Rounds up.

Converts time values in microseconds to ticks. Computes result in 32 bit precision. Rounds up to the next highest output unit.

Warning
:   Generated. Do not edit. See above.

Parameters
:   | t | Source time in microseconds. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) |
    | --- | --- |

Returns
:   The converted time value in ticks. [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

## [◆ ](#ga1a977f93dc94ce9db54b3c9fdf9ba2f9)k\_us\_to\_ticks\_ceil64

| #define k\_us\_to\_ticks\_ceil64 | ( |  | *t* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[time_units.h](time__units_8h.md)>`

**Value:**

z\_tmcvt\_64(t, Z\_HZ\_us, Z\_HZ\_ticks, true, true, false)

Convert microseconds to ticks.

64 bits. Rounds up.

Converts time values in microseconds to ticks. Computes result in 64 bit precision. Rounds up to the next highest output unit.

Warning
:   Generated. Do not edit. See above.

Parameters
:   | t | Source time in microseconds. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) |
    | --- | --- |

Returns
:   The converted time value in ticks. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

## [◆ ](#ga96f32803affb56c366cbab5967c6b76c)k\_us\_to\_ticks\_floor32

| #define k\_us\_to\_ticks\_floor32 | ( |  | *t* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[time_units.h](time__units_8h.md)>`

**Value:**

z\_tmcvt\_32(t, Z\_HZ\_us, Z\_HZ\_ticks, true, false, false)

Convert microseconds to ticks.

32 bits. Truncates.

Converts time values in microseconds to ticks. Computes result in 32 bit precision. Truncates to the next lowest output unit.

Warning
:   Generated. Do not edit. See above.

Parameters
:   | t | Source time in microseconds. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) |
    | --- | --- |

Returns
:   The converted time value in ticks. [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

## [◆ ](#gaf6b4fb83131e5a52d9be875e5466d022)k\_us\_to\_ticks\_floor64

| #define k\_us\_to\_ticks\_floor64 | ( |  | *t* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[time_units.h](time__units_8h.md)>`

**Value:**

z\_tmcvt\_64(t, Z\_HZ\_us, Z\_HZ\_ticks, true, false, false)

Convert microseconds to ticks.

64 bits. Truncates.

Converts time values in microseconds to ticks. Computes result in 64 bit precision. Truncates to the next lowest output unit.

Warning
:   Generated. Do not edit. See above.

Parameters
:   | t | Source time in microseconds. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) |
    | --- | --- |

Returns
:   The converted time value in ticks. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

## [◆ ](#ga5b0286cc82370178c852c3fa290eb61d)k\_us\_to\_ticks\_near32

| #define k\_us\_to\_ticks\_near32 | ( |  | *t* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[time_units.h](time__units_8h.md)>`

**Value:**

z\_tmcvt\_32(t, Z\_HZ\_us, Z\_HZ\_ticks, true, false, true)

Convert microseconds to ticks.

32 bits. Round nearest.

Converts time values in microseconds to ticks. Computes result in 32 bit precision. Rounds to the nearest output unit.

Warning
:   Generated. Do not edit. See above.

Parameters
:   | t | Source time in microseconds. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) |
    | --- | --- |

Returns
:   The converted time value in ticks. [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

## [◆ ](#gaf2aae5316fcb5e99f4a77b99a5db27f9)k\_us\_to\_ticks\_near64

| #define k\_us\_to\_ticks\_near64 | ( |  | *t* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[time_units.h](time__units_8h.md)>`

**Value:**

z\_tmcvt\_64(t, Z\_HZ\_us, Z\_HZ\_ticks, true, false, true)

Convert microseconds to ticks.

64 bits. Round nearest.

Converts time values in microseconds to ticks. Computes result in 64 bit precision. Rounds to the nearest output unit.

Warning
:   Generated. Do not edit. See above.

Parameters
:   | t | Source time in microseconds. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) |
    | --- | --- |

Returns
:   The converted time value in ticks. [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1)

## [◆ ](#gafe3ef19636d5002350794fa01b480d16)sys\_clock\_hw\_cycles\_per\_sec

| #define sys\_clock\_hw\_cycles\_per\_sec | ( |  | ) |  |
| --- | --- | --- | --- | --- |

`#include <[time_units.h](time__units_8h.md)>`

**Value:**

CONFIG\_SYS\_CLOCK\_HW\_CYCLES\_PER\_SEC

Get the system timer frequency.

Returns
:   system timer frequency in Hz

## [◆ ](#ga9f9c4c41f62c7578a30209475201efed)SYS\_FOREVER\_MS

| #define SYS\_FOREVER\_MS   (-1) |
| --- |

`#include <[time_units.h](time__units_8h.md)>`

System-wide macro to denote "forever" in milliseconds.

Usage of this macro is limited to APIs that want to expose a timeout value that can optionally be unlimited, or "forever". This macro can not be fed into kernel functions or macros directly. Use [SYS\_TIMEOUT\_MS](#ga6504e9e6fe4955e0bc31eccd4cfc01b7) instead.

## [◆ ](#gad8743aaa97d3b2650908020ffb76ef0e)SYS\_FOREVER\_US

| #define SYS\_FOREVER\_US   (-1) |
| --- |

`#include <[time_units.h](time__units_8h.md)>`

System-wide macro to denote "forever" in microseconds.

See [SYS\_FOREVER\_MS](#ga9f9c4c41f62c7578a30209475201efed).

## [◆ ](#ga6504e9e6fe4955e0bc31eccd4cfc01b7)SYS\_TIMEOUT\_MS

| #define SYS\_TIMEOUT\_MS | ( |  | *ms* | ) |  |
| --- | --- | --- | --- | --- | --- |

`#include <[time_units.h](time__units_8h.md)>`

**Value:**

Z\_TIMEOUT\_TICKS((ms) == [SYS\_FOREVER\_MS](#ga9f9c4c41f62c7578a30209475201efed) ? \

[K\_TICKS\_FOREVER](group__clock__apis.md#ga66e180b3d8940c30786a1d972cbd6d8d) : Z\_TIMEOUT\_MS\_TICKS(ms))

[K\_TICKS\_FOREVER](group__clock__apis.md#ga66e180b3d8940c30786a1d972cbd6d8d)

#define K\_TICKS\_FOREVER

**Definition** sys\_clock.h:51

[SYS\_FOREVER\_MS](#ga9f9c4c41f62c7578a30209475201efed)

#define SYS\_FOREVER\_MS

System-wide macro to denote "forever" in milliseconds.

**Definition** time\_units.h:33

System-wide macro to convert milliseconds to kernel timeouts.

## [◆ ](#ga387f15169fe1c0c58745548eceae1556)TIME\_CONSTEXPR

| #define TIME\_CONSTEXPR |
| --- |

`#include <[time_units.h](time__units_8h.md)>`

- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

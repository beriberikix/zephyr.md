---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/time__units_8h.html
original_path: doxygen/html/time__units_8h.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

time\_units.h File Reference

`#include <[zephyr/toolchain.h](toolchain_8h_source.md)>`  
`#include <[zephyr/sys/util.h](sys_2util_8h_source.md)>`

[Go to the source code of this file.](time__units_8h_source.md)

| Macros | |
| --- | --- |
| #define | [SYS\_FOREVER\_MS](group__timeutil__unit__apis.md#ga9f9c4c41f62c7578a30209475201efed)   (-1) |
|  | System-wide macro to denote "forever" in milliseconds. |
| #define | [SYS\_FOREVER\_US](group__timeutil__unit__apis.md#gad8743aaa97d3b2650908020ffb76ef0e)   (-1) |
|  | System-wide macro to denote "forever" in microseconds. |
| #define | [SYS\_TIMEOUT\_MS](group__timeutil__unit__apis.md#ga6504e9e6fe4955e0bc31eccd4cfc01b7)(ms) |
|  | System-wide macro to convert milliseconds to kernel timeouts. |
| #define | [TIME\_CONSTEXPR](group__timeutil__unit__apis.md#ga387f15169fe1c0c58745548eceae1556) |
| #define | [sys\_clock\_hw\_cycles\_per\_sec](group__timeutil__unit__apis.md#gafe3ef19636d5002350794fa01b480d16)() |
|  | Get the system timer frequency. |
| #define | [k\_sec\_to\_cyc\_floor32](group__timeutil__unit__apis.md#ga38efeb3c71b28e98c6f18f63a2c59334)(t) |
|  | Convert seconds to hardware cycles. |
| #define | [k\_sec\_to\_cyc\_floor64](group__timeutil__unit__apis.md#gaa9b2ed48e2b68d509a4eee305cdcd2fe)(t) |
|  | Convert seconds to hardware cycles. |
| #define | [k\_sec\_to\_cyc\_near32](group__timeutil__unit__apis.md#ga5a6ec23bd5644867f211eb5f47d81a3e)(t) |
|  | Convert seconds to hardware cycles. |
| #define | [k\_sec\_to\_cyc\_near64](group__timeutil__unit__apis.md#gab1722b870ef8c9ed1084f104974c83a3)(t) |
|  | Convert seconds to hardware cycles. |
| #define | [k\_sec\_to\_cyc\_ceil32](group__timeutil__unit__apis.md#ga197fe61819a3c51802f080187a39f2d5)(t) |
|  | Convert seconds to hardware cycles. |
| #define | [k\_sec\_to\_cyc\_ceil64](group__timeutil__unit__apis.md#ga363ec5ce8d2365d25107e4c630222a9a)(t) |
|  | Convert seconds to hardware cycles. |
| #define | [k\_sec\_to\_ticks\_floor32](group__timeutil__unit__apis.md#gab6a57f08409edf9fba80837c3da34fb8)(t) |
|  | Convert seconds to ticks. |
| #define | [k\_sec\_to\_ticks\_floor64](group__timeutil__unit__apis.md#gafee9fc110890fba84640acac74af6717)(t) |
|  | Convert seconds to ticks. |
| #define | [k\_sec\_to\_ticks\_near32](group__timeutil__unit__apis.md#ga4fbbf706ce9a69ab8b2b09bd3b0d4a3e)(t) |
|  | Convert seconds to ticks. |
| #define | [k\_sec\_to\_ticks\_near64](group__timeutil__unit__apis.md#gafbdfa2986e27ea95b0347319e8a23c68)(t) |
|  | Convert seconds to ticks. |
| #define | [k\_sec\_to\_ticks\_ceil32](group__timeutil__unit__apis.md#ga20d46aec38239513826d5d5259b5836c)(t) |
|  | Convert seconds to ticks. |
| #define | [k\_sec\_to\_ticks\_ceil64](group__timeutil__unit__apis.md#gad382b2d98f84705c4c4e7a775bb549e8)(t) |
|  | Convert seconds to ticks. |
| #define | [k\_ms\_to\_cyc\_floor32](group__timeutil__unit__apis.md#ga2d60494645102034a7864ab0235bbfe4)(t) |
|  | Convert milliseconds to hardware cycles. |
| #define | [k\_ms\_to\_cyc\_floor64](group__timeutil__unit__apis.md#ga4d3e1ec8eed229a08072aea744d40bba)(t) |
|  | Convert milliseconds to hardware cycles. |
| #define | [k\_ms\_to\_cyc\_near32](group__timeutil__unit__apis.md#ga8a0d31e998f1a19a3ee8200c173eb7c9)(t) |
|  | Convert milliseconds to hardware cycles. |
| #define | [k\_ms\_to\_cyc\_near64](group__timeutil__unit__apis.md#gab2bcf34a4899619fcf083819a078a09e)(t) |
|  | Convert milliseconds to hardware cycles. |
| #define | [k\_ms\_to\_cyc\_ceil32](group__timeutil__unit__apis.md#gab4636150867df2c4e918c12ec2e9bc5f)(t) |
|  | Convert milliseconds to hardware cycles. |
| #define | [k\_ms\_to\_cyc\_ceil64](group__timeutil__unit__apis.md#ga82829fc9e99658faf91e5925c9545c9f)(t) |
|  | Convert milliseconds to hardware cycles. |
| #define | [k\_ms\_to\_ticks\_floor32](group__timeutil__unit__apis.md#gaf41d7ca19e5bb47824374698ce409ea1)(t) |
|  | Convert milliseconds to ticks. |
| #define | [k\_ms\_to\_ticks\_floor64](group__timeutil__unit__apis.md#gaa6ea6977308dfd2f092ba0ac4e779a31)(t) |
|  | Convert milliseconds to ticks. |
| #define | [k\_ms\_to\_ticks\_near32](group__timeutil__unit__apis.md#ga0a61385f187c7c2a0f5288b17873b3db)(t) |
|  | Convert milliseconds to ticks. |
| #define | [k\_ms\_to\_ticks\_near64](group__timeutil__unit__apis.md#gab2f6dd223151224cd9fa0491f196c1f6)(t) |
|  | Convert milliseconds to ticks. |
| #define | [k\_ms\_to\_ticks\_ceil32](group__timeutil__unit__apis.md#gac74a319bcb69cc714818413ae15af7a2)(t) |
|  | Convert milliseconds to ticks. |
| #define | [k\_ms\_to\_ticks\_ceil64](group__timeutil__unit__apis.md#gaa623d51d51b18a2e54b20d36d2f81c42)(t) |
|  | Convert milliseconds to ticks. |
| #define | [k\_us\_to\_cyc\_floor32](group__timeutil__unit__apis.md#ga66c1ea8197e7adc01c837163e0aa4b62)(t) |
|  | Convert microseconds to hardware cycles. |
| #define | [k\_us\_to\_cyc\_floor64](group__timeutil__unit__apis.md#gac78731d5891b2389dc227608decf28dd)(t) |
|  | Convert microseconds to hardware cycles. |
| #define | [k\_us\_to\_cyc\_near32](group__timeutil__unit__apis.md#ga01dabb87e1a4864e47fcd39cc4bce869)(t) |
|  | Convert microseconds to hardware cycles. |
| #define | [k\_us\_to\_cyc\_near64](group__timeutil__unit__apis.md#ga49a64e1f11cf450fdd770d67617cbe23)(t) |
|  | Convert microseconds to hardware cycles. |
| #define | [k\_us\_to\_cyc\_ceil32](group__timeutil__unit__apis.md#ga689a3f97643be5362c8c70c6d9d81051)(t) |
|  | Convert microseconds to hardware cycles. |
| #define | [k\_us\_to\_cyc\_ceil64](group__timeutil__unit__apis.md#ga2f65f04acc1daf019470beb04f16e276)(t) |
|  | Convert microseconds to hardware cycles. |
| #define | [k\_us\_to\_ticks\_floor32](group__timeutil__unit__apis.md#ga96f32803affb56c366cbab5967c6b76c)(t) |
|  | Convert microseconds to ticks. |
| #define | [k\_us\_to\_ticks\_floor64](group__timeutil__unit__apis.md#gaf6b4fb83131e5a52d9be875e5466d022)(t) |
|  | Convert microseconds to ticks. |
| #define | [k\_us\_to\_ticks\_near32](group__timeutil__unit__apis.md#ga5b0286cc82370178c852c3fa290eb61d)(t) |
|  | Convert microseconds to ticks. |
| #define | [k\_us\_to\_ticks\_near64](group__timeutil__unit__apis.md#gaf2aae5316fcb5e99f4a77b99a5db27f9)(t) |
|  | Convert microseconds to ticks. |
| #define | [k\_us\_to\_ticks\_ceil32](group__timeutil__unit__apis.md#ga950ac5ce654ec92e0af61e000de884a7)(t) |
|  | Convert microseconds to ticks. |
| #define | [k\_us\_to\_ticks\_ceil64](group__timeutil__unit__apis.md#ga1a977f93dc94ce9db54b3c9fdf9ba2f9)(t) |
|  | Convert microseconds to ticks. |
| #define | [k\_ns\_to\_cyc\_floor32](group__timeutil__unit__apis.md#ga46013e42990cfa561da06fb2bffaa261)(t) |
|  | Convert nanoseconds to hardware cycles. |
| #define | [k\_ns\_to\_cyc\_floor64](group__timeutil__unit__apis.md#gafc4ff458df5f4d1f221bcf0799d25335)(t) |
|  | Convert nanoseconds to hardware cycles. |
| #define | [k\_ns\_to\_cyc\_near32](group__timeutil__unit__apis.md#gac8e586ebc94174ccdabf6f49dd0251e6)(t) |
|  | Convert nanoseconds to hardware cycles. |
| #define | [k\_ns\_to\_cyc\_near64](group__timeutil__unit__apis.md#gae6ec742a39a72b0a3dd7bc3da4a98403)(t) |
|  | Convert nanoseconds to hardware cycles. |
| #define | [k\_ns\_to\_cyc\_ceil32](group__timeutil__unit__apis.md#ga928ace6a14c0c2eb6aaa027f545601a7)(t) |
|  | Convert nanoseconds to hardware cycles. |
| #define | [k\_ns\_to\_cyc\_ceil64](group__timeutil__unit__apis.md#ga82264e42744defb8acf69caa8612e476)(t) |
|  | Convert nanoseconds to hardware cycles. |
| #define | [k\_ns\_to\_ticks\_floor32](group__timeutil__unit__apis.md#ga4b0a61273dfbebd9273c0dc71ea74c65)(t) |
|  | Convert nanoseconds to ticks. |
| #define | [k\_ns\_to\_ticks\_floor64](group__timeutil__unit__apis.md#ga6089738092396227384c2dbb2510e002)(t) |
|  | Convert nanoseconds to ticks. |
| #define | [k\_ns\_to\_ticks\_near32](group__timeutil__unit__apis.md#ga308b172f1fb6e1452c14db444ad7e75e)(t) |
|  | Convert nanoseconds to ticks. |
| #define | [k\_ns\_to\_ticks\_near64](group__timeutil__unit__apis.md#ga50c08351970ea8e62a0509b68898901a)(t) |
|  | Convert nanoseconds to ticks. |
| #define | [k\_ns\_to\_ticks\_ceil32](group__timeutil__unit__apis.md#gad958afbd9f86f94ccd5c9569e7587fad)(t) |
|  | Convert nanoseconds to ticks. |
| #define | [k\_ns\_to\_ticks\_ceil64](group__timeutil__unit__apis.md#ga1078f0f8764f7bad744cfb1ffd675c70)(t) |
|  | Convert nanoseconds to ticks. |
| #define | [k\_cyc\_to\_sec\_floor32](group__timeutil__unit__apis.md#ga7a83cefe2d1e0828c6cdf949d4be9674)(t) |
|  | Convert hardware cycles to seconds. |
| #define | [k\_cyc\_to\_sec\_floor64](group__timeutil__unit__apis.md#gadb48b4c005c8e4f1a30f018192fe4ae5)(t) |
|  | Convert hardware cycles to seconds. |
| #define | [k\_cyc\_to\_sec\_near32](group__timeutil__unit__apis.md#ga41d9d97ae4abc59eb235626682b767c9)(t) |
|  | Convert hardware cycles to seconds. |
| #define | [k\_cyc\_to\_sec\_near64](group__timeutil__unit__apis.md#ga8dccd0c590fb4c2c399b0e0a120a5753)(t) |
|  | Convert hardware cycles to seconds. |
| #define | [k\_cyc\_to\_sec\_ceil32](group__timeutil__unit__apis.md#gaeaf83a64009e2a834b0d65ead788e856)(t) |
|  | Convert hardware cycles to seconds. |
| #define | [k\_cyc\_to\_sec\_ceil64](group__timeutil__unit__apis.md#ga2c64ffb238dd5047413d394b39900d61)(t) |
|  | Convert hardware cycles to seconds. |
| #define | [k\_cyc\_to\_ms\_floor32](group__timeutil__unit__apis.md#ga5f9f903e6e4eba5415cae3f337d565ed)(t) |
|  | Convert hardware cycles to milliseconds. |
| #define | [k\_cyc\_to\_ms\_floor64](group__timeutil__unit__apis.md#gaeaa9339beec5b82b924302bbc57923f6)(t) |
|  | Convert hardware cycles to milliseconds. |
| #define | [k\_cyc\_to\_ms\_near32](group__timeutil__unit__apis.md#gaba2f18bc00740fb0411371d2d2f3d949)(t) |
|  | Convert hardware cycles to milliseconds. |
| #define | [k\_cyc\_to\_ms\_near64](group__timeutil__unit__apis.md#ga217f0b8bf86a24654419c3ccfd6e7822)(t) |
|  | Convert hardware cycles to milliseconds. |
| #define | [k\_cyc\_to\_ms\_ceil32](group__timeutil__unit__apis.md#ga40bf11b01ba76673c67569e8d1e55d92)(t) |
|  | Convert hardware cycles to milliseconds. |
| #define | [k\_cyc\_to\_ms\_ceil64](group__timeutil__unit__apis.md#gaf85474dc07ce8165379415f4977aa44f)(t) |
|  | Convert hardware cycles to milliseconds. |
| #define | [k\_cyc\_to\_us\_floor32](group__timeutil__unit__apis.md#ga86392f2bddfbb7c895c08becf9c8c485)(t) |
|  | Convert hardware cycles to microseconds. |
| #define | [k\_cyc\_to\_us\_floor64](group__timeutil__unit__apis.md#gad3376aa7ab36b6b7f5a1f9c9977cee4a)(t) |
|  | Convert hardware cycles to microseconds. |
| #define | [k\_cyc\_to\_us\_near32](group__timeutil__unit__apis.md#ga1314249a8a404f00c8a03d6c77e0c752)(t) |
|  | Convert hardware cycles to microseconds. |
| #define | [k\_cyc\_to\_us\_near64](group__timeutil__unit__apis.md#ga869ccaf50e83712d0bafe0f8e238fc61)(t) |
|  | Convert hardware cycles to microseconds. |
| #define | [k\_cyc\_to\_us\_ceil32](group__timeutil__unit__apis.md#ga051fbec0b352b4fb3116544c8c33250a)(t) |
|  | Convert hardware cycles to microseconds. |
| #define | [k\_cyc\_to\_us\_ceil64](group__timeutil__unit__apis.md#ga90b09be4536f6877f67a60b3c33f5299)(t) |
|  | Convert hardware cycles to microseconds. |
| #define | [k\_cyc\_to\_ns\_floor32](group__timeutil__unit__apis.md#ga775c4d72bd0ecb9a6ad947f34c479754)(t) |
|  | Convert hardware cycles to nanoseconds. |
| #define | [k\_cyc\_to\_ns\_floor64](group__timeutil__unit__apis.md#ga665d5fc98ffe8bd1cf78ca994f58724a)(t) |
|  | Convert hardware cycles to nanoseconds. |
| #define | [k\_cyc\_to\_ns\_near32](group__timeutil__unit__apis.md#gabd5378a62e480fc1b79b3326c8f02d5f)(t) |
|  | Convert hardware cycles to nanoseconds. |
| #define | [k\_cyc\_to\_ns\_near64](group__timeutil__unit__apis.md#gad36269d0d63bee37e09da46cfe516c8c)(t) |
|  | Convert hardware cycles to nanoseconds. |
| #define | [k\_cyc\_to\_ns\_ceil32](group__timeutil__unit__apis.md#ga19526c845440ed793068fa8d8d5088ff)(t) |
|  | Convert hardware cycles to nanoseconds. |
| #define | [k\_cyc\_to\_ns\_ceil64](group__timeutil__unit__apis.md#gab2889da75f359d248a6eb61fdc3d53c0)(t) |
|  | Convert hardware cycles to nanoseconds. |
| #define | [k\_cyc\_to\_ticks\_floor32](group__timeutil__unit__apis.md#ga2efd0e2611cbeb696778eb73cf24b7ee)(t) |
|  | Convert hardware cycles to ticks. |
| #define | [k\_cyc\_to\_ticks\_floor64](group__timeutil__unit__apis.md#gaad0256d9429dfa5c5a194f1419691cfc)(t) |
|  | Convert hardware cycles to ticks. |
| #define | [k\_cyc\_to\_ticks\_near32](group__timeutil__unit__apis.md#ga4601ea99148307043d2d47a2e9fccb8e)(t) |
|  | Convert hardware cycles to ticks. |
| #define | [k\_cyc\_to\_ticks\_near64](group__timeutil__unit__apis.md#gafa97757f07a5048d67d6eca4a72cf39c)(t) |
|  | Convert hardware cycles to ticks. |
| #define | [k\_cyc\_to\_ticks\_ceil32](group__timeutil__unit__apis.md#gae7653e92b9b44accaa9ee2764237f595)(t) |
|  | Convert hardware cycles to ticks. |
| #define | [k\_cyc\_to\_ticks\_ceil64](group__timeutil__unit__apis.md#ga0fa410ff13d0cd467d160c1c14cf24a6)(t) |
|  | Convert hardware cycles to ticks. |
| #define | [k\_ticks\_to\_sec\_floor32](group__timeutil__unit__apis.md#ga824ffc9857fa2d4bccb3a9f4a56b8f18)(t) |
|  | Convert ticks to seconds. |
| #define | [k\_ticks\_to\_sec\_floor64](group__timeutil__unit__apis.md#ga6e9ef943c78cbb5963d8eece896b6189)(t) |
|  | Convert ticks to seconds. |
| #define | [k\_ticks\_to\_sec\_near32](group__timeutil__unit__apis.md#ga15284161d40816f06b2bbf4cd03a0fed)(t) |
|  | Convert ticks to seconds. |
| #define | [k\_ticks\_to\_sec\_near64](group__timeutil__unit__apis.md#gab6b9b6d752ec3c8b69d9f27ca5f7b85e)(t) |
|  | Convert ticks to seconds. |
| #define | [k\_ticks\_to\_sec\_ceil32](group__timeutil__unit__apis.md#ga3986215ef060ab2ff9cc7c576eb05b01)(t) |
|  | Convert ticks to seconds. |
| #define | [k\_ticks\_to\_sec\_ceil64](group__timeutil__unit__apis.md#ga02493c454fbbbf6787b036ca7f739073)(t) |
|  | Convert ticks to seconds. |
| #define | [k\_ticks\_to\_ms\_floor32](group__timeutil__unit__apis.md#ga6ecf0ab60ac29c60d6a6b66a45c86664)(t) |
|  | Convert ticks to milliseconds. |
| #define | [k\_ticks\_to\_ms\_floor64](group__timeutil__unit__apis.md#gac417ab53d5d493d95e24e7f777f8a4e0)(t) |
|  | Convert ticks to milliseconds. |
| #define | [k\_ticks\_to\_ms\_near32](group__timeutil__unit__apis.md#ga8f1133f69f154d593fc127d2b00931c8)(t) |
|  | Convert ticks to milliseconds. |
| #define | [k\_ticks\_to\_ms\_near64](group__timeutil__unit__apis.md#gac3578501567233a7576c61cfd6cf28cb)(t) |
|  | Convert ticks to milliseconds. |
| #define | [k\_ticks\_to\_ms\_ceil32](group__timeutil__unit__apis.md#ga3f2c3cf86ef1d243b43f29958a108088)(t) |
|  | Convert ticks to milliseconds. |
| #define | [k\_ticks\_to\_ms\_ceil64](group__timeutil__unit__apis.md#gabee58122304820b36d601268eb4598e2)(t) |
|  | Convert ticks to milliseconds. |
| #define | [k\_ticks\_to\_us\_floor32](group__timeutil__unit__apis.md#ga86767fd65071fc7c57f25434386caeed)(t) |
|  | Convert ticks to microseconds. |
| #define | [k\_ticks\_to\_us\_floor64](group__timeutil__unit__apis.md#ga27cac5d9974320ef12c6bcacdae8b47c)(t) |
|  | Convert ticks to microseconds. |
| #define | [k\_ticks\_to\_us\_near32](group__timeutil__unit__apis.md#ga328649dd1ec1fae9c69eb3a75709a9f2)(t) |
|  | Convert ticks to microseconds. |
| #define | [k\_ticks\_to\_us\_near64](group__timeutil__unit__apis.md#ga5735cb347e01fa391368d2fb54d6d965)(t) |
|  | Convert ticks to microseconds. |
| #define | [k\_ticks\_to\_us\_ceil32](group__timeutil__unit__apis.md#gadd968c2033d548c03072e46c895375bc)(t) |
|  | Convert ticks to microseconds. |
| #define | [k\_ticks\_to\_us\_ceil64](group__timeutil__unit__apis.md#gad1c6d9e60835c6c00960778395cdbacc)(t) |
|  | Convert ticks to microseconds. |
| #define | [k\_ticks\_to\_ns\_floor32](group__timeutil__unit__apis.md#ga5c2a1ae6f66fcf22971c40301e78be8a)(t) |
|  | Convert ticks to nanoseconds. |
| #define | [k\_ticks\_to\_ns\_floor64](group__timeutil__unit__apis.md#ga8c8c4d713c5716e5b0d41b014b394edf)(t) |
|  | Convert ticks to nanoseconds. |
| #define | [k\_ticks\_to\_ns\_near32](group__timeutil__unit__apis.md#ga26c20d96c08dc26d4664f3d66507e0bb)(t) |
|  | Convert ticks to nanoseconds. |
| #define | [k\_ticks\_to\_ns\_near64](group__timeutil__unit__apis.md#ga3b0a2f92a3d61be64d4b80101129bc83)(t) |
|  | Convert ticks to nanoseconds. |
| #define | [k\_ticks\_to\_ns\_ceil32](group__timeutil__unit__apis.md#gae28b7099ffbda7617f4049cd730921f8)(t) |
|  | Convert ticks to nanoseconds. |
| #define | [k\_ticks\_to\_ns\_ceil64](group__timeutil__unit__apis.md#ga0221878e17c689e7f40940a201c4fdd7)(t) |
|  | Convert ticks to nanoseconds. |
| #define | [k\_ticks\_to\_cyc\_floor32](group__timeutil__unit__apis.md#ga629a18a817e4b0240dc6bc9018d8809a)(t) |
|  | Convert ticks to hardware cycles. |
| #define | [k\_ticks\_to\_cyc\_floor64](group__timeutil__unit__apis.md#ga5593c0751ec707a63ce25aed1567b2de)(t) |
|  | Convert ticks to hardware cycles. |
| #define | [k\_ticks\_to\_cyc\_near32](group__timeutil__unit__apis.md#gaf8d7352f4d2325ddb3aec3111cc8e124)(t) |
|  | Convert ticks to hardware cycles. |
| #define | [k\_ticks\_to\_cyc\_near64](group__timeutil__unit__apis.md#ga7eed234908b9db5236de6c7543f40da1)(t) |
|  | Convert ticks to hardware cycles. |
| #define | [k\_ticks\_to\_cyc\_ceil32](group__timeutil__unit__apis.md#ga00f31f894f66dde999714fe0cbab2178)(t) |
|  | Convert ticks to hardware cycles. |
| #define | [k\_ticks\_to\_cyc\_ceil64](group__timeutil__unit__apis.md#ga4fa97b6aa81457142fc82cc73ef6c7a5)(t) |
|  | Convert ticks to hardware cycles. |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sys](dir_85ec07b7ac0b888617bae1400221d199.md)
- [time\_units.h](time__units_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

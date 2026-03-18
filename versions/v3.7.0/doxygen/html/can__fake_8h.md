---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/can__fake_8h.html
original_path: doxygen/html/can__fake_8h.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

can\_fake.h File Reference

`#include <[zephyr/drivers/can.h](drivers_2can_8h_source.md)>`  
`#include <[zephyr/fff.h](fff_8h_source.md)>`

[Go to the source code of this file.](can__fake_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [fake\_can\_start\_Fake](structfake__can__start__Fake.md) |
| struct | [fake\_can\_stop\_Fake](structfake__can__stop__Fake.md) |
| struct | [fake\_can\_set\_timing\_Fake](structfake__can__set__timing__Fake.md) |
| struct | [fake\_can\_set\_timing\_data\_Fake](structfake__can__set__timing__data__Fake.md) |
| struct | [fake\_can\_get\_capabilities\_Fake](structfake__can__get__capabilities__Fake.md) |
| struct | [fake\_can\_set\_mode\_Fake](structfake__can__set__mode__Fake.md) |
| struct | [fake\_can\_send\_Fake](structfake__can__send__Fake.md) |
| struct | [fake\_can\_add\_rx\_filter\_Fake](structfake__can__add__rx__filter__Fake.md) |
| struct | [fake\_can\_remove\_rx\_filter\_Fake](structfake__can__remove__rx__filter__Fake.md) |
| struct | [fake\_can\_recover\_Fake](structfake__can__recover__Fake.md) |
| struct | [fake\_can\_get\_state\_Fake](structfake__can__get__state__Fake.md) |
| struct | [fake\_can\_set\_state\_change\_callback\_Fake](structfake__can__set__state__change__callback__Fake.md) |
| struct | [fake\_can\_get\_max\_filters\_Fake](structfake__can__get__max__filters__Fake.md) |
| struct | [fake\_can\_get\_core\_clock\_Fake](structfake__can__get__core__clock__Fake.md) |

| Typedefs | |
| --- | --- |
| typedef struct fake\_can\_start\_Fake | [fake\_can\_start\_Fake](#ad41a7e86bb3e0304f80dde9f7aa5696c) |
| typedef struct fake\_can\_stop\_Fake | [fake\_can\_stop\_Fake](#a5a35d6fd259208a8acedc22cbcfe738a) |
| typedef struct fake\_can\_set\_timing\_Fake | [fake\_can\_set\_timing\_Fake](#ad2f3d84bb356fcacf51155226939a578) |
| typedef struct fake\_can\_set\_timing\_data\_Fake | [fake\_can\_set\_timing\_data\_Fake](#aa5895c0b555be4186e2cb9e4af24e6d1) |
| typedef struct fake\_can\_get\_capabilities\_Fake | [fake\_can\_get\_capabilities\_Fake](#a04d5795e2f3177abade83d7fda4c67dd) |
| typedef struct fake\_can\_set\_mode\_Fake | [fake\_can\_set\_mode\_Fake](#a2b1f98d1c82956cc96011132e9036aaf) |
| typedef struct fake\_can\_send\_Fake | [fake\_can\_send\_Fake](#a6913470772bfbfbcf4fcb0ef86917cb5) |
| typedef struct fake\_can\_add\_rx\_filter\_Fake | [fake\_can\_add\_rx\_filter\_Fake](#aae57b47045c6ba06cec32b019800a00c) |
| typedef struct fake\_can\_remove\_rx\_filter\_Fake | [fake\_can\_remove\_rx\_filter\_Fake](#ad867d60daac00997bbbe407866b41c7c) |
| typedef struct fake\_can\_recover\_Fake | [fake\_can\_recover\_Fake](#a5852dfaf1b16a5d680a096f7fe679d61) |
| typedef struct fake\_can\_get\_state\_Fake | [fake\_can\_get\_state\_Fake](#ad3f46e4bb9ed5726c0fe2e3e012608a9) |
| typedef struct fake\_can\_set\_state\_change\_callback\_Fake | [fake\_can\_set\_state\_change\_callback\_Fake](#a85c7003b7227d3554dddc3d7548f83b2) |
| typedef struct fake\_can\_get\_max\_filters\_Fake | [fake\_can\_get\_max\_filters\_Fake](#a80a4c05334239173039704eda7036eed) |
| typedef struct fake\_can\_get\_core\_clock\_Fake | [fake\_can\_get\_core\_clock\_Fake](#aeb3fe244bb2f7d2d5439bcd3fee91f41) |

| Functions | |
| --- | --- |
| void | [fake\_can\_start\_reset](#a429e8ea55405852b9685011ae010659d) (void) |
| int | [fake\_can\_start](#a5e914edb27ac71877770d2eda4d12168) (const struct [device](structdevice.md) \*arg0) |
| void | [fake\_can\_stop\_reset](#a299323678a48004b6715e7720864cd98) (void) |
| int | [fake\_can\_stop](#ac6e6dbfe92179f3bc3d8af87adb86b92) (const struct [device](structdevice.md) \*arg0) |
| void | [fake\_can\_set\_timing\_reset](#a1afb36cb7e1e4e593b6d9d3d9b6e03e0) (void) |
| int | [fake\_can\_set\_timing](#a1fb34fd3c818455f5229f40b5ae12b2d) (const struct [device](structdevice.md) \*arg0, const struct [can\_timing](structcan__timing.md) \*arg1) |
| void | [fake\_can\_set\_timing\_data\_reset](#a7d324afebad914afe3c7f2f9f3af1a75) (void) |
| int | [fake\_can\_set\_timing\_data](#a6c76206203aa4576156c64b1db1bfcd2) (const struct [device](structdevice.md) \*arg0, const struct [can\_timing](structcan__timing.md) \*arg1) |
| void | [fake\_can\_get\_capabilities\_reset](#adca1226d44a2c0c858a67177c66aebf9) (void) |
| int | [fake\_can\_get\_capabilities](#ab2dc51fd7ba6044d25fc7a2711af790a) (const struct [device](structdevice.md) \*arg0, [can\_mode\_t](group__can__interface.md#ga0b2a1456e66f4522a30cf1400fdfced7) \*arg1) |
| void | [fake\_can\_set\_mode\_reset](#ad249e308684e0e3f51aa13b9be1d3eeb) (void) |
| int | [fake\_can\_set\_mode](#a8173a9fd5b1b1cf27269957694def2c6) (const struct [device](structdevice.md) \*arg0, [can\_mode\_t](group__can__interface.md#ga0b2a1456e66f4522a30cf1400fdfced7) arg1) |
| void | [fake\_can\_send\_reset](#a01cb21a9a1e954b39edf627c9f107dbb) (void) |
| int | [fake\_can\_send](#a7afc5d8f3fc1a07024c861b05c0b4e0a) (const struct [device](structdevice.md) \*arg0, const struct [can\_frame](structcan__frame.md) \*arg1, [k\_timeout\_t](structk__timeout__t.md) arg2, [can\_tx\_callback\_t](group__can__interface.md#gab3675297d3e528bf19e2072f6a84bfca) arg3, void \*arg4) |
| void | [fake\_can\_add\_rx\_filter\_reset](#a71fd2facb5896f076c25352c3efd213c) (void) |
| int | [fake\_can\_add\_rx\_filter](#a4f71e88bf6db1c701e98d40730e164c8) (const struct [device](structdevice.md) \*arg0, [can\_rx\_callback\_t](group__can__interface.md#gaab9525fafab78c0da0a78a2dae39bd6f) arg1, void \*arg2, const struct [can\_filter](structcan__filter.md) \*arg3) |
| void | [fake\_can\_remove\_rx\_filter\_reset](#a8d704885d992aa3f6fb377cc2f0880e2) (void) |
| void | [fake\_can\_remove\_rx\_filter](#a8731abdacd8354e7a4772289bfda130f) (const struct [device](structdevice.md) \*arg0, int arg1) |
| void | [fake\_can\_recover\_reset](#a7dc1dfa338b913d48dae0eb8129aeb48) (void) |
| int | [fake\_can\_recover](#a5894e3d832e853a26df7b612b00e651e) (const struct [device](structdevice.md) \*arg0, [k\_timeout\_t](structk__timeout__t.md) arg1) |
| void | [fake\_can\_get\_state\_reset](#a076fdd422b48ced2dc4f6d5c78f63194) (void) |
| int | [fake\_can\_get\_state](#a864f1e7500cf69387822e0dad8f8eb78) (const struct [device](structdevice.md) \*arg0, enum [can\_state](group__can__interface.md#gac7ec472c26c564dd7067c49f67c8d2f7) \*arg1, struct [can\_bus\_err\_cnt](structcan__bus__err__cnt.md) \*arg2) |
| void | [fake\_can\_set\_state\_change\_callback\_reset](#a0ec75a4bf5a729e9f86e037124046918) (void) |
| void | [fake\_can\_set\_state\_change\_callback](#ae3c1524cc1dcd6de77cc347392ab05dc) (const struct [device](structdevice.md) \*arg0, [can\_state\_change\_callback\_t](group__can__interface.md#ga002ff7ba1f5be374510a902459dd9d3d) arg1, void \*arg2) |
| void | [fake\_can\_get\_max\_filters\_reset](#a238186e79177feb2ebc6c6f65205c9c5) (void) |
| int | [fake\_can\_get\_max\_filters](#ad4f291d6297e4ebd336b199bb9836930) (const struct [device](structdevice.md) \*arg0, [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) arg1) |
| void | [fake\_can\_get\_core\_clock\_reset](#a572e31f7f32877d6292b185e9b6696e8) (void) |
| int | [fake\_can\_get\_core\_clock](#adaaefe390feebf9b84ed5479a86172d7) (const struct [device](structdevice.md) \*arg0, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*arg1) |

| Variables | |
| --- | --- |
| [fake\_can\_start\_Fake](structfake__can__start__Fake.md) | [fake\_can\_start\_fake](#a1962b9cac135a1ecb454fa87637c7b46) |
| [fake\_can\_stop\_Fake](structfake__can__stop__Fake.md) | [fake\_can\_stop\_fake](#ac15a91c767d92692ddf6c7a59cb94499) |
| [fake\_can\_set\_timing\_Fake](structfake__can__set__timing__Fake.md) | [fake\_can\_set\_timing\_fake](#a052d183150326c3590f7143a6afd9228) |
| [fake\_can\_set\_timing\_data\_Fake](structfake__can__set__timing__data__Fake.md) | [fake\_can\_set\_timing\_data\_fake](#a6a5d709ef98eda22f3595af5ae240d14) |
| [fake\_can\_get\_capabilities\_Fake](structfake__can__get__capabilities__Fake.md) | [fake\_can\_get\_capabilities\_fake](#a408aaa649f5a197e573f801e546076ca) |
| [fake\_can\_set\_mode\_Fake](structfake__can__set__mode__Fake.md) | [fake\_can\_set\_mode\_fake](#a4f789b00ba83a80bc75b04b6799ce572) |
| [fake\_can\_send\_Fake](structfake__can__send__Fake.md) | [fake\_can\_send\_fake](#a84925007d5d77ead31e78e949cba0f7d) |
| [fake\_can\_add\_rx\_filter\_Fake](structfake__can__add__rx__filter__Fake.md) | [fake\_can\_add\_rx\_filter\_fake](#a9b05d007e7877d56e94722b17aea10fd) |
| [fake\_can\_remove\_rx\_filter\_Fake](structfake__can__remove__rx__filter__Fake.md) | [fake\_can\_remove\_rx\_filter\_fake](#ab350b59af19dfa00cb981a8835aeca76) |
| [fake\_can\_recover\_Fake](structfake__can__recover__Fake.md) | [fake\_can\_recover\_fake](#a1f04a81c75562f868518d011e8fe9911) |
| [fake\_can\_get\_state\_Fake](structfake__can__get__state__Fake.md) | [fake\_can\_get\_state\_fake](#af563820ee8d02bce89f349d12a46f9f1) |
| [fake\_can\_set\_state\_change\_callback\_Fake](structfake__can__set__state__change__callback__Fake.md) | [fake\_can\_set\_state\_change\_callback\_fake](#a63e0933bc6255b8663efe2a8661bfdf7) |
| [fake\_can\_get\_max\_filters\_Fake](structfake__can__get__max__filters__Fake.md) | [fake\_can\_get\_max\_filters\_fake](#a0950f8fd3abd1d4aa294fe100bfcfb2a) |
| [fake\_can\_get\_core\_clock\_Fake](structfake__can__get__core__clock__Fake.md) | [fake\_can\_get\_core\_clock\_fake](#a0aab479cca9f1157c0a32804ea749698) |

## Typedef Documentation

## [◆ ](#aae57b47045c6ba06cec32b019800a00c)fake\_can\_add\_rx\_filter\_Fake

| typedef struct fake\_can\_add\_rx\_filter\_Fake fake\_can\_add\_rx\_filter\_Fake |
| --- |

## [◆ ](#a04d5795e2f3177abade83d7fda4c67dd)fake\_can\_get\_capabilities\_Fake

| typedef struct fake\_can\_get\_capabilities\_Fake fake\_can\_get\_capabilities\_Fake |
| --- |

## [◆ ](#aeb3fe244bb2f7d2d5439bcd3fee91f41)fake\_can\_get\_core\_clock\_Fake

| typedef struct fake\_can\_get\_core\_clock\_Fake fake\_can\_get\_core\_clock\_Fake |
| --- |

## [◆ ](#a80a4c05334239173039704eda7036eed)fake\_can\_get\_max\_filters\_Fake

| typedef struct fake\_can\_get\_max\_filters\_Fake fake\_can\_get\_max\_filters\_Fake |
| --- |

## [◆ ](#ad3f46e4bb9ed5726c0fe2e3e012608a9)fake\_can\_get\_state\_Fake

| typedef struct fake\_can\_get\_state\_Fake fake\_can\_get\_state\_Fake |
| --- |

## [◆ ](#a5852dfaf1b16a5d680a096f7fe679d61)fake\_can\_recover\_Fake

| typedef struct fake\_can\_recover\_Fake fake\_can\_recover\_Fake |
| --- |

## [◆ ](#ad867d60daac00997bbbe407866b41c7c)fake\_can\_remove\_rx\_filter\_Fake

| typedef struct fake\_can\_remove\_rx\_filter\_Fake fake\_can\_remove\_rx\_filter\_Fake |
| --- |

## [◆ ](#a6913470772bfbfbcf4fcb0ef86917cb5)fake\_can\_send\_Fake

| typedef struct fake\_can\_send\_Fake fake\_can\_send\_Fake |
| --- |

## [◆ ](#a2b1f98d1c82956cc96011132e9036aaf)fake\_can\_set\_mode\_Fake

| typedef struct fake\_can\_set\_mode\_Fake fake\_can\_set\_mode\_Fake |
| --- |

## [◆ ](#a85c7003b7227d3554dddc3d7548f83b2)fake\_can\_set\_state\_change\_callback\_Fake

| typedef struct fake\_can\_set\_state\_change\_callback\_Fake fake\_can\_set\_state\_change\_callback\_Fake |
| --- |

## [◆ ](#aa5895c0b555be4186e2cb9e4af24e6d1)fake\_can\_set\_timing\_data\_Fake

| typedef struct fake\_can\_set\_timing\_data\_Fake fake\_can\_set\_timing\_data\_Fake |
| --- |

## [◆ ](#ad2f3d84bb356fcacf51155226939a578)fake\_can\_set\_timing\_Fake

| typedef struct fake\_can\_set\_timing\_Fake fake\_can\_set\_timing\_Fake |
| --- |

## [◆ ](#ad41a7e86bb3e0304f80dde9f7aa5696c)fake\_can\_start\_Fake

| typedef struct fake\_can\_start\_Fake fake\_can\_start\_Fake |
| --- |

## [◆ ](#a5a35d6fd259208a8acedc22cbcfe738a)fake\_can\_stop\_Fake

| typedef struct fake\_can\_stop\_Fake fake\_can\_stop\_Fake |
| --- |

## Function Documentation

## [◆ ](#a4f71e88bf6db1c701e98d40730e164c8)fake\_can\_add\_rx\_filter()

| int fake\_can\_add\_rx\_filter | ( | const struct [device](structdevice.md) \* | *arg0*, |
| --- | --- | --- | --- |
|  |  | [can\_rx\_callback\_t](group__can__interface.md#gaab9525fafab78c0da0a78a2dae39bd6f) | *arg1*, |
|  |  | void \* | *arg2*, |
|  |  | const struct [can\_filter](structcan__filter.md) \* | *arg3* ) |

## [◆ ](#a71fd2facb5896f076c25352c3efd213c)fake\_can\_add\_rx\_filter\_reset()

| void fake\_can\_add\_rx\_filter\_reset | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#ab2dc51fd7ba6044d25fc7a2711af790a)fake\_can\_get\_capabilities()

| int fake\_can\_get\_capabilities | ( | const struct [device](structdevice.md) \* | *arg0*, |
| --- | --- | --- | --- |
|  |  | [can\_mode\_t](group__can__interface.md#ga0b2a1456e66f4522a30cf1400fdfced7) \* | *arg1* ) |

## [◆ ](#adca1226d44a2c0c858a67177c66aebf9)fake\_can\_get\_capabilities\_reset()

| void fake\_can\_get\_capabilities\_reset | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#adaaefe390feebf9b84ed5479a86172d7)fake\_can\_get\_core\_clock()

| int fake\_can\_get\_core\_clock | ( | const struct [device](structdevice.md) \* | *arg0*, |
| --- | --- | --- | --- |
|  |  | [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \* | *arg1* ) |

## [◆ ](#a572e31f7f32877d6292b185e9b6696e8)fake\_can\_get\_core\_clock\_reset()

| void fake\_can\_get\_core\_clock\_reset | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#ad4f291d6297e4ebd336b199bb9836930)fake\_can\_get\_max\_filters()

| int fake\_can\_get\_max\_filters | ( | const struct [device](structdevice.md) \* | *arg0*, |
| --- | --- | --- | --- |
|  |  | [bool](stdbool_8h.md#abb452686968e48b67397da5f97445f5b) | *arg1* ) |

## [◆ ](#a238186e79177feb2ebc6c6f65205c9c5)fake\_can\_get\_max\_filters\_reset()

| void fake\_can\_get\_max\_filters\_reset | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a864f1e7500cf69387822e0dad8f8eb78)fake\_can\_get\_state()

| int fake\_can\_get\_state | ( | const struct [device](structdevice.md) \* | *arg0*, |
| --- | --- | --- | --- |
|  |  | enum [can\_state](group__can__interface.md#gac7ec472c26c564dd7067c49f67c8d2f7) \* | *arg1*, |
|  |  | struct [can\_bus\_err\_cnt](structcan__bus__err__cnt.md) \* | *arg2* ) |

## [◆ ](#a076fdd422b48ced2dc4f6d5c78f63194)fake\_can\_get\_state\_reset()

| void fake\_can\_get\_state\_reset | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a5894e3d832e853a26df7b612b00e651e)fake\_can\_recover()

| int fake\_can\_recover | ( | const struct [device](structdevice.md) \* | *arg0*, |
| --- | --- | --- | --- |
|  |  | [k\_timeout\_t](structk__timeout__t.md) | *arg1* ) |

## [◆ ](#a7dc1dfa338b913d48dae0eb8129aeb48)fake\_can\_recover\_reset()

| void fake\_can\_recover\_reset | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a8731abdacd8354e7a4772289bfda130f)fake\_can\_remove\_rx\_filter()

| void fake\_can\_remove\_rx\_filter | ( | const struct [device](structdevice.md) \* | *arg0*, |
| --- | --- | --- | --- |
|  |  | int | *arg1* ) |

## [◆ ](#a8d704885d992aa3f6fb377cc2f0880e2)fake\_can\_remove\_rx\_filter\_reset()

| void fake\_can\_remove\_rx\_filter\_reset | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a7afc5d8f3fc1a07024c861b05c0b4e0a)fake\_can\_send()

| int fake\_can\_send | ( | const struct [device](structdevice.md) \* | *arg0*, |
| --- | --- | --- | --- |
|  |  | const struct [can\_frame](structcan__frame.md) \* | *arg1*, |
|  |  | [k\_timeout\_t](structk__timeout__t.md) | *arg2*, |
|  |  | [can\_tx\_callback\_t](group__can__interface.md#gab3675297d3e528bf19e2072f6a84bfca) | *arg3*, |
|  |  | void \* | *arg4* ) |

## [◆ ](#a01cb21a9a1e954b39edf627c9f107dbb)fake\_can\_send\_reset()

| void fake\_can\_send\_reset | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a8173a9fd5b1b1cf27269957694def2c6)fake\_can\_set\_mode()

| int fake\_can\_set\_mode | ( | const struct [device](structdevice.md) \* | *arg0*, |
| --- | --- | --- | --- |
|  |  | [can\_mode\_t](group__can__interface.md#ga0b2a1456e66f4522a30cf1400fdfced7) | *arg1* ) |

## [◆ ](#ad249e308684e0e3f51aa13b9be1d3eeb)fake\_can\_set\_mode\_reset()

| void fake\_can\_set\_mode\_reset | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#ae3c1524cc1dcd6de77cc347392ab05dc)fake\_can\_set\_state\_change\_callback()

| void fake\_can\_set\_state\_change\_callback | ( | const struct [device](structdevice.md) \* | *arg0*, |
| --- | --- | --- | --- |
|  |  | [can\_state\_change\_callback\_t](group__can__interface.md#ga002ff7ba1f5be374510a902459dd9d3d) | *arg1*, |
|  |  | void \* | *arg2* ) |

## [◆ ](#a0ec75a4bf5a729e9f86e037124046918)fake\_can\_set\_state\_change\_callback\_reset()

| void fake\_can\_set\_state\_change\_callback\_reset | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a1fb34fd3c818455f5229f40b5ae12b2d)fake\_can\_set\_timing()

| int fake\_can\_set\_timing | ( | const struct [device](structdevice.md) \* | *arg0*, |
| --- | --- | --- | --- |
|  |  | const struct [can\_timing](structcan__timing.md) \* | *arg1* ) |

## [◆ ](#a6c76206203aa4576156c64b1db1bfcd2)fake\_can\_set\_timing\_data()

| int fake\_can\_set\_timing\_data | ( | const struct [device](structdevice.md) \* | *arg0*, |
| --- | --- | --- | --- |
|  |  | const struct [can\_timing](structcan__timing.md) \* | *arg1* ) |

## [◆ ](#a7d324afebad914afe3c7f2f9f3af1a75)fake\_can\_set\_timing\_data\_reset()

| void fake\_can\_set\_timing\_data\_reset | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a1afb36cb7e1e4e593b6d9d3d9b6e03e0)fake\_can\_set\_timing\_reset()

| void fake\_can\_set\_timing\_reset | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a5e914edb27ac71877770d2eda4d12168)fake\_can\_start()

| int fake\_can\_start | ( | const struct [device](structdevice.md) \* | *arg0* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a429e8ea55405852b9685011ae010659d)fake\_can\_start\_reset()

| void fake\_can\_start\_reset | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#ac6e6dbfe92179f3bc3d8af87adb86b92)fake\_can\_stop()

| int fake\_can\_stop | ( | const struct [device](structdevice.md) \* | *arg0* | ) |  |
| --- | --- | --- | --- | --- | --- |

## [◆ ](#a299323678a48004b6715e7720864cd98)fake\_can\_stop\_reset()

| void fake\_can\_stop\_reset | ( | void |  | ) |  |
| --- | --- | --- | --- | --- | --- |

## Variable Documentation

## [◆ ](#a9b05d007e7877d56e94722b17aea10fd)fake\_can\_add\_rx\_filter\_fake

| | [fake\_can\_add\_rx\_filter\_Fake](structfake__can__add__rx__filter__Fake.md) fake\_can\_add\_rx\_filter\_fake | | --- | | extern |
| --- | --- | --- |

## [◆ ](#a408aaa649f5a197e573f801e546076ca)fake\_can\_get\_capabilities\_fake

| | [fake\_can\_get\_capabilities\_Fake](structfake__can__get__capabilities__Fake.md) fake\_can\_get\_capabilities\_fake | | --- | | extern |
| --- | --- | --- |

## [◆ ](#a0aab479cca9f1157c0a32804ea749698)fake\_can\_get\_core\_clock\_fake

| | [fake\_can\_get\_core\_clock\_Fake](structfake__can__get__core__clock__Fake.md) fake\_can\_get\_core\_clock\_fake | | --- | | extern |
| --- | --- | --- |

## [◆ ](#a0950f8fd3abd1d4aa294fe100bfcfb2a)fake\_can\_get\_max\_filters\_fake

| | [fake\_can\_get\_max\_filters\_Fake](structfake__can__get__max__filters__Fake.md) fake\_can\_get\_max\_filters\_fake | | --- | | extern |
| --- | --- | --- |

## [◆ ](#af563820ee8d02bce89f349d12a46f9f1)fake\_can\_get\_state\_fake

| | [fake\_can\_get\_state\_Fake](structfake__can__get__state__Fake.md) fake\_can\_get\_state\_fake | | --- | | extern |
| --- | --- | --- |

## [◆ ](#a1f04a81c75562f868518d011e8fe9911)fake\_can\_recover\_fake

| | [fake\_can\_recover\_Fake](structfake__can__recover__Fake.md) fake\_can\_recover\_fake | | --- | | extern |
| --- | --- | --- |

## [◆ ](#ab350b59af19dfa00cb981a8835aeca76)fake\_can\_remove\_rx\_filter\_fake

| | [fake\_can\_remove\_rx\_filter\_Fake](structfake__can__remove__rx__filter__Fake.md) fake\_can\_remove\_rx\_filter\_fake | | --- | | extern |
| --- | --- | --- |

## [◆ ](#a84925007d5d77ead31e78e949cba0f7d)fake\_can\_send\_fake

| | [fake\_can\_send\_Fake](structfake__can__send__Fake.md) fake\_can\_send\_fake | | --- | | extern |
| --- | --- | --- |

## [◆ ](#a4f789b00ba83a80bc75b04b6799ce572)fake\_can\_set\_mode\_fake

| | [fake\_can\_set\_mode\_Fake](structfake__can__set__mode__Fake.md) fake\_can\_set\_mode\_fake | | --- | | extern |
| --- | --- | --- |

## [◆ ](#a63e0933bc6255b8663efe2a8661bfdf7)fake\_can\_set\_state\_change\_callback\_fake

| | [fake\_can\_set\_state\_change\_callback\_Fake](structfake__can__set__state__change__callback__Fake.md) fake\_can\_set\_state\_change\_callback\_fake | | --- | | extern |
| --- | --- | --- |

## [◆ ](#a6a5d709ef98eda22f3595af5ae240d14)fake\_can\_set\_timing\_data\_fake

| | [fake\_can\_set\_timing\_data\_Fake](structfake__can__set__timing__data__Fake.md) fake\_can\_set\_timing\_data\_fake | | --- | | extern |
| --- | --- | --- |

## [◆ ](#a052d183150326c3590f7143a6afd9228)fake\_can\_set\_timing\_fake

| | [fake\_can\_set\_timing\_Fake](structfake__can__set__timing__Fake.md) fake\_can\_set\_timing\_fake | | --- | | extern |
| --- | --- | --- |

## [◆ ](#a1962b9cac135a1ecb454fa87637c7b46)fake\_can\_start\_fake

| | [fake\_can\_start\_Fake](structfake__can__start__Fake.md) fake\_can\_start\_fake | | --- | | extern |
| --- | --- | --- |

## [◆ ](#ac15a91c767d92692ddf6c7a59cb94499)fake\_can\_stop\_fake

| | [fake\_can\_stop\_Fake](structfake__can__stop__Fake.md) fake\_can\_stop\_fake | | --- | | extern |
| --- | --- | --- |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [can](dir_d26220086854d96f67fb3f45a38ba4bc.md)
- [can\_fake.h](can__fake_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

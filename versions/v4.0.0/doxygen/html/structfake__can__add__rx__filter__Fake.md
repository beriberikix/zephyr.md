---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/structfake__can__add__rx__filter__Fake.html
original_path: doxygen/html/structfake__can__add__rx__filter__Fake.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

fake\_can\_add\_rx\_filter\_Fake Struct Reference

`#include <[can_fake.h](can__fake_8h_source.md)>`

| Data Fields | |
| --- | --- |
| const struct [device](structdevice.md) \* | [arg0\_val](#a1e2b32f5a776ca085afa7bbb3035f68e) |
| const struct [device](structdevice.md) \* | [arg0\_history](#a53ee3dde1b6ced22e58602d893f3d2f9) [(50u)] |
| [can\_rx\_callback\_t](group__can__interface.md#gaab9525fafab78c0da0a78a2dae39bd6f) | [arg1\_val](#a9f820096dedce016f922ab2266c2508c) |
| [can\_rx\_callback\_t](group__can__interface.md#gaab9525fafab78c0da0a78a2dae39bd6f) | [arg1\_history](#ac6ca6374922f1c3833b95163efd597cc) [(50u)] |
| void \* | [arg2\_val](#ad3e5768cf52549e127fb656c4074739c) |
| void \* | [arg2\_history](#a174251aed70777a0ee91b56af6c5a7d4) [(50u)] |
| const struct [can\_filter](structcan__filter.md) \* | [arg3\_val](#a58dd0100d6b39028b0702d429c4b457e) |
| const struct [can\_filter](structcan__filter.md) \* | [arg3\_history](#af71cfd10e61bea9c837b29c73cfa6a1e) [(50u)] |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [call\_count](#a2c3483d2fa78d35787ef2425bb737d5f) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [arg\_history\_len](#a83d8cdd2ed74d7d3718eac833b565182) |
| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int | [arg\_histories\_dropped](#a2033cd767b8e6a83c178541b5a96a18d) |
| int | [return\_val](#af4f7fffeefa4ee007196c7a1a7ecb6fa) |
| int | [return\_val\_seq\_len](#a874ff24a2dc5fcf432a6d1aba211803c) |
| int | [return\_val\_seq\_idx](#a1a772b7a858141d1ef6868c56d34680a) |
| int \* | [return\_val\_seq](#a1f32d4a0d24dc7d73e9058e61c547136) |
| int | [return\_val\_history](#a5c5af920eac3df52bc7cc5a69afa61f4) [(50u)] |
| int | [custom\_fake\_seq\_len](#a3536ce0fd8952a54d9ff2693972385e8) |
| int | [custom\_fake\_seq\_idx](#ab33e6a4aec033c1068280f40dad1f643) |
| int(\* | [custom\_fake](#af70f0d3c9e56cae27e5579383e62aecb) )(const struct [device](structdevice.md) \*, [can\_rx\_callback\_t](group__can__interface.md#gaab9525fafab78c0da0a78a2dae39bd6f), void \*, const struct [can\_filter](structcan__filter.md) \*) |
| int(\*\* | [custom\_fake\_seq](#a595df2a0ec403abbaf5495513ddd37ab) )(const struct [device](structdevice.md) \*, [can\_rx\_callback\_t](group__can__interface.md#gaab9525fafab78c0da0a78a2dae39bd6f), void \*, const struct [can\_filter](structcan__filter.md) \*) |

## Field Documentation

## [◆ ](#a53ee3dde1b6ced22e58602d893f3d2f9)arg0\_history

| const struct [device](structdevice.md)\* fake\_can\_add\_rx\_filter\_Fake::arg0\_history[(50u)] |
| --- |

## [◆ ](#a1e2b32f5a776ca085afa7bbb3035f68e)arg0\_val

| const struct [device](structdevice.md)\* fake\_can\_add\_rx\_filter\_Fake::arg0\_val |
| --- |

## [◆ ](#ac6ca6374922f1c3833b95163efd597cc)arg1\_history

| [can\_rx\_callback\_t](group__can__interface.md#gaab9525fafab78c0da0a78a2dae39bd6f) fake\_can\_add\_rx\_filter\_Fake::arg1\_history[(50u)] |
| --- |

## [◆ ](#a9f820096dedce016f922ab2266c2508c)arg1\_val

| [can\_rx\_callback\_t](group__can__interface.md#gaab9525fafab78c0da0a78a2dae39bd6f) fake\_can\_add\_rx\_filter\_Fake::arg1\_val |
| --- |

## [◆ ](#a174251aed70777a0ee91b56af6c5a7d4)arg2\_history

| void\* fake\_can\_add\_rx\_filter\_Fake::arg2\_history[(50u)] |
| --- |

## [◆ ](#ad3e5768cf52549e127fb656c4074739c)arg2\_val

| void\* fake\_can\_add\_rx\_filter\_Fake::arg2\_val |
| --- |

## [◆ ](#af71cfd10e61bea9c837b29c73cfa6a1e)arg3\_history

| const struct [can\_filter](structcan__filter.md)\* fake\_can\_add\_rx\_filter\_Fake::arg3\_history[(50u)] |
| --- |

## [◆ ](#a58dd0100d6b39028b0702d429c4b457e)arg3\_val

| const struct [can\_filter](structcan__filter.md)\* fake\_can\_add\_rx\_filter\_Fake::arg3\_val |
| --- |

## [◆ ](#a2033cd767b8e6a83c178541b5a96a18d)arg\_histories\_dropped

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int fake\_can\_add\_rx\_filter\_Fake::arg\_histories\_dropped |
| --- |

## [◆ ](#a83d8cdd2ed74d7d3718eac833b565182)arg\_history\_len

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int fake\_can\_add\_rx\_filter\_Fake::arg\_history\_len |
| --- |

## [◆ ](#a2c3483d2fa78d35787ef2425bb737d5f)call\_count

| [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) int fake\_can\_add\_rx\_filter\_Fake::call\_count |
| --- |

## [◆ ](#af70f0d3c9e56cae27e5579383e62aecb)custom\_fake

| int(\* fake\_can\_add\_rx\_filter\_Fake::custom\_fake) (const struct [device](structdevice.md) \*, [can\_rx\_callback\_t](group__can__interface.md#gaab9525fafab78c0da0a78a2dae39bd6f), void \*, const struct [can\_filter](structcan__filter.md) \*) |
| --- |

## [◆ ](#a595df2a0ec403abbaf5495513ddd37ab)custom\_fake\_seq

| int(\*\* fake\_can\_add\_rx\_filter\_Fake::custom\_fake\_seq) (const struct [device](structdevice.md) \*, [can\_rx\_callback\_t](group__can__interface.md#gaab9525fafab78c0da0a78a2dae39bd6f), void \*, const struct [can\_filter](structcan__filter.md) \*) |
| --- |

## [◆ ](#ab33e6a4aec033c1068280f40dad1f643)custom\_fake\_seq\_idx

| int fake\_can\_add\_rx\_filter\_Fake::custom\_fake\_seq\_idx |
| --- |

## [◆ ](#a3536ce0fd8952a54d9ff2693972385e8)custom\_fake\_seq\_len

| int fake\_can\_add\_rx\_filter\_Fake::custom\_fake\_seq\_len |
| --- |

## [◆ ](#af4f7fffeefa4ee007196c7a1a7ecb6fa)return\_val

| int fake\_can\_add\_rx\_filter\_Fake::return\_val |
| --- |

## [◆ ](#a5c5af920eac3df52bc7cc5a69afa61f4)return\_val\_history

| int fake\_can\_add\_rx\_filter\_Fake::return\_val\_history[(50u)] |
| --- |

## [◆ ](#a1f32d4a0d24dc7d73e9058e61c547136)return\_val\_seq

| int\* fake\_can\_add\_rx\_filter\_Fake::return\_val\_seq |
| --- |

## [◆ ](#a1a772b7a858141d1ef6868c56d34680a)return\_val\_seq\_idx

| int fake\_can\_add\_rx\_filter\_Fake::return\_val\_seq\_idx |
| --- |

## [◆ ](#a874ff24a2dc5fcf432a6d1aba211803c)return\_val\_seq\_len

| int fake\_can\_add\_rx\_filter\_Fake::return\_val\_seq\_len |
| --- |

---

The documentation for this struct was generated from the following file:

- zephyr/drivers/can/[can\_fake.h](can__fake_8h_source.md)

- [fake\_can\_add\_rx\_filter\_Fake](structfake__can__add__rx__filter__Fake.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

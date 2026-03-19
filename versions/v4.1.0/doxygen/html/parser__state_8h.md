---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/parser__state_8h.html
original_path: doxygen/html/parser__state_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

parser\_state.h File Reference

[Go to the source code of this file.](parser__state_8h_source.md)

| Enumerations | |
| --- | --- |
| enum | [state](#adc6e5733fc3c22f0a7b2914188c49c90) {     [s\_dead](#adc6e5733fc3c22f0a7b2914188c49c90ae928e87617dbca34f86693408ffb8b08) = 1 , [s\_start\_req\_or\_res](#adc6e5733fc3c22f0a7b2914188c49c90a5a871b16732400896f13a0b4bf4d2d2e) , [s\_res\_or\_resp\_H](#adc6e5733fc3c22f0a7b2914188c49c90ad55e2affc1684fca9fc2d2dfa0ef02be) , [s\_start\_res](#adc6e5733fc3c22f0a7b2914188c49c90a17f7885ac699f68b5179b74e264605d8) ,     [s\_res\_H](#adc6e5733fc3c22f0a7b2914188c49c90a1e52abf531e01c40b73cb9e8b3fdd9f4) , [s\_res\_HT](#adc6e5733fc3c22f0a7b2914188c49c90aef104c331e8e270e735d1aed0430d32e) , [s\_res\_HTT](#adc6e5733fc3c22f0a7b2914188c49c90aac9df6a576e6b66610d1c78e0a0fce85) , [s\_res\_HTTP](#adc6e5733fc3c22f0a7b2914188c49c90a49cdf111588eeedd1593e549fdb2b4b7) ,     [s\_res\_first\_http\_major](#adc6e5733fc3c22f0a7b2914188c49c90a758a72c507e51909cd1ab0f84148ac3c) , [s\_res\_http\_major](#adc6e5733fc3c22f0a7b2914188c49c90a4581640a88dc9931031916da00dc9bc6) , [s\_res\_first\_http\_minor](#adc6e5733fc3c22f0a7b2914188c49c90a2a4dde0eafd4f5bcb5284744ccafe86a) , [s\_res\_http\_minor](#adc6e5733fc3c22f0a7b2914188c49c90a76ed9bbc2d835b88cb30299abcdd67e8) ,     [s\_res\_first\_status\_code](#adc6e5733fc3c22f0a7b2914188c49c90a246c6aaa49d61e24a43dbb1e4d601b2a) , [s\_res\_status\_code](#adc6e5733fc3c22f0a7b2914188c49c90aefa1bc8b7519ce8b995dc7e71e551f15) , [s\_res\_status\_start](#adc6e5733fc3c22f0a7b2914188c49c90aef8541c5f33f59dfbed9e429ecd92d21) , [s\_res\_status](#adc6e5733fc3c22f0a7b2914188c49c90a3159d98e8c993680b7640db1e6eed22c) ,     [s\_res\_line\_almost\_done](#adc6e5733fc3c22f0a7b2914188c49c90a94807fb310f4104dd03e2ddb1ab4ae9b) , [s\_start\_req](#adc6e5733fc3c22f0a7b2914188c49c90a726ed5570859dca67883ae410c1b9f5b) , [s\_req\_method](#adc6e5733fc3c22f0a7b2914188c49c90a5dd2f6b19fd4e3cb6b428e094ab7e443) , [s\_req\_spaces\_before\_url](#adc6e5733fc3c22f0a7b2914188c49c90a48289d7f47c2a74a9b9c498e5c8070c8) ,     [s\_req\_schema](#adc6e5733fc3c22f0a7b2914188c49c90a77eeb3ce03bff5e0a71d81e6689715ea) , [s\_req\_schema\_slash](#adc6e5733fc3c22f0a7b2914188c49c90ac76a17504862a273d8cb490d612f9759) , [s\_req\_schema\_slash\_slash](#adc6e5733fc3c22f0a7b2914188c49c90a80fae8bf0e824df045b912278ad0316d) , [s\_req\_server\_start](#adc6e5733fc3c22f0a7b2914188c49c90afe0af478bf5e6e82c2d36dc6209fa72c) ,     [s\_req\_server](#adc6e5733fc3c22f0a7b2914188c49c90a68c1b3800638f03d6ad0e3cb6da31acf) , [s\_req\_server\_with\_at](#adc6e5733fc3c22f0a7b2914188c49c90a0d0a86b054a404f46184e4e7e41e0d26) , [s\_req\_path](#adc6e5733fc3c22f0a7b2914188c49c90a490988d398dd839f49be96a79f1dcffe) , [s\_req\_query\_string\_start](#adc6e5733fc3c22f0a7b2914188c49c90a3c7bfb6f21eb5f914d33e49bd3ca4809) ,     [s\_req\_query\_string](#adc6e5733fc3c22f0a7b2914188c49c90a36add21fb73304295cc924d6014c11ef) , [s\_req\_fragment\_start](#adc6e5733fc3c22f0a7b2914188c49c90ae2c4dfd6dc9680c009c6e2554af4341d) , [s\_req\_fragment](#adc6e5733fc3c22f0a7b2914188c49c90ac379ae76d71944b4daf9519e3b22a1a1) , [s\_req\_http\_start](#adc6e5733fc3c22f0a7b2914188c49c90aeadb7f8e79fd094e250279f8afec062f) ,     [s\_req\_http\_H](#adc6e5733fc3c22f0a7b2914188c49c90a7c3dea78ecb0ee88212988ed0b90a5e7) , [s\_req\_http\_HT](#adc6e5733fc3c22f0a7b2914188c49c90ae4f0cd1ac4cbbc85edd6073bc27b85b7) , [s\_req\_http\_HTT](#adc6e5733fc3c22f0a7b2914188c49c90aee2b77d4458cf570e1a7bab584ba5907) , [s\_req\_http\_HTTP](#adc6e5733fc3c22f0a7b2914188c49c90a641d4adec0c7f121153854eae440c2c3) ,     [s\_req\_first\_http\_major](#adc6e5733fc3c22f0a7b2914188c49c90a8a068d6a93bae075f7ba5694c46d2de6) , [s\_req\_http\_major](#adc6e5733fc3c22f0a7b2914188c49c90aad6b279013498df4ef81557cec965fe6) , [s\_req\_first\_http\_minor](#adc6e5733fc3c22f0a7b2914188c49c90af5876995d7ba04281d118e845db8110d) , [s\_req\_http\_minor](#adc6e5733fc3c22f0a7b2914188c49c90a64272a20486c8d0694704832aea24872) ,     [s\_req\_line\_almost\_done](#adc6e5733fc3c22f0a7b2914188c49c90abb02b342bbb8d22a763b55386db8c0fb) , [s\_header\_field\_start](#adc6e5733fc3c22f0a7b2914188c49c90a85e4e4637f2bc962302e1ba3a3f5f769) , [s\_header\_field](#adc6e5733fc3c22f0a7b2914188c49c90a3353eed9aa8e2fd854b9f82d3ac1bff1) , [s\_header\_value\_discard\_ws](#adc6e5733fc3c22f0a7b2914188c49c90ae58f59a3755eed3117db8930dc78c6ec) ,     [s\_header\_value\_discard\_ws\_almost\_done](#adc6e5733fc3c22f0a7b2914188c49c90a0eeafcb1a1e4409ffd8c034be9af860d) , [s\_header\_value\_discard\_lws](#adc6e5733fc3c22f0a7b2914188c49c90a2dc9752e25cc2a00c3c89bbdf9b0f23b) , [s\_header\_value\_start](#adc6e5733fc3c22f0a7b2914188c49c90aa99f675903d976e1912fb54c5a71baa0) , [s\_header\_value](#adc6e5733fc3c22f0a7b2914188c49c90a4aa98ee464114fd4b6a00b02d5a83a69) ,     [s\_header\_value\_lws](#adc6e5733fc3c22f0a7b2914188c49c90ab837338881e7c475bbaff41b146fc57d) , [s\_header\_almost\_done](#adc6e5733fc3c22f0a7b2914188c49c90a484786609cb1b307e43c55b5b3078435) , [s\_chunk\_size\_start](#adc6e5733fc3c22f0a7b2914188c49c90af9d6a67a8cad297aa880c91180699409) , [s\_chunk\_size](#adc6e5733fc3c22f0a7b2914188c49c90a63c8547a6c351def0a6d1d1529c90aad) ,     [s\_chunk\_parameters](#adc6e5733fc3c22f0a7b2914188c49c90a6c9131528d4f92c9b42361fcd943744a) , [s\_chunk\_size\_almost\_done](#adc6e5733fc3c22f0a7b2914188c49c90a16494186a1ec7a1e140af1b4eaa09d20) , [s\_headers\_almost\_done](#adc6e5733fc3c22f0a7b2914188c49c90abe81888b100852a3ff950be05d2650fe) , [s\_headers\_done](#adc6e5733fc3c22f0a7b2914188c49c90a209e6e32f0783f5d76fad26c46013390) ,     [s\_chunk\_data](#adc6e5733fc3c22f0a7b2914188c49c90a1dfa1c7e958daff320dcca379e1891f2) , [s\_chunk\_data\_almost\_done](#adc6e5733fc3c22f0a7b2914188c49c90aff85ea02669f8cf3bae62121928668c0) , [s\_chunk\_data\_done](#adc6e5733fc3c22f0a7b2914188c49c90a159666494992773deef3d091d61efa64) , [s\_body\_identity](#adc6e5733fc3c22f0a7b2914188c49c90a08e05eb8bc0a42e6e84fa22dd75bdc95) ,     [s\_body\_identity\_eof](#adc6e5733fc3c22f0a7b2914188c49c90a1ae8a6fc8117d6baa6a0812d077f5b73) , [s\_message\_done](#adc6e5733fc3c22f0a7b2914188c49c90ae830ce7380ef6c61643a332ab63f6774)   } |

## Enumeration Type Documentation

## [◆ ](#adc6e5733fc3c22f0a7b2914188c49c90)state

| enum [state](#adc6e5733fc3c22f0a7b2914188c49c90) |
| --- |

| Enumerator | |
| --- | --- |
| s\_dead |  |
| s\_start\_req\_or\_res |  |
| s\_res\_or\_resp\_H |  |
| s\_start\_res |  |
| s\_res\_H |  |
| s\_res\_HT |  |
| s\_res\_HTT |  |
| s\_res\_HTTP |  |
| s\_res\_first\_http\_major |  |
| s\_res\_http\_major |  |
| s\_res\_first\_http\_minor |  |
| s\_res\_http\_minor |  |
| s\_res\_first\_status\_code |  |
| s\_res\_status\_code |  |
| s\_res\_status\_start |  |
| s\_res\_status |  |
| s\_res\_line\_almost\_done |  |
| s\_start\_req |  |
| s\_req\_method |  |
| s\_req\_spaces\_before\_url |  |
| s\_req\_schema |  |
| s\_req\_schema\_slash |  |
| s\_req\_schema\_slash\_slash |  |
| s\_req\_server\_start |  |
| s\_req\_server |  |
| s\_req\_server\_with\_at |  |
| s\_req\_path |  |
| s\_req\_query\_string\_start |  |
| s\_req\_query\_string |  |
| s\_req\_fragment\_start |  |
| s\_req\_fragment |  |
| s\_req\_http\_start |  |
| s\_req\_http\_H |  |
| s\_req\_http\_HT |  |
| s\_req\_http\_HTT |  |
| s\_req\_http\_HTTP |  |
| s\_req\_first\_http\_major |  |
| s\_req\_http\_major |  |
| s\_req\_first\_http\_minor |  |
| s\_req\_http\_minor |  |
| s\_req\_line\_almost\_done |  |
| s\_header\_field\_start |  |
| s\_header\_field |  |
| s\_header\_value\_discard\_ws |  |
| s\_header\_value\_discard\_ws\_almost\_done |  |
| s\_header\_value\_discard\_lws |  |
| s\_header\_value\_start |  |
| s\_header\_value |  |
| s\_header\_value\_lws |  |
| s\_header\_almost\_done |  |
| s\_chunk\_size\_start |  |
| s\_chunk\_size |  |
| s\_chunk\_parameters |  |
| s\_chunk\_size\_almost\_done |  |
| s\_headers\_almost\_done |  |
| s\_headers\_done |  |
| s\_chunk\_data |  |
| s\_chunk\_data\_almost\_done |  |
| s\_chunk\_data\_done |  |
| s\_body\_identity |  |
| s\_body\_identity\_eof |  |
| s\_message\_done |  |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [net](dir_d16b1c8acafe48878f854fbac26f332e.md)
- [http](dir_12a17b6e7ad2c8cb36f68b2ff871e607.md)
- [parser\_state.h](parser__state_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

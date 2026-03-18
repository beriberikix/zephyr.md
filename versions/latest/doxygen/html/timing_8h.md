---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/timing_8h.html
original_path: doxygen/html/timing_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

timing.h File Reference

`#include <[zephyr/sys/arch_interface.h](arch__interface_8h_source.md)>`  
`#include <[zephyr/timing/types.h](include_2zephyr_2timing_2types_8h_source.md)>`

[Go to the source code of this file.](timing_8h_source.md)

| Functions | |
| --- | --- |
| void | [soc\_timing\_init](group__timing__api__soc.md#ga46359ee972c8af3540ffd866e1722fd0) (void) |
|  | Initialize the timing subsystem on SoC. |
| void | [soc\_timing\_start](group__timing__api__soc.md#ga38bf58ad86707eba888ebf19b2bb3020) (void) |
|  | Signal the start of the timing information gathering. |
| void | [soc\_timing\_stop](group__timing__api__soc.md#ga1d05ea99038456ff1b6b2bf8c5289688) (void) |
|  | Signal the end of the timing information gathering. |
| [timing\_t](include_2zephyr_2timing_2types_8h.md#a08ae2ef7b1cd6f125db0cb548ea1f0e2) | [soc\_timing\_counter\_get](group__timing__api__soc.md#ga58abe336c243b2edb34d77b8247ac9e2) (void) |
|  | Return timing counter. |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [soc\_timing\_cycles\_get](group__timing__api__soc.md#ga97f010f79b60089b982d60d543e07660) (volatile [timing\_t](include_2zephyr_2timing_2types_8h.md#a08ae2ef7b1cd6f125db0cb548ea1f0e2) \*const start, volatile [timing\_t](include_2zephyr_2timing_2types_8h.md#a08ae2ef7b1cd6f125db0cb548ea1f0e2) \*const end) |
|  | Get number of cycles between `start` and `end`. |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [soc\_timing\_freq\_get](group__timing__api__soc.md#gaf9416f2d3438df707e883e4b4a212a7f) (void) |
|  | Get frequency of counter used (in Hz). |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [soc\_timing\_cycles\_to\_ns](group__timing__api__soc.md#gaa6135848e3b4aa536d977fcbe8b71d5e) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) cycles) |
|  | Convert number of `cycles` into nanoseconds. |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [soc\_timing\_cycles\_to\_ns\_avg](group__timing__api__soc.md#ga54e65aedaaa3befce5ce1f2e92740fdd) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) cycles, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) count) |
|  | Convert number of `cycles` into nanoseconds with averaging. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [soc\_timing\_freq\_get\_mhz](group__timing__api__soc.md#ga7fecec11527b307c39467745912bd511) (void) |
|  | Get frequency of counter used (in MHz). |
| void | [board\_timing\_init](group__timing__api__board.md#ga742db89830e823a804691d1946a8659c) (void) |
|  | Initialize the timing subsystem. |
| void | [board\_timing\_start](group__timing__api__board.md#gaf086f6f6881fd1e530a91f56c7ca3972) (void) |
|  | Signal the start of the timing information gathering. |
| void | [board\_timing\_stop](group__timing__api__board.md#ga5cf801e99ca32b4dcb86d82c8d4c10d8) (void) |
|  | Signal the end of the timing information gathering. |
| [timing\_t](include_2zephyr_2timing_2types_8h.md#a08ae2ef7b1cd6f125db0cb548ea1f0e2) | [board\_timing\_counter\_get](group__timing__api__board.md#gafda53aa3668e5a98d92d48eec6c6da3a) (void) |
|  | Return timing counter. |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [board\_timing\_cycles\_get](group__timing__api__board.md#ga087f9f0a8915ec2f23e64c2e8b023ec8) (volatile [timing\_t](include_2zephyr_2timing_2types_8h.md#a08ae2ef7b1cd6f125db0cb548ea1f0e2) \*const start, volatile [timing\_t](include_2zephyr_2timing_2types_8h.md#a08ae2ef7b1cd6f125db0cb548ea1f0e2) \*const end) |
|  | Get number of cycles between `start` and `end`. |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [board\_timing\_freq\_get](group__timing__api__board.md#ga905f59f65aae3802906274ff6d8ab1ee) (void) |
|  | Get frequency of counter used (in Hz). |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [board\_timing\_cycles\_to\_ns](group__timing__api__board.md#ga05755593eaf5ab7c2cc9af3d33bea343) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) cycles) |
|  | Convert number of `cycles` into nanoseconds. |
| [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [board\_timing\_cycles\_to\_ns\_avg](group__timing__api__board.md#ga69ec0aee09f8492f293a3e90a49faa83) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) cycles, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) count) |
|  | Convert number of `cycles` into nanoseconds with averaging. |
| [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [board\_timing\_freq\_get\_mhz](group__timing__api__board.md#gac32edf3332275176d6fa7563da0e06ff) (void) |
|  | Get frequency of counter used (in MHz). |
| void | [timing\_init](group__timing__api.md#ga50ff9040b99d95c56f494014831e4b47) (void) |
|  | Initialize the timing subsystem. |
| void | [timing\_start](group__timing__api.md#ga3c28bb4ced0467c284d33c800e070bde) (void) |
|  | Signal the start of the timing information gathering. |
| void | [timing\_stop](group__timing__api.md#gade1584bf683c9c61905513efa4d99cf2) (void) |
|  | Signal the end of the timing information gathering. |
| static [timing\_t](include_2zephyr_2timing_2types_8h.md#a08ae2ef7b1cd6f125db0cb548ea1f0e2) | [timing\_counter\_get](group__timing__api.md#gaa5736c87362de09749af1d8ff30b8208) (void) |
|  | Return timing counter. |
| static [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [timing\_cycles\_get](group__timing__api.md#gaa12074c7645b19578e7ca573c6aa2955) (volatile [timing\_t](include_2zephyr_2timing_2types_8h.md#a08ae2ef7b1cd6f125db0cb548ea1f0e2) \*const start, volatile [timing\_t](include_2zephyr_2timing_2types_8h.md#a08ae2ef7b1cd6f125db0cb548ea1f0e2) \*const end) |
|  | Get number of cycles between `start` and `end`. |
| static [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [timing\_freq\_get](group__timing__api.md#gab72ed08d19630cb4cbea4977f2e6723b) (void) |
|  | Get frequency of counter used (in Hz). |
| static [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [timing\_cycles\_to\_ns](group__timing__api.md#ga14a85981068350f33c63c93c4b71afe2) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) cycles) |
|  | Convert number of `cycles` into nanoseconds. |
| static [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) | [timing\_cycles\_to\_ns\_avg](group__timing__api.md#ga28b0252f3395b6e6b549cb03ea4dbef4) ([uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) cycles, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) count) |
|  | Convert number of `cycles` into nanoseconds with averaging. |
| static [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) | [timing\_freq\_get\_mhz](group__timing__api.md#ga65370ad32eadf61c84b90dc04ecd1d56) (void) |
|  | Get frequency of counter used (in MHz). |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [timing](dir_80ed10ac409b2daa43226282975e73af.md)
- [timing.h](timing_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

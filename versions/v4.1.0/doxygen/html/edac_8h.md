---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/edac_8h.html
original_path: doxygen/html/edac_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

edac.h File Reference

EDAC API header file.
[More...](#details)

`#include <[errno.h](errno_8h_source.md)>`  
`#include <[sys/types.h](lib_2libc_2minimal_2include_2sys_2types_8h_source.md)>`

[Go to the source code of this file.](edac_8h_source.md)

| Enumerations | |
| --- | --- |
| enum | [edac\_error\_type](group__edac.md#ga3eb3da4d056d8e6167083301eb1276d6) { [EDAC\_ERROR\_TYPE\_DRAM\_COR](group__edac.md#gga3eb3da4d056d8e6167083301eb1276d6a941e09125e6040d7114ee17328fd4b02) = BIT(0) , [EDAC\_ERROR\_TYPE\_DRAM\_UC](group__edac.md#gga3eb3da4d056d8e6167083301eb1276d6a5b03fd27f37f01171e50c2997bc29a2f) = BIT(1) } |
|  | EDAC error type. [More...](group__edac.md#ga3eb3da4d056d8e6167083301eb1276d6) |

| Functions | |
| --- | --- |
| Optional interfaces | |
| EDAC Optional Interfaces | |
| static int | [edac\_inject\_set\_param1](group__edac.md#gad058d74c811e77b00730e25f2060cce5) (const struct [device](structdevice.md) \*dev, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) value) |
|  | Set injection parameter param1. |
| static int | [edac\_inject\_get\_param1](group__edac.md#ga9817f47eeaf532e3789816e412eb5077) (const struct [device](structdevice.md) \*dev, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*value) |
|  | Get injection parameter param1. |
| static int | [edac\_inject\_set\_param2](group__edac.md#ga9ed608245ba68aee6b235752a87a5c39) (const struct [device](structdevice.md) \*dev, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) value) |
|  | Set injection parameter param2. |
| static int | [edac\_inject\_get\_param2](group__edac.md#ga37e097d550f91072b890d6c2d4b215fa) (const struct [device](structdevice.md) \*dev, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*value) |
|  | Get injection parameter param2. |
| static int | [edac\_inject\_set\_error\_type](group__edac.md#ga2b0ea084501faf52aeec5af33a1ca97b) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) error\_type) |
|  | Set error type value. |
| static int | [edac\_inject\_get\_error\_type](group__edac.md#gafb0cbc5082e88250a1e5955dd7d1770c) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*error\_type) |
|  | Get error type value. |
| static int | [edac\_inject\_error\_trigger](group__edac.md#gaf02830c2e621e73a7c4add38a92f6d7c) (const struct [device](structdevice.md) \*dev) |
|  | Set injection control. |
| Mandatory interfaces | |
| EDAC Mandatory Interfaces | |
| static int | [edac\_ecc\_error\_log\_get](group__edac.md#ga905539bb96ff8c9f6f6a9fde6b3928e2) (const struct [device](structdevice.md) \*dev, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*value) |
|  | Get ECC Error Log. |
| static int | [edac\_ecc\_error\_log\_clear](group__edac.md#gaa8c798b60b3b99ae6b8f8358253d1385) (const struct [device](structdevice.md) \*dev) |
|  | Clear ECC Error Log. |
| static int | [edac\_parity\_error\_log\_get](group__edac.md#gaa6cba09e19de241ed045387c85cc3f1c) (const struct [device](structdevice.md) \*dev, [uint64\_t](stdint_8h.md#a2095b9bffea4b2656950c6c0419edbf1) \*value) |
|  | Get Parity Error Log. |
| static int | [edac\_parity\_error\_log\_clear](group__edac.md#gab60aa37ba86e2038fe979481cc6134c2) (const struct [device](structdevice.md) \*dev) |
|  | Clear Parity Error Log. |
| static int | [edac\_errors\_cor\_get](group__edac.md#gaea2915b6c3c4eef2c94c6f60e788dcfe) (const struct [device](structdevice.md) \*dev) |
|  | Get number of correctable errors. |
| static int | [edac\_errors\_uc\_get](group__edac.md#gaec79969648e56e98031d46abe73c2b82) (const struct [device](structdevice.md) \*dev) |
|  | Get number of uncorrectable errors. |
| static int | [edac\_notify\_callback\_set](group__edac.md#ga2def500f72a06271d9a10243bfdf6527) (const struct [device](structdevice.md) \*dev, edac\_notify\_callback\_f cb) |
|  | Register callback function for memory error exception. |

## Detailed Description

EDAC API header file.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [edac.h](edac_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

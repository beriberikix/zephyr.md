---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/error__types_8h.html
original_path: doxygen/html/error__types_8h.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

error\_types.h File Reference

[Go to the source code of this file.](error__types_8h_source.md)

| Enumerations | |
| --- | --- |
| enum | [i3c\_sdr\_controller\_error\_types](#a79ba58b71019ccd9b76f65aaf4ebe1b0) {     [I3C\_ERROR\_CE0](#a79ba58b71019ccd9b76f65aaf4ebe1b0a29a9faf9402dbad479d7c72af3074282) , [I3C\_ERROR\_CE1](#a79ba58b71019ccd9b76f65aaf4ebe1b0ae60ebbf70623d022df65ce8837a5bddb) , [I3C\_ERROR\_CE2](#a79ba58b71019ccd9b76f65aaf4ebe1b0a46fdc1719e801fbb6a61db7b7675a574) , [I3C\_ERROR\_CE3](#a79ba58b71019ccd9b76f65aaf4ebe1b0ac18dd1126126aed36d7c4ca399133e1f) ,     [I3C\_ERROR\_CE\_UNKNOWN](#a79ba58b71019ccd9b76f65aaf4ebe1b0a936f9c9f75c2fef25d9a3a0b6dc45502) , [I3C\_ERROR\_CE\_NONE](#a79ba58b71019ccd9b76f65aaf4ebe1b0af8c1a2219f28b91b11206f7fafd12707) , [I3C\_ERROR\_CE\_MAX](#a79ba58b71019ccd9b76f65aaf4ebe1b0a8dfdbe43a58837e87eb08da228c462e7) = I3C\_ERROR\_CE\_UNKNOWN , [I3C\_ERROR\_CE\_INVALID](#a79ba58b71019ccd9b76f65aaf4ebe1b0a72a987f540981d0c0ef973cf835707a0)   } |
|  | I3C SDR Controller Error Types. [More...](#a79ba58b71019ccd9b76f65aaf4ebe1b0) |
| enum | [i3c\_sdr\_target\_error\_types](#a176c3429a9a5b786639223eea9221f91) {     [I3C\_ERROR\_TE0](#a176c3429a9a5b786639223eea9221f91ae9d64998fe25f44268fc35944e23661a) , [I3C\_ERROR\_TE1](#a176c3429a9a5b786639223eea9221f91aa79f8166d1c6bf18311adf11e6c612fe) , [I3C\_ERROR\_TE2](#a176c3429a9a5b786639223eea9221f91ab6d0cb581f823ba39934c835eed7207e) , [I3C\_ERROR\_TE3](#a176c3429a9a5b786639223eea9221f91a4d5a837d35c5a752fee2cb4cdf761cd3) ,     [I3C\_ERROR\_TE4](#a176c3429a9a5b786639223eea9221f91a3fd9d3a819fb1f3d79e53757aaa03dfd) , [I3C\_ERROR\_TE5](#a176c3429a9a5b786639223eea9221f91ab014ca57d29162e7cf3116be36693c8f) , [I3C\_ERROR\_TE6](#a176c3429a9a5b786639223eea9221f91a3f5f0fe6d716fd7df84b99df707c2a8e) , [I3C\_ERROR\_DBR](#a176c3429a9a5b786639223eea9221f91ab02aee605de8820b586908bafcd8e285) ,     [I3C\_ERROR\_TE\_UNKNOWN](#a176c3429a9a5b786639223eea9221f91a24684b50d96bf68a5a4c6f819c393791) , [I3C\_ERROR\_TE\_NONE](#a176c3429a9a5b786639223eea9221f91a5bc59253e371b88471b5d9bc15cd9c3a) , [I3C\_ERROR\_TE\_MAX](#a176c3429a9a5b786639223eea9221f91a7e6c2b9e56fc594ca57501adb09b26c7) = I3C\_ERROR\_TE\_UNKNOWN , [I3C\_ERROR\_TE\_INVALID](#a176c3429a9a5b786639223eea9221f91adb9cd0b5e4c5e0ae96f941d39a4af23a)   } |
|  | I3C SDR Target Error Types. [More...](#a176c3429a9a5b786639223eea9221f91) |

## Enumeration Type Documentation

## [◆ ](#a79ba58b71019ccd9b76f65aaf4ebe1b0)i3c\_sdr\_controller\_error\_types

| enum [i3c\_sdr\_controller\_error\_types](#a79ba58b71019ccd9b76f65aaf4ebe1b0) |
| --- |

I3C SDR Controller Error Types.

These are error types defined by the I3C specification.

[I3C\_ERROR\_CE\_UNKNOWN](#a79ba58b71019ccd9b76f65aaf4ebe1b0a936f9c9f75c2fef25d9a3a0b6dc45502) and [I3C\_ERROR\_CE\_NONE](#a79ba58b71019ccd9b76f65aaf4ebe1b0af8c1a2219f28b91b11206f7fafd12707) are not official error types according to the specification. These are there simply to aid in error handling during interactions with the I3C drivers and subsystem.

| Enumerator | |
| --- | --- |
| I3C\_ERROR\_CE0 | Transaction after sending CCC. |
| I3C\_ERROR\_CE1 | Monitoring Error. |
| I3C\_ERROR\_CE2 | No response to broadcast address (0x7E). |
| I3C\_ERROR\_CE3 | Failed Controller Handoff. |
| I3C\_ERROR\_CE\_UNKNOWN | Unknown error (not official error type). |
| I3C\_ERROR\_CE\_NONE | No error (not official error type). |
| I3C\_ERROR\_CE\_MAX |  |
| I3C\_ERROR\_CE\_INVALID |  |

## [◆ ](#a176c3429a9a5b786639223eea9221f91)i3c\_sdr\_target\_error\_types

| enum [i3c\_sdr\_target\_error\_types](#a176c3429a9a5b786639223eea9221f91) |
| --- |

I3C SDR Target Error Types.

These are error types defined by the I3C specification.

[I3C\_ERROR\_TE\_UNKNOWN](#a176c3429a9a5b786639223eea9221f91a24684b50d96bf68a5a4c6f819c393791) and [I3C\_ERROR\_TE\_NONE](#a176c3429a9a5b786639223eea9221f91a5bc59253e371b88471b5d9bc15cd9c3a) are not official error types according to the specification. These are there simply to aid in error handling during interactions with the I3C drivers and subsystem.

| Enumerator | |
| --- | --- |
| I3C\_ERROR\_TE0 | Invalid Broadcast Address or Dynamic Address after DA assignment. |
| I3C\_ERROR\_TE1 | CCC type. |
| I3C\_ERROR\_TE2 | Write Data. |
| I3C\_ERROR\_TE3 | Assigned Address during Dynamic Address Arbitration. |
| I3C\_ERROR\_TE4 | 0x7E/R missing after RESTART during Dynamic Address Arbitration |
| I3C\_ERROR\_TE5 | Transaction after detecting CCC. |
| I3C\_ERROR\_TE6 | Monitoring Error. |
| I3C\_ERROR\_DBR | Dead Bus Recovery. |
| I3C\_ERROR\_TE\_UNKNOWN | Unknown error (not official error type). |
| I3C\_ERROR\_TE\_NONE | No error (not official error type). |
| I3C\_ERROR\_TE\_MAX |  |
| I3C\_ERROR\_TE\_INVALID |  |

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [i3c](dir_7fe10d7a610a8b04680264e2afe29300.md)
- [error\_types.h](error__types_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

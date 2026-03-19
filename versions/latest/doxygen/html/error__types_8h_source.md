---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/error__types_8h_source.html
original_path: doxygen/html/error__types_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

error\_types.h

[Go to the documentation of this file.](error__types_8h.md)

1/\*

2 \* Copyright 2024 Meta Platforms, Inc. and its affiliates

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_I3C\_ERROR\_TYPES\_H\_

8#define ZEPHYR\_INCLUDE\_DRIVERS\_I3C\_ERROR\_TYPES\_H\_

9

10#ifdef \_\_cplusplus

11extern "C" {

12#endif

13

[ 24](error__types_8h.md#a79ba58b71019ccd9b76f65aaf4ebe1b0)enum [i3c\_sdr\_controller\_error\_types](error__types_8h.md#a79ba58b71019ccd9b76f65aaf4ebe1b0) {

[ 26](error__types_8h.md#a79ba58b71019ccd9b76f65aaf4ebe1b0a29a9faf9402dbad479d7c72af3074282) [I3C\_ERROR\_CE0](error__types_8h.md#a79ba58b71019ccd9b76f65aaf4ebe1b0a29a9faf9402dbad479d7c72af3074282),

27

[ 29](error__types_8h.md#a79ba58b71019ccd9b76f65aaf4ebe1b0ae60ebbf70623d022df65ce8837a5bddb) [I3C\_ERROR\_CE1](error__types_8h.md#a79ba58b71019ccd9b76f65aaf4ebe1b0ae60ebbf70623d022df65ce8837a5bddb),

30

[ 32](error__types_8h.md#a79ba58b71019ccd9b76f65aaf4ebe1b0a46fdc1719e801fbb6a61db7b7675a574) [I3C\_ERROR\_CE2](error__types_8h.md#a79ba58b71019ccd9b76f65aaf4ebe1b0a46fdc1719e801fbb6a61db7b7675a574),

33

[ 35](error__types_8h.md#a79ba58b71019ccd9b76f65aaf4ebe1b0ac18dd1126126aed36d7c4ca399133e1f) [I3C\_ERROR\_CE3](error__types_8h.md#a79ba58b71019ccd9b76f65aaf4ebe1b0ac18dd1126126aed36d7c4ca399133e1f),

36

[ 38](error__types_8h.md#a79ba58b71019ccd9b76f65aaf4ebe1b0a936f9c9f75c2fef25d9a3a0b6dc45502) [I3C\_ERROR\_CE\_UNKNOWN](error__types_8h.md#a79ba58b71019ccd9b76f65aaf4ebe1b0a936f9c9f75c2fef25d9a3a0b6dc45502),

39

[ 41](error__types_8h.md#a79ba58b71019ccd9b76f65aaf4ebe1b0af8c1a2219f28b91b11206f7fafd12707) [I3C\_ERROR\_CE\_NONE](error__types_8h.md#a79ba58b71019ccd9b76f65aaf4ebe1b0af8c1a2219f28b91b11206f7fafd12707),

42

[ 43](error__types_8h.md#a79ba58b71019ccd9b76f65aaf4ebe1b0a8dfdbe43a58837e87eb08da228c462e7) [I3C\_ERROR\_CE\_MAX](error__types_8h.md#a79ba58b71019ccd9b76f65aaf4ebe1b0a8dfdbe43a58837e87eb08da228c462e7) = [I3C\_ERROR\_CE\_UNKNOWN](error__types_8h.md#a79ba58b71019ccd9b76f65aaf4ebe1b0a936f9c9f75c2fef25d9a3a0b6dc45502),

[ 44](error__types_8h.md#a79ba58b71019ccd9b76f65aaf4ebe1b0a72a987f540981d0c0ef973cf835707a0) [I3C\_ERROR\_CE\_INVALID](error__types_8h.md#a79ba58b71019ccd9b76f65aaf4ebe1b0a72a987f540981d0c0ef973cf835707a0),

45};

46

[ 57](error__types_8h.md#a176c3429a9a5b786639223eea9221f91)enum [i3c\_sdr\_target\_error\_types](error__types_8h.md#a176c3429a9a5b786639223eea9221f91) {

[ 62](error__types_8h.md#a176c3429a9a5b786639223eea9221f91ae9d64998fe25f44268fc35944e23661a) [I3C\_ERROR\_TE0](error__types_8h.md#a176c3429a9a5b786639223eea9221f91ae9d64998fe25f44268fc35944e23661a),

63

[ 65](error__types_8h.md#a176c3429a9a5b786639223eea9221f91aa79f8166d1c6bf18311adf11e6c612fe) [I3C\_ERROR\_TE1](error__types_8h.md#a176c3429a9a5b786639223eea9221f91aa79f8166d1c6bf18311adf11e6c612fe),

66

[ 68](error__types_8h.md#a176c3429a9a5b786639223eea9221f91ab6d0cb581f823ba39934c835eed7207e) [I3C\_ERROR\_TE2](error__types_8h.md#a176c3429a9a5b786639223eea9221f91ab6d0cb581f823ba39934c835eed7207e),

69

[ 71](error__types_8h.md#a176c3429a9a5b786639223eea9221f91a4d5a837d35c5a752fee2cb4cdf761cd3) [I3C\_ERROR\_TE3](error__types_8h.md#a176c3429a9a5b786639223eea9221f91a4d5a837d35c5a752fee2cb4cdf761cd3),

72

[ 74](error__types_8h.md#a176c3429a9a5b786639223eea9221f91a3fd9d3a819fb1f3d79e53757aaa03dfd) [I3C\_ERROR\_TE4](error__types_8h.md#a176c3429a9a5b786639223eea9221f91a3fd9d3a819fb1f3d79e53757aaa03dfd),

75

[ 77](error__types_8h.md#a176c3429a9a5b786639223eea9221f91ab014ca57d29162e7cf3116be36693c8f) [I3C\_ERROR\_TE5](error__types_8h.md#a176c3429a9a5b786639223eea9221f91ab014ca57d29162e7cf3116be36693c8f),

78

[ 80](error__types_8h.md#a176c3429a9a5b786639223eea9221f91a3f5f0fe6d716fd7df84b99df707c2a8e) [I3C\_ERROR\_TE6](error__types_8h.md#a176c3429a9a5b786639223eea9221f91a3f5f0fe6d716fd7df84b99df707c2a8e),

81

[ 83](error__types_8h.md#a176c3429a9a5b786639223eea9221f91ab02aee605de8820b586908bafcd8e285) [I3C\_ERROR\_DBR](error__types_8h.md#a176c3429a9a5b786639223eea9221f91ab02aee605de8820b586908bafcd8e285),

84

[ 86](error__types_8h.md#a176c3429a9a5b786639223eea9221f91a24684b50d96bf68a5a4c6f819c393791) [I3C\_ERROR\_TE\_UNKNOWN](error__types_8h.md#a176c3429a9a5b786639223eea9221f91a24684b50d96bf68a5a4c6f819c393791),

87

[ 89](error__types_8h.md#a176c3429a9a5b786639223eea9221f91a5bc59253e371b88471b5d9bc15cd9c3a) [I3C\_ERROR\_TE\_NONE](error__types_8h.md#a176c3429a9a5b786639223eea9221f91a5bc59253e371b88471b5d9bc15cd9c3a),

90

[ 91](error__types_8h.md#a176c3429a9a5b786639223eea9221f91a7e6c2b9e56fc594ca57501adb09b26c7) [I3C\_ERROR\_TE\_MAX](error__types_8h.md#a176c3429a9a5b786639223eea9221f91a7e6c2b9e56fc594ca57501adb09b26c7) = [I3C\_ERROR\_TE\_UNKNOWN](error__types_8h.md#a176c3429a9a5b786639223eea9221f91a24684b50d96bf68a5a4c6f819c393791),

[ 92](error__types_8h.md#a176c3429a9a5b786639223eea9221f91adb9cd0b5e4c5e0ae96f941d39a4af23a) [I3C\_ERROR\_TE\_INVALID](error__types_8h.md#a176c3429a9a5b786639223eea9221f91adb9cd0b5e4c5e0ae96f941d39a4af23a),

93};

94

95#ifdef \_\_cplusplus

96}

97#endif

98

99#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_I3C\_ERROR\_TYPES\_H\_ \*/

[i3c\_sdr\_target\_error\_types](error__types_8h.md#a176c3429a9a5b786639223eea9221f91)

i3c\_sdr\_target\_error\_types

I3C SDR Target Error Types.

**Definition** error\_types.h:57

[I3C\_ERROR\_TE\_UNKNOWN](error__types_8h.md#a176c3429a9a5b786639223eea9221f91a24684b50d96bf68a5a4c6f819c393791)

@ I3C\_ERROR\_TE\_UNKNOWN

Unknown error (not official error type).

**Definition** error\_types.h:86

[I3C\_ERROR\_TE6](error__types_8h.md#a176c3429a9a5b786639223eea9221f91a3f5f0fe6d716fd7df84b99df707c2a8e)

@ I3C\_ERROR\_TE6

Monitoring Error.

**Definition** error\_types.h:80

[I3C\_ERROR\_TE4](error__types_8h.md#a176c3429a9a5b786639223eea9221f91a3fd9d3a819fb1f3d79e53757aaa03dfd)

@ I3C\_ERROR\_TE4

0x7E/R missing after RESTART during Dynamic Address Arbitration

**Definition** error\_types.h:74

[I3C\_ERROR\_TE3](error__types_8h.md#a176c3429a9a5b786639223eea9221f91a4d5a837d35c5a752fee2cb4cdf761cd3)

@ I3C\_ERROR\_TE3

Assigned Address during Dynamic Address Arbitration.

**Definition** error\_types.h:71

[I3C\_ERROR\_TE\_NONE](error__types_8h.md#a176c3429a9a5b786639223eea9221f91a5bc59253e371b88471b5d9bc15cd9c3a)

@ I3C\_ERROR\_TE\_NONE

No error (not official error type).

**Definition** error\_types.h:89

[I3C\_ERROR\_TE\_MAX](error__types_8h.md#a176c3429a9a5b786639223eea9221f91a7e6c2b9e56fc594ca57501adb09b26c7)

@ I3C\_ERROR\_TE\_MAX

**Definition** error\_types.h:91

[I3C\_ERROR\_TE1](error__types_8h.md#a176c3429a9a5b786639223eea9221f91aa79f8166d1c6bf18311adf11e6c612fe)

@ I3C\_ERROR\_TE1

CCC type.

**Definition** error\_types.h:65

[I3C\_ERROR\_TE5](error__types_8h.md#a176c3429a9a5b786639223eea9221f91ab014ca57d29162e7cf3116be36693c8f)

@ I3C\_ERROR\_TE5

Transaction after detecting CCC.

**Definition** error\_types.h:77

[I3C\_ERROR\_DBR](error__types_8h.md#a176c3429a9a5b786639223eea9221f91ab02aee605de8820b586908bafcd8e285)

@ I3C\_ERROR\_DBR

Dead Bus Recovery.

**Definition** error\_types.h:83

[I3C\_ERROR\_TE2](error__types_8h.md#a176c3429a9a5b786639223eea9221f91ab6d0cb581f823ba39934c835eed7207e)

@ I3C\_ERROR\_TE2

Write Data.

**Definition** error\_types.h:68

[I3C\_ERROR\_TE\_INVALID](error__types_8h.md#a176c3429a9a5b786639223eea9221f91adb9cd0b5e4c5e0ae96f941d39a4af23a)

@ I3C\_ERROR\_TE\_INVALID

**Definition** error\_types.h:92

[I3C\_ERROR\_TE0](error__types_8h.md#a176c3429a9a5b786639223eea9221f91ae9d64998fe25f44268fc35944e23661a)

@ I3C\_ERROR\_TE0

Invalid Broadcast Address or Dynamic Address after DA assignment.

**Definition** error\_types.h:62

[i3c\_sdr\_controller\_error\_types](error__types_8h.md#a79ba58b71019ccd9b76f65aaf4ebe1b0)

i3c\_sdr\_controller\_error\_types

I3C SDR Controller Error Types.

**Definition** error\_types.h:24

[I3C\_ERROR\_CE0](error__types_8h.md#a79ba58b71019ccd9b76f65aaf4ebe1b0a29a9faf9402dbad479d7c72af3074282)

@ I3C\_ERROR\_CE0

Transaction after sending CCC.

**Definition** error\_types.h:26

[I3C\_ERROR\_CE2](error__types_8h.md#a79ba58b71019ccd9b76f65aaf4ebe1b0a46fdc1719e801fbb6a61db7b7675a574)

@ I3C\_ERROR\_CE2

No response to broadcast address (0x7E).

**Definition** error\_types.h:32

[I3C\_ERROR\_CE\_INVALID](error__types_8h.md#a79ba58b71019ccd9b76f65aaf4ebe1b0a72a987f540981d0c0ef973cf835707a0)

@ I3C\_ERROR\_CE\_INVALID

**Definition** error\_types.h:44

[I3C\_ERROR\_CE\_MAX](error__types_8h.md#a79ba58b71019ccd9b76f65aaf4ebe1b0a8dfdbe43a58837e87eb08da228c462e7)

@ I3C\_ERROR\_CE\_MAX

**Definition** error\_types.h:43

[I3C\_ERROR\_CE\_UNKNOWN](error__types_8h.md#a79ba58b71019ccd9b76f65aaf4ebe1b0a936f9c9f75c2fef25d9a3a0b6dc45502)

@ I3C\_ERROR\_CE\_UNKNOWN

Unknown error (not official error type).

**Definition** error\_types.h:38

[I3C\_ERROR\_CE3](error__types_8h.md#a79ba58b71019ccd9b76f65aaf4ebe1b0ac18dd1126126aed36d7c4ca399133e1f)

@ I3C\_ERROR\_CE3

Failed Controller Handoff.

**Definition** error\_types.h:35

[I3C\_ERROR\_CE1](error__types_8h.md#a79ba58b71019ccd9b76f65aaf4ebe1b0ae60ebbf70623d022df65ce8837a5bddb)

@ I3C\_ERROR\_CE1

Monitoring Error.

**Definition** error\_types.h:29

[I3C\_ERROR\_CE\_NONE](error__types_8h.md#a79ba58b71019ccd9b76f65aaf4ebe1b0af8c1a2219f28b91b11206f7fafd12707)

@ I3C\_ERROR\_CE\_NONE

No error (not official error type).

**Definition** error\_types.h:41

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [i3c](dir_7fe10d7a610a8b04680264e2afe29300.md)
- [error\_types.h](error__types_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

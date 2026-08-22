---
version: v4.2.0
source_url: https://docs.zephyrproject.org/4.2.0/doxygen/html/ubx_8h_source.html
original_path: doxygen/html/ubx_8h_source.html
---

| Logo | Zephyr API Documentation 4.2.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

ubx.h

[Go to the documentation of this file.](ubx_8h.md)

1/\*

2 \* Copyright (c) 2024 NXP

3 \* Copyright (c) 2025 Croxel Inc.

4 \* Copyright (c) 2025 CogniPilot Foundation

5 \*

6 \* SPDX-License-Identifier: Apache-2.0

7 \*/

8

9#include <[zephyr/kernel.h](kernel_8h.md)>

10#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

11#include <[zephyr/sys/atomic.h](sys_2atomic_8h.md)>

12

13#include <[zephyr/modem/pipe.h](pipe_8h.md)>

14#include <[zephyr/modem/ubx/protocol.h](modem_2ubx_2protocol_8h.md)>

15

16#ifndef ZEPHYR\_MODEM\_UBX\_

[ 17](ubx_8h.md#af3b5ad7b53c97ba7ec6a96d2b44f3c27)#define ZEPHYR\_MODEM\_UBX\_

18

19#ifdef \_\_cplusplus

20extern "C" {

21#endif

22

29

30struct [modem\_ubx](structmodem__ubx.md);

31

[ 32](group__modem__ubx.md#gae0bfe22e7e8d7d38ae9f41648f7fcfda)typedef void (\*[modem\_ubx\_match\_callback](group__modem__ubx.md#gae0bfe22e7e8d7d38ae9f41648f7fcfda))(struct [modem\_ubx](structmodem__ubx.md) \*ubx,

33 const struct [ubx\_frame](structubx__frame.md) \*frame,

34 size\_t len,

35 void \*user\_data);

36

[ 37](structmodem__ubx__match.md)struct [modem\_ubx\_match](structmodem__ubx__match.md) {

[ 38](structmodem__ubx__match.md#aba64a4f7825a1f3b3cbee6f3473d7f74) struct [ubx\_frame\_match](structubx__frame__match.md) [filter](structmodem__ubx__match.md#aba64a4f7825a1f3b3cbee6f3473d7f74);

[ 39](structmodem__ubx__match.md#a657d7961121ed1860635df96597b88b8) [modem\_ubx\_match\_callback](group__modem__ubx.md#gae0bfe22e7e8d7d38ae9f41648f7fcfda) [handler](structmodem__ubx__match.md#a657d7961121ed1860635df96597b88b8);

40};

41

[ 42](group__modem__ubx.md#ga8a37614e3a9cf6d4773b9e74de79d340)#define MODEM\_UBX\_MATCH\_ARRAY\_DEFINE(\_name, ...) \

43 struct modem\_ubx\_match \_name[] = {\_\_VA\_ARGS\_\_};

44

[ 45](group__modem__ubx.md#ga4c04f643a1ea9f0fc940d286713be30e)#define MODEM\_UBX\_MATCH\_DEFINE(\_class\_id, \_msg\_id, \_handler) \

46{ \

47 .filter = { \

48 .class = \_class\_id, \

49 .id = \_msg\_id, \

50 }, \

51 .handler = \_handler, \

52}

53

[ 54](structmodem__ubx__script.md)struct [modem\_ubx\_script](structmodem__ubx__script.md) {

55 struct {

[ 56](structmodem__ubx__script.md#aade7c60068e44b39bfac09415e31417c) const struct [ubx\_frame](structubx__frame.md) \*[buf](structmodem__ubx__script.md#aade7c60068e44b39bfac09415e31417c);

[ 57](structmodem__ubx__script.md#a033047efbf34102985fad507711905ec) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [len](structmodem__ubx__script.md#a033047efbf34102985fad507711905ec);

[ 58](structmodem__ubx__script.md#ab91b22317aa1cfb36f7c24de2b425137) } [request](structmodem__ubx__script.md#ab91b22317aa1cfb36f7c24de2b425137);

59 struct {

[ 60](structmodem__ubx__script.md#aa1ffe8666c2e2169c6067710f9b3ccc7) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[buf](structmodem__ubx__script.md#aade7c60068e44b39bfac09415e31417c);

[ 61](structmodem__ubx__script.md#a9882eb3b10b9739c916f5317fda412ea) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [buf\_len](structmodem__ubx__script.md#a9882eb3b10b9739c916f5317fda412ea);

[ 62](structmodem__ubx__script.md#a716f90ed421af01c829cb716d94a9a76) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [received\_len](structmodem__ubx__script.md#a716f90ed421af01c829cb716d94a9a76);

[ 63](structmodem__ubx__script.md#a90d08ee6c3832f3d0198cea0aa7b3b8d) } [response](structmodem__ubx__script.md#a90d08ee6c3832f3d0198cea0aa7b3b8d);

[ 64](structmodem__ubx__script.md#a1e91925ba17f30685db67d4f326d2f31) struct [modem\_ubx\_match](structmodem__ubx__match.md) [match](structmodem__ubx__script.md#a1e91925ba17f30685db67d4f326d2f31);

[ 65](structmodem__ubx__script.md#a4910a3551004f19249c66a5b695795ce) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [retry\_count](structmodem__ubx__script.md#a4910a3551004f19249c66a5b695795ce);

[ 66](structmodem__ubx__script.md#a041de757b5fb26f1cdfb89cb19610f11) [k\_timeout\_t](structk__timeout__t.md) [timeout](structmodem__ubx__script.md#a041de757b5fb26f1cdfb89cb19610f11);

67};

68

[ 69](structmodem__ubx.md)struct [modem\_ubx](structmodem__ubx.md) {

[ 70](structmodem__ubx.md#ad98fcc4a93781ff5cd5406cb0560c849) void \*[user\_data](structmodem__ubx.md#ad98fcc4a93781ff5cd5406cb0560c849);

[ 71](structmodem__ubx.md#a337b4afe37e031ecd563572951be9412) [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) [attached](structmodem__ubx.md#a337b4afe37e031ecd563572951be9412);

[ 72](structmodem__ubx.md#a0bc3ee485c2e6f63727efae5b61a64ac) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[receive\_buf](structmodem__ubx.md#a0bc3ee485c2e6f63727efae5b61a64ac);

[ 73](structmodem__ubx.md#a4add513db024eb040de858e8901bc017) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [receive\_buf\_size](structmodem__ubx.md#a4add513db024eb040de858e8901bc017);

[ 74](structmodem__ubx.md#a639183a5a24d953015df30f64b2f1c85) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [receive\_buf\_offset](structmodem__ubx.md#a639183a5a24d953015df30f64b2f1c85);

[ 75](structmodem__ubx.md#ac9a3b4009eabeb92e2e3cff093d74d2c) struct [modem\_ubx\_script](structmodem__ubx__script.md) \*[script](structmodem__ubx.md#ac9a3b4009eabeb92e2e3cff093d74d2c);

[ 76](structmodem__ubx.md#a1b853c80109313feaebfb8cdb24b950c) struct modem\_pipe \*[pipe](structmodem__ubx.md#a1b853c80109313feaebfb8cdb24b950c);

[ 77](structmodem__ubx.md#adfd9249b1f72aae1f2b9818cbf0de640) struct [k\_work](structk__work.md) [process\_work](structmodem__ubx.md#adfd9249b1f72aae1f2b9818cbf0de640);

[ 78](structmodem__ubx.md#ae5c5914a3c88b908e80646d71ada7bfe) struct [k\_sem](structk__sem.md) [script\_stopped\_sem](structmodem__ubx.md#ae5c5914a3c88b908e80646d71ada7bfe);

[ 79](structmodem__ubx.md#a0489f188b1dcdd54ba756ad821c62db5) struct [k\_sem](structk__sem.md) [script\_running\_sem](structmodem__ubx.md#a0489f188b1dcdd54ba756ad821c62db5);

80 struct {

[ 81](structmodem__ubx.md#ae7182d2345bcd3585828f0f48d42321a) const struct [modem\_ubx\_match](structmodem__ubx__match.md) \*[array](structmodem__ubx.md#ae7182d2345bcd3585828f0f48d42321a);

[ 82](structmodem__ubx.md#a98b8d6b02acbfa564b510b6f7c9908d5) size\_t [size](structmodem__ubx.md#a98b8d6b02acbfa564b510b6f7c9908d5);

[ 83](structmodem__ubx.md#aeeb735c338ed161d7eddeaa561cca5d9) } [unsol\_matches](structmodem__ubx.md#aeeb735c338ed161d7eddeaa561cca5d9);

84};

85

[ 86](structmodem__ubx__config.md)struct [modem\_ubx\_config](structmodem__ubx__config.md) {

[ 87](structmodem__ubx__config.md#acac2ab2800443c4f60cbf5df9ca8cd5e) void \*[user\_data](structmodem__ubx__config.md#acac2ab2800443c4f60cbf5df9ca8cd5e);

[ 88](structmodem__ubx__config.md#a7ac0f254167c3197366b210bef2ac75d) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[receive\_buf](structmodem__ubx__config.md#a7ac0f254167c3197366b210bef2ac75d);

[ 89](structmodem__ubx__config.md#a75634cde7a69ef78ea0370f423307a0e) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [receive\_buf\_size](structmodem__ubx__config.md#a75634cde7a69ef78ea0370f423307a0e);

90 struct {

[ 91](structmodem__ubx__config.md#a75237681e1c9bf094b347e71e1ad823e) const struct [modem\_ubx\_match](structmodem__ubx__match.md) \*[array](structmodem__ubx__config.md#a75237681e1c9bf094b347e71e1ad823e);

[ 92](structmodem__ubx__config.md#a19f107638346a44bddc73045f595ec98) size\_t [size](structmodem__ubx__config.md#a19f107638346a44bddc73045f595ec98);

[ 93](structmodem__ubx__config.md#a08ba4ac10872f451a302fcbc04a04253) } [unsol\_matches](structmodem__ubx__config.md#a08ba4ac10872f451a302fcbc04a04253);

94};

95

[ 105](group__modem__ubx.md#ga4e459f955e34c9059702c3d7f9794948)int [modem\_ubx\_attach](group__modem__ubx.md#ga4e459f955e34c9059702c3d7f9794948)(struct [modem\_ubx](structmodem__ubx.md) \*ubx, struct modem\_pipe \*pipe);

106

[ 112](group__modem__ubx.md#ga68210f4afd5880c532d82fd0bac1d933)void [modem\_ubx\_release](group__modem__ubx.md#ga68210f4afd5880c532d82fd0bac1d933)(struct [modem\_ubx](structmodem__ubx.md) \*ubx);

113

[ 120](group__modem__ubx.md#gaf49363fb4decb4656566b508a061212f)int [modem\_ubx\_init](group__modem__ubx.md#gaf49363fb4decb4656566b508a061212f)(struct [modem\_ubx](structmodem__ubx.md) \*ubx, const struct [modem\_ubx\_config](structmodem__ubx__config.md) \*config);

121

[ 148](group__modem__ubx.md#ga770650b055fd597f000a1d4f9daaf712)int [modem\_ubx\_run\_script](group__modem__ubx.md#ga770650b055fd597f000a1d4f9daaf712)(struct [modem\_ubx](structmodem__ubx.md) \*ubx, struct [modem\_ubx\_script](structmodem__ubx__script.md) \*script);

149

[ 150](group__modem__ubx.md#ga0fd0def90f6304e679c4123e3c8d0c3f)int [modem\_ubx\_run\_script\_for\_each](group__modem__ubx.md#ga0fd0def90f6304e679c4123e3c8d0c3f)(struct [modem\_ubx](structmodem__ubx.md) \*ubx, struct [modem\_ubx\_script](structmodem__ubx__script.md) \*script,

151 struct [ubx\_frame](structubx__frame.md) \*array, size\_t array\_size);

152

156

157#ifdef \_\_cplusplus

158}

159#endif

160

161#endif /\* ZEPHYR\_MODEM\_UBX\_ \*/

[atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8)

long atomic\_t

**Definition** atomic\_types.h:15

[modem\_ubx\_run\_script\_for\_each](group__modem__ubx.md#ga0fd0def90f6304e679c4123e3c8d0c3f)

int modem\_ubx\_run\_script\_for\_each(struct modem\_ubx \*ubx, struct modem\_ubx\_script \*script, struct ubx\_frame \*array, size\_t array\_size)

[modem\_ubx\_attach](group__modem__ubx.md#ga4e459f955e34c9059702c3d7f9794948)

int modem\_ubx\_attach(struct modem\_ubx \*ubx, struct modem\_pipe \*pipe)

Attach pipe to Modem Ubx.

[modem\_ubx\_release](group__modem__ubx.md#ga68210f4afd5880c532d82fd0bac1d933)

void modem\_ubx\_release(struct modem\_ubx \*ubx)

Release pipe from Modem Ubx instance.

[modem\_ubx\_run\_script](group__modem__ubx.md#ga770650b055fd597f000a1d4f9daaf712)

int modem\_ubx\_run\_script(struct modem\_ubx \*ubx, struct modem\_ubx\_script \*script)

Writes the ubx frame in script.request and reads back its response (if available).

[modem\_ubx\_match\_callback](group__modem__ubx.md#gae0bfe22e7e8d7d38ae9f41648f7fcfda)

void(\* modem\_ubx\_match\_callback)(struct modem\_ubx \*ubx, const struct ubx\_frame \*frame, size\_t len, void \*user\_data)

**Definition** ubx.h:32

[modem\_ubx\_init](group__modem__ubx.md#gaf49363fb4decb4656566b508a061212f)

int modem\_ubx\_init(struct modem\_ubx \*ubx, const struct modem\_ubx\_config \*config)

Initialize Modem Ubx instance.

[types.h](include_2zephyr_2types_8h.md)

[kernel.h](kernel_8h.md)

Public kernel APIs.

[protocol.h](modem_2ubx_2protocol_8h.md)

[pipe.h](pipe_8h.md)

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[k\_sem](structk__sem.md)

Semaphore structure.

**Definition** kernel.h:3275

[k\_timeout\_t](structk__timeout__t.md)

Kernel timeout type.

**Definition** clock.h:65

[k\_work](structk__work.md)

A structure used to submit work.

**Definition** kernel.h:4073

[modem\_ubx\_config](structmodem__ubx__config.md)

**Definition** ubx.h:86

[modem\_ubx\_config::unsol\_matches](structmodem__ubx__config.md#a08ba4ac10872f451a302fcbc04a04253)

struct modem\_ubx\_config::@064247072102043330135135206211045316343340146202 unsol\_matches

[modem\_ubx\_config::size](structmodem__ubx__config.md#a19f107638346a44bddc73045f595ec98)

size\_t size

**Definition** ubx.h:92

[modem\_ubx\_config::array](structmodem__ubx__config.md#a75237681e1c9bf094b347e71e1ad823e)

const struct modem\_ubx\_match \* array

**Definition** ubx.h:91

[modem\_ubx\_config::receive\_buf\_size](structmodem__ubx__config.md#a75634cde7a69ef78ea0370f423307a0e)

uint16\_t receive\_buf\_size

**Definition** ubx.h:89

[modem\_ubx\_config::receive\_buf](structmodem__ubx__config.md#a7ac0f254167c3197366b210bef2ac75d)

uint8\_t \* receive\_buf

**Definition** ubx.h:88

[modem\_ubx\_config::user\_data](structmodem__ubx__config.md#acac2ab2800443c4f60cbf5df9ca8cd5e)

void \* user\_data

**Definition** ubx.h:87

[modem\_ubx\_match](structmodem__ubx__match.md)

**Definition** ubx.h:37

[modem\_ubx\_match::handler](structmodem__ubx__match.md#a657d7961121ed1860635df96597b88b8)

modem\_ubx\_match\_callback handler

**Definition** ubx.h:39

[modem\_ubx\_match::filter](structmodem__ubx__match.md#aba64a4f7825a1f3b3cbee6f3473d7f74)

struct ubx\_frame\_match filter

**Definition** ubx.h:38

[modem\_ubx\_script](structmodem__ubx__script.md)

**Definition** ubx.h:54

[modem\_ubx\_script::len](structmodem__ubx__script.md#a033047efbf34102985fad507711905ec)

uint16\_t len

**Definition** ubx.h:57

[modem\_ubx\_script::timeout](structmodem__ubx__script.md#a041de757b5fb26f1cdfb89cb19610f11)

k\_timeout\_t timeout

**Definition** ubx.h:66

[modem\_ubx\_script::match](structmodem__ubx__script.md#a1e91925ba17f30685db67d4f326d2f31)

struct modem\_ubx\_match match

**Definition** ubx.h:64

[modem\_ubx\_script::retry\_count](structmodem__ubx__script.md#a4910a3551004f19249c66a5b695795ce)

uint16\_t retry\_count

**Definition** ubx.h:65

[modem\_ubx\_script::received\_len](structmodem__ubx__script.md#a716f90ed421af01c829cb716d94a9a76)

uint16\_t received\_len

**Definition** ubx.h:62

[modem\_ubx\_script::response](structmodem__ubx__script.md#a90d08ee6c3832f3d0198cea0aa7b3b8d)

struct modem\_ubx\_script::@125262324261144301256337001320113377072112120173 response

[modem\_ubx\_script::buf\_len](structmodem__ubx__script.md#a9882eb3b10b9739c916f5317fda412ea)

uint16\_t buf\_len

**Definition** ubx.h:61

[modem\_ubx\_script::buf](structmodem__ubx__script.md#aade7c60068e44b39bfac09415e31417c)

const struct ubx\_frame \* buf

**Definition** ubx.h:56

[modem\_ubx\_script::request](structmodem__ubx__script.md#ab91b22317aa1cfb36f7c24de2b425137)

struct modem\_ubx\_script::@352254277043233371101045333366114317241110234076 request

[modem\_ubx](structmodem__ubx.md)

**Definition** ubx.h:69

[modem\_ubx::script\_running\_sem](structmodem__ubx.md#a0489f188b1dcdd54ba756ad821c62db5)

struct k\_sem script\_running\_sem

**Definition** ubx.h:79

[modem\_ubx::receive\_buf](structmodem__ubx.md#a0bc3ee485c2e6f63727efae5b61a64ac)

uint8\_t \* receive\_buf

**Definition** ubx.h:72

[modem\_ubx::pipe](structmodem__ubx.md#a1b853c80109313feaebfb8cdb24b950c)

struct modem\_pipe \* pipe

**Definition** ubx.h:76

[modem\_ubx::attached](structmodem__ubx.md#a337b4afe37e031ecd563572951be9412)

atomic\_t attached

**Definition** ubx.h:71

[modem\_ubx::receive\_buf\_size](structmodem__ubx.md#a4add513db024eb040de858e8901bc017)

uint16\_t receive\_buf\_size

**Definition** ubx.h:73

[modem\_ubx::receive\_buf\_offset](structmodem__ubx.md#a639183a5a24d953015df30f64b2f1c85)

uint16\_t receive\_buf\_offset

**Definition** ubx.h:74

[modem\_ubx::size](structmodem__ubx.md#a98b8d6b02acbfa564b510b6f7c9908d5)

size\_t size

**Definition** ubx.h:82

[modem\_ubx::script](structmodem__ubx.md#ac9a3b4009eabeb92e2e3cff093d74d2c)

struct modem\_ubx\_script \* script

**Definition** ubx.h:75

[modem\_ubx::user\_data](structmodem__ubx.md#ad98fcc4a93781ff5cd5406cb0560c849)

void \* user\_data

**Definition** ubx.h:70

[modem\_ubx::process\_work](structmodem__ubx.md#adfd9249b1f72aae1f2b9818cbf0de640)

struct k\_work process\_work

**Definition** ubx.h:77

[modem\_ubx::script\_stopped\_sem](structmodem__ubx.md#ae5c5914a3c88b908e80646d71ada7bfe)

struct k\_sem script\_stopped\_sem

**Definition** ubx.h:78

[modem\_ubx::array](structmodem__ubx.md#ae7182d2345bcd3585828f0f48d42321a)

const struct modem\_ubx\_match \* array

**Definition** ubx.h:81

[modem\_ubx::unsol\_matches](structmodem__ubx.md#aeeb735c338ed161d7eddeaa561cca5d9)

struct modem\_ubx::@222303241252066212057020164220110307037317275334 unsol\_matches

[ubx\_frame\_match](structubx__frame__match.md)

**Definition** protocol.h:38

[ubx\_frame](structubx__frame.md)

**Definition** protocol.h:29

[atomic.h](sys_2atomic_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [modem](dir_a816d481c0f951d2967bb275acf5f3dd.md)
- [ubx.h](ubx_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

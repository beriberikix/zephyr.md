---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/hdr__ddr_8h_source.html
original_path: doxygen/html/hdr__ddr_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

hdr\_ddr.h

[Go to the documentation of this file.](hdr__ddr_8h.md)

1/\*

2 \* Copyright 2024 Meta Platforms

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_I3C\_HDR\_DDR\_H\_

8#define ZEPHYR\_INCLUDE\_DRIVERS\_I3C\_HDR\_DDR\_H\_

9

16

17#include <[errno.h](errno_8h.md)>

18#include <stddef.h>

19#include <[stdint.h](stdint_8h.md)>

20

21#include <[zephyr/drivers/i3c.h](i3c_8h.md)>

22

23#ifdef \_\_cplusplus

24extern "C" {

25#endif

26

[ 41](group__i3c__hdr__ddr.md#ga9bf00a59c3c08f4bf1ffd5ae32c0fad8)static inline int [i3c\_hdr\_ddr\_write](group__i3c__hdr__ddr.md#ga9bf00a59c3c08f4bf1ffd5ae32c0fad8)(struct [i3c\_device\_desc](structi3c__device__desc.md) \*target, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615),

42 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_bytes)

43{

44 struct [i3c\_msg](structi3c__msg.md) msg;

45

46 msg.[buf](structi3c__msg.md#aa9d8920782b1a024b70970d60886deff) = [buf](structi3c__msg.md#aa9d8920782b1a024b70970d60886deff);

47 msg.[len](structi3c__msg.md#ada6582cdd126f36e64f17f66ae3817f0) = num\_bytes;

48 msg.[flags](structi3c__msg.md#a05113fb61ebbc95ded15fcfe374c0217) = [I3C\_MSG\_WRITE](group__i3c__transfer__api.md#ga72f9fb65d218521ad006febf3dd6851b) | [I3C\_MSG\_STOP](group__i3c__transfer__api.md#ga0d4ae269a53af945837d158f638d8b5c) | [I3C\_MSG\_HDR](group__i3c__transfer__api.md#gad827935caf8503aeaedd1aceb53d4e38);

49 msg.[hdr\_mode](structi3c__msg.md#a53f5ef80b2cf467e9ff557be7cc568c9) = [I3C\_MSG\_HDR\_DDR](group__i3c__transfer__api.md#gac7386b21323d30148bd9456b9d180d7a);

50 msg.[hdr\_cmd\_code](structi3c__msg.md#acab199ec89bfa84915c66e71c872a40b) = [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615);

51

52 return [i3c\_transfer](group__i3c__transfer__api.md#ga067c0f1e3c9abb6ef34ce48cb7e45cb8)(target, &msg, 1);

53}

54

[ 69](group__i3c__hdr__ddr.md#ga11e788383aeb52184fdd6483cf702d40)static inline int [i3c\_hdr\_ddr\_read](group__i3c__hdr__ddr.md#ga11e788383aeb52184fdd6483cf702d40)(struct [i3c\_device\_desc](structi3c__device__desc.md) \*target, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615),

70 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[buf](structi3c__msg.md#aa9d8920782b1a024b70970d60886deff), [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_bytes)

71{

72 struct [i3c\_msg](structi3c__msg.md) msg;

73

74 msg.[buf](structi3c__msg.md#aa9d8920782b1a024b70970d60886deff) = [buf](structi3c__msg.md#aa9d8920782b1a024b70970d60886deff);

75 msg.[len](structi3c__msg.md#ada6582cdd126f36e64f17f66ae3817f0) = num\_bytes;

76 msg.[flags](structi3c__msg.md#a05113fb61ebbc95ded15fcfe374c0217) = [I3C\_MSG\_STOP](group__i3c__transfer__api.md#ga0d4ae269a53af945837d158f638d8b5c) | [I3C\_MSG\_HDR](group__i3c__transfer__api.md#gad827935caf8503aeaedd1aceb53d4e38);

77 msg.[hdr\_mode](structi3c__msg.md#a53f5ef80b2cf467e9ff557be7cc568c9) = [I3C\_MSG\_HDR\_DDR](group__i3c__transfer__api.md#gac7386b21323d30148bd9456b9d180d7a);

78 msg.[hdr\_cmd\_code](structi3c__msg.md#acab199ec89bfa84915c66e71c872a40b) = [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615);

79

80 return [i3c\_transfer](group__i3c__transfer__api.md#ga067c0f1e3c9abb6ef34ce48cb7e45cb8)(target, &msg, 1);

81}

82

[ 102](group__i3c__hdr__ddr.md#gaa752f1095c84ad1b94fb09cc0aeee4fa)static inline int [i3c\_hdr\_ddr\_write\_read](group__i3c__hdr__ddr.md#gaa752f1095c84ad1b94fb09cc0aeee4fa)(struct [i3c\_device\_desc](structi3c__device__desc.md) \*target,

103 const void \*write\_buf, size\_t num\_write, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) read\_cmd,

104 void \*read\_buf, size\_t num\_read, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) write\_cmd)

105{

106 struct [i3c\_msg](structi3c__msg.md) msg[2];

107

108 msg[0].[buf](structi3c__msg.md#aa9d8920782b1a024b70970d60886deff) = ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*)write\_buf;

109 msg[0].[len](structi3c__msg.md#ada6582cdd126f36e64f17f66ae3817f0) = num\_write;

110 msg[0].[flags](structi3c__msg.md#a05113fb61ebbc95ded15fcfe374c0217) = [I3C\_MSG\_WRITE](group__i3c__transfer__api.md#ga72f9fb65d218521ad006febf3dd6851b) | [I3C\_MSG\_HDR](group__i3c__transfer__api.md#gad827935caf8503aeaedd1aceb53d4e38);

111 msg[0].[hdr\_mode](structi3c__msg.md#a53f5ef80b2cf467e9ff557be7cc568c9) = [I3C\_MSG\_HDR\_DDR](group__i3c__transfer__api.md#gac7386b21323d30148bd9456b9d180d7a);

112 msg[0].[hdr\_cmd\_code](structi3c__msg.md#acab199ec89bfa84915c66e71c872a40b) = write\_cmd;

113

114 msg[1].[buf](structi3c__msg.md#aa9d8920782b1a024b70970d60886deff) = ([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*)read\_buf;

115 msg[1].[len](structi3c__msg.md#ada6582cdd126f36e64f17f66ae3817f0) = num\_read;

116 msg[1].[flags](structi3c__msg.md#a05113fb61ebbc95ded15fcfe374c0217) = [I3C\_MSG\_RESTART](group__i3c__transfer__api.md#gad9ff03f4fdcb117b90c17d667a49c295) | [I3C\_MSG\_READ](group__i3c__transfer__api.md#ga6ba89782a8646f96dc1f9fa3b9cd2058) | [I3C\_MSG\_HDR](group__i3c__transfer__api.md#gad827935caf8503aeaedd1aceb53d4e38) | [I3C\_MSG\_STOP](group__i3c__transfer__api.md#ga0d4ae269a53af945837d158f638d8b5c);

117 msg[1].[hdr\_mode](structi3c__msg.md#a53f5ef80b2cf467e9ff557be7cc568c9) = [I3C\_MSG\_HDR\_DDR](group__i3c__transfer__api.md#gac7386b21323d30148bd9456b9d180d7a);

118 msg[1].[hdr\_cmd\_code](structi3c__msg.md#acab199ec89bfa84915c66e71c872a40b) = read\_cmd;

119

120 return [i3c\_transfer](group__i3c__transfer__api.md#ga067c0f1e3c9abb6ef34ce48cb7e45cb8)(target, msg, 2);

121}

122

123#ifdef \_\_cplusplus

124}

125#endif

126

130

131#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_I3C\_HDR\_DDR\_H\_ \*/

[errno.h](errno_8h.md)

System error numbers.

[cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615)

static void cmd(uint32\_t command)

Execute a display list command by co-processor engine.

**Definition** ft8xx\_reference\_api.h:153

[i3c\_hdr\_ddr\_read](group__i3c__hdr__ddr.md#ga11e788383aeb52184fdd6483cf702d40)

static int i3c\_hdr\_ddr\_read(struct i3c\_device\_desc \*target, uint8\_t cmd, uint8\_t \*buf, uint32\_t num\_bytes)

Read a set amount of data from an I3C target device with HDR DDR.

**Definition** hdr\_ddr.h:69

[i3c\_hdr\_ddr\_write](group__i3c__hdr__ddr.md#ga9bf00a59c3c08f4bf1ffd5ae32c0fad8)

static int i3c\_hdr\_ddr\_write(struct i3c\_device\_desc \*target, uint8\_t cmd, uint8\_t \*buf, uint32\_t num\_bytes)

Write a set amount of data to an I3C target device with HDR DDR.

**Definition** hdr\_ddr.h:41

[i3c\_hdr\_ddr\_write\_read](group__i3c__hdr__ddr.md#gaa752f1095c84ad1b94fb09cc0aeee4fa)

static int i3c\_hdr\_ddr\_write\_read(struct i3c\_device\_desc \*target, const void \*write\_buf, size\_t num\_write, uint8\_t read\_cmd, void \*read\_buf, size\_t num\_read, uint8\_t write\_cmd)

Write then read data from an I3C target device with HDR DDR.

**Definition** hdr\_ddr.h:102

[i3c\_transfer](group__i3c__transfer__api.md#ga067c0f1e3c9abb6ef34ce48cb7e45cb8)

int i3c\_transfer(struct i3c\_device\_desc \*target, struct i3c\_msg \*msgs, uint8\_t num\_msgs)

Perform data transfer from the controller to a I3C target device.

[I3C\_MSG\_STOP](group__i3c__transfer__api.md#ga0d4ae269a53af945837d158f638d8b5c)

#define I3C\_MSG\_STOP

Send STOP after this message.

**Definition** i3c.h:396

[I3C\_MSG\_READ](group__i3c__transfer__api.md#ga6ba89782a8646f96dc1f9fa3b9cd2058)

#define I3C\_MSG\_READ

Read message from I3C bus.

**Definition** i3c.h:389

[I3C\_MSG\_WRITE](group__i3c__transfer__api.md#ga72f9fb65d218521ad006febf3dd6851b)

#define I3C\_MSG\_WRITE

Write message to I3C bus.

**Definition** i3c.h:386

[I3C\_MSG\_HDR\_DDR](group__i3c__transfer__api.md#gac7386b21323d30148bd9456b9d180d7a)

#define I3C\_MSG\_HDR\_DDR

I3C HDR-DDR (Double Data Rate).

**Definition** i3c.h:440

[I3C\_MSG\_HDR](group__i3c__transfer__api.md#gad827935caf8503aeaedd1aceb53d4e38)

#define I3C\_MSG\_HDR

Transfer use HDR mode.

**Definition** i3c.h:410

[I3C\_MSG\_RESTART](group__i3c__transfer__api.md#gad9ff03f4fdcb117b90c17d667a49c295)

#define I3C\_MSG\_RESTART

RESTART I3C transaction for this message.

**Definition** i3c.h:407

[i3c.h](i3c_8h.md)

[stdint.h](stdint_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[i3c\_device\_desc](structi3c__device__desc.md)

Structure describing a I3C target device.

**Definition** i3c.h:913

[i3c\_msg](structi3c__msg.md)

One I3C Message.

**Definition** i3c.h:472

[i3c\_msg::flags](structi3c__msg.md#a05113fb61ebbc95ded15fcfe374c0217)

uint8\_t flags

Flags for this message.

**Definition** i3c.h:489

[i3c\_msg::hdr\_mode](structi3c__msg.md#a53f5ef80b2cf467e9ff557be7cc568c9)

uint8\_t hdr\_mode

HDR mode (I3C\_MSG\_HDR\_MODE\*) for transfer if any I3C\_MSG\_HDR\_\* is set in flags.

**Definition** i3c.h:497

[i3c\_msg::buf](structi3c__msg.md#aa9d8920782b1a024b70970d60886deff)

uint8\_t \* buf

Data buffer in bytes.

**Definition** i3c.h:474

[i3c\_msg::hdr\_cmd\_code](structi3c__msg.md#acab199ec89bfa84915c66e71c872a40b)

uint8\_t hdr\_cmd\_code

HDR command code field (7-bit) for HDR-DDR, HDR-TSP and HDR-TSL.

**Definition** i3c.h:500

[i3c\_msg::len](structi3c__msg.md#ada6582cdd126f36e64f17f66ae3817f0)

uint32\_t len

Length of buffer in bytes.

**Definition** i3c.h:477

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [i3c](dir_7fe10d7a610a8b04680264e2afe29300.md)
- [hdr\_ddr.h](hdr__ddr_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

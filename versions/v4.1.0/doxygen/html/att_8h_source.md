---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/att_8h_source.html
original_path: doxygen/html/att_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

att.h

[Go to the documentation of this file.](att_8h.md)

1

4

5/\*

6 \* Copyright (c) 2016 Intel Corporation

7 \*

8 \* SPDX-License-Identifier: Apache-2.0

9 \*/

10#ifndef ZEPHYR\_INCLUDE\_BLUETOOTH\_ATT\_H\_

11#define ZEPHYR\_INCLUDE\_BLUETOOTH\_ATT\_H\_

12

19

20#include <[zephyr/sys/slist.h](slist_8h.md)>

21#include <[zephyr/bluetooth/conn.h](conn_8h.md)>

22

23#ifdef \_\_cplusplus

24extern "C" {

25#endif

26

27/\* Error codes for Error response PDU

28 \*

29 \* Defined by The Bluetooth Core Specification, Version 5.4, Vol 3, Part F, Section 3.4.1.1

30 \*/

[ 32](group__bt__att.md#ga0032756d54c08d37c101769be8ef2070)#define BT\_ATT\_ERR\_SUCCESS 0x00

[ 34](group__bt__att.md#gab8d9a6870360f0e5dd7290895202879f)#define BT\_ATT\_ERR\_INVALID\_HANDLE 0x01

[ 36](group__bt__att.md#gac26ed224b7f8fb7717b40fe3a545be7e)#define BT\_ATT\_ERR\_READ\_NOT\_PERMITTED 0x02

[ 38](group__bt__att.md#ga2378ff92f5afaff1e4392b1dc2e7326c)#define BT\_ATT\_ERR\_WRITE\_NOT\_PERMITTED 0x03

[ 40](group__bt__att.md#ga7f1cbe6eb3ed0999bafab729c7b0a6a6)#define BT\_ATT\_ERR\_INVALID\_PDU 0x04

[ 42](group__bt__att.md#ga269e711af78a7a30a770b3d7db210c8a)#define BT\_ATT\_ERR\_AUTHENTICATION 0x05

[ 44](group__bt__att.md#gafcfa214f6f5b600647886f27cebecb49)#define BT\_ATT\_ERR\_NOT\_SUPPORTED 0x06

[ 46](group__bt__att.md#ga997d113b71af6b4019c26ca3893f3dbb)#define BT\_ATT\_ERR\_INVALID\_OFFSET 0x07

[ 48](group__bt__att.md#ga30b28071d7057c2c68b10da34ba32faf)#define BT\_ATT\_ERR\_AUTHORIZATION 0x08

[ 50](group__bt__att.md#gaa135b2315173e7852afe4e1624169ce2)#define BT\_ATT\_ERR\_PREPARE\_QUEUE\_FULL 0x09

[ 52](group__bt__att.md#ga5dfcd07918dc665bf600a25608b0736d)#define BT\_ATT\_ERR\_ATTRIBUTE\_NOT\_FOUND 0x0a

[ 54](group__bt__att.md#ga240561711499f11b267d2e5ed8fc99f5)#define BT\_ATT\_ERR\_ATTRIBUTE\_NOT\_LONG 0x0b

[ 56](group__bt__att.md#ga2ed58d79dfbd701a97377b171f1b0793)#define BT\_ATT\_ERR\_ENCRYPTION\_KEY\_SIZE 0x0c

[ 58](group__bt__att.md#ga21207d5beb27fe50856f001bd18e1efa)#define BT\_ATT\_ERR\_INVALID\_ATTRIBUTE\_LEN 0x0d

[ 64](group__bt__att.md#ga992baa1f0d763a00f314bdcf59965bdd)#define BT\_ATT\_ERR\_UNLIKELY 0x0e

[ 66](group__bt__att.md#ga8a5235e39b05fa85b5b4f4bfb449683b)#define BT\_ATT\_ERR\_INSUFFICIENT\_ENCRYPTION 0x0f

[ 73](group__bt__att.md#ga0611fc39d9d09ea4f0e556b4910f09ed)#define BT\_ATT\_ERR\_UNSUPPORTED\_GROUP\_TYPE 0x10

[ 75](group__bt__att.md#gaf4a81bc81cad14bf91463d4376a3a868)#define BT\_ATT\_ERR\_INSUFFICIENT\_RESOURCES 0x11

[ 77](group__bt__att.md#ga2b9a58bf48f1b76e743cb7fef3aed3a8)#define BT\_ATT\_ERR\_DB\_OUT\_OF\_SYNC 0x12

[ 79](group__bt__att.md#ga52ffe5ff2eb092bcdc2ebb05684030d7)#define BT\_ATT\_ERR\_VALUE\_NOT\_ALLOWED 0x13

80

81/\* Common Profile Error Codes

82 \*

83 \* Defined by the Supplement to the Bluetooth Core Specification (CSS), v11, Part B, Section 1.2.

84 \*/

[ 86](group__bt__att.md#ga8363770d0832f3df8fb1d0a22bc3551e)#define BT\_ATT\_ERR\_WRITE\_REQ\_REJECTED 0xfc

[ 88](group__bt__att.md#ga8f623146d7fda4b71514277cfbcd4b21)#define BT\_ATT\_ERR\_CCC\_IMPROPER\_CONF 0xfd

[ 90](group__bt__att.md#gaf9e46c363487c61dbff50790993107f7)#define BT\_ATT\_ERR\_PROCEDURE\_IN\_PROGRESS 0xfe

[ 92](group__bt__att.md#gad49773d5e7a39f49c5a06bbaa4f8c365)#define BT\_ATT\_ERR\_OUT\_OF\_RANGE 0xff

93

94/\* Version 5.2, Vol 3, Part F, 3.2.9 defines maximum attribute length to 512 \*/

[ 95](group__bt__att.md#ga3c4df4336916e082115d43f9716acb36)#define BT\_ATT\_MAX\_ATTRIBUTE\_LEN 512

96

97/\* Handle 0x0000 is reserved for future use \*/

[ 98](group__bt__att.md#gad0aa088f621b8965013c3ced27480df7)#define BT\_ATT\_FIRST\_ATTRIBUTE\_HANDLE 0x0001

99/\* 0xffff is defined as the maximum, and thus last, valid attribute handle \*/

[ 100](group__bt__att.md#ga1b3dc5fedec8d8632d3650405d1ff988)#define BT\_ATT\_LAST\_ATTRIBUTE\_HANDLE 0xffff

101

118#if defined(CONFIG\_BT\_ATT\_ERR\_TO\_STR)

119const char \*[bt\_att\_err\_to\_str](group__bt__att.md#gad2305f28744276d97aefd26bdb79023c)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) att\_err);

120#else

[ 121](group__bt__att.md#gad2305f28744276d97aefd26bdb79023c)static inline const char \*[bt\_att\_err\_to\_str](group__bt__att.md#gad2305f28744276d97aefd26bdb79023c)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) att\_err)

122{

123 ARG\_UNUSED(att\_err);

124

125 return "";

126}

127#endif

128

129#if defined(CONFIG\_BT\_EATT)

130#if defined(CONFIG\_BT\_TESTING)

131

132int bt\_eatt\_disconnect\_one(struct bt\_conn \*conn);

133

134/\* Reconfigure all EATT channels on connection \*/

135int bt\_eatt\_reconfigure(struct bt\_conn \*conn, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) mtu);

136

137#endif /\* CONFIG\_BT\_TESTING \*/

138

[ 154](group__bt__att.md#ga748194cbbd54a3336d3c788f08e3de99)int [bt\_eatt\_connect](group__bt__att.md#ga748194cbbd54a3336d3c788f08e3de99)(struct bt\_conn \*conn, size\_t num\_channels);

155

[ 163](group__bt__att.md#ga3cabc05e8f5c0418ff02dd7122b7565e)size\_t [bt\_eatt\_count](group__bt__att.md#ga3cabc05e8f5c0418ff02dd7122b7565e)(struct bt\_conn \*conn);

164

165#endif /\* CONFIG\_BT\_EATT \*/

166

[ 171](group__bt__att.md#gac593a27ecf029f33f50f990b2947562c)enum [bt\_att\_chan\_opt](group__bt__att.md#gac593a27ecf029f33f50f990b2947562c) {

[ 173](group__bt__att.md#ggac593a27ecf029f33f50f990b2947562ca14e709b93e78dcc511339a99360ba739) [BT\_ATT\_CHAN\_OPT\_NONE](group__bt__att.md#ggac593a27ecf029f33f50f990b2947562ca14e709b93e78dcc511339a99360ba739) = 0x0,

[ 175](group__bt__att.md#ggac593a27ecf029f33f50f990b2947562ca72c7152b997d4726347c2bfda7da94c4) [BT\_ATT\_CHAN\_OPT\_UNENHANCED\_ONLY](group__bt__att.md#ggac593a27ecf029f33f50f990b2947562ca72c7152b997d4726347c2bfda7da94c4) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

[ 177](group__bt__att.md#ggac593a27ecf029f33f50f990b2947562ca7bfd06bd0c22eb16b82a4cbed6675ed6) [BT\_ATT\_CHAN\_OPT\_ENHANCED\_ONLY](group__bt__att.md#ggac593a27ecf029f33f50f990b2947562ca7bfd06bd0c22eb16b82a4cbed6675ed6) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

178};

179

180#ifdef \_\_cplusplus

181}

182#endif

183

187

188#endif /\* ZEPHYR\_INCLUDE\_BLUETOOTH\_ATT\_H\_ \*/

[conn.h](conn_8h.md)

Bluetooth connection handling.

[bt\_eatt\_count](group__bt__att.md#ga3cabc05e8f5c0418ff02dd7122b7565e)

size\_t bt\_eatt\_count(struct bt\_conn \*conn)

Get number of EATT channels connected.

[bt\_eatt\_connect](group__bt__att.md#ga748194cbbd54a3336d3c788f08e3de99)

int bt\_eatt\_connect(struct bt\_conn \*conn, size\_t num\_channels)

Connect Enhanced ATT channels.

[bt\_att\_chan\_opt](group__bt__att.md#gac593a27ecf029f33f50f990b2947562c)

bt\_att\_chan\_opt

ATT channel option bit field values.

**Definition** att.h:171

[bt\_att\_err\_to\_str](group__bt__att.md#gad2305f28744276d97aefd26bdb79023c)

static const char \* bt\_att\_err\_to\_str(uint8\_t att\_err)

Converts a ATT error to string.

**Definition** att.h:121

[BT\_ATT\_CHAN\_OPT\_NONE](group__bt__att.md#ggac593a27ecf029f33f50f990b2947562ca14e709b93e78dcc511339a99360ba739)

@ BT\_ATT\_CHAN\_OPT\_NONE

Both Enhanced and Unenhanced channels can be used.

**Definition** att.h:173

[BT\_ATT\_CHAN\_OPT\_UNENHANCED\_ONLY](group__bt__att.md#ggac593a27ecf029f33f50f990b2947562ca72c7152b997d4726347c2bfda7da94c4)

@ BT\_ATT\_CHAN\_OPT\_UNENHANCED\_ONLY

Only Unenhanced channels will be used.

**Definition** att.h:175

[BT\_ATT\_CHAN\_OPT\_ENHANCED\_ONLY](group__bt__att.md#ggac593a27ecf029f33f50f990b2947562ca7bfd06bd0c22eb16b82a4cbed6675ed6)

@ BT\_ATT\_CHAN\_OPT\_ENHANCED\_ONLY

Only Enhanced channels will be used.

**Definition** att.h:177

[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)

#define BIT(n)

Unsigned integer with bit position n set (signed in assembly language).

**Definition** util\_macro.h:44

[slist.h](slist_8h.md)

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [bluetooth](dir_1e7161d1e31b4a807184ef42c14f2a24.md)
- [att.h](att_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

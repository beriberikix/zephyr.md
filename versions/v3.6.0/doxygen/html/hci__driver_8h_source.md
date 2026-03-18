---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/hci__driver_8h_source.html
original_path: doxygen/html/hci__driver_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

hci\_driver.h

[Go to the documentation of this file.](hci__driver_8h.md)

1

4

5/\*

6 \* Copyright (c) 2015-2016 Intel Corporation

7 \*

8 \* SPDX-License-Identifier: Apache-2.0

9 \*/

10#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_BLUETOOTH\_HCI\_DRIVER\_H\_

11#define ZEPHYR\_INCLUDE\_DRIVERS\_BLUETOOTH\_HCI\_DRIVER\_H\_

12

19

20#include <[stdbool.h](stdbool_8h.md)>

21#include <[zephyr/net/buf.h](net_2buf_8h.md)>

22#include <[zephyr/bluetooth/buf.h](bluetooth_2buf_8h.md)>

23#include <[zephyr/bluetooth/hci\_vs.h](hci__vs_8h.md)>

24#include <[zephyr/device.h](device_8h.md)>

25

26#ifdef \_\_cplusplus

27extern "C" {

28#endif

29

30enum {

31 /\* The host should never send HCI\_Reset \*/

[ 32](group__bt__hci__driver.md#gga8f5a83b514f6d2da7548c38f7c3c166ea18274691e4c0129f945e88304778a241) [BT\_QUIRK\_NO\_RESET](group__bt__hci__driver.md#gga8f5a83b514f6d2da7548c38f7c3c166ea18274691e4c0129f945e88304778a241) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

33 /\* The controller does not auto-initiate a DLE procedure when the

34 \* initial connection data length parameters are not equal to the

35 \* default data length parameters. Therefore the host should initiate

36 \* the DLE procedure after connection establishment. \*/

[ 37](group__bt__hci__driver.md#gga8f5a83b514f6d2da7548c38f7c3c166ea7b8e6d2f5604015c92c623193b9fe1e4) [BT\_QUIRK\_NO\_AUTO\_DLE](group__bt__hci__driver.md#gga8f5a83b514f6d2da7548c38f7c3c166ea7b8e6d2f5604015c92c623193b9fe1e4) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

38};

39

[ 40](group__bt__hci__driver.md#ga011e658a6ae4f947412b294cf423178f)#define IS\_BT\_QUIRK\_NO\_AUTO\_DLE(bt\_dev) ((bt\_dev)->drv->quirks & BT\_QUIRK\_NO\_AUTO\_DLE)

41

42/\* @brief The HCI event shall be given to bt\_recv\_prio \*/

[ 43](group__bt__hci__driver.md#gaa7a28bc6e6a79128d3a95c3ccd3b1866)#define BT\_HCI\_EVT\_FLAG\_RECV\_PRIO BIT(0)

44/\* @brief The HCI event shall be given to bt\_recv. \*/

[ 45](group__bt__hci__driver.md#ga61e4e2d22dec695f53f5aed6ce809859)#define BT\_HCI\_EVT\_FLAG\_RECV BIT(1)

46

[ 60](group__bt__hci__driver.md#ga1f1b10f6d84f4a5cf4b895b6685874ef)static inline [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bt\_hci\_evt\_get\_flags](group__bt__hci__driver.md#ga1f1b10f6d84f4a5cf4b895b6685874ef)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) evt)

61{

62 switch (evt) {

63 case [BT\_HCI\_EVT\_DISCONN\_COMPLETE](hci__types_8h.md#a32e5051a114f8987b49c6957c84d60e2):

64 return [BT\_HCI\_EVT\_FLAG\_RECV](group__bt__hci__driver.md#ga61e4e2d22dec695f53f5aed6ce809859) | [BT\_HCI\_EVT\_FLAG\_RECV\_PRIO](group__bt__hci__driver.md#gaa7a28bc6e6a79128d3a95c3ccd3b1866);

65 /\* fallthrough \*/

66#if defined(CONFIG\_BT\_CONN) || defined(CONFIG\_BT\_ISO)

67 case [BT\_HCI\_EVT\_NUM\_COMPLETED\_PACKETS](hci__types_8h.md#a883433c60959629a013d34cea21ab88f):

68#if defined(CONFIG\_BT\_CONN)

69 case [BT\_HCI\_EVT\_DATA\_BUF\_OVERFLOW](hci__types_8h.md#ae747b016101bc9e9614163288c5c0d15):

70 \_\_fallthrough;

71#endif /\* defined(CONFIG\_BT\_CONN) \*/

72#endif /\* CONFIG\_BT\_CONN || CONFIG\_BT\_ISO \*/

73 case [BT\_HCI\_EVT\_CMD\_COMPLETE](hci__types_8h.md#a06f6cf60885ac051cdc9b463fc3b7de7):

74 case [BT\_HCI\_EVT\_CMD\_STATUS](hci__types_8h.md#a2b35e7484351228243bb3564273c5bff):

75 return [BT\_HCI\_EVT\_FLAG\_RECV\_PRIO](group__bt__hci__driver.md#gaa7a28bc6e6a79128d3a95c3ccd3b1866);

76 default:

77 return [BT\_HCI\_EVT\_FLAG\_RECV](group__bt__hci__driver.md#ga61e4e2d22dec695f53f5aed6ce809859);

78 }

79}

80

[ 98](group__bt__hci__driver.md#gaca80bc9dacc4fa44416bd545bd185ef7)int [bt\_recv](group__bt__hci__driver.md#gaca80bc9dacc4fa44416bd545bd185ef7)(struct [net\_buf](structnet__buf.md) \*buf);

99

[ 117](group__bt__hci__driver.md#ga19c61df1660d6049ae6b03afe3554fee)int [bt\_recv\_prio](group__bt__hci__driver.md#ga19c61df1660d6049ae6b03afe3554fee)(struct [net\_buf](structnet__buf.md) \*buf);

118

[ 126](group__bt__hci__driver.md#ga502a6580da2e06f24f021c7bc4bff50f)[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [bt\_read\_static\_addr](group__bt__hci__driver.md#ga502a6580da2e06f24f021c7bc4bff50f)(struct [bt\_hci\_vs\_static\_addr](structbt__hci__vs__static__addr.md) addrs[], [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) size);

127

[ 129](group__bt__hci__driver.md#gaa24c7d2d9e2c35d6cd9cfcf650fb65ef)enum [bt\_hci\_driver\_bus](group__bt__hci__driver.md#gaa24c7d2d9e2c35d6cd9cfcf650fb65ef) {

[ 130](group__bt__hci__driver.md#ggaa24c7d2d9e2c35d6cd9cfcf650fb65efa885401f44dae9e39caf4a4838b547db9) [BT\_HCI\_DRIVER\_BUS\_VIRTUAL](group__bt__hci__driver.md#ggaa24c7d2d9e2c35d6cd9cfcf650fb65efa885401f44dae9e39caf4a4838b547db9) = 0,

[ 131](group__bt__hci__driver.md#ggaa24c7d2d9e2c35d6cd9cfcf650fb65efac2b08e3e52f795deabffd3638a421b68) [BT\_HCI\_DRIVER\_BUS\_USB](group__bt__hci__driver.md#ggaa24c7d2d9e2c35d6cd9cfcf650fb65efac2b08e3e52f795deabffd3638a421b68) = 1,

[ 132](group__bt__hci__driver.md#ggaa24c7d2d9e2c35d6cd9cfcf650fb65efa08bc821327d571bf9659eda7e06a5129) [BT\_HCI\_DRIVER\_BUS\_PCCARD](group__bt__hci__driver.md#ggaa24c7d2d9e2c35d6cd9cfcf650fb65efa08bc821327d571bf9659eda7e06a5129) = 2,

[ 133](group__bt__hci__driver.md#ggaa24c7d2d9e2c35d6cd9cfcf650fb65efa39c5fca0c61c99db6541d01fb55e41f4) [BT\_HCI\_DRIVER\_BUS\_UART](group__bt__hci__driver.md#ggaa24c7d2d9e2c35d6cd9cfcf650fb65efa39c5fca0c61c99db6541d01fb55e41f4) = 3,

[ 134](group__bt__hci__driver.md#ggaa24c7d2d9e2c35d6cd9cfcf650fb65efa5790e933f10773e30da6c7b922a443fa) [BT\_HCI\_DRIVER\_BUS\_RS232](group__bt__hci__driver.md#ggaa24c7d2d9e2c35d6cd9cfcf650fb65efa5790e933f10773e30da6c7b922a443fa) = 4,

[ 135](group__bt__hci__driver.md#ggaa24c7d2d9e2c35d6cd9cfcf650fb65efab4c130c7862cbbd6be7827b6462dab90) [BT\_HCI\_DRIVER\_BUS\_PCI](group__bt__hci__driver.md#ggaa24c7d2d9e2c35d6cd9cfcf650fb65efab4c130c7862cbbd6be7827b6462dab90) = 5,

[ 136](group__bt__hci__driver.md#ggaa24c7d2d9e2c35d6cd9cfcf650fb65efab572fbb186634bc08a3bce457cf38c74) [BT\_HCI\_DRIVER\_BUS\_SDIO](group__bt__hci__driver.md#ggaa24c7d2d9e2c35d6cd9cfcf650fb65efab572fbb186634bc08a3bce457cf38c74) = 6,

[ 137](group__bt__hci__driver.md#ggaa24c7d2d9e2c35d6cd9cfcf650fb65efa49f2ba9eeaafa266d905a30b2caf015a) [BT\_HCI\_DRIVER\_BUS\_SPI](group__bt__hci__driver.md#ggaa24c7d2d9e2c35d6cd9cfcf650fb65efa49f2ba9eeaafa266d905a30b2caf015a) = 7,

[ 138](group__bt__hci__driver.md#ggaa24c7d2d9e2c35d6cd9cfcf650fb65efa0d8c310b05d2c982e8de720dbdc2d742) [BT\_HCI\_DRIVER\_BUS\_I2C](group__bt__hci__driver.md#ggaa24c7d2d9e2c35d6cd9cfcf650fb65efa0d8c310b05d2c982e8de720dbdc2d742) = 8,

[ 139](group__bt__hci__driver.md#ggaa24c7d2d9e2c35d6cd9cfcf650fb65efa8473c5abdf2f5839c9df54fc00ee3800) [BT\_HCI\_DRIVER\_BUS\_IPM](group__bt__hci__driver.md#ggaa24c7d2d9e2c35d6cd9cfcf650fb65efa8473c5abdf2f5839c9df54fc00ee3800) = 9,

140};

141

142#if defined(CONFIG\_BT\_HCI\_SETUP) || defined(\_\_DOXYGEN\_\_)

[ 143](structbt__hci__setup__params.md)struct [bt\_hci\_setup\_params](structbt__hci__setup__params.md) {

[ 148](structbt__hci__setup__params.md#a6aea62826eeab39e6af40f9005548f3f) [bt\_addr\_t](structbt__addr__t.md) [public\_addr](structbt__hci__setup__params.md#a6aea62826eeab39e6af40f9005548f3f);

149};

150#endif

151

[ 158](structbt__hci__driver.md)struct [bt\_hci\_driver](structbt__hci__driver.md) {

[ 160](structbt__hci__driver.md#a4036d2609565058a46b1a677fc7ec93e) const char \*[name](structbt__hci__driver.md#a4036d2609565058a46b1a677fc7ec93e);

161

[ 163](structbt__hci__driver.md#acd9a4d631da22b4638afd4593cff7d0c) enum [bt\_hci\_driver\_bus](group__bt__hci__driver.md#gaa24c7d2d9e2c35d6cd9cfcf650fb65ef) [bus](structbt__hci__driver.md#acd9a4d631da22b4638afd4593cff7d0c);

164

[ 170](structbt__hci__driver.md#a0dd8d706ee7ded476a90b19a946226b8) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [quirks](structbt__hci__driver.md#a0dd8d706ee7ded476a90b19a946226b8);

171

[ 185](structbt__hci__driver.md#aabacc7c98a08a8a53f6aca436fac87d0) int (\*[open](structbt__hci__driver.md#aabacc7c98a08a8a53f6aca436fac87d0))(void);

186

[ 198](structbt__hci__driver.md#ae76bda7ebee44966554ba7b58da30e87) int (\*[close](structbt__hci__driver.md#ae76bda7ebee44966554ba7b58da30e87))(void);

199

[ 212](structbt__hci__driver.md#abcfc79474fc44aae260d61ff99fdb666) int (\*[send](structbt__hci__driver.md#abcfc79474fc44aae260d61ff99fdb666))(struct [net\_buf](structnet__buf.md) \*buf);

213

214#if defined(CONFIG\_BT\_HCI\_SETUP) || defined(\_\_DOXYGEN\_\_)

[ 226](structbt__hci__driver.md#af2dd8b2817aab56738e7f447987efd2b) int (\*[setup](structbt__hci__driver.md#af2dd8b2817aab56738e7f447987efd2b))(const struct [bt\_hci\_setup\_params](structbt__hci__setup__params.md) \*params);

227#endif /\* defined(CONFIG\_BT\_HCI\_SETUP) || defined(\_\_DOXYGEN\_\_)\*/

228};

229

[ 240](group__bt__hci__driver.md#ga642d226772448dccbd14f2c287d687f0)int [bt\_hci\_driver\_register](group__bt__hci__driver.md#ga642d226772448dccbd14f2c287d687f0)(const struct [bt\_hci\_driver](structbt__hci__driver.md) \*drv);

241

[ 253](group__bt__hci__driver.md#gadd813c1343955a7bb95135eb0fbe9cd5)int [bt\_hci\_transport\_setup](group__bt__hci__driver.md#gadd813c1343955a7bb95135eb0fbe9cd5)(const struct [device](structdevice.md) \*dev);

254

[ 266](group__bt__hci__driver.md#gae29dbf165252ddf9085c7387706fd09c)int [bt\_hci\_transport\_teardown](group__bt__hci__driver.md#gae29dbf165252ddf9085c7387706fd09c)(const struct [device](structdevice.md) \*dev);

267

[ 279](group__bt__hci__driver.md#ga362df79e2f782159f7e85d63817421bb)struct [net\_buf](structnet__buf.md) \*[bt\_hci\_evt\_create](group__bt__hci__driver.md#ga362df79e2f782159f7e85d63817421bb)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) evt, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [len](structnet__buf.md#ae75b7ca728fb7440ea483be8bf88bc38));

280

[ 293](group__bt__hci__driver.md#ga8ab7dc7d38f3bc7be72e34d7a9f14212)struct [net\_buf](structnet__buf.md) \*[bt\_hci\_cmd\_complete\_create](group__bt__hci__driver.md#ga8ab7dc7d38f3bc7be72e34d7a9f14212)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) op, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) plen);

294

[ 307](group__bt__hci__driver.md#gab6b790e6dd0e8251d6cf10b0a7cce5f7)struct [net\_buf](structnet__buf.md) \*[bt\_hci\_cmd\_status\_create](group__bt__hci__driver.md#gab6b790e6dd0e8251d6cf10b0a7cce5f7)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) op, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) status);

308

309#ifdef \_\_cplusplus

310}

311#endif

312

316

317#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_BLUETOOTH\_HCI\_DRIVER\_H\_ \*/

[buf.h](bluetooth_2buf_8h.md)

Bluetooth data buffer API.

[device.h](device_8h.md)

[bt\_recv\_prio](group__bt__hci__driver.md#ga19c61df1660d6049ae6b03afe3554fee)

int bt\_recv\_prio(struct net\_buf \*buf)

Receive high priority data from the controller/HCI driver.

[bt\_hci\_evt\_get\_flags](group__bt__hci__driver.md#ga1f1b10f6d84f4a5cf4b895b6685874ef)

static uint8\_t bt\_hci\_evt\_get\_flags(uint8\_t evt)

Get HCI event flags.

**Definition** hci\_driver.h:60

[bt\_hci\_evt\_create](group__bt__hci__driver.md#ga362df79e2f782159f7e85d63817421bb)

struct net\_buf \* bt\_hci\_evt\_create(uint8\_t evt, uint8\_t len)

Allocate an HCI event buffer.

[bt\_read\_static\_addr](group__bt__hci__driver.md#ga502a6580da2e06f24f021c7bc4bff50f)

uint8\_t bt\_read\_static\_addr(struct bt\_hci\_vs\_static\_addr addrs[], uint8\_t size)

Read static addresses from the controller.

[BT\_HCI\_EVT\_FLAG\_RECV](group__bt__hci__driver.md#ga61e4e2d22dec695f53f5aed6ce809859)

#define BT\_HCI\_EVT\_FLAG\_RECV

**Definition** hci\_driver.h:45

[bt\_hci\_driver\_register](group__bt__hci__driver.md#ga642d226772448dccbd14f2c287d687f0)

int bt\_hci\_driver\_register(const struct bt\_hci\_driver \*drv)

Register a new HCI driver to the Bluetooth stack.

[bt\_hci\_cmd\_complete\_create](group__bt__hci__driver.md#ga8ab7dc7d38f3bc7be72e34d7a9f14212)

struct net\_buf \* bt\_hci\_cmd\_complete\_create(uint16\_t op, uint8\_t plen)

Allocate an HCI Command Complete event buffer.

[bt\_hci\_driver\_bus](group__bt__hci__driver.md#gaa24c7d2d9e2c35d6cd9cfcf650fb65ef)

bt\_hci\_driver\_bus

Possible values for the 'bus' member of the bt\_hci\_driver struct.

**Definition** hci\_driver.h:129

[BT\_HCI\_EVT\_FLAG\_RECV\_PRIO](group__bt__hci__driver.md#gaa7a28bc6e6a79128d3a95c3ccd3b1866)

#define BT\_HCI\_EVT\_FLAG\_RECV\_PRIO

**Definition** hci\_driver.h:43

[bt\_hci\_cmd\_status\_create](group__bt__hci__driver.md#gab6b790e6dd0e8251d6cf10b0a7cce5f7)

struct net\_buf \* bt\_hci\_cmd\_status\_create(uint16\_t op, uint8\_t status)

Allocate an HCI Command Status event buffer.

[bt\_recv](group__bt__hci__driver.md#gaca80bc9dacc4fa44416bd545bd185ef7)

int bt\_recv(struct net\_buf \*buf)

Receive data from the controller/HCI driver.

[bt\_hci\_transport\_setup](group__bt__hci__driver.md#gadd813c1343955a7bb95135eb0fbe9cd5)

int bt\_hci\_transport\_setup(const struct device \*dev)

Setup the HCI transport, which usually means to reset the Bluetooth IC.

[bt\_hci\_transport\_teardown](group__bt__hci__driver.md#gae29dbf165252ddf9085c7387706fd09c)

int bt\_hci\_transport\_teardown(const struct device \*dev)

Teardown the HCI transport.

[BT\_QUIRK\_NO\_RESET](group__bt__hci__driver.md#gga8f5a83b514f6d2da7548c38f7c3c166ea18274691e4c0129f945e88304778a241)

@ BT\_QUIRK\_NO\_RESET

**Definition** hci\_driver.h:32

[BT\_QUIRK\_NO\_AUTO\_DLE](group__bt__hci__driver.md#gga8f5a83b514f6d2da7548c38f7c3c166ea7b8e6d2f5604015c92c623193b9fe1e4)

@ BT\_QUIRK\_NO\_AUTO\_DLE

**Definition** hci\_driver.h:37

[BT\_HCI\_DRIVER\_BUS\_PCCARD](group__bt__hci__driver.md#ggaa24c7d2d9e2c35d6cd9cfcf650fb65efa08bc821327d571bf9659eda7e06a5129)

@ BT\_HCI\_DRIVER\_BUS\_PCCARD

**Definition** hci\_driver.h:132

[BT\_HCI\_DRIVER\_BUS\_I2C](group__bt__hci__driver.md#ggaa24c7d2d9e2c35d6cd9cfcf650fb65efa0d8c310b05d2c982e8de720dbdc2d742)

@ BT\_HCI\_DRIVER\_BUS\_I2C

**Definition** hci\_driver.h:138

[BT\_HCI\_DRIVER\_BUS\_UART](group__bt__hci__driver.md#ggaa24c7d2d9e2c35d6cd9cfcf650fb65efa39c5fca0c61c99db6541d01fb55e41f4)

@ BT\_HCI\_DRIVER\_BUS\_UART

**Definition** hci\_driver.h:133

[BT\_HCI\_DRIVER\_BUS\_SPI](group__bt__hci__driver.md#ggaa24c7d2d9e2c35d6cd9cfcf650fb65efa49f2ba9eeaafa266d905a30b2caf015a)

@ BT\_HCI\_DRIVER\_BUS\_SPI

**Definition** hci\_driver.h:137

[BT\_HCI\_DRIVER\_BUS\_RS232](group__bt__hci__driver.md#ggaa24c7d2d9e2c35d6cd9cfcf650fb65efa5790e933f10773e30da6c7b922a443fa)

@ BT\_HCI\_DRIVER\_BUS\_RS232

**Definition** hci\_driver.h:134

[BT\_HCI\_DRIVER\_BUS\_IPM](group__bt__hci__driver.md#ggaa24c7d2d9e2c35d6cd9cfcf650fb65efa8473c5abdf2f5839c9df54fc00ee3800)

@ BT\_HCI\_DRIVER\_BUS\_IPM

**Definition** hci\_driver.h:139

[BT\_HCI\_DRIVER\_BUS\_VIRTUAL](group__bt__hci__driver.md#ggaa24c7d2d9e2c35d6cd9cfcf650fb65efa885401f44dae9e39caf4a4838b547db9)

@ BT\_HCI\_DRIVER\_BUS\_VIRTUAL

**Definition** hci\_driver.h:130

[BT\_HCI\_DRIVER\_BUS\_PCI](group__bt__hci__driver.md#ggaa24c7d2d9e2c35d6cd9cfcf650fb65efab4c130c7862cbbd6be7827b6462dab90)

@ BT\_HCI\_DRIVER\_BUS\_PCI

**Definition** hci\_driver.h:135

[BT\_HCI\_DRIVER\_BUS\_SDIO](group__bt__hci__driver.md#ggaa24c7d2d9e2c35d6cd9cfcf650fb65efab572fbb186634bc08a3bce457cf38c74)

@ BT\_HCI\_DRIVER\_BUS\_SDIO

**Definition** hci\_driver.h:136

[BT\_HCI\_DRIVER\_BUS\_USB](group__bt__hci__driver.md#ggaa24c7d2d9e2c35d6cd9cfcf650fb65efac2b08e3e52f795deabffd3638a421b68)

@ BT\_HCI\_DRIVER\_BUS\_USB

**Definition** hci\_driver.h:131

[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)

#define BIT(n)

Unsigned integer with bit position n set (signed in assembly language).

**Definition** util\_macro.h:44

[BT\_HCI\_EVT\_CMD\_COMPLETE](hci__types_8h.md#a06f6cf60885ac051cdc9b463fc3b7de7)

#define BT\_HCI\_EVT\_CMD\_COMPLETE

**Definition** hci\_types.h:2335

[BT\_HCI\_EVT\_CMD\_STATUS](hci__types_8h.md#a2b35e7484351228243bb3564273c5bff)

#define BT\_HCI\_EVT\_CMD\_STATUS

**Definition** hci\_types.h:2345

[BT\_HCI\_EVT\_DISCONN\_COMPLETE](hci__types_8h.md#a32e5051a114f8987b49c6957c84d60e2)

#define BT\_HCI\_EVT\_DISCONN\_COMPLETE

**Definition** hci\_types.h:2292

[BT\_HCI\_EVT\_NUM\_COMPLETED\_PACKETS](hci__types_8h.md#a883433c60959629a013d34cea21ab88f)

#define BT\_HCI\_EVT\_NUM\_COMPLETED\_PACKETS

**Definition** hci\_types.h:2364

[BT\_HCI\_EVT\_DATA\_BUF\_OVERFLOW](hci__types_8h.md#ae747b016101bc9e9614163288c5c0d15)

#define BT\_HCI\_EVT\_DATA\_BUF\_OVERFLOW

**Definition** hci\_types.h:2403

[hci\_vs.h](hci__vs_8h.md)

[buf.h](net_2buf_8h.md)

Buffer management.

[stdbool.h](stdbool_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[bt\_addr\_t](structbt__addr__t.md)

Bluetooth Device Address.

**Definition** addr.h:40

[bt\_hci\_driver](structbt__hci__driver.md)

Abstraction which represents the HCI transport to the controller.

**Definition** hci\_driver.h:158

[bt\_hci\_driver::quirks](structbt__hci__driver.md#a0dd8d706ee7ded476a90b19a946226b8)

uint32\_t quirks

Specific controller quirks.

**Definition** hci\_driver.h:170

[bt\_hci\_driver::name](structbt__hci__driver.md#a4036d2609565058a46b1a677fc7ec93e)

const char \* name

Name of the driver.

**Definition** hci\_driver.h:160

[bt\_hci\_driver::open](structbt__hci__driver.md#aabacc7c98a08a8a53f6aca436fac87d0)

int(\* open)(void)

Open the HCI transport.

**Definition** hci\_driver.h:185

[bt\_hci\_driver::send](structbt__hci__driver.md#abcfc79474fc44aae260d61ff99fdb666)

int(\* send)(struct net\_buf \*buf)

Send HCI buffer to controller.

**Definition** hci\_driver.h:212

[bt\_hci\_driver::bus](structbt__hci__driver.md#acd9a4d631da22b4638afd4593cff7d0c)

enum bt\_hci\_driver\_bus bus

Bus of the transport (BT\_HCI\_DRIVER\_BUS\_\*).

**Definition** hci\_driver.h:163

[bt\_hci\_driver::close](structbt__hci__driver.md#ae76bda7ebee44966554ba7b58da30e87)

int(\* close)(void)

Close the HCI transport.

**Definition** hci\_driver.h:198

[bt\_hci\_driver::setup](structbt__hci__driver.md#af2dd8b2817aab56738e7f447987efd2b)

int(\* setup)(const struct bt\_hci\_setup\_params \*params)

HCI vendor-specific setup.

**Definition** hci\_driver.h:226

[bt\_hci\_setup\_params](structbt__hci__setup__params.md)

**Definition** hci\_driver.h:143

[bt\_hci\_setup\_params::public\_addr](structbt__hci__setup__params.md#a6aea62826eeab39e6af40f9005548f3f)

bt\_addr\_t public\_addr

The public identity address to give to the controller.

**Definition** hci\_driver.h:148

[bt\_hci\_vs\_static\_addr](structbt__hci__vs__static__addr.md)

**Definition** hci\_vs.h:112

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:387

[net\_buf](structnet__buf.md)

Network buffer representation.

**Definition** buf.h:910

[net\_buf::len](structnet__buf.md#ae75b7ca728fb7440ea483be8bf88bc38)

uint16\_t len

Length of the data behind the data pointer.

**Definition** buf.h:939

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [bluetooth](dir_95992648d5602e5c89adafd44bf19e08.md)
- [hci\_driver.h](hci__driver_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

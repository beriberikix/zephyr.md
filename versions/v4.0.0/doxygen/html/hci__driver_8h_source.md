---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/hci__driver_8h_source.html
original_path: doxygen/html/hci__driver_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
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

22

23#include <[stdbool.h](stdbool_8h.md)>

24#include <[zephyr/net\_buf.h](net__buf_8h.md)>

25#include <[zephyr/bluetooth/buf.h](bluetooth_2buf_8h.md)>

26#include <[zephyr/bluetooth/hci\_vs.h](hci__vs_8h.md)>

27#include <[zephyr/device.h](device_8h.md)>

28

29#ifdef \_\_cplusplus

30extern "C" {

31#endif

32

33enum {

34 /\* The host should never send HCI\_Reset \*/

[ 35](group__bt__hci__driver.md#gga8f5a83b514f6d2da7548c38f7c3c166ea18274691e4c0129f945e88304778a241) [BT\_QUIRK\_NO\_RESET](group__bt__hci__driver.md#gga8f5a83b514f6d2da7548c38f7c3c166ea18274691e4c0129f945e88304778a241) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

36 /\* The controller does not auto-initiate a DLE procedure when the

37 \* initial connection data length parameters are not equal to the

38 \* default data length parameters. Therefore the host should initiate

39 \* the DLE procedure after connection establishment. \*/

[ 40](group__bt__hci__driver.md#gga8f5a83b514f6d2da7548c38f7c3c166ea7b8e6d2f5604015c92c623193b9fe1e4) [BT\_QUIRK\_NO\_AUTO\_DLE](group__bt__hci__driver.md#gga8f5a83b514f6d2da7548c38f7c3c166ea7b8e6d2f5604015c92c623193b9fe1e4) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

41};

42

[ 56](group__bt__hci__driver.md#gaca80bc9dacc4fa44416bd545bd185ef7)\_\_deprecated int [bt\_recv](group__bt__hci__driver.md#gaca80bc9dacc4fa44416bd545bd185ef7)(struct [net\_buf](structnet__buf.md) \*buf);

57

[ 59](group__bt__hci__driver.md#gaa24c7d2d9e2c35d6cd9cfcf650fb65ef)enum [bt\_hci\_driver\_bus](group__bt__hci__driver.md#gaa24c7d2d9e2c35d6cd9cfcf650fb65ef) {

[ 60](group__bt__hci__driver.md#ggaa24c7d2d9e2c35d6cd9cfcf650fb65efa885401f44dae9e39caf4a4838b547db9) [BT\_HCI\_DRIVER\_BUS\_VIRTUAL](group__bt__hci__driver.md#ggaa24c7d2d9e2c35d6cd9cfcf650fb65efa885401f44dae9e39caf4a4838b547db9) = 0,

[ 61](group__bt__hci__driver.md#ggaa24c7d2d9e2c35d6cd9cfcf650fb65efac2b08e3e52f795deabffd3638a421b68) [BT\_HCI\_DRIVER\_BUS\_USB](group__bt__hci__driver.md#ggaa24c7d2d9e2c35d6cd9cfcf650fb65efac2b08e3e52f795deabffd3638a421b68) = 1,

[ 62](group__bt__hci__driver.md#ggaa24c7d2d9e2c35d6cd9cfcf650fb65efa08bc821327d571bf9659eda7e06a5129) [BT\_HCI\_DRIVER\_BUS\_PCCARD](group__bt__hci__driver.md#ggaa24c7d2d9e2c35d6cd9cfcf650fb65efa08bc821327d571bf9659eda7e06a5129) = 2,

[ 63](group__bt__hci__driver.md#ggaa24c7d2d9e2c35d6cd9cfcf650fb65efa39c5fca0c61c99db6541d01fb55e41f4) [BT\_HCI\_DRIVER\_BUS\_UART](group__bt__hci__driver.md#ggaa24c7d2d9e2c35d6cd9cfcf650fb65efa39c5fca0c61c99db6541d01fb55e41f4) = 3,

[ 64](group__bt__hci__driver.md#ggaa24c7d2d9e2c35d6cd9cfcf650fb65efa5790e933f10773e30da6c7b922a443fa) [BT\_HCI\_DRIVER\_BUS\_RS232](group__bt__hci__driver.md#ggaa24c7d2d9e2c35d6cd9cfcf650fb65efa5790e933f10773e30da6c7b922a443fa) = 4,

[ 65](group__bt__hci__driver.md#ggaa24c7d2d9e2c35d6cd9cfcf650fb65efab4c130c7862cbbd6be7827b6462dab90) [BT\_HCI\_DRIVER\_BUS\_PCI](group__bt__hci__driver.md#ggaa24c7d2d9e2c35d6cd9cfcf650fb65efab4c130c7862cbbd6be7827b6462dab90) = 5,

[ 66](group__bt__hci__driver.md#ggaa24c7d2d9e2c35d6cd9cfcf650fb65efab572fbb186634bc08a3bce457cf38c74) [BT\_HCI\_DRIVER\_BUS\_SDIO](group__bt__hci__driver.md#ggaa24c7d2d9e2c35d6cd9cfcf650fb65efab572fbb186634bc08a3bce457cf38c74) = 6,

[ 67](group__bt__hci__driver.md#ggaa24c7d2d9e2c35d6cd9cfcf650fb65efa49f2ba9eeaafa266d905a30b2caf015a) [BT\_HCI\_DRIVER\_BUS\_SPI](group__bt__hci__driver.md#ggaa24c7d2d9e2c35d6cd9cfcf650fb65efa49f2ba9eeaafa266d905a30b2caf015a) = 7,

[ 68](group__bt__hci__driver.md#ggaa24c7d2d9e2c35d6cd9cfcf650fb65efa0d8c310b05d2c982e8de720dbdc2d742) [BT\_HCI\_DRIVER\_BUS\_I2C](group__bt__hci__driver.md#ggaa24c7d2d9e2c35d6cd9cfcf650fb65efa0d8c310b05d2c982e8de720dbdc2d742) = 8,

[ 69](group__bt__hci__driver.md#ggaa24c7d2d9e2c35d6cd9cfcf650fb65efa8473c5abdf2f5839c9df54fc00ee3800) [BT\_HCI\_DRIVER\_BUS\_IPM](group__bt__hci__driver.md#ggaa24c7d2d9e2c35d6cd9cfcf650fb65efa8473c5abdf2f5839c9df54fc00ee3800) = 9,

70};

71

72#if defined(CONFIG\_BT\_HCI\_SETUP) || defined(\_\_DOXYGEN\_\_)

73struct [bt\_hci\_setup\_params](structbt__hci__setup__params.md) {

78 bt\_addr\_t [public\_addr](structbt__hci__setup__params.md#a6aea62826eeab39e6af40f9005548f3f);

79};

80#endif

81

[ 88](structbt__hci__driver.md)struct [bt\_hci\_driver](structbt__hci__driver.md) {

[ 90](structbt__hci__driver.md#a4036d2609565058a46b1a677fc7ec93e) const char \*[name](structbt__hci__driver.md#a4036d2609565058a46b1a677fc7ec93e);

91

[ 93](structbt__hci__driver.md#acd9a4d631da22b4638afd4593cff7d0c) enum [bt\_hci\_driver\_bus](group__bt__hci__driver.md#gaa24c7d2d9e2c35d6cd9cfcf650fb65ef) [bus](structbt__hci__driver.md#acd9a4d631da22b4638afd4593cff7d0c);

94

[ 100](structbt__hci__driver.md#a0dd8d706ee7ded476a90b19a946226b8) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [quirks](structbt__hci__driver.md#a0dd8d706ee7ded476a90b19a946226b8);

101

[ 111](structbt__hci__driver.md#aabacc7c98a08a8a53f6aca436fac87d0) int (\*[open](structbt__hci__driver.md#aabacc7c98a08a8a53f6aca436fac87d0))(void);

112

[ 121](structbt__hci__driver.md#ae76bda7ebee44966554ba7b58da30e87) int (\*[close](structbt__hci__driver.md#ae76bda7ebee44966554ba7b58da30e87))(void);

122

[ 135](structbt__hci__driver.md#abcfc79474fc44aae260d61ff99fdb666) int (\*[send](structbt__hci__driver.md#abcfc79474fc44aae260d61ff99fdb666))(struct [net\_buf](structnet__buf.md) \*buf);

136

137#if defined(CONFIG\_BT\_HCI\_SETUP) || defined(\_\_DOXYGEN\_\_)

[ 149](structbt__hci__driver.md#af2dd8b2817aab56738e7f447987efd2b) int (\*[setup](structbt__hci__driver.md#af2dd8b2817aab56738e7f447987efd2b))(const struct [bt\_hci\_setup\_params](structbt__hci__setup__params.md) \*params);

150#endif /\* defined(CONFIG\_BT\_HCI\_SETUP) || defined(\_\_DOXYGEN\_\_)\*/

151};

152

[ 165](group__bt__hci__driver.md#ga642d226772448dccbd14f2c287d687f0)\_\_deprecated int [bt\_hci\_driver\_register](group__bt__hci__driver.md#ga642d226772448dccbd14f2c287d687f0)(const struct [bt\_hci\_driver](structbt__hci__driver.md) \*drv);

166

[ 178](group__bt__hci__driver.md#gadd813c1343955a7bb95135eb0fbe9cd5)int [bt\_hci\_transport\_setup](group__bt__hci__driver.md#gadd813c1343955a7bb95135eb0fbe9cd5)(const struct [device](structdevice.md) \*dev);

179

[ 191](group__bt__hci__driver.md#gae29dbf165252ddf9085c7387706fd09c)int [bt\_hci\_transport\_teardown](group__bt__hci__driver.md#gae29dbf165252ddf9085c7387706fd09c)(const struct [device](structdevice.md) \*dev);

192

[ 204](group__bt__hci__driver.md#ga362df79e2f782159f7e85d63817421bb)struct [net\_buf](structnet__buf.md) \*[bt\_hci\_evt\_create](group__bt__hci__driver.md#ga362df79e2f782159f7e85d63817421bb)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) evt, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [len](structnet__buf.md#ae75b7ca728fb7440ea483be8bf88bc38));

205

[ 218](group__bt__hci__driver.md#ga8ab7dc7d38f3bc7be72e34d7a9f14212)struct [net\_buf](structnet__buf.md) \*[bt\_hci\_cmd\_complete\_create](group__bt__hci__driver.md#ga8ab7dc7d38f3bc7be72e34d7a9f14212)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) op, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) plen);

219

[ 232](group__bt__hci__driver.md#gab6b790e6dd0e8251d6cf10b0a7cce5f7)struct [net\_buf](structnet__buf.md) \*[bt\_hci\_cmd\_status\_create](group__bt__hci__driver.md#gab6b790e6dd0e8251d6cf10b0a7cce5f7)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) op, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) status);

233

234#ifdef \_\_cplusplus

235}

236#endif

237

241

242#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_BLUETOOTH\_HCI\_DRIVER\_H\_ \*/

[buf.h](bluetooth_2buf_8h.md)

Bluetooth data buffer API.

[device.h](device_8h.md)

[bt\_hci\_evt\_create](group__bt__hci__driver.md#ga362df79e2f782159f7e85d63817421bb)

struct net\_buf \* bt\_hci\_evt\_create(uint8\_t evt, uint8\_t len)

Allocate an HCI event buffer.

[bt\_hci\_driver\_register](group__bt__hci__driver.md#ga642d226772448dccbd14f2c287d687f0)

int bt\_hci\_driver\_register(const struct bt\_hci\_driver \*drv)

Register a new HCI driver to the Bluetooth stack.

[bt\_hci\_cmd\_complete\_create](group__bt__hci__driver.md#ga8ab7dc7d38f3bc7be72e34d7a9f14212)

struct net\_buf \* bt\_hci\_cmd\_complete\_create(uint16\_t op, uint8\_t plen)

Allocate an HCI Command Complete event buffer.

[bt\_hci\_driver\_bus](group__bt__hci__driver.md#gaa24c7d2d9e2c35d6cd9cfcf650fb65ef)

bt\_hci\_driver\_bus

Possible values for the 'bus' member of the bt\_hci\_driver struct.

**Definition** hci\_driver.h:59

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

**Definition** hci\_driver.h:35

[BT\_QUIRK\_NO\_AUTO\_DLE](group__bt__hci__driver.md#gga8f5a83b514f6d2da7548c38f7c3c166ea7b8e6d2f5604015c92c623193b9fe1e4)

@ BT\_QUIRK\_NO\_AUTO\_DLE

**Definition** hci\_driver.h:40

[BT\_HCI\_DRIVER\_BUS\_PCCARD](group__bt__hci__driver.md#ggaa24c7d2d9e2c35d6cd9cfcf650fb65efa08bc821327d571bf9659eda7e06a5129)

@ BT\_HCI\_DRIVER\_BUS\_PCCARD

**Definition** hci\_driver.h:62

[BT\_HCI\_DRIVER\_BUS\_I2C](group__bt__hci__driver.md#ggaa24c7d2d9e2c35d6cd9cfcf650fb65efa0d8c310b05d2c982e8de720dbdc2d742)

@ BT\_HCI\_DRIVER\_BUS\_I2C

**Definition** hci\_driver.h:68

[BT\_HCI\_DRIVER\_BUS\_UART](group__bt__hci__driver.md#ggaa24c7d2d9e2c35d6cd9cfcf650fb65efa39c5fca0c61c99db6541d01fb55e41f4)

@ BT\_HCI\_DRIVER\_BUS\_UART

**Definition** hci\_driver.h:63

[BT\_HCI\_DRIVER\_BUS\_SPI](group__bt__hci__driver.md#ggaa24c7d2d9e2c35d6cd9cfcf650fb65efa49f2ba9eeaafa266d905a30b2caf015a)

@ BT\_HCI\_DRIVER\_BUS\_SPI

**Definition** hci\_driver.h:67

[BT\_HCI\_DRIVER\_BUS\_RS232](group__bt__hci__driver.md#ggaa24c7d2d9e2c35d6cd9cfcf650fb65efa5790e933f10773e30da6c7b922a443fa)

@ BT\_HCI\_DRIVER\_BUS\_RS232

**Definition** hci\_driver.h:64

[BT\_HCI\_DRIVER\_BUS\_IPM](group__bt__hci__driver.md#ggaa24c7d2d9e2c35d6cd9cfcf650fb65efa8473c5abdf2f5839c9df54fc00ee3800)

@ BT\_HCI\_DRIVER\_BUS\_IPM

**Definition** hci\_driver.h:69

[BT\_HCI\_DRIVER\_BUS\_VIRTUAL](group__bt__hci__driver.md#ggaa24c7d2d9e2c35d6cd9cfcf650fb65efa885401f44dae9e39caf4a4838b547db9)

@ BT\_HCI\_DRIVER\_BUS\_VIRTUAL

**Definition** hci\_driver.h:60

[BT\_HCI\_DRIVER\_BUS\_PCI](group__bt__hci__driver.md#ggaa24c7d2d9e2c35d6cd9cfcf650fb65efab4c130c7862cbbd6be7827b6462dab90)

@ BT\_HCI\_DRIVER\_BUS\_PCI

**Definition** hci\_driver.h:65

[BT\_HCI\_DRIVER\_BUS\_SDIO](group__bt__hci__driver.md#ggaa24c7d2d9e2c35d6cd9cfcf650fb65efab572fbb186634bc08a3bce457cf38c74)

@ BT\_HCI\_DRIVER\_BUS\_SDIO

**Definition** hci\_driver.h:66

[BT\_HCI\_DRIVER\_BUS\_USB](group__bt__hci__driver.md#ggaa24c7d2d9e2c35d6cd9cfcf650fb65efac2b08e3e52f795deabffd3638a421b68)

@ BT\_HCI\_DRIVER\_BUS\_USB

**Definition** hci\_driver.h:61

[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)

#define BIT(n)

Unsigned integer with bit position n set (signed in assembly language).

**Definition** util\_macro.h:44

[hci\_vs.h](hci__vs_8h.md)

[net\_buf.h](net__buf_8h.md)

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

[bt\_hci\_driver](structbt__hci__driver.md)

Abstraction which represents the HCI transport to the controller.

**Definition** hci\_driver.h:88

[bt\_hci\_driver::quirks](structbt__hci__driver.md#a0dd8d706ee7ded476a90b19a946226b8)

uint32\_t quirks

Specific controller quirks.

**Definition** hci\_driver.h:100

[bt\_hci\_driver::name](structbt__hci__driver.md#a4036d2609565058a46b1a677fc7ec93e)

const char \* name

Name of the driver.

**Definition** hci\_driver.h:90

[bt\_hci\_driver::open](structbt__hci__driver.md#aabacc7c98a08a8a53f6aca436fac87d0)

int(\* open)(void)

Open the HCI transport.

**Definition** hci\_driver.h:111

[bt\_hci\_driver::send](structbt__hci__driver.md#abcfc79474fc44aae260d61ff99fdb666)

int(\* send)(struct net\_buf \*buf)

Send HCI buffer to controller.

**Definition** hci\_driver.h:135

[bt\_hci\_driver::bus](structbt__hci__driver.md#acd9a4d631da22b4638afd4593cff7d0c)

enum bt\_hci\_driver\_bus bus

Bus of the transport (BT\_HCI\_DRIVER\_BUS\_\*).

**Definition** hci\_driver.h:93

[bt\_hci\_driver::close](structbt__hci__driver.md#ae76bda7ebee44966554ba7b58da30e87)

int(\* close)(void)

Close the HCI transport.

**Definition** hci\_driver.h:121

[bt\_hci\_driver::setup](structbt__hci__driver.md#af2dd8b2817aab56738e7f447987efd2b)

int(\* setup)(const struct bt\_hci\_setup\_params \*params)

HCI vendor-specific setup.

**Definition** hci\_driver.h:149

[bt\_hci\_setup\_params](structbt__hci__setup__params.md)

**Definition** bluetooth.h:34

[bt\_hci\_setup\_params::public\_addr](structbt__hci__setup__params.md#a6aea62826eeab39e6af40f9005548f3f)

bt\_addr\_t public\_addr

The public identity address to give to the controller.

**Definition** bluetooth.h:39

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:412

[net\_buf](structnet__buf.md)

Network buffer representation.

**Definition** net\_buf.h:1006

[net\_buf::len](structnet__buf.md#ae75b7ca728fb7440ea483be8bf88bc38)

uint16\_t len

Length of the data behind the data pointer.

**Definition** net\_buf.h:1035

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [bluetooth](dir_95992648d5602e5c89adafd44bf19e08.md)
- [hci\_driver.h](hci__driver_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

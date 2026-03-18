---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/drivers_2bluetooth_8h_source.html
original_path: doxygen/html/drivers_2bluetooth_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

bluetooth.h

[Go to the documentation of this file.](drivers_2bluetooth_8h.md)

1

8#ifndef ZEPHYR\_INCLUDE\_DRIVERS\_BLUETOOTH\_H\_

9#define ZEPHYR\_INCLUDE\_DRIVERS\_BLUETOOTH\_H\_

10

21

22#include <[stdbool.h](stdbool_8h.md)>

23#include <[stdint.h](stdint_8h.md)>

24#include <[zephyr/net/buf.h](net_2buf_8h.md)>

25#include <[zephyr/bluetooth/buf.h](bluetooth_2buf_8h.md)>

26#include <[zephyr/bluetooth/addr.h](addr_8h.md)>

27#include <[zephyr/bluetooth/hci\_vs.h](hci__vs_8h.md)>

28#include <[zephyr/device.h](device_8h.md)>

29

30#ifdef \_\_cplusplus

31extern "C" {

32#endif

33

[ 34](structbt__hci__setup__params.md)struct [bt\_hci\_setup\_params](structbt__hci__setup__params.md) {

[ 39](structbt__hci__setup__params.md#a6aea62826eeab39e6af40f9005548f3f) [bt\_addr\_t](structbt__addr__t.md) [public\_addr](structbt__hci__setup__params.md#a6aea62826eeab39e6af40f9005548f3f);

40};

41

42enum {

43 /\* The host should never send HCI\_Reset \*/

[ 44](group__bt__hci__api.md#gga687e88a53cddde1d7cbf3057678e66c5ae6ea7b95de2c304ceafbf7a02373a0c1) [BT\_HCI\_QUIRK\_NO\_RESET](group__bt__hci__api.md#gga687e88a53cddde1d7cbf3057678e66c5ae6ea7b95de2c304ceafbf7a02373a0c1) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(0),

45 /\* The controller does not auto-initiate a DLE procedure when the

46 \* initial connection data length parameters are not equal to the

47 \* default data length parameters. Therefore the host should initiate

48 \* the DLE procedure after connection establishment.

49 \*/

[ 50](group__bt__hci__api.md#gga687e88a53cddde1d7cbf3057678e66c5a8ae71e8530f0aedbc107d38ca09b3ff2) [BT\_HCI\_QUIRK\_NO\_AUTO\_DLE](group__bt__hci__api.md#gga687e88a53cddde1d7cbf3057678e66c5a8ae71e8530f0aedbc107d38ca09b3ff2) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

51};

52

[ 54](group__bt__hci__api.md#ga82f70de5f5df8c14fea7440410431a49)enum [bt\_hci\_bus](group__bt__hci__api.md#ga82f70de5f5df8c14fea7440410431a49) {

[ 55](group__bt__hci__api.md#gga82f70de5f5df8c14fea7440410431a49a28b6bd5870a2a955ec17017de22dc2ab) [BT\_HCI\_BUS\_VIRTUAL](group__bt__hci__api.md#gga82f70de5f5df8c14fea7440410431a49a28b6bd5870a2a955ec17017de22dc2ab) = 0,

[ 56](group__bt__hci__api.md#gga82f70de5f5df8c14fea7440410431a49a34115533231b4abe577c75e9e308ef7f) [BT\_HCI\_BUS\_USB](group__bt__hci__api.md#gga82f70de5f5df8c14fea7440410431a49a34115533231b4abe577c75e9e308ef7f) = 1,

[ 57](group__bt__hci__api.md#gga82f70de5f5df8c14fea7440410431a49a67e2e3bbbcbc08ea57819dd8c83bae61) [BT\_HCI\_BUS\_PCCARD](group__bt__hci__api.md#gga82f70de5f5df8c14fea7440410431a49a67e2e3bbbcbc08ea57819dd8c83bae61) = 2,

[ 58](group__bt__hci__api.md#gga82f70de5f5df8c14fea7440410431a49a9318109c873bfc7411ac35c87042c604) [BT\_HCI\_BUS\_UART](group__bt__hci__api.md#gga82f70de5f5df8c14fea7440410431a49a9318109c873bfc7411ac35c87042c604) = 3,

[ 59](group__bt__hci__api.md#gga82f70de5f5df8c14fea7440410431a49accd587417c6e531be0c6f2b3cfe4b4fe) [BT\_HCI\_BUS\_RS232](group__bt__hci__api.md#gga82f70de5f5df8c14fea7440410431a49accd587417c6e531be0c6f2b3cfe4b4fe) = 4,

[ 60](group__bt__hci__api.md#gga82f70de5f5df8c14fea7440410431a49aba69a4fa7ba0d2ce97a193ef80bc7196) [BT\_HCI\_BUS\_PCI](group__bt__hci__api.md#gga82f70de5f5df8c14fea7440410431a49aba69a4fa7ba0d2ce97a193ef80bc7196) = 5,

[ 61](group__bt__hci__api.md#gga82f70de5f5df8c14fea7440410431a49ae0ff096a7460128bc97195faf3fab0c4) [BT\_HCI\_BUS\_SDIO](group__bt__hci__api.md#gga82f70de5f5df8c14fea7440410431a49ae0ff096a7460128bc97195faf3fab0c4) = 6,

[ 62](group__bt__hci__api.md#gga82f70de5f5df8c14fea7440410431a49a8959ae675c1362e10d0125116f691530) [BT\_HCI\_BUS\_SPI](group__bt__hci__api.md#gga82f70de5f5df8c14fea7440410431a49a8959ae675c1362e10d0125116f691530) = 7,

[ 63](group__bt__hci__api.md#gga82f70de5f5df8c14fea7440410431a49aeba46b1b3c164a6ac5b6ca71ba448a98) [BT\_HCI\_BUS\_I2C](group__bt__hci__api.md#gga82f70de5f5df8c14fea7440410431a49aeba46b1b3c164a6ac5b6ca71ba448a98) = 8,

[ 64](group__bt__hci__api.md#gga82f70de5f5df8c14fea7440410431a49a42bdfecd1d9941977338d6b4d8a5a86b) [BT\_HCI\_BUS\_IPM](group__bt__hci__api.md#gga82f70de5f5df8c14fea7440410431a49a42bdfecd1d9941977338d6b4d8a5a86b) = 9,

65};

66

[ 67](group__bt__hci__api.md#ga5e61116282ab2555f1dcd93c2858157e)#define BT\_DT\_HCI\_QUIRK\_OR(node\_id, prop, idx) DT\_STRING\_TOKEN\_BY\_IDX(node\_id, prop, idx)

[ 68](group__bt__hci__api.md#ga73fc76e779a3dd45a680b09063471887)#define BT\_DT\_HCI\_QUIRKS\_GET(node\_id) COND\_CODE\_1(DT\_NODE\_HAS\_PROP(node\_id, bt\_hci\_quirks), \

69 (DT\_FOREACH\_PROP\_ELEM\_SEP(node\_id, \

70 bt\_hci\_quirks, \

71 BT\_DT\_HCI\_QUIRK\_OR, \

72 (|))), \

73 (0))

[ 74](group__bt__hci__api.md#ga9e97337a538670bbc2dde4b35a6c8a25)#define BT\_DT\_HCI\_QUIRKS\_INST\_GET(inst) BT\_DT\_HCI\_QUIRKS\_GET(DT\_DRV\_INST(inst))

75

[ 76](group__bt__hci__api.md#gaf66891071ade556e5906e71f0f0d2678)#define BT\_DT\_HCI\_NAME\_GET(node\_id) DT\_PROP\_OR(node\_id, bt\_hci\_name, "HCI")

[ 77](group__bt__hci__api.md#gae14d26da17a9b761226f9c68537d4161)#define BT\_DT\_HCI\_NAME\_INST\_GET(inst) BT\_DT\_HCI\_NAME\_GET(DT\_DRV\_INST(inst))

78

[ 79](group__bt__hci__api.md#ga766eaafe5d88d9d1efa0b3f09a334fc8)#define BT\_DT\_HCI\_BUS\_GET(node\_id) DT\_STRING\_TOKEN\_OR(node\_id, bt\_hci\_bus, BT\_HCI\_BUS\_VIRTUAL)

[ 80](group__bt__hci__api.md#gafb7922cf9937229bb75ab7b4fd7c37bb)#define BT\_DT\_HCI\_BUS\_INST\_GET(inst) BT\_DT\_HCI\_BUS\_GET(DT\_DRV\_INST(inst))

81

[ 82](group__bt__hci__api.md#ga79b12569871b2b6c8420c245e9505aed)typedef int (\*[bt\_hci\_recv\_t](group__bt__hci__api.md#ga79b12569871b2b6c8420c245e9505aed))(const struct [device](structdevice.md) \*dev, struct [net\_buf](structnet__buf.md) \*buf);

83

[ 84](structbt__hci__driver__api.md)\_\_subsystem struct [bt\_hci\_driver\_api](structbt__hci__driver__api.md) {

[ 85](structbt__hci__driver__api.md#a5e324fbcb48110d45b3dfa3e63c149d9) int (\*[open](structbt__hci__driver__api.md#a5e324fbcb48110d45b3dfa3e63c149d9))(const struct [device](structdevice.md) \*dev, [bt\_hci\_recv\_t](group__bt__hci__api.md#ga79b12569871b2b6c8420c245e9505aed) [recv](group__bsd__sockets.md#gae11da452beee536eac85d5f26e5cdd40));

[ 86](structbt__hci__driver__api.md#a6ce182bca140ff9fb53953afa01acf75) int (\*[close](structbt__hci__driver__api.md#a6ce182bca140ff9fb53953afa01acf75))(const struct [device](structdevice.md) \*dev);

[ 87](structbt__hci__driver__api.md#ae8b1e9370b0f651eeed4b85bfabf13d1) int (\*[send](structbt__hci__driver__api.md#ae8b1e9370b0f651eeed4b85bfabf13d1))(const struct [device](structdevice.md) \*dev, struct [net\_buf](structnet__buf.md) \*buf);

88#if defined(CONFIG\_BT\_HCI\_SETUP)

89 int (\*setup)(const struct [device](structdevice.md) \*dev,

90 const struct [bt\_hci\_setup\_params](structbt__hci__setup__params.md) \*param);

91#endif /\* defined(CONFIG\_BT\_HCI\_SETUP) \*/

92};

93

[ 109](group__bt__hci__api.md#gac744c98801cea5afd13d6774154e71c8)static inline int [bt\_hci\_open](group__bt__hci__api.md#gac744c98801cea5afd13d6774154e71c8)(const struct [device](structdevice.md) \*dev, [bt\_hci\_recv\_t](group__bt__hci__api.md#ga79b12569871b2b6c8420c245e9505aed) [recv](group__bsd__sockets.md#gae11da452beee536eac85d5f26e5cdd40))

110{

111 const struct [bt\_hci\_driver\_api](structbt__hci__driver__api.md) \*api = (const struct [bt\_hci\_driver\_api](structbt__hci__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

112

113 return api->[open](structbt__hci__driver__api.md#a5e324fbcb48110d45b3dfa3e63c149d9)(dev, [recv](group__bsd__sockets.md#gae11da452beee536eac85d5f26e5cdd40));

114}

115

[ 126](group__bt__hci__api.md#gad187f0aff959a4756b281aa33d1b4394)static inline int [bt\_hci\_close](group__bt__hci__api.md#gad187f0aff959a4756b281aa33d1b4394)(const struct [device](structdevice.md) \*dev)

127{

128 const struct [bt\_hci\_driver\_api](structbt__hci__driver__api.md) \*api = (const struct [bt\_hci\_driver\_api](structbt__hci__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

129

130 if (api->[close](structbt__hci__driver__api.md#a6ce182bca140ff9fb53953afa01acf75) == NULL) {

131 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

132 }

133

134 return api->[close](structbt__hci__driver__api.md#a6ce182bca140ff9fb53953afa01acf75)(dev);

135}

136

[ 150](group__bt__hci__api.md#ga64079b6f03479561c1c7d09b3af81ede)static inline int [bt\_hci\_send](group__bt__hci__api.md#ga64079b6f03479561c1c7d09b3af81ede)(const struct [device](structdevice.md) \*dev, struct [net\_buf](structnet__buf.md) \*buf)

151{

152 const struct [bt\_hci\_driver\_api](structbt__hci__driver__api.md) \*api = (const struct [bt\_hci\_driver\_api](structbt__hci__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

153

154 return api->[send](structbt__hci__driver__api.md#ae8b1e9370b0f651eeed4b85bfabf13d1)(dev, buf);

155}

156

157#if defined(CONFIG\_BT\_HCI\_SETUP) || defined(\_\_DOXYGEN\_\_)

[ 170](group__bt__hci__api.md#ga45ce7bf5fe86f5fff3d8838d247b1d47)static inline int [bt\_hci\_setup](group__bt__hci__api.md#ga45ce7bf5fe86f5fff3d8838d247b1d47)(const struct [device](structdevice.md) \*dev, struct [bt\_hci\_setup\_params](structbt__hci__setup__params.md) \*params)

171{

172 const struct [bt\_hci\_driver\_api](structbt__hci__driver__api.md) \*api = (const struct [bt\_hci\_driver\_api](structbt__hci__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

173

174 if (api->setup == NULL) {

175 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

176 }

177

178 return api->setup(dev, params);

179}

180#endif

181

185

186/\* The following functions are not strictly part of the HCI driver API, in that

187 \* they do not take as input a struct device which implements the HCI driver API.

188 \*/

189

[ 201](drivers_2bluetooth_8h.md#add813c1343955a7bb95135eb0fbe9cd5)int [bt\_hci\_transport\_setup](drivers_2bluetooth_8h.md#add813c1343955a7bb95135eb0fbe9cd5)(const struct [device](structdevice.md) \*dev);

202

[ 214](drivers_2bluetooth_8h.md#ae29dbf165252ddf9085c7387706fd09c)int [bt\_hci\_transport\_teardown](drivers_2bluetooth_8h.md#ae29dbf165252ddf9085c7387706fd09c)(const struct [device](structdevice.md) \*dev);

215

[ 227](drivers_2bluetooth_8h.md#a362df79e2f782159f7e85d63817421bb)struct [net\_buf](structnet__buf.md) \*[bt\_hci\_evt\_create](drivers_2bluetooth_8h.md#a362df79e2f782159f7e85d63817421bb)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) evt, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [len](structnet__buf.md#ae75b7ca728fb7440ea483be8bf88bc38));

228

[ 241](drivers_2bluetooth_8h.md#a8ab7dc7d38f3bc7be72e34d7a9f14212)struct [net\_buf](structnet__buf.md) \*[bt\_hci\_cmd\_complete\_create](drivers_2bluetooth_8h.md#a8ab7dc7d38f3bc7be72e34d7a9f14212)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) op, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) plen);

242

[ 255](drivers_2bluetooth_8h.md#ab6b790e6dd0e8251d6cf10b0a7cce5f7)struct [net\_buf](structnet__buf.md) \*[bt\_hci\_cmd\_status\_create](drivers_2bluetooth_8h.md#ab6b790e6dd0e8251d6cf10b0a7cce5f7)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) op, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) status);

256

257#ifdef \_\_cplusplus

258}

259#endif

260

261#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_BLUETOOTH\_H\_ \*/

[addr.h](addr_8h.md)

Bluetooth device address definitions and utilities.

[buf.h](bluetooth_2buf_8h.md)

Bluetooth data buffer API.

[device.h](device_8h.md)

[bt\_hci\_evt\_create](drivers_2bluetooth_8h.md#a362df79e2f782159f7e85d63817421bb)

struct net\_buf \* bt\_hci\_evt\_create(uint8\_t evt, uint8\_t len)

Allocate an HCI event buffer.

[bt\_hci\_cmd\_complete\_create](drivers_2bluetooth_8h.md#a8ab7dc7d38f3bc7be72e34d7a9f14212)

struct net\_buf \* bt\_hci\_cmd\_complete\_create(uint16\_t op, uint8\_t plen)

Allocate an HCI Command Complete event buffer.

[bt\_hci\_cmd\_status\_create](drivers_2bluetooth_8h.md#ab6b790e6dd0e8251d6cf10b0a7cce5f7)

struct net\_buf \* bt\_hci\_cmd\_status\_create(uint16\_t op, uint8\_t status)

Allocate an HCI Command Status event buffer.

[bt\_hci\_transport\_setup](drivers_2bluetooth_8h.md#add813c1343955a7bb95135eb0fbe9cd5)

int bt\_hci\_transport\_setup(const struct device \*dev)

Setup the HCI transport, which usually means to reset the Bluetooth IC.

[bt\_hci\_transport\_teardown](drivers_2bluetooth_8h.md#ae29dbf165252ddf9085c7387706fd09c)

int bt\_hci\_transport\_teardown(const struct device \*dev)

Teardown the HCI transport.

[recv](group__bsd__sockets.md#gae11da452beee536eac85d5f26e5cdd40)

static ssize\_t recv(int sock, void \*buf, size\_t max\_len, int flags)

POSIX wrapper for zsock\_recv.

**Definition** socket.h:922

[bt\_hci\_setup](group__bt__hci__api.md#ga45ce7bf5fe86f5fff3d8838d247b1d47)

static int bt\_hci\_setup(const struct device \*dev, struct bt\_hci\_setup\_params \*params)

HCI vendor-specific setup.

**Definition** bluetooth.h:170

[bt\_hci\_send](group__bt__hci__api.md#ga64079b6f03479561c1c7d09b3af81ede)

static int bt\_hci\_send(const struct device \*dev, struct net\_buf \*buf)

Send HCI buffer to controller.

**Definition** bluetooth.h:150

[bt\_hci\_recv\_t](group__bt__hci__api.md#ga79b12569871b2b6c8420c245e9505aed)

int(\* bt\_hci\_recv\_t)(const struct device \*dev, struct net\_buf \*buf)

**Definition** bluetooth.h:82

[bt\_hci\_bus](group__bt__hci__api.md#ga82f70de5f5df8c14fea7440410431a49)

bt\_hci\_bus

Possible values for the 'bus' member of the bt\_hci\_driver struct.

**Definition** bluetooth.h:54

[bt\_hci\_open](group__bt__hci__api.md#gac744c98801cea5afd13d6774154e71c8)

static int bt\_hci\_open(const struct device \*dev, bt\_hci\_recv\_t recv)

Open the HCI transport.

**Definition** bluetooth.h:109

[bt\_hci\_close](group__bt__hci__api.md#gad187f0aff959a4756b281aa33d1b4394)

static int bt\_hci\_close(const struct device \*dev)

Close the HCI transport.

**Definition** bluetooth.h:126

[BT\_HCI\_QUIRK\_NO\_AUTO\_DLE](group__bt__hci__api.md#gga687e88a53cddde1d7cbf3057678e66c5a8ae71e8530f0aedbc107d38ca09b3ff2)

@ BT\_HCI\_QUIRK\_NO\_AUTO\_DLE

**Definition** bluetooth.h:50

[BT\_HCI\_QUIRK\_NO\_RESET](group__bt__hci__api.md#gga687e88a53cddde1d7cbf3057678e66c5ae6ea7b95de2c304ceafbf7a02373a0c1)

@ BT\_HCI\_QUIRK\_NO\_RESET

**Definition** bluetooth.h:44

[BT\_HCI\_BUS\_VIRTUAL](group__bt__hci__api.md#gga82f70de5f5df8c14fea7440410431a49a28b6bd5870a2a955ec17017de22dc2ab)

@ BT\_HCI\_BUS\_VIRTUAL

**Definition** bluetooth.h:55

[BT\_HCI\_BUS\_USB](group__bt__hci__api.md#gga82f70de5f5df8c14fea7440410431a49a34115533231b4abe577c75e9e308ef7f)

@ BT\_HCI\_BUS\_USB

**Definition** bluetooth.h:56

[BT\_HCI\_BUS\_IPM](group__bt__hci__api.md#gga82f70de5f5df8c14fea7440410431a49a42bdfecd1d9941977338d6b4d8a5a86b)

@ BT\_HCI\_BUS\_IPM

**Definition** bluetooth.h:64

[BT\_HCI\_BUS\_PCCARD](group__bt__hci__api.md#gga82f70de5f5df8c14fea7440410431a49a67e2e3bbbcbc08ea57819dd8c83bae61)

@ BT\_HCI\_BUS\_PCCARD

**Definition** bluetooth.h:57

[BT\_HCI\_BUS\_SPI](group__bt__hci__api.md#gga82f70de5f5df8c14fea7440410431a49a8959ae675c1362e10d0125116f691530)

@ BT\_HCI\_BUS\_SPI

**Definition** bluetooth.h:62

[BT\_HCI\_BUS\_UART](group__bt__hci__api.md#gga82f70de5f5df8c14fea7440410431a49a9318109c873bfc7411ac35c87042c604)

@ BT\_HCI\_BUS\_UART

**Definition** bluetooth.h:58

[BT\_HCI\_BUS\_PCI](group__bt__hci__api.md#gga82f70de5f5df8c14fea7440410431a49aba69a4fa7ba0d2ce97a193ef80bc7196)

@ BT\_HCI\_BUS\_PCI

**Definition** bluetooth.h:60

[BT\_HCI\_BUS\_RS232](group__bt__hci__api.md#gga82f70de5f5df8c14fea7440410431a49accd587417c6e531be0c6f2b3cfe4b4fe)

@ BT\_HCI\_BUS\_RS232

**Definition** bluetooth.h:59

[BT\_HCI\_BUS\_SDIO](group__bt__hci__api.md#gga82f70de5f5df8c14fea7440410431a49ae0ff096a7460128bc97195faf3fab0c4)

@ BT\_HCI\_BUS\_SDIO

**Definition** bluetooth.h:61

[BT\_HCI\_BUS\_I2C](group__bt__hci__api.md#gga82f70de5f5df8c14fea7440410431a49aeba46b1b3c164a6ac5b6ca71ba448a98)

@ BT\_HCI\_BUS\_I2C

**Definition** bluetooth.h:63

[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)

#define BIT(n)

Unsigned integer with bit position n set (signed in assembly language).

**Definition** util\_macro.h:44

[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b)

#define ENOSYS

Function not implemented.

**Definition** errno.h:82

[hci\_vs.h](hci__vs_8h.md)

[buf.h](net_2buf_8h.md)

Buffer management.

[stdbool.h](stdbool_8h.md)

[stdint.h](stdint_8h.md)

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[bt\_addr\_t](structbt__addr__t.md)

Bluetooth Device Address.

**Definition** addr.h:40

[bt\_hci\_driver\_api](structbt__hci__driver__api.md)

**Definition** bluetooth.h:84

[bt\_hci\_driver\_api::open](structbt__hci__driver__api.md#a5e324fbcb48110d45b3dfa3e63c149d9)

int(\* open)(const struct device \*dev, bt\_hci\_recv\_t recv)

**Definition** bluetooth.h:85

[bt\_hci\_driver\_api::close](structbt__hci__driver__api.md#a6ce182bca140ff9fb53953afa01acf75)

int(\* close)(const struct device \*dev)

**Definition** bluetooth.h:86

[bt\_hci\_driver\_api::send](structbt__hci__driver__api.md#ae8b1e9370b0f651eeed4b85bfabf13d1)

int(\* send)(const struct device \*dev, struct net\_buf \*buf)

**Definition** bluetooth.h:87

[bt\_hci\_setup\_params](structbt__hci__setup__params.md)

**Definition** bluetooth.h:34

[bt\_hci\_setup\_params::public\_addr](structbt__hci__setup__params.md#a6aea62826eeab39e6af40f9005548f3f)

bt\_addr\_t public\_addr

The public identity address to give to the controller.

**Definition** bluetooth.h:39

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:403

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:409

[net\_buf](structnet__buf.md)

Network buffer representation.

**Definition** buf.h:1004

[net\_buf::len](structnet__buf.md#ae75b7ca728fb7440ea483be8bf88bc38)

uint16\_t len

Length of the data behind the data pointer.

**Definition** buf.h:1033

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [bluetooth.h](drivers_2bluetooth_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/drivers_2bluetooth_8h_source.html
original_path: doxygen/html/drivers_2bluetooth_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
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

24#include <[zephyr/net\_buf.h](net__buf_8h.md)>

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

49 \*

50 \* That requirement is stated in Core Spec v5.4 Vol 6 Part B. 4.5.10

51 \* Data PDU length management:

52 \*

53 \* > For a new connection:

54 \* > - ... If either value is not 27, then the Controller should

55 \* > initiate the Data Length Update procedure at the earliest

56 \* > practical opportunity.

57 \*/

[ 58](group__bt__hci__api.md#gga687e88a53cddde1d7cbf3057678e66c5a8ae71e8530f0aedbc107d38ca09b3ff2) [BT\_HCI\_QUIRK\_NO\_AUTO\_DLE](group__bt__hci__api.md#gga687e88a53cddde1d7cbf3057678e66c5a8ae71e8530f0aedbc107d38ca09b3ff2) = [BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)(1),

59};

60

[ 62](group__bt__hci__api.md#ga82f70de5f5df8c14fea7440410431a49)enum [bt\_hci\_bus](group__bt__hci__api.md#ga82f70de5f5df8c14fea7440410431a49) {

[ 63](group__bt__hci__api.md#gga82f70de5f5df8c14fea7440410431a49a28b6bd5870a2a955ec17017de22dc2ab) [BT\_HCI\_BUS\_VIRTUAL](group__bt__hci__api.md#gga82f70de5f5df8c14fea7440410431a49a28b6bd5870a2a955ec17017de22dc2ab) = 0,

[ 64](group__bt__hci__api.md#gga82f70de5f5df8c14fea7440410431a49a34115533231b4abe577c75e9e308ef7f) [BT\_HCI\_BUS\_USB](group__bt__hci__api.md#gga82f70de5f5df8c14fea7440410431a49a34115533231b4abe577c75e9e308ef7f) = 1,

[ 65](group__bt__hci__api.md#gga82f70de5f5df8c14fea7440410431a49a67e2e3bbbcbc08ea57819dd8c83bae61) [BT\_HCI\_BUS\_PCCARD](group__bt__hci__api.md#gga82f70de5f5df8c14fea7440410431a49a67e2e3bbbcbc08ea57819dd8c83bae61) = 2,

[ 66](group__bt__hci__api.md#gga82f70de5f5df8c14fea7440410431a49a9318109c873bfc7411ac35c87042c604) [BT\_HCI\_BUS\_UART](group__bt__hci__api.md#gga82f70de5f5df8c14fea7440410431a49a9318109c873bfc7411ac35c87042c604) = 3,

[ 67](group__bt__hci__api.md#gga82f70de5f5df8c14fea7440410431a49accd587417c6e531be0c6f2b3cfe4b4fe) [BT\_HCI\_BUS\_RS232](group__bt__hci__api.md#gga82f70de5f5df8c14fea7440410431a49accd587417c6e531be0c6f2b3cfe4b4fe) = 4,

[ 68](group__bt__hci__api.md#gga82f70de5f5df8c14fea7440410431a49aba69a4fa7ba0d2ce97a193ef80bc7196) [BT\_HCI\_BUS\_PCI](group__bt__hci__api.md#gga82f70de5f5df8c14fea7440410431a49aba69a4fa7ba0d2ce97a193ef80bc7196) = 5,

[ 69](group__bt__hci__api.md#gga82f70de5f5df8c14fea7440410431a49ae0ff096a7460128bc97195faf3fab0c4) [BT\_HCI\_BUS\_SDIO](group__bt__hci__api.md#gga82f70de5f5df8c14fea7440410431a49ae0ff096a7460128bc97195faf3fab0c4) = 6,

[ 70](group__bt__hci__api.md#gga82f70de5f5df8c14fea7440410431a49a8959ae675c1362e10d0125116f691530) [BT\_HCI\_BUS\_SPI](group__bt__hci__api.md#gga82f70de5f5df8c14fea7440410431a49a8959ae675c1362e10d0125116f691530) = 7,

[ 71](group__bt__hci__api.md#gga82f70de5f5df8c14fea7440410431a49aeba46b1b3c164a6ac5b6ca71ba448a98) [BT\_HCI\_BUS\_I2C](group__bt__hci__api.md#gga82f70de5f5df8c14fea7440410431a49aeba46b1b3c164a6ac5b6ca71ba448a98) = 8,

[ 72](group__bt__hci__api.md#gga82f70de5f5df8c14fea7440410431a49af9c2a67a32f9674b8477fda88ae1eeeb) [BT\_HCI\_BUS\_SMD](group__bt__hci__api.md#gga82f70de5f5df8c14fea7440410431a49af9c2a67a32f9674b8477fda88ae1eeeb) = 9,

[ 73](group__bt__hci__api.md#gga82f70de5f5df8c14fea7440410431a49a6e6267d67649996a3887666c06dac257) [BT\_HCI\_BUS\_VIRTIO](group__bt__hci__api.md#gga82f70de5f5df8c14fea7440410431a49a6e6267d67649996a3887666c06dac257) = 10,

[ 74](group__bt__hci__api.md#gga82f70de5f5df8c14fea7440410431a49aa963581272eb97fc5cbb314c820b7b37) [BT\_HCI\_BUS\_IPC](group__bt__hci__api.md#gga82f70de5f5df8c14fea7440410431a49aa963581272eb97fc5cbb314c820b7b37) = 11,

75 /\* IPM is deprecated and simply an alias for IPC \*/

[ 76](group__bt__hci__api.md#gga82f70de5f5df8c14fea7440410431a49a42bdfecd1d9941977338d6b4d8a5a86b) [BT\_HCI\_BUS\_IPM](group__bt__hci__api.md#gga82f70de5f5df8c14fea7440410431a49a42bdfecd1d9941977338d6b4d8a5a86b) = [BT\_HCI\_BUS\_IPC](group__bt__hci__api.md#gga82f70de5f5df8c14fea7440410431a49aa963581272eb97fc5cbb314c820b7b37),

77};

78

[ 79](group__bt__hci__api.md#ga5e61116282ab2555f1dcd93c2858157e)#define BT\_DT\_HCI\_QUIRK\_OR(node\_id, prop, idx) \

80 UTIL\_CAT(BT\_HCI\_QUIRK\_, DT\_STRING\_UPPER\_TOKEN\_BY\_IDX(node\_id, prop, idx))

[ 81](group__bt__hci__api.md#ga73fc76e779a3dd45a680b09063471887)#define BT\_DT\_HCI\_QUIRKS\_GET(node\_id) COND\_CODE\_1(DT\_NODE\_HAS\_PROP(node\_id, bt\_hci\_quirks), \

82 (DT\_FOREACH\_PROP\_ELEM\_SEP(node\_id, \

83 bt\_hci\_quirks, \

84 BT\_DT\_HCI\_QUIRK\_OR, \

85 (|))), \

86 (0))

[ 87](group__bt__hci__api.md#ga9e97337a538670bbc2dde4b35a6c8a25)#define BT\_DT\_HCI\_QUIRKS\_INST\_GET(inst) BT\_DT\_HCI\_QUIRKS\_GET(DT\_DRV\_INST(inst))

88

[ 89](group__bt__hci__api.md#gaf66891071ade556e5906e71f0f0d2678)#define BT\_DT\_HCI\_NAME\_GET(node\_id) DT\_PROP\_OR(node\_id, bt\_hci\_name, "HCI")

[ 90](group__bt__hci__api.md#gae14d26da17a9b761226f9c68537d4161)#define BT\_DT\_HCI\_NAME\_INST\_GET(inst) BT\_DT\_HCI\_NAME\_GET(DT\_DRV\_INST(inst))

91

[ 92](group__bt__hci__api.md#ga766eaafe5d88d9d1efa0b3f09a334fc8)#define BT\_DT\_HCI\_BUS\_GET(node\_id) \

93 UTIL\_CAT(BT\_HCI\_BUS\_, DT\_STRING\_UPPER\_TOKEN\_OR(node\_id, bt\_hci\_bus, VIRTUAL))

[ 94](group__bt__hci__api.md#gafb7922cf9937229bb75ab7b4fd7c37bb)#define BT\_DT\_HCI\_BUS\_INST\_GET(inst) BT\_DT\_HCI\_BUS\_GET(DT\_DRV\_INST(inst))

95

[ 96](group__bt__hci__api.md#ga79b12569871b2b6c8420c245e9505aed)typedef int (\*[bt\_hci\_recv\_t](group__bt__hci__api.md#ga79b12569871b2b6c8420c245e9505aed))(const struct [device](structdevice.md) \*dev, struct [net\_buf](structnet__buf.md) \*buf);

97

[ 98](structbt__hci__driver__api.md)\_\_subsystem struct [bt\_hci\_driver\_api](structbt__hci__driver__api.md) {

[ 99](structbt__hci__driver__api.md#a5e324fbcb48110d45b3dfa3e63c149d9) int (\*[open](structbt__hci__driver__api.md#a5e324fbcb48110d45b3dfa3e63c149d9))(const struct [device](structdevice.md) \*dev, [bt\_hci\_recv\_t](group__bt__hci__api.md#ga79b12569871b2b6c8420c245e9505aed) [recv](group__bsd__sockets.md#gae11da452beee536eac85d5f26e5cdd40));

[ 100](structbt__hci__driver__api.md#a6ce182bca140ff9fb53953afa01acf75) int (\*[close](structbt__hci__driver__api.md#a6ce182bca140ff9fb53953afa01acf75))(const struct [device](structdevice.md) \*dev);

[ 101](structbt__hci__driver__api.md#ae8b1e9370b0f651eeed4b85bfabf13d1) int (\*[send](structbt__hci__driver__api.md#ae8b1e9370b0f651eeed4b85bfabf13d1))(const struct [device](structdevice.md) \*dev, struct [net\_buf](structnet__buf.md) \*buf);

102#if defined(CONFIG\_BT\_HCI\_SETUP)

103 int (\*setup)(const struct [device](structdevice.md) \*dev,

104 const struct [bt\_hci\_setup\_params](structbt__hci__setup__params.md) \*param);

105#endif /\* defined(CONFIG\_BT\_HCI\_SETUP) \*/

106};

107

[ 123](group__bt__hci__api.md#gac744c98801cea5afd13d6774154e71c8)static inline int [bt\_hci\_open](group__bt__hci__api.md#gac744c98801cea5afd13d6774154e71c8)(const struct [device](structdevice.md) \*dev, [bt\_hci\_recv\_t](group__bt__hci__api.md#ga79b12569871b2b6c8420c245e9505aed) [recv](group__bsd__sockets.md#gae11da452beee536eac85d5f26e5cdd40))

124{

125 const struct [bt\_hci\_driver\_api](structbt__hci__driver__api.md) \*api = (const struct [bt\_hci\_driver\_api](structbt__hci__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

126

127 return api->[open](structbt__hci__driver__api.md#a5e324fbcb48110d45b3dfa3e63c149d9)(dev, [recv](group__bsd__sockets.md#gae11da452beee536eac85d5f26e5cdd40));

128}

129

[ 140](group__bt__hci__api.md#gad187f0aff959a4756b281aa33d1b4394)static inline int [bt\_hci\_close](group__bt__hci__api.md#gad187f0aff959a4756b281aa33d1b4394)(const struct [device](structdevice.md) \*dev)

141{

142 const struct [bt\_hci\_driver\_api](structbt__hci__driver__api.md) \*api = (const struct [bt\_hci\_driver\_api](structbt__hci__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

143

144 if (api->[close](structbt__hci__driver__api.md#a6ce182bca140ff9fb53953afa01acf75) == NULL) {

145 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

146 }

147

148 return api->[close](structbt__hci__driver__api.md#a6ce182bca140ff9fb53953afa01acf75)(dev);

149}

150

[ 164](group__bt__hci__api.md#ga64079b6f03479561c1c7d09b3af81ede)static inline int [bt\_hci\_send](group__bt__hci__api.md#ga64079b6f03479561c1c7d09b3af81ede)(const struct [device](structdevice.md) \*dev, struct [net\_buf](structnet__buf.md) \*buf)

165{

166 const struct [bt\_hci\_driver\_api](structbt__hci__driver__api.md) \*api = (const struct [bt\_hci\_driver\_api](structbt__hci__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

167

168 return api->[send](structbt__hci__driver__api.md#ae8b1e9370b0f651eeed4b85bfabf13d1)(dev, buf);

169}

170

171#if defined(CONFIG\_BT\_HCI\_SETUP) || defined(\_\_DOXYGEN\_\_)

[ 184](group__bt__hci__api.md#ga45ce7bf5fe86f5fff3d8838d247b1d47)static inline int [bt\_hci\_setup](group__bt__hci__api.md#ga45ce7bf5fe86f5fff3d8838d247b1d47)(const struct [device](structdevice.md) \*dev, struct [bt\_hci\_setup\_params](structbt__hci__setup__params.md) \*params)

185{

186 const struct [bt\_hci\_driver\_api](structbt__hci__driver__api.md) \*api = (const struct [bt\_hci\_driver\_api](structbt__hci__driver__api.md) \*)dev->[api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d);

187

188 if (api->setup == NULL) {

189 return -[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b);

190 }

191

192 return api->setup(dev, params);

193}

194#endif

195

199

200/\* The following functions are not strictly part of the HCI driver API, in that

201 \* they do not take as input a struct device which implements the HCI driver API.

202 \*/

203

[ 215](drivers_2bluetooth_8h.md#add813c1343955a7bb95135eb0fbe9cd5)int [bt\_hci\_transport\_setup](drivers_2bluetooth_8h.md#add813c1343955a7bb95135eb0fbe9cd5)(const struct [device](structdevice.md) \*dev);

216

[ 228](drivers_2bluetooth_8h.md#ae29dbf165252ddf9085c7387706fd09c)int [bt\_hci\_transport\_teardown](drivers_2bluetooth_8h.md#ae29dbf165252ddf9085c7387706fd09c)(const struct [device](structdevice.md) \*dev);

229

[ 241](drivers_2bluetooth_8h.md#a362df79e2f782159f7e85d63817421bb)struct [net\_buf](structnet__buf.md) \*[bt\_hci\_evt\_create](drivers_2bluetooth_8h.md#a362df79e2f782159f7e85d63817421bb)([uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) evt, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [len](structnet__buf.md#ae75b7ca728fb7440ea483be8bf88bc38));

242

[ 255](drivers_2bluetooth_8h.md#a8ab7dc7d38f3bc7be72e34d7a9f14212)struct [net\_buf](structnet__buf.md) \*[bt\_hci\_cmd\_complete\_create](drivers_2bluetooth_8h.md#a8ab7dc7d38f3bc7be72e34d7a9f14212)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) op, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) plen);

256

[ 269](drivers_2bluetooth_8h.md#ab6b790e6dd0e8251d6cf10b0a7cce5f7)struct [net\_buf](structnet__buf.md) \*[bt\_hci\_cmd\_status\_create](drivers_2bluetooth_8h.md#ab6b790e6dd0e8251d6cf10b0a7cce5f7)([uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) op, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) status);

270

271#ifdef \_\_cplusplus

272}

273#endif

274

275#endif /\* ZEPHYR\_INCLUDE\_DRIVERS\_BLUETOOTH\_H\_ \*/

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

**Definition** socket.h:873

[bt\_hci\_setup](group__bt__hci__api.md#ga45ce7bf5fe86f5fff3d8838d247b1d47)

static int bt\_hci\_setup(const struct device \*dev, struct bt\_hci\_setup\_params \*params)

HCI vendor-specific setup.

**Definition** bluetooth.h:184

[bt\_hci\_send](group__bt__hci__api.md#ga64079b6f03479561c1c7d09b3af81ede)

static int bt\_hci\_send(const struct device \*dev, struct net\_buf \*buf)

Send HCI buffer to controller.

**Definition** bluetooth.h:164

[bt\_hci\_recv\_t](group__bt__hci__api.md#ga79b12569871b2b6c8420c245e9505aed)

int(\* bt\_hci\_recv\_t)(const struct device \*dev, struct net\_buf \*buf)

**Definition** bluetooth.h:96

[bt\_hci\_bus](group__bt__hci__api.md#ga82f70de5f5df8c14fea7440410431a49)

bt\_hci\_bus

Possible values for the 'bus' member of the bt\_hci\_driver struct.

**Definition** bluetooth.h:62

[bt\_hci\_open](group__bt__hci__api.md#gac744c98801cea5afd13d6774154e71c8)

static int bt\_hci\_open(const struct device \*dev, bt\_hci\_recv\_t recv)

Open the HCI transport.

**Definition** bluetooth.h:123

[bt\_hci\_close](group__bt__hci__api.md#gad187f0aff959a4756b281aa33d1b4394)

static int bt\_hci\_close(const struct device \*dev)

Close the HCI transport.

**Definition** bluetooth.h:140

[BT\_HCI\_QUIRK\_NO\_AUTO\_DLE](group__bt__hci__api.md#gga687e88a53cddde1d7cbf3057678e66c5a8ae71e8530f0aedbc107d38ca09b3ff2)

@ BT\_HCI\_QUIRK\_NO\_AUTO\_DLE

**Definition** bluetooth.h:58

[BT\_HCI\_QUIRK\_NO\_RESET](group__bt__hci__api.md#gga687e88a53cddde1d7cbf3057678e66c5ae6ea7b95de2c304ceafbf7a02373a0c1)

@ BT\_HCI\_QUIRK\_NO\_RESET

**Definition** bluetooth.h:44

[BT\_HCI\_BUS\_VIRTUAL](group__bt__hci__api.md#gga82f70de5f5df8c14fea7440410431a49a28b6bd5870a2a955ec17017de22dc2ab)

@ BT\_HCI\_BUS\_VIRTUAL

**Definition** bluetooth.h:63

[BT\_HCI\_BUS\_USB](group__bt__hci__api.md#gga82f70de5f5df8c14fea7440410431a49a34115533231b4abe577c75e9e308ef7f)

@ BT\_HCI\_BUS\_USB

**Definition** bluetooth.h:64

[BT\_HCI\_BUS\_IPM](group__bt__hci__api.md#gga82f70de5f5df8c14fea7440410431a49a42bdfecd1d9941977338d6b4d8a5a86b)

@ BT\_HCI\_BUS\_IPM

**Definition** bluetooth.h:76

[BT\_HCI\_BUS\_PCCARD](group__bt__hci__api.md#gga82f70de5f5df8c14fea7440410431a49a67e2e3bbbcbc08ea57819dd8c83bae61)

@ BT\_HCI\_BUS\_PCCARD

**Definition** bluetooth.h:65

[BT\_HCI\_BUS\_VIRTIO](group__bt__hci__api.md#gga82f70de5f5df8c14fea7440410431a49a6e6267d67649996a3887666c06dac257)

@ BT\_HCI\_BUS\_VIRTIO

**Definition** bluetooth.h:73

[BT\_HCI\_BUS\_SPI](group__bt__hci__api.md#gga82f70de5f5df8c14fea7440410431a49a8959ae675c1362e10d0125116f691530)

@ BT\_HCI\_BUS\_SPI

**Definition** bluetooth.h:70

[BT\_HCI\_BUS\_UART](group__bt__hci__api.md#gga82f70de5f5df8c14fea7440410431a49a9318109c873bfc7411ac35c87042c604)

@ BT\_HCI\_BUS\_UART

**Definition** bluetooth.h:66

[BT\_HCI\_BUS\_IPC](group__bt__hci__api.md#gga82f70de5f5df8c14fea7440410431a49aa963581272eb97fc5cbb314c820b7b37)

@ BT\_HCI\_BUS\_IPC

**Definition** bluetooth.h:74

[BT\_HCI\_BUS\_PCI](group__bt__hci__api.md#gga82f70de5f5df8c14fea7440410431a49aba69a4fa7ba0d2ce97a193ef80bc7196)

@ BT\_HCI\_BUS\_PCI

**Definition** bluetooth.h:68

[BT\_HCI\_BUS\_RS232](group__bt__hci__api.md#gga82f70de5f5df8c14fea7440410431a49accd587417c6e531be0c6f2b3cfe4b4fe)

@ BT\_HCI\_BUS\_RS232

**Definition** bluetooth.h:67

[BT\_HCI\_BUS\_SDIO](group__bt__hci__api.md#gga82f70de5f5df8c14fea7440410431a49ae0ff096a7460128bc97195faf3fab0c4)

@ BT\_HCI\_BUS\_SDIO

**Definition** bluetooth.h:69

[BT\_HCI\_BUS\_I2C](group__bt__hci__api.md#gga82f70de5f5df8c14fea7440410431a49aeba46b1b3c164a6ac5b6ca71ba448a98)

@ BT\_HCI\_BUS\_I2C

**Definition** bluetooth.h:71

[BT\_HCI\_BUS\_SMD](group__bt__hci__api.md#gga82f70de5f5df8c14fea7440410431a49af9c2a67a32f9674b8477fda88ae1eeeb)

@ BT\_HCI\_BUS\_SMD

**Definition** bluetooth.h:72

[BIT](group__sys-util.md#ga3a8ea58898cb58fc96013383d39f482c)

#define BIT(n)

Unsigned integer with bit position n set (signed in assembly language).

**Definition** util\_macro.h:44

[ENOSYS](group__system__errno.md#ga43785b9969e0bd1af532dbde06c5540b)

#define ENOSYS

Function not implemented.

**Definition** errno.h:82

[hci\_vs.h](hci__vs_8h.md)

[net\_buf.h](net__buf_8h.md)

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

**Definition** bluetooth.h:98

[bt\_hci\_driver\_api::open](structbt__hci__driver__api.md#a5e324fbcb48110d45b3dfa3e63c149d9)

int(\* open)(const struct device \*dev, bt\_hci\_recv\_t recv)

**Definition** bluetooth.h:99

[bt\_hci\_driver\_api::close](structbt__hci__driver__api.md#a6ce182bca140ff9fb53953afa01acf75)

int(\* close)(const struct device \*dev)

**Definition** bluetooth.h:100

[bt\_hci\_driver\_api::send](structbt__hci__driver__api.md#ae8b1e9370b0f651eeed4b85bfabf13d1)

int(\* send)(const struct device \*dev, struct net\_buf \*buf)

**Definition** bluetooth.h:101

[bt\_hci\_setup\_params](structbt__hci__setup__params.md)

**Definition** bluetooth.h:34

[bt\_hci\_setup\_params::public\_addr](structbt__hci__setup__params.md#a6aea62826eeab39e6af40f9005548f3f)

bt\_addr\_t public\_addr

The public identity address to give to the controller.

**Definition** bluetooth.h:39

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:412

[device::api](structdevice.md#a4a2e6a2cfeb6efed7d5383c33458f46d)

const void \* api

Address of the API structure exposed by the device instance.

**Definition** device.h:418

[net\_buf](structnet__buf.md)

Network buffer representation.

**Definition** net\_buf.h:1006

[net\_buf::len](structnet__buf.md#ae75b7ca728fb7440ea483be8bf88bc38)

uint16\_t len

Length of the data behind the data pointer.

**Definition** net\_buf.h:1035

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [bluetooth.h](drivers_2bluetooth_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

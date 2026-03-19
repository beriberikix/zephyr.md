---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/doxygen/html/cmux_8h_source.html
original_path: doxygen/html/cmux_8h_source.html
---

| Logo | Zephyr API Documentation 4.0.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

cmux.h

[Go to the documentation of this file.](cmux_8h.md)

1/\*

2 \* Copyright (c) 2022 Trackunit Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7/\*

8 \* This library uses CMUX to create multiple data channels, called DLCIs, on a single serial bus.

9 \* Each DLCI has an address from 1 to 63. DLCI address 0 is reserved for control commands.

10 \*

11 \* Design overview:

12 \*

13 \* DLCI1 <-----------+ +-------> DLCI1

14 \* v v

15 \* DLCI2 <---> CMUX instance <--> Serial bus <--> Client <--> DLCI2

16 \* ^ ^

17 \* DLCI3 <-----------+ +-------> DLCI3

18 \*

19 \* Writing to and from the CMUX instances is done using the modem\_pipe API.

20 \*/

21

22#include <[zephyr/kernel.h](kernel_8h.md)>

23#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

24#include <[zephyr/sys/ring\_buffer.h](ring__buffer_8h.md)>

25#include <[zephyr/sys/atomic.h](sys_2atomic_8h.md)>

26

27#include <[zephyr/modem/pipe.h](pipe_8h.md)>

28#include <[zephyr/modem/stats.h](modem_2stats_8h.md)>

29

30#ifndef ZEPHYR\_MODEM\_CMUX\_

31#define ZEPHYR\_MODEM\_CMUX\_

32

33#ifdef \_\_cplusplus

34extern "C" {

35#endif

36

43

44struct modem\_cmux;

45

[ 46](group__modem__cmux.md#gab60ea756d37bd9ed59f07c6380952d36)enum [modem\_cmux\_event](group__modem__cmux.md#gab60ea756d37bd9ed59f07c6380952d36) {

[ 47](group__modem__cmux.md#ggab60ea756d37bd9ed59f07c6380952d36a8d37518bf5ba31237e59a413f36be4b2) [MODEM\_CMUX\_EVENT\_CONNECTED](group__modem__cmux.md#ggab60ea756d37bd9ed59f07c6380952d36a8d37518bf5ba31237e59a413f36be4b2) = 0,

[ 48](group__modem__cmux.md#ggab60ea756d37bd9ed59f07c6380952d36a095af6ed667b014e4beb4c13c34c8a21) [MODEM\_CMUX\_EVENT\_DISCONNECTED](group__modem__cmux.md#ggab60ea756d37bd9ed59f07c6380952d36a095af6ed667b014e4beb4c13c34c8a21),

49};

50

[ 51](group__modem__cmux.md#ga998b334620c9970ebbb0bcf620ea5923)typedef void (\*[modem\_cmux\_callback](group__modem__cmux.md#ga998b334620c9970ebbb0bcf620ea5923))(struct modem\_cmux \*cmux, enum [modem\_cmux\_event](group__modem__cmux.md#gab60ea756d37bd9ed59f07c6380952d36) event,

52 void \*user\_data);

53

57

58enum modem\_cmux\_state {

59 MODEM\_CMUX\_STATE\_DISCONNECTED = 0,

60 MODEM\_CMUX\_STATE\_CONNECTING,

61 MODEM\_CMUX\_STATE\_CONNECTED,

62 MODEM\_CMUX\_STATE\_DISCONNECTING,

63};

64

65enum modem\_cmux\_receive\_state {

66 MODEM\_CMUX\_RECEIVE\_STATE\_SOF = 0,

67 MODEM\_CMUX\_RECEIVE\_STATE\_RESYNC,

68 MODEM\_CMUX\_RECEIVE\_STATE\_ADDRESS,

69 MODEM\_CMUX\_RECEIVE\_STATE\_ADDRESS\_CONT,

70 MODEM\_CMUX\_RECEIVE\_STATE\_CONTROL,

71 MODEM\_CMUX\_RECEIVE\_STATE\_LENGTH,

72 MODEM\_CMUX\_RECEIVE\_STATE\_LENGTH\_CONT,

73 MODEM\_CMUX\_RECEIVE\_STATE\_DATA,

74 MODEM\_CMUX\_RECEIVE\_STATE\_FCS,

75 MODEM\_CMUX\_RECEIVE\_STATE\_DROP,

76 MODEM\_CMUX\_RECEIVE\_STATE\_EOF,

77};

78

79enum modem\_cmux\_dlci\_state {

80 MODEM\_CMUX\_DLCI\_STATE\_CLOSED,

81 MODEM\_CMUX\_DLCI\_STATE\_OPENING,

82 MODEM\_CMUX\_DLCI\_STATE\_OPEN,

83 MODEM\_CMUX\_DLCI\_STATE\_CLOSING,

84};

85

86struct modem\_cmux\_dlci {

87 [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) node;

88

89 /\* Pipe \*/

90 struct modem\_pipe pipe;

91

92 /\* Context \*/

93 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) dlci\_address;

94 struct modem\_cmux \*cmux;

95

96 /\* Receive buffer \*/

97 struct ring\_buf receive\_rb;

98 struct k\_mutex receive\_rb\_lock;

99

100 /\* Work \*/

101 struct k\_work\_delayable open\_work;

102 struct k\_work\_delayable close\_work;

103

104 /\* State \*/

105 enum modem\_cmux\_dlci\_state [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90);

106

107 /\* Statistics \*/

108#if CONFIG\_MODEM\_STATS

109 struct modem\_stats\_buffer receive\_buf\_stats;

110#endif

111};

112

113struct modem\_cmux\_frame {

114 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) dlci\_address;

115 bool cr;

116 bool pf;

117 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) type;

118 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data;

119 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) data\_len;

120};

121

122struct modem\_cmux\_work {

123 struct k\_work\_delayable dwork;

124 struct modem\_cmux \*cmux;

125};

126

127struct modem\_cmux {

128 /\* Bus pipe \*/

129 struct modem\_pipe \*pipe;

130

131 /\* Event handler \*/

132 [modem\_cmux\_callback](group__modem__cmux.md#ga998b334620c9970ebbb0bcf620ea5923) callback;

133 void \*user\_data;

134

135 /\* DLCI channel contexts \*/

136 [sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) dlcis;

137

138 /\* State \*/

139 enum modem\_cmux\_state [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90);

140 bool flow\_control\_on;

141

142 /\* Work lock \*/

143 bool attached;

144 struct k\_spinlock work\_lock;

145

146 /\* Receive state\*/

147 enum modem\_cmux\_receive\_state receive\_state;

148

149 /\* Receive buffer \*/

150 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*receive\_buf;

151 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) receive\_buf\_size;

152 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) receive\_buf\_len;

153

154 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) work\_buf[CONFIG\_MODEM\_CMUX\_WORK\_BUFFER\_SIZE];

155

156 /\* Transmit buffer \*/

157 struct ring\_buf transmit\_rb;

158 struct k\_mutex transmit\_rb\_lock;

159

160 /\* Received frame \*/

161 struct modem\_cmux\_frame frame;

162 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) frame\_header[5];

163 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) frame\_header\_len;

164

165 /\* Work \*/

166 struct k\_work\_delayable receive\_work;

167 struct k\_work\_delayable transmit\_work;

168 struct k\_work\_delayable connect\_work;

169 struct k\_work\_delayable disconnect\_work;

170

171 /\* Synchronize actions \*/

172 struct k\_event event;

173

174 /\* Statistics \*/

175#if CONFIG\_MODEM\_STATS

176 struct modem\_stats\_buffer receive\_buf\_stats;

177 struct modem\_stats\_buffer transmit\_buf\_stats;

178#endif

179};

180

184

[ 188](structmodem__cmux__config.md)struct [modem\_cmux\_config](structmodem__cmux__config.md) {

[ 190](structmodem__cmux__config.md#a2cba948c704f02429022d360326b9838) [modem\_cmux\_callback](group__modem__cmux.md#ga998b334620c9970ebbb0bcf620ea5923) [callback](structmodem__cmux__config.md#a2cba948c704f02429022d360326b9838);

[ 192](structmodem__cmux__config.md#a6714790f733ba7e4431353b6cdbbe3ee) void \*[user\_data](structmodem__cmux__config.md#a6714790f733ba7e4431353b6cdbbe3ee);

[ 194](structmodem__cmux__config.md#a2935694a75a95da8571b1c520a9800c8) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[receive\_buf](structmodem__cmux__config.md#a2935694a75a95da8571b1c520a9800c8);

[ 196](structmodem__cmux__config.md#a2fcf4ba7f088701ec6c5b750c8af3a89) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [receive\_buf\_size](structmodem__cmux__config.md#a2fcf4ba7f088701ec6c5b750c8af3a89);

[ 198](structmodem__cmux__config.md#a6920bf8f7c52522e8b76ba09051887c5) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[transmit\_buf](structmodem__cmux__config.md#a6920bf8f7c52522e8b76ba09051887c5);

[ 200](structmodem__cmux__config.md#ae028b4dde63311a810c67686dc662154) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [transmit\_buf\_size](structmodem__cmux__config.md#ae028b4dde63311a810c67686dc662154);

201};

202

[ 208](group__modem__cmux.md#gad72973ad82504ae64d184ce11572ab88)void [modem\_cmux\_init](group__modem__cmux.md#gad72973ad82504ae64d184ce11572ab88)(struct modem\_cmux \*cmux, const struct [modem\_cmux\_config](structmodem__cmux__config.md) \*config);

209

[ 213](structmodem__cmux__dlci__config.md)struct [modem\_cmux\_dlci\_config](structmodem__cmux__dlci__config.md) {

[ 215](structmodem__cmux__dlci__config.md#ad0b1fe93bbee6343c8446da5a0ad88c9) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [dlci\_address](structmodem__cmux__dlci__config.md#ad0b1fe93bbee6343c8446da5a0ad88c9);

[ 217](structmodem__cmux__dlci__config.md#ad3d6c1e0adce243aa536e52e5e4c4374) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[receive\_buf](structmodem__cmux__dlci__config.md#ad3d6c1e0adce243aa536e52e5e4c4374);

[ 219](structmodem__cmux__dlci__config.md#af7715440c78d87466f91464000db1fef) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [receive\_buf\_size](structmodem__cmux__dlci__config.md#af7715440c78d87466f91464000db1fef);

220};

221

[ 229](group__modem__cmux.md#gabfd8e728eb8940b4093ae132b7add7d7)struct modem\_pipe \*[modem\_cmux\_dlci\_init](group__modem__cmux.md#gabfd8e728eb8940b4093ae132b7add7d7)(struct modem\_cmux \*cmux, struct modem\_cmux\_dlci \*dlci,

230 const struct [modem\_cmux\_dlci\_config](structmodem__cmux__dlci__config.md) \*config);

231

[ 238](group__modem__cmux.md#gab85f5c71a3cf131ff97aa47749197cb3)int [modem\_cmux\_attach](group__modem__cmux.md#gab85f5c71a3cf131ff97aa47749197cb3)(struct modem\_cmux \*cmux, struct modem\_pipe \*pipe);

239

[ 250](group__modem__cmux.md#ga362cd4b2dff122e3bbaee02b378dd226)int [modem\_cmux\_connect](group__modem__cmux.md#ga362cd4b2dff122e3bbaee02b378dd226)(struct modem\_cmux \*cmux);

251

[ 262](group__modem__cmux.md#ga9fa4a1cd9cf1e1c253e621c650a611d0)int [modem\_cmux\_connect\_async](group__modem__cmux.md#ga9fa4a1cd9cf1e1c253e621c650a611d0)(struct modem\_cmux \*cmux);

263

[ 274](group__modem__cmux.md#ga482171f67db206780d0b8a2cf5b32a93)int [modem\_cmux\_disconnect](group__modem__cmux.md#ga482171f67db206780d0b8a2cf5b32a93)(struct modem\_cmux \*cmux);

275

[ 286](group__modem__cmux.md#ga988c8efbebf63871730918d862b7c490)int [modem\_cmux\_disconnect\_async](group__modem__cmux.md#ga988c8efbebf63871730918d862b7c490)(struct modem\_cmux \*cmux);

287

[ 298](group__modem__cmux.md#gadc7c6ff92b7ac52717151bd6bf1efdff)void [modem\_cmux\_release](group__modem__cmux.md#gadc7c6ff92b7ac52717151bd6bf1efdff)(struct modem\_cmux \*cmux);

299

303

304#ifdef \_\_cplusplus

305}

306#endif

307

308#endif /\* ZEPHYR\_MODEM\_CMUX\_ \*/

[modem\_cmux\_connect](group__modem__cmux.md#ga362cd4b2dff122e3bbaee02b378dd226)

int modem\_cmux\_connect(struct modem\_cmux \*cmux)

Connect CMUX instance.

[modem\_cmux\_disconnect](group__modem__cmux.md#ga482171f67db206780d0b8a2cf5b32a93)

int modem\_cmux\_disconnect(struct modem\_cmux \*cmux)

Close down and disconnect CMUX instance.

[modem\_cmux\_disconnect\_async](group__modem__cmux.md#ga988c8efbebf63871730918d862b7c490)

int modem\_cmux\_disconnect\_async(struct modem\_cmux \*cmux)

Close down and disconnect CMUX instance asynchronously.

[modem\_cmux\_callback](group__modem__cmux.md#ga998b334620c9970ebbb0bcf620ea5923)

void(\* modem\_cmux\_callback)(struct modem\_cmux \*cmux, enum modem\_cmux\_event event, void \*user\_data)

**Definition** cmux.h:51

[modem\_cmux\_connect\_async](group__modem__cmux.md#ga9fa4a1cd9cf1e1c253e621c650a611d0)

int modem\_cmux\_connect\_async(struct modem\_cmux \*cmux)

Connect CMUX instance asynchronously.

[modem\_cmux\_event](group__modem__cmux.md#gab60ea756d37bd9ed59f07c6380952d36)

modem\_cmux\_event

**Definition** cmux.h:46

[modem\_cmux\_attach](group__modem__cmux.md#gab85f5c71a3cf131ff97aa47749197cb3)

int modem\_cmux\_attach(struct modem\_cmux \*cmux, struct modem\_pipe \*pipe)

Attach CMUX instance to pipe.

[modem\_cmux\_dlci\_init](group__modem__cmux.md#gabfd8e728eb8940b4093ae132b7add7d7)

struct modem\_pipe \* modem\_cmux\_dlci\_init(struct modem\_cmux \*cmux, struct modem\_cmux\_dlci \*dlci, const struct modem\_cmux\_dlci\_config \*config)

Initialize DLCI instance and register it with CMUX instance.

[modem\_cmux\_init](group__modem__cmux.md#gad72973ad82504ae64d184ce11572ab88)

void modem\_cmux\_init(struct modem\_cmux \*cmux, const struct modem\_cmux\_config \*config)

Initialize CMUX instance.

[modem\_cmux\_release](group__modem__cmux.md#gadc7c6ff92b7ac52717151bd6bf1efdff)

void modem\_cmux\_release(struct modem\_cmux \*cmux)

Release CMUX instance from pipe.

[MODEM\_CMUX\_EVENT\_DISCONNECTED](group__modem__cmux.md#ggab60ea756d37bd9ed59f07c6380952d36a095af6ed667b014e4beb4c13c34c8a21)

@ MODEM\_CMUX\_EVENT\_DISCONNECTED

**Definition** cmux.h:48

[MODEM\_CMUX\_EVENT\_CONNECTED](group__modem__cmux.md#ggab60ea756d37bd9ed59f07c6380952d36a8d37518bf5ba31237e59a413f36be4b2)

@ MODEM\_CMUX\_EVENT\_CONNECTED

**Definition** cmux.h:47

[sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8)

struct \_slist sys\_slist\_t

Single-linked list structure.

**Definition** slist.h:49

[sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493)

struct \_snode sys\_snode\_t

Single-linked list node structure.

**Definition** slist.h:39

[types.h](include_2zephyr_2types_8h.md)

[kernel.h](kernel_8h.md)

Public kernel APIs.

[stats.h](modem_2stats_8h.md)

[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)

state

**Definition** parser\_state.h:29

[pipe.h](pipe_8h.md)

[ring\_buffer.h](ring__buffer_8h.md)

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[modem\_cmux\_config](structmodem__cmux__config.md)

Contains CMUX instance configuration data.

**Definition** cmux.h:188

[modem\_cmux\_config::receive\_buf](structmodem__cmux__config.md#a2935694a75a95da8571b1c520a9800c8)

uint8\_t \* receive\_buf

Receive buffer.

**Definition** cmux.h:194

[modem\_cmux\_config::callback](structmodem__cmux__config.md#a2cba948c704f02429022d360326b9838)

modem\_cmux\_callback callback

Invoked when event occurs.

**Definition** cmux.h:190

[modem\_cmux\_config::receive\_buf\_size](structmodem__cmux__config.md#a2fcf4ba7f088701ec6c5b750c8af3a89)

uint16\_t receive\_buf\_size

Size of receive buffer in bytes [127, ...].

**Definition** cmux.h:196

[modem\_cmux\_config::user\_data](structmodem__cmux__config.md#a6714790f733ba7e4431353b6cdbbe3ee)

void \* user\_data

Free to use pointer passed to event handler when invoked.

**Definition** cmux.h:192

[modem\_cmux\_config::transmit\_buf](structmodem__cmux__config.md#a6920bf8f7c52522e8b76ba09051887c5)

uint8\_t \* transmit\_buf

Transmit buffer.

**Definition** cmux.h:198

[modem\_cmux\_config::transmit\_buf\_size](structmodem__cmux__config.md#ae028b4dde63311a810c67686dc662154)

uint16\_t transmit\_buf\_size

Size of transmit buffer in bytes [149, ...].

**Definition** cmux.h:200

[modem\_cmux\_dlci\_config](structmodem__cmux__dlci__config.md)

CMUX DLCI configuration.

**Definition** cmux.h:213

[modem\_cmux\_dlci\_config::dlci\_address](structmodem__cmux__dlci__config.md#ad0b1fe93bbee6343c8446da5a0ad88c9)

uint8\_t dlci\_address

DLCI channel address.

**Definition** cmux.h:215

[modem\_cmux\_dlci\_config::receive\_buf](structmodem__cmux__dlci__config.md#ad3d6c1e0adce243aa536e52e5e4c4374)

uint8\_t \* receive\_buf

Receive buffer used by pipe.

**Definition** cmux.h:217

[modem\_cmux\_dlci\_config::receive\_buf\_size](structmodem__cmux__dlci__config.md#af7715440c78d87466f91464000db1fef)

uint16\_t receive\_buf\_size

Size of receive buffer used by pipe [127, ...].

**Definition** cmux.h:219

[atomic.h](sys_2atomic_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [modem](dir_a816d481c0f951d2967bb275acf5f3dd.md)
- [cmux.h](cmux_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

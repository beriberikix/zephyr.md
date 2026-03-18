---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/cmux_8h_source.html
original_path: doxygen/html/cmux_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
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

22#include <[zephyr/kernel.h](include_2zephyr_2kernel_8h.md)>

23#include <[zephyr/types.h](include_2zephyr_2types_8h.md)>

24#include <[zephyr/sys/ring\_buffer.h](ring__buffer_8h.md)>

25#include <[zephyr/sys/atomic.h](atomic_8h.md)>

26

27#include <[zephyr/modem/pipe.h](pipe_8h.md)>

28

29#ifndef ZEPHYR\_MODEM\_CMUX\_

30#define ZEPHYR\_MODEM\_CMUX\_

31

32#ifdef \_\_cplusplus

33extern "C" {

34#endif

35

42

43struct modem\_cmux;

44

[ 45](group__modem__cmux.md#gab60ea756d37bd9ed59f07c6380952d36)enum [modem\_cmux\_event](group__modem__cmux.md#gab60ea756d37bd9ed59f07c6380952d36) {

[ 46](group__modem__cmux.md#ggab60ea756d37bd9ed59f07c6380952d36a8d37518bf5ba31237e59a413f36be4b2) [MODEM\_CMUX\_EVENT\_CONNECTED](group__modem__cmux.md#ggab60ea756d37bd9ed59f07c6380952d36a8d37518bf5ba31237e59a413f36be4b2) = 0,

[ 47](group__modem__cmux.md#ggab60ea756d37bd9ed59f07c6380952d36a095af6ed667b014e4beb4c13c34c8a21) [MODEM\_CMUX\_EVENT\_DISCONNECTED](group__modem__cmux.md#ggab60ea756d37bd9ed59f07c6380952d36a095af6ed667b014e4beb4c13c34c8a21),

48};

49

[ 50](group__modem__cmux.md#ga998b334620c9970ebbb0bcf620ea5923)typedef void (\*[modem\_cmux\_callback](group__modem__cmux.md#ga998b334620c9970ebbb0bcf620ea5923))(struct modem\_cmux \*cmux, enum [modem\_cmux\_event](group__modem__cmux.md#gab60ea756d37bd9ed59f07c6380952d36) event,

51 void \*user\_data);

52

56

57enum modem\_cmux\_state {

58 MODEM\_CMUX\_STATE\_DISCONNECTED = 0,

59 MODEM\_CMUX\_STATE\_CONNECTING,

60 MODEM\_CMUX\_STATE\_CONNECTED,

61 MODEM\_CMUX\_STATE\_DISCONNECTING,

62};

63

64enum modem\_cmux\_receive\_state {

65 MODEM\_CMUX\_RECEIVE\_STATE\_SOF = 0,

66 MODEM\_CMUX\_RECEIVE\_STATE\_RESYNC,

67 MODEM\_CMUX\_RECEIVE\_STATE\_ADDRESS,

68 MODEM\_CMUX\_RECEIVE\_STATE\_ADDRESS\_CONT,

69 MODEM\_CMUX\_RECEIVE\_STATE\_CONTROL,

70 MODEM\_CMUX\_RECEIVE\_STATE\_LENGTH,

71 MODEM\_CMUX\_RECEIVE\_STATE\_LENGTH\_CONT,

72 MODEM\_CMUX\_RECEIVE\_STATE\_DATA,

73 MODEM\_CMUX\_RECEIVE\_STATE\_FCS,

74 MODEM\_CMUX\_RECEIVE\_STATE\_DROP,

75 MODEM\_CMUX\_RECEIVE\_STATE\_EOF,

76};

77

78enum modem\_cmux\_dlci\_state {

79 MODEM\_CMUX\_DLCI\_STATE\_CLOSED,

80 MODEM\_CMUX\_DLCI\_STATE\_OPENING,

81 MODEM\_CMUX\_DLCI\_STATE\_OPEN,

82 MODEM\_CMUX\_DLCI\_STATE\_CLOSING,

83};

84

85struct modem\_cmux\_dlci {

86 [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) node;

87

88 /\* Pipe \*/

89 struct modem\_pipe pipe;

90

91 /\* Context \*/

92 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) dlci\_address;

93 struct modem\_cmux \*cmux;

94

95 /\* Receive buffer \*/

96 struct ring\_buf receive\_rb;

97 struct k\_mutex receive\_rb\_lock;

98

99 /\* Work \*/

100 struct k\_work\_delayable open\_work;

101 struct k\_work\_delayable close\_work;

102

103 /\* State \*/

104 enum modem\_cmux\_dlci\_state [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90);

105};

106

107struct modem\_cmux\_frame {

108 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) dlci\_address;

109 bool cr;

110 bool pf;

111 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) type;

112 const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*data;

113 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) data\_len;

114};

115

116struct modem\_cmux\_work {

117 struct k\_work\_delayable dwork;

118 struct modem\_cmux \*cmux;

119};

120

121struct modem\_cmux {

122 /\* Bus pipe \*/

123 struct modem\_pipe \*pipe;

124

125 /\* Event handler \*/

126 [modem\_cmux\_callback](group__modem__cmux.md#ga998b334620c9970ebbb0bcf620ea5923) callback;

127 void \*user\_data;

128

129 /\* DLCI channel contexts \*/

130 [sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8) dlcis;

131

132 /\* State \*/

133 enum modem\_cmux\_state [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90);

134 bool flow\_control\_on;

135

136 /\* Receive state\*/

137 enum modem\_cmux\_receive\_state receive\_state;

138

139 /\* Receive buffer \*/

140 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*receive\_buf;

141 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) receive\_buf\_size;

142 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) receive\_buf\_len;

143

144 /\* Transmit buffer \*/

145 struct ring\_buf transmit\_rb;

146 struct k\_mutex transmit\_rb\_lock;

147

148 /\* Received frame \*/

149 struct modem\_cmux\_frame frame;

150 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) frame\_header[5];

151 [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) frame\_header\_len;

152

153 /\* Work \*/

154 struct k\_work\_delayable receive\_work;

155 struct k\_work\_delayable transmit\_work;

156 struct k\_work\_delayable connect\_work;

157 struct k\_work\_delayable disconnect\_work;

158

159 /\* Synchronize actions \*/

160 struct k\_event event;

161};

162

166

[ 170](structmodem__cmux__config.md)struct [modem\_cmux\_config](structmodem__cmux__config.md) {

[ 172](structmodem__cmux__config.md#a2cba948c704f02429022d360326b9838) [modem\_cmux\_callback](group__modem__cmux.md#ga998b334620c9970ebbb0bcf620ea5923) [callback](structmodem__cmux__config.md#a2cba948c704f02429022d360326b9838);

[ 174](structmodem__cmux__config.md#a6714790f733ba7e4431353b6cdbbe3ee) void \*[user\_data](structmodem__cmux__config.md#a6714790f733ba7e4431353b6cdbbe3ee);

[ 176](structmodem__cmux__config.md#a2935694a75a95da8571b1c520a9800c8) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[receive\_buf](structmodem__cmux__config.md#a2935694a75a95da8571b1c520a9800c8);

[ 178](structmodem__cmux__config.md#a2fcf4ba7f088701ec6c5b750c8af3a89) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [receive\_buf\_size](structmodem__cmux__config.md#a2fcf4ba7f088701ec6c5b750c8af3a89);

[ 180](structmodem__cmux__config.md#a6920bf8f7c52522e8b76ba09051887c5) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[transmit\_buf](structmodem__cmux__config.md#a6920bf8f7c52522e8b76ba09051887c5);

[ 182](structmodem__cmux__config.md#ae028b4dde63311a810c67686dc662154) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [transmit\_buf\_size](structmodem__cmux__config.md#ae028b4dde63311a810c67686dc662154);

183};

184

[ 190](group__modem__cmux.md#gad72973ad82504ae64d184ce11572ab88)void [modem\_cmux\_init](group__modem__cmux.md#gad72973ad82504ae64d184ce11572ab88)(struct modem\_cmux \*cmux, const struct [modem\_cmux\_config](structmodem__cmux__config.md) \*config);

191

[ 195](structmodem__cmux__dlci__config.md)struct [modem\_cmux\_dlci\_config](structmodem__cmux__dlci__config.md) {

[ 197](structmodem__cmux__dlci__config.md#ad0b1fe93bbee6343c8446da5a0ad88c9) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [dlci\_address](structmodem__cmux__dlci__config.md#ad0b1fe93bbee6343c8446da5a0ad88c9);

[ 199](structmodem__cmux__dlci__config.md#ad3d6c1e0adce243aa536e52e5e4c4374) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*[receive\_buf](structmodem__cmux__dlci__config.md#ad3d6c1e0adce243aa536e52e5e4c4374);

[ 201](structmodem__cmux__dlci__config.md#af7715440c78d87466f91464000db1fef) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [receive\_buf\_size](structmodem__cmux__dlci__config.md#af7715440c78d87466f91464000db1fef);

202};

203

[ 211](group__modem__cmux.md#gabfd8e728eb8940b4093ae132b7add7d7)struct modem\_pipe \*[modem\_cmux\_dlci\_init](group__modem__cmux.md#gabfd8e728eb8940b4093ae132b7add7d7)(struct modem\_cmux \*cmux, struct modem\_cmux\_dlci \*dlci,

212 const struct [modem\_cmux\_dlci\_config](structmodem__cmux__dlci__config.md) \*config);

213

[ 220](group__modem__cmux.md#gab85f5c71a3cf131ff97aa47749197cb3)int [modem\_cmux\_attach](group__modem__cmux.md#gab85f5c71a3cf131ff97aa47749197cb3)(struct modem\_cmux \*cmux, struct modem\_pipe \*pipe);

221

[ 232](group__modem__cmux.md#ga362cd4b2dff122e3bbaee02b378dd226)int [modem\_cmux\_connect](group__modem__cmux.md#ga362cd4b2dff122e3bbaee02b378dd226)(struct modem\_cmux \*cmux);

233

[ 244](group__modem__cmux.md#ga9fa4a1cd9cf1e1c253e621c650a611d0)int [modem\_cmux\_connect\_async](group__modem__cmux.md#ga9fa4a1cd9cf1e1c253e621c650a611d0)(struct modem\_cmux \*cmux);

245

[ 256](group__modem__cmux.md#ga482171f67db206780d0b8a2cf5b32a93)int [modem\_cmux\_disconnect](group__modem__cmux.md#ga482171f67db206780d0b8a2cf5b32a93)(struct modem\_cmux \*cmux);

257

[ 268](group__modem__cmux.md#ga988c8efbebf63871730918d862b7c490)int [modem\_cmux\_disconnect\_async](group__modem__cmux.md#ga988c8efbebf63871730918d862b7c490)(struct modem\_cmux \*cmux);

269

[ 280](group__modem__cmux.md#gadc7c6ff92b7ac52717151bd6bf1efdff)void [modem\_cmux\_release](group__modem__cmux.md#gadc7c6ff92b7ac52717151bd6bf1efdff)(struct modem\_cmux \*cmux);

281

285

286#ifdef \_\_cplusplus

287}

288#endif

289

290#endif /\* ZEPHYR\_MODEM\_CMUX\_ \*/

[atomic.h](atomic_8h.md)

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

**Definition** cmux.h:50

[modem\_cmux\_connect\_async](group__modem__cmux.md#ga9fa4a1cd9cf1e1c253e621c650a611d0)

int modem\_cmux\_connect\_async(struct modem\_cmux \*cmux)

Connect CMUX instance asynchronously.

[modem\_cmux\_event](group__modem__cmux.md#gab60ea756d37bd9ed59f07c6380952d36)

modem\_cmux\_event

**Definition** cmux.h:45

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

**Definition** cmux.h:47

[MODEM\_CMUX\_EVENT\_CONNECTED](group__modem__cmux.md#ggab60ea756d37bd9ed59f07c6380952d36a8d37518bf5ba31237e59a413f36be4b2)

@ MODEM\_CMUX\_EVENT\_CONNECTED

**Definition** cmux.h:46

[sys\_slist\_t](group__single-linked-list__apis.md#ga44658c336b634c03938a251cdc8134f8)

struct \_slist sys\_slist\_t

Single-linked list structure.

**Definition** slist.h:49

[sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493)

struct \_snode sys\_snode\_t

Single-linked list node structure.

**Definition** slist.h:39

[kernel.h](include_2zephyr_2kernel_8h.md)

Public kernel APIs.

[types.h](include_2zephyr_2types_8h.md)

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

**Definition** cmux.h:170

[modem\_cmux\_config::receive\_buf](structmodem__cmux__config.md#a2935694a75a95da8571b1c520a9800c8)

uint8\_t \* receive\_buf

Receive buffer.

**Definition** cmux.h:176

[modem\_cmux\_config::callback](structmodem__cmux__config.md#a2cba948c704f02429022d360326b9838)

modem\_cmux\_callback callback

Invoked when event occurs.

**Definition** cmux.h:172

[modem\_cmux\_config::receive\_buf\_size](structmodem__cmux__config.md#a2fcf4ba7f088701ec6c5b750c8af3a89)

uint16\_t receive\_buf\_size

Size of receive buffer in bytes [127, ...].

**Definition** cmux.h:178

[modem\_cmux\_config::user\_data](structmodem__cmux__config.md#a6714790f733ba7e4431353b6cdbbe3ee)

void \* user\_data

Free to use pointer passed to event handler when invoked.

**Definition** cmux.h:174

[modem\_cmux\_config::transmit\_buf](structmodem__cmux__config.md#a6920bf8f7c52522e8b76ba09051887c5)

uint8\_t \* transmit\_buf

Transmit buffer.

**Definition** cmux.h:180

[modem\_cmux\_config::transmit\_buf\_size](structmodem__cmux__config.md#ae028b4dde63311a810c67686dc662154)

uint16\_t transmit\_buf\_size

Size of transmit buffer in bytes [149, ...].

**Definition** cmux.h:182

[modem\_cmux\_dlci\_config](structmodem__cmux__dlci__config.md)

CMUX DLCI configuration.

**Definition** cmux.h:195

[modem\_cmux\_dlci\_config::dlci\_address](structmodem__cmux__dlci__config.md#ad0b1fe93bbee6343c8446da5a0ad88c9)

uint8\_t dlci\_address

DLCI channel address.

**Definition** cmux.h:197

[modem\_cmux\_dlci\_config::receive\_buf](structmodem__cmux__dlci__config.md#ad3d6c1e0adce243aa536e52e5e4c4374)

uint8\_t \* receive\_buf

Receive buffer used by pipe.

**Definition** cmux.h:199

[modem\_cmux\_dlci\_config::receive\_buf\_size](structmodem__cmux__dlci__config.md#af7715440c78d87466f91464000db1fef)

uint16\_t receive\_buf\_size

Size of receive buffer used by pipe [127, ...].

**Definition** cmux.h:201

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [modem](dir_a816d481c0f951d2967bb275acf5f3dd.md)
- [cmux.h](cmux_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

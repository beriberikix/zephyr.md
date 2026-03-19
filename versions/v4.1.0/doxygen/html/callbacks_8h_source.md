---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/callbacks_8h_source.html
original_path: doxygen/html/callbacks_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

callbacks.h

[Go to the documentation of this file.](callbacks_8h.md)

[ 1](group__mcumgr__callback__api.md#gae61f705224a859776ee5161dfda5ed7d)/\*

2 \* Copyright (c) 2022-2023 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef H\_MCUMGR\_CALLBACKS\_

8#define H\_MCUMGR\_CALLBACKS\_

9

10#include <[inttypes.h](inttypes_8h.md)>

11#include <[zephyr/sys/slist.h](slist_8h.md)>

12#include <[zephyr/mgmt/mcumgr/mgmt/mgmt.h](mgmt_8h.md)>

13

14#ifdef CONFIG\_MCUMGR\_GRP\_FS

15#include <[zephyr/mgmt/mcumgr/grp/fs\_mgmt/fs\_mgmt\_callbacks.h](fs__mgmt__callbacks_8h.md)>

16#endif

17

18#ifdef CONFIG\_MCUMGR\_GRP\_IMG

19#include <[zephyr/mgmt/mcumgr/grp/img\_mgmt/img\_mgmt\_callbacks.h](img__mgmt__callbacks_8h.md)>

20#endif

21

22#ifdef CONFIG\_MCUMGR\_GRP\_OS

23#include <[zephyr/mgmt/mcumgr/grp/os\_mgmt/os\_mgmt\_callbacks.h](os__mgmt__callbacks_8h.md)>

24#endif

25

26#ifdef CONFIG\_MCUMGR\_GRP\_SETTINGS

27#include <[zephyr/mgmt/mcumgr/grp/settings\_mgmt/settings\_mgmt\_callbacks.h](settings__mgmt__callbacks_8h.md)>

28#endif

29

30#ifdef CONFIG\_MCUMGR\_GRP\_ENUM

31#include <[zephyr/mgmt/mcumgr/grp/enum\_mgmt/enum\_mgmt\_callbacks.h](enum__mgmt__callbacks_8h.md)>

32#endif

33

34#ifdef \_\_cplusplus

35extern "C" {

36#endif

37

44

47#define MGMT\_EVT\_OP\_ID\_ALL 0xffff

48

50#define MGMT\_DEF\_EVT\_OP\_ID(group, event\_id) ((group << 16) | BIT(event\_id))

51

53#define MGMT\_DEF\_EVT\_OP\_ALL(group) ((group << 16) | MGMT\_EVT\_OP\_ID\_ALL)

55

[ 57](group__mcumgr__callback__api.md#gaa3290bd9a21f9718adac92bfe313161f)#define MGMT\_EVT\_GET\_GROUP(event) ((event >> 16) & MGMT\_EVT\_OP\_ID\_ALL)

58

[ 60](group__mcumgr__callback__api.md#ga4c6ff3fb3b14a31e65248cec9840b1dd)#define MGMT\_EVT\_GET\_ID(event) (event & MGMT\_EVT\_OP\_ID\_ALL)

61

[ 65](group__mcumgr__callback__api.md#ga1ba636c0efb7a91630ed9743e6fd4d6c)enum [mgmt\_cb\_return](group__mcumgr__callback__api.md#ga1ba636c0efb7a91630ed9743e6fd4d6c) {

[ 67](group__mcumgr__callback__api.md#gga1ba636c0efb7a91630ed9743e6fd4d6cac9a6240975af04d413048d762ca1b0da) [MGMT\_CB\_OK](group__mcumgr__callback__api.md#gga1ba636c0efb7a91630ed9743e6fd4d6cac9a6240975af04d413048d762ca1b0da),

68

[ 70](group__mcumgr__callback__api.md#gga1ba636c0efb7a91630ed9743e6fd4d6ca6ca7c4ba7dc1c300489da4a935b7d990) [MGMT\_CB\_ERROR\_RC](group__mcumgr__callback__api.md#gga1ba636c0efb7a91630ed9743e6fd4d6ca6ca7c4ba7dc1c300489da4a935b7d990),

71

[ 76](group__mcumgr__callback__api.md#gga1ba636c0efb7a91630ed9743e6fd4d6cad88f720a1d62658c346e8bebfb81d66d) [MGMT\_CB\_ERROR\_ERR](group__mcumgr__callback__api.md#gga1ba636c0efb7a91630ed9743e6fd4d6cad88f720a1d62658c346e8bebfb81d66d),

77};

78

108typedef enum [mgmt\_cb\_return](group__mcumgr__callback__api.md#ga1ba636c0efb7a91630ed9743e6fd4d6c) (\*[mgmt\_cb](group__mcumgr__callback__api.md#gae61f705224a859776ee5161dfda5ed7d))([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) event, enum [mgmt\_cb\_return](group__mcumgr__callback__api.md#ga1ba636c0efb7a91630ed9743e6fd4d6c) prev\_status,

109 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*rc, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*[group](structgroup.md), bool \*abort\_more, void \*data,

110 size\_t data\_size);

111

[ 115](group__mcumgr__callback__api.md#ga40ecf8933112abe76d7fedb3dcc7cdbe)enum [mgmt\_cb\_groups](group__mcumgr__callback__api.md#ga40ecf8933112abe76d7fedb3dcc7cdbe) {

[ 116](group__mcumgr__callback__api.md#gga40ecf8933112abe76d7fedb3dcc7cdbea0529ffba74faffdc8f0ad33ab3c4786a) [MGMT\_EVT\_GRP\_ALL](group__mcumgr__callback__api.md#gga40ecf8933112abe76d7fedb3dcc7cdbea0529ffba74faffdc8f0ad33ab3c4786a) = 0,

[ 117](group__mcumgr__callback__api.md#gga40ecf8933112abe76d7fedb3dcc7cdbea18b3bfbd15159108bf60fd8e0569658c) [MGMT\_EVT\_GRP\_SMP](group__mcumgr__callback__api.md#gga40ecf8933112abe76d7fedb3dcc7cdbea18b3bfbd15159108bf60fd8e0569658c),

[ 118](group__mcumgr__callback__api.md#gga40ecf8933112abe76d7fedb3dcc7cdbea34df22b866cd61f81bdc7d743edce2ae) [MGMT\_EVT\_GRP\_OS](group__mcumgr__callback__api.md#gga40ecf8933112abe76d7fedb3dcc7cdbea34df22b866cd61f81bdc7d743edce2ae),

[ 119](group__mcumgr__callback__api.md#gga40ecf8933112abe76d7fedb3dcc7cdbeaf55a2f10814a24eb11660ffe4bb930e1) [MGMT\_EVT\_GRP\_IMG](group__mcumgr__callback__api.md#gga40ecf8933112abe76d7fedb3dcc7cdbeaf55a2f10814a24eb11660ffe4bb930e1),

[ 120](group__mcumgr__callback__api.md#gga40ecf8933112abe76d7fedb3dcc7cdbea5504e38868b808ea6e46965bf3e6da48) [MGMT\_EVT\_GRP\_FS](group__mcumgr__callback__api.md#gga40ecf8933112abe76d7fedb3dcc7cdbea5504e38868b808ea6e46965bf3e6da48),

[ 121](group__mcumgr__callback__api.md#gga40ecf8933112abe76d7fedb3dcc7cdbea541b2a1541ad78bdfb3d26dc314ba536) [MGMT\_EVT\_GRP\_SETTINGS](group__mcumgr__callback__api.md#gga40ecf8933112abe76d7fedb3dcc7cdbea541b2a1541ad78bdfb3d26dc314ba536),

[ 122](group__mcumgr__callback__api.md#gga40ecf8933112abe76d7fedb3dcc7cdbeac23aa88bc1047404e2d75f7c5de7a6a3) [MGMT\_EVT\_GRP\_ENUM](group__mcumgr__callback__api.md#gga40ecf8933112abe76d7fedb3dcc7cdbeac23aa88bc1047404e2d75f7c5de7a6a3),

123

[ 124](group__mcumgr__callback__api.md#gga40ecf8933112abe76d7fedb3dcc7cdbea66361c0b52e996d2feb0a7c84532594d) [MGMT\_EVT\_GRP\_USER\_CUSTOM\_START](group__mcumgr__callback__api.md#gga40ecf8933112abe76d7fedb3dcc7cdbea66361c0b52e996d2feb0a7c84532594d) = [MGMT\_GROUP\_ID\_PERUSER](group__mcumgr__mgmt__api.md#gga81f98b9a0c3810f7d607b783f8e259b5af2504389290c7b2a3537f4ebfb730726),

125};

126

[ 130](group__mcumgr__callback__api.md#gaab6470007be89e5aab88838456f9561a)enum [smp\_all\_events](group__mcumgr__callback__api.md#gaab6470007be89e5aab88838456f9561a) {

[ 132](group__mcumgr__callback__api.md#ggaab6470007be89e5aab88838456f9561aaf9e289ad5f7e0fd8bec581f67951813a) [MGMT\_EVT\_OP\_ALL](group__mcumgr__callback__api.md#ggaab6470007be89e5aab88838456f9561aaf9e289ad5f7e0fd8bec581f67951813a) = MGMT\_DEF\_EVT\_OP\_ALL([MGMT\_EVT\_GRP\_ALL](group__mcumgr__callback__api.md#gga40ecf8933112abe76d7fedb3dcc7cdbea0529ffba74faffdc8f0ad33ab3c4786a)),

133};

134

[ 138](group__mcumgr__callback__api.md#ga590788274b4508c6203685d9e9252184)enum [smp\_group\_events](group__mcumgr__callback__api.md#ga590788274b4508c6203685d9e9252184) {

[ 140](group__mcumgr__callback__api.md#gga590788274b4508c6203685d9e9252184a933f494aa22d52d536bb6c3de0dbeb28) [MGMT\_EVT\_OP\_CMD\_RECV](group__mcumgr__callback__api.md#gga590788274b4508c6203685d9e9252184a933f494aa22d52d536bb6c3de0dbeb28) = MGMT\_DEF\_EVT\_OP\_ID([MGMT\_EVT\_GRP\_SMP](group__mcumgr__callback__api.md#gga40ecf8933112abe76d7fedb3dcc7cdbea18b3bfbd15159108bf60fd8e0569658c), 0),

141

[ 143](group__mcumgr__callback__api.md#gga590788274b4508c6203685d9e9252184afc1cee09954cdc6dfaee196dd7518770) [MGMT\_EVT\_OP\_CMD\_STATUS](group__mcumgr__callback__api.md#gga590788274b4508c6203685d9e9252184afc1cee09954cdc6dfaee196dd7518770) = MGMT\_DEF\_EVT\_OP\_ID([MGMT\_EVT\_GRP\_SMP](group__mcumgr__callback__api.md#gga40ecf8933112abe76d7fedb3dcc7cdbea18b3bfbd15159108bf60fd8e0569658c), 1),

144

[ 146](group__mcumgr__callback__api.md#gga590788274b4508c6203685d9e9252184adb820d1a8cdea6c74a5a39f096deab12) [MGMT\_EVT\_OP\_CMD\_DONE](group__mcumgr__callback__api.md#gga590788274b4508c6203685d9e9252184adb820d1a8cdea6c74a5a39f096deab12) = MGMT\_DEF\_EVT\_OP\_ID([MGMT\_EVT\_GRP\_SMP](group__mcumgr__callback__api.md#gga40ecf8933112abe76d7fedb3dcc7cdbea18b3bfbd15159108bf60fd8e0569658c), 2),

147

[ 149](group__mcumgr__callback__api.md#gga590788274b4508c6203685d9e9252184aa447c50326ec3f90c66314e744de0e70) [MGMT\_EVT\_OP\_CMD\_ALL](group__mcumgr__callback__api.md#gga590788274b4508c6203685d9e9252184aa447c50326ec3f90c66314e744de0e70) = MGMT\_DEF\_EVT\_OP\_ALL([MGMT\_EVT\_GRP\_SMP](group__mcumgr__callback__api.md#gga40ecf8933112abe76d7fedb3dcc7cdbea18b3bfbd15159108bf60fd8e0569658c)),

150};

151

[ 155](group__mcumgr__callback__api.md#ga324223c20cbefe3400272e2789082c79)enum [fs\_mgmt\_group\_events](group__mcumgr__callback__api.md#ga324223c20cbefe3400272e2789082c79) {

[ 157](group__mcumgr__callback__api.md#gga324223c20cbefe3400272e2789082c79a0475953c86b97afa8e4ed30da3f736d3) [MGMT\_EVT\_OP\_FS\_MGMT\_FILE\_ACCESS](group__mcumgr__callback__api.md#gga324223c20cbefe3400272e2789082c79a0475953c86b97afa8e4ed30da3f736d3) = MGMT\_DEF\_EVT\_OP\_ID([MGMT\_EVT\_GRP\_FS](group__mcumgr__callback__api.md#gga40ecf8933112abe76d7fedb3dcc7cdbea5504e38868b808ea6e46965bf3e6da48), 0),

158

[ 160](group__mcumgr__callback__api.md#gga324223c20cbefe3400272e2789082c79a9d0806e3d6f0276930af97370ae23b53) [MGMT\_EVT\_OP\_FS\_MGMT\_ALL](group__mcumgr__callback__api.md#gga324223c20cbefe3400272e2789082c79a9d0806e3d6f0276930af97370ae23b53) = MGMT\_DEF\_EVT\_OP\_ALL([MGMT\_EVT\_GRP\_FS](group__mcumgr__callback__api.md#gga40ecf8933112abe76d7fedb3dcc7cdbea5504e38868b808ea6e46965bf3e6da48)),

161};

162

[ 166](group__mcumgr__callback__api.md#ga3fa2c42bade08cca1122e32f6315f107)enum [img\_mgmt\_group\_events](group__mcumgr__callback__api.md#ga3fa2c42bade08cca1122e32f6315f107) {

[ 168](group__mcumgr__callback__api.md#gga3fa2c42bade08cca1122e32f6315f107a19d53f0c0f6649858e97fbcecfbaf24c) [MGMT\_EVT\_OP\_IMG\_MGMT\_DFU\_CHUNK](group__mcumgr__callback__api.md#gga3fa2c42bade08cca1122e32f6315f107a19d53f0c0f6649858e97fbcecfbaf24c) = MGMT\_DEF\_EVT\_OP\_ID([MGMT\_EVT\_GRP\_IMG](group__mcumgr__callback__api.md#gga40ecf8933112abe76d7fedb3dcc7cdbeaf55a2f10814a24eb11660ffe4bb930e1), 0),

169

[ 171](group__mcumgr__callback__api.md#gga3fa2c42bade08cca1122e32f6315f107af6424b9e8f800bde22a764da459a50a8) [MGMT\_EVT\_OP\_IMG\_MGMT\_DFU\_STOPPED](group__mcumgr__callback__api.md#gga3fa2c42bade08cca1122e32f6315f107af6424b9e8f800bde22a764da459a50a8) = MGMT\_DEF\_EVT\_OP\_ID([MGMT\_EVT\_GRP\_IMG](group__mcumgr__callback__api.md#gga40ecf8933112abe76d7fedb3dcc7cdbeaf55a2f10814a24eb11660ffe4bb930e1), 1),

172

[ 174](group__mcumgr__callback__api.md#gga3fa2c42bade08cca1122e32f6315f107af8836c552e137e15d5e859515f067bbf) [MGMT\_EVT\_OP\_IMG\_MGMT\_DFU\_STARTED](group__mcumgr__callback__api.md#gga3fa2c42bade08cca1122e32f6315f107af8836c552e137e15d5e859515f067bbf) = MGMT\_DEF\_EVT\_OP\_ID([MGMT\_EVT\_GRP\_IMG](group__mcumgr__callback__api.md#gga40ecf8933112abe76d7fedb3dcc7cdbeaf55a2f10814a24eb11660ffe4bb930e1), 2),

175

[ 177](group__mcumgr__callback__api.md#gga3fa2c42bade08cca1122e32f6315f107a2ff64450efa47d0d460c866f5634bce4) [MGMT\_EVT\_OP\_IMG\_MGMT\_DFU\_PENDING](group__mcumgr__callback__api.md#gga3fa2c42bade08cca1122e32f6315f107a2ff64450efa47d0d460c866f5634bce4) = MGMT\_DEF\_EVT\_OP\_ID([MGMT\_EVT\_GRP\_IMG](group__mcumgr__callback__api.md#gga40ecf8933112abe76d7fedb3dcc7cdbeaf55a2f10814a24eb11660ffe4bb930e1), 3),

178

[ 180](group__mcumgr__callback__api.md#gga3fa2c42bade08cca1122e32f6315f107a36e486e194d0d6013d188b4ed70a95fb) [MGMT\_EVT\_OP\_IMG\_MGMT\_DFU\_CONFIRMED](group__mcumgr__callback__api.md#gga3fa2c42bade08cca1122e32f6315f107a36e486e194d0d6013d188b4ed70a95fb) = MGMT\_DEF\_EVT\_OP\_ID([MGMT\_EVT\_GRP\_IMG](group__mcumgr__callback__api.md#gga40ecf8933112abe76d7fedb3dcc7cdbeaf55a2f10814a24eb11660ffe4bb930e1), 4),

181

[ 183](group__mcumgr__callback__api.md#gga3fa2c42bade08cca1122e32f6315f107a4204cb29c7308f103644162839abcb88) [MGMT\_EVT\_OP\_IMG\_MGMT\_DFU\_CHUNK\_WRITE\_COMPLETE](group__mcumgr__callback__api.md#gga3fa2c42bade08cca1122e32f6315f107a4204cb29c7308f103644162839abcb88) = MGMT\_DEF\_EVT\_OP\_ID([MGMT\_EVT\_GRP\_IMG](group__mcumgr__callback__api.md#gga40ecf8933112abe76d7fedb3dcc7cdbeaf55a2f10814a24eb11660ffe4bb930e1), 5),

184

[ 189](group__mcumgr__callback__api.md#gga3fa2c42bade08cca1122e32f6315f107a52a1b8f3d4dae7bab74fd6187500acc7) [MGMT\_EVT\_OP\_IMG\_MGMT\_IMAGE\_SLOT\_STATE](group__mcumgr__callback__api.md#gga3fa2c42bade08cca1122e32f6315f107a52a1b8f3d4dae7bab74fd6187500acc7) = MGMT\_DEF\_EVT\_OP\_ID([MGMT\_EVT\_GRP\_IMG](group__mcumgr__callback__api.md#gga40ecf8933112abe76d7fedb3dcc7cdbeaf55a2f10814a24eb11660ffe4bb930e1), 6),

190

[ 195](group__mcumgr__callback__api.md#gga3fa2c42bade08cca1122e32f6315f107acd93051e050127a961843e3a8650fda3) [MGMT\_EVT\_OP\_IMG\_MGMT\_SLOT\_INFO\_IMAGE](group__mcumgr__callback__api.md#gga3fa2c42bade08cca1122e32f6315f107acd93051e050127a961843e3a8650fda3) = MGMT\_DEF\_EVT\_OP\_ID([MGMT\_EVT\_GRP\_IMG](group__mcumgr__callback__api.md#gga40ecf8933112abe76d7fedb3dcc7cdbeaf55a2f10814a24eb11660ffe4bb930e1), 7),

196

[ 201](group__mcumgr__callback__api.md#gga3fa2c42bade08cca1122e32f6315f107a9e1b6d2ae97ef43edc7ad4749b7ac9b0) [MGMT\_EVT\_OP\_IMG\_MGMT\_SLOT\_INFO\_SLOT](group__mcumgr__callback__api.md#gga3fa2c42bade08cca1122e32f6315f107a9e1b6d2ae97ef43edc7ad4749b7ac9b0) = MGMT\_DEF\_EVT\_OP\_ID([MGMT\_EVT\_GRP\_IMG](group__mcumgr__callback__api.md#gga40ecf8933112abe76d7fedb3dcc7cdbeaf55a2f10814a24eb11660ffe4bb930e1), 8),

202

[ 204](group__mcumgr__callback__api.md#gga3fa2c42bade08cca1122e32f6315f107a0ba2354ef268ed22c51df7e5708c50bf) [MGMT\_EVT\_OP\_IMG\_MGMT\_ALL](group__mcumgr__callback__api.md#gga3fa2c42bade08cca1122e32f6315f107a0ba2354ef268ed22c51df7e5708c50bf) = MGMT\_DEF\_EVT\_OP\_ALL([MGMT\_EVT\_GRP\_IMG](group__mcumgr__callback__api.md#gga40ecf8933112abe76d7fedb3dcc7cdbeaf55a2f10814a24eb11660ffe4bb930e1)),

205};

206

[ 210](group__mcumgr__callback__api.md#ga261346c700a2522542d8282ca76f88a5)enum [os\_mgmt\_group\_events](group__mcumgr__callback__api.md#ga261346c700a2522542d8282ca76f88a5) {

[ 212](group__mcumgr__callback__api.md#gga261346c700a2522542d8282ca76f88a5a9feea9f8cfcca803a18be03e08583c52) [MGMT\_EVT\_OP\_OS\_MGMT\_RESET](group__mcumgr__callback__api.md#gga261346c700a2522542d8282ca76f88a5a9feea9f8cfcca803a18be03e08583c52) = MGMT\_DEF\_EVT\_OP\_ID([MGMT\_EVT\_GRP\_OS](group__mcumgr__callback__api.md#gga40ecf8933112abe76d7fedb3dcc7cdbea34df22b866cd61f81bdc7d743edce2ae), 0),

213

[ 215](group__mcumgr__callback__api.md#gga261346c700a2522542d8282ca76f88a5a60756021758616ee8d90b5508cb34ba5) [MGMT\_EVT\_OP\_OS\_MGMT\_INFO\_CHECK](group__mcumgr__callback__api.md#gga261346c700a2522542d8282ca76f88a5a60756021758616ee8d90b5508cb34ba5) = MGMT\_DEF\_EVT\_OP\_ID([MGMT\_EVT\_GRP\_OS](group__mcumgr__callback__api.md#gga40ecf8933112abe76d7fedb3dcc7cdbea34df22b866cd61f81bdc7d743edce2ae), 1),

216

[ 218](group__mcumgr__callback__api.md#gga261346c700a2522542d8282ca76f88a5ac931d11c7cc4160a9f93c3f011a26f0f) [MGMT\_EVT\_OP\_OS\_MGMT\_INFO\_APPEND](group__mcumgr__callback__api.md#gga261346c700a2522542d8282ca76f88a5ac931d11c7cc4160a9f93c3f011a26f0f) = MGMT\_DEF\_EVT\_OP\_ID([MGMT\_EVT\_GRP\_OS](group__mcumgr__callback__api.md#gga40ecf8933112abe76d7fedb3dcc7cdbea34df22b866cd61f81bdc7d743edce2ae), 2),

219

[ 221](group__mcumgr__callback__api.md#gga261346c700a2522542d8282ca76f88a5a06b0f21e6905a28251f04ec544095a2d) [MGMT\_EVT\_OP\_OS\_MGMT\_DATETIME\_GET](group__mcumgr__callback__api.md#gga261346c700a2522542d8282ca76f88a5a06b0f21e6905a28251f04ec544095a2d) = MGMT\_DEF\_EVT\_OP\_ID([MGMT\_EVT\_GRP\_OS](group__mcumgr__callback__api.md#gga40ecf8933112abe76d7fedb3dcc7cdbea34df22b866cd61f81bdc7d743edce2ae), 3),

222

[ 224](group__mcumgr__callback__api.md#gga261346c700a2522542d8282ca76f88a5a3cd3ee81f3c691c81a11de2dc6ccf98b) [MGMT\_EVT\_OP\_OS\_MGMT\_DATETIME\_SET](group__mcumgr__callback__api.md#gga261346c700a2522542d8282ca76f88a5a3cd3ee81f3c691c81a11de2dc6ccf98b) = MGMT\_DEF\_EVT\_OP\_ID([MGMT\_EVT\_GRP\_OS](group__mcumgr__callback__api.md#gga40ecf8933112abe76d7fedb3dcc7cdbea34df22b866cd61f81bdc7d743edce2ae), 4),

225

[ 230](group__mcumgr__callback__api.md#gga261346c700a2522542d8282ca76f88a5a683d22d5d17a493a2f0732371dc116bf) [MGMT\_EVT\_OP\_OS\_MGMT\_BOOTLOADER\_INFO](group__mcumgr__callback__api.md#gga261346c700a2522542d8282ca76f88a5a683d22d5d17a493a2f0732371dc116bf) = MGMT\_DEF\_EVT\_OP\_ID([MGMT\_EVT\_GRP\_OS](group__mcumgr__callback__api.md#gga40ecf8933112abe76d7fedb3dcc7cdbea34df22b866cd61f81bdc7d743edce2ae), 5),

231

[ 233](group__mcumgr__callback__api.md#gga261346c700a2522542d8282ca76f88a5ae5e0c2779b106a03a675ee2f9b1c389a) [MGMT\_EVT\_OP\_OS\_MGMT\_ALL](group__mcumgr__callback__api.md#gga261346c700a2522542d8282ca76f88a5ae5e0c2779b106a03a675ee2f9b1c389a) = MGMT\_DEF\_EVT\_OP\_ALL([MGMT\_EVT\_GRP\_OS](group__mcumgr__callback__api.md#gga40ecf8933112abe76d7fedb3dcc7cdbea34df22b866cd61f81bdc7d743edce2ae)),

234};

235

[ 239](group__mcumgr__callback__api.md#ga1711bc9f45a8114a6b0c89db4a40e3de)enum [settings\_mgmt\_group\_events](group__mcumgr__callback__api.md#ga1711bc9f45a8114a6b0c89db4a40e3de) {

[ 241](group__mcumgr__callback__api.md#gga1711bc9f45a8114a6b0c89db4a40e3dea65c675aa2e807d9977a5ff13a97c75a0) [MGMT\_EVT\_OP\_SETTINGS\_MGMT\_ACCESS](group__mcumgr__callback__api.md#gga1711bc9f45a8114a6b0c89db4a40e3dea65c675aa2e807d9977a5ff13a97c75a0) = MGMT\_DEF\_EVT\_OP\_ID([MGMT\_EVT\_GRP\_SETTINGS](group__mcumgr__callback__api.md#gga40ecf8933112abe76d7fedb3dcc7cdbea541b2a1541ad78bdfb3d26dc314ba536), 0),

242

[ 244](group__mcumgr__callback__api.md#gga1711bc9f45a8114a6b0c89db4a40e3deac91ef1ec87aabb0b3f3587a9303bdbf2) [MGMT\_EVT\_OP\_SETTINGS\_MGMT\_ALL](group__mcumgr__callback__api.md#gga1711bc9f45a8114a6b0c89db4a40e3deac91ef1ec87aabb0b3f3587a9303bdbf2) = MGMT\_DEF\_EVT\_OP\_ALL([MGMT\_EVT\_GRP\_SETTINGS](group__mcumgr__callback__api.md#gga40ecf8933112abe76d7fedb3dcc7cdbea541b2a1541ad78bdfb3d26dc314ba536)),

245};

246

[ 250](group__mcumgr__callback__api.md#ga7ddc4c031948a2fee56fcbdb7d675a1d)enum [enum\_mgmt\_group\_events](group__mcumgr__callback__api.md#ga7ddc4c031948a2fee56fcbdb7d675a1d) {

[ 252](group__mcumgr__callback__api.md#gga7ddc4c031948a2fee56fcbdb7d675a1da749daeaef01327a881f91671b9222abf) [MGMT\_EVT\_OP\_ENUM\_MGMT\_DETAILS](group__mcumgr__callback__api.md#gga7ddc4c031948a2fee56fcbdb7d675a1da749daeaef01327a881f91671b9222abf) = MGMT\_DEF\_EVT\_OP\_ID([MGMT\_EVT\_GRP\_ENUM](group__mcumgr__callback__api.md#gga40ecf8933112abe76d7fedb3dcc7cdbeac23aa88bc1047404e2d75f7c5de7a6a3), 0),

253

[ 255](group__mcumgr__callback__api.md#gga7ddc4c031948a2fee56fcbdb7d675a1da5f19a62b627e602db48748c91ce2354b) [MGMT\_EVT\_OP\_ENUM\_MGMT\_ALL](group__mcumgr__callback__api.md#gga7ddc4c031948a2fee56fcbdb7d675a1da5f19a62b627e602db48748c91ce2354b) = MGMT\_DEF\_EVT\_OP\_ALL([MGMT\_EVT\_GRP\_ENUM](group__mcumgr__callback__api.md#gga40ecf8933112abe76d7fedb3dcc7cdbeac23aa88bc1047404e2d75f7c5de7a6a3)),

256};

257

[ 261](structmgmt__callback.md)struct [mgmt\_callback](structmgmt__callback.md) {

[ 263](structmgmt__callback.md#a4595cb6a72ebf8b9396e63a8f31c497f) [sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493) [node](structmgmt__callback.md#a4595cb6a72ebf8b9396e63a8f31c497f);

264

[ 266](structmgmt__callback.md#acd79e73a2a3d44697bbda2b401d1e7df) [mgmt\_cb](group__mcumgr__callback__api.md#gae61f705224a859776ee5161dfda5ed7d) [callback](structmgmt__callback.md#acd79e73a2a3d44697bbda2b401d1e7df);

267

[ 277](structmgmt__callback.md#a3dc18e5f7e3e00c1c05cc104bb1f3ab1) [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [event\_id](structmgmt__callback.md#a3dc18e5f7e3e00c1c05cc104bb1f3ab1);

278};

279

[ 283](structmgmt__evt__op__cmd__arg.md)struct [mgmt\_evt\_op\_cmd\_arg](structmgmt__evt__op__cmd__arg.md) {

[ 285](structmgmt__evt__op__cmd__arg.md#a0607126986dc0a1e9a0dae348d278741) [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) [group](structmgmt__evt__op__cmd__arg.md#a0607126986dc0a1e9a0dae348d278741);

286

[ 288](structmgmt__evt__op__cmd__arg.md#ac461e832ea0997ae19be72df4caf0bb7) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [id](structmgmt__evt__op__cmd__arg.md#ac461e832ea0997ae19be72df4caf0bb7);

289

290 union {

[ 292](structmgmt__evt__op__cmd__arg.md#acbd58ae2efe86685df33e58450753fe1) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [op](structmgmt__evt__op__cmd__arg.md#acbd58ae2efe86685df33e58450753fe1);

293

[ 295](structmgmt__evt__op__cmd__arg.md#a7e7a469f944d27d92e25e42d56fa32d2) int [err](structmgmt__evt__op__cmd__arg.md#a7e7a469f944d27d92e25e42d56fa32d2);

296

[ 298](structmgmt__evt__op__cmd__arg.md#a4d08fca41a60aee6c458d510d528a307) int [status](structmgmt__evt__op__cmd__arg.md#a4d08fca41a60aee6c458d510d528a307);

299 };

300};

301

[ 309](group__mcumgr__callback__api.md#gab309008a29ddcde95654ad812463d3bc)[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [mgmt\_evt\_get\_index](group__mcumgr__callback__api.md#gab309008a29ddcde95654ad812463d3bc)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) event);

310

[ 327](group__mcumgr__callback__api.md#gaf9308502f8137f7fb80667941cdd46ca)enum [mgmt\_cb\_return](group__mcumgr__callback__api.md#ga1ba636c0efb7a91630ed9743e6fd4d6c) [mgmt\_callback\_notify](group__mcumgr__callback__api.md#gaf9308502f8137f7fb80667941cdd46ca)([uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) event, void \*data, size\_t data\_size,

328 [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) \*err\_rc, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*err\_group);

329

[ 335](group__mcumgr__callback__api.md#gaaf698627904995930784c96fb48a1d7b)void [mgmt\_callback\_register](group__mcumgr__callback__api.md#gaaf698627904995930784c96fb48a1d7b)(struct [mgmt\_callback](structmgmt__callback.md) \*callback);

336

[ 342](group__mcumgr__callback__api.md#ga24d97d6d17c5586a45abacb59d906bd2)void [mgmt\_callback\_unregister](group__mcumgr__callback__api.md#ga24d97d6d17c5586a45abacb59d906bd2)(struct [mgmt\_callback](structmgmt__callback.md) \*callback);

343

347

348#ifdef \_\_cplusplus

349}

350#endif

351

352#endif /\* H\_MCUMGR\_CALLBACKS\_ \*/

[enum\_mgmt\_callbacks.h](enum__mgmt__callbacks_8h.md)

[fs\_mgmt\_callbacks.h](fs__mgmt__callbacks_8h.md)

[settings\_mgmt\_group\_events](group__mcumgr__callback__api.md#ga1711bc9f45a8114a6b0c89db4a40e3de)

settings\_mgmt\_group\_events

MGMT event opcodes for settings management group.

**Definition** callbacks.h:239

[mgmt\_cb\_return](group__mcumgr__callback__api.md#ga1ba636c0efb7a91630ed9743e6fd4d6c)

mgmt\_cb\_return

MGMT event callback return value.

**Definition** callbacks.h:65

[mgmt\_callback\_unregister](group__mcumgr__callback__api.md#ga24d97d6d17c5586a45abacb59d906bd2)

void mgmt\_callback\_unregister(struct mgmt\_callback \*callback)

Unregister event callback function.

[os\_mgmt\_group\_events](group__mcumgr__callback__api.md#ga261346c700a2522542d8282ca76f88a5)

os\_mgmt\_group\_events

MGMT event opcodes for operating system management group.

**Definition** callbacks.h:210

[fs\_mgmt\_group\_events](group__mcumgr__callback__api.md#ga324223c20cbefe3400272e2789082c79)

fs\_mgmt\_group\_events

MGMT event opcodes for filesystem management group.

**Definition** callbacks.h:155

[img\_mgmt\_group\_events](group__mcumgr__callback__api.md#ga3fa2c42bade08cca1122e32f6315f107)

img\_mgmt\_group\_events

MGMT event opcodes for image management group.

**Definition** callbacks.h:166

[mgmt\_cb\_groups](group__mcumgr__callback__api.md#ga40ecf8933112abe76d7fedb3dcc7cdbe)

mgmt\_cb\_groups

MGMT event callback group IDs.

**Definition** callbacks.h:115

[smp\_group\_events](group__mcumgr__callback__api.md#ga590788274b4508c6203685d9e9252184)

smp\_group\_events

MGMT event opcodes for base SMP command processing.

**Definition** callbacks.h:138

[enum\_mgmt\_group\_events](group__mcumgr__callback__api.md#ga7ddc4c031948a2fee56fcbdb7d675a1d)

enum\_mgmt\_group\_events

MGMT event opcodes for enumeration management group.

**Definition** callbacks.h:250

[smp\_all\_events](group__mcumgr__callback__api.md#gaab6470007be89e5aab88838456f9561a)

smp\_all\_events

MGMT event opcodes for all command processing.

**Definition** callbacks.h:130

[mgmt\_callback\_register](group__mcumgr__callback__api.md#gaaf698627904995930784c96fb48a1d7b)

void mgmt\_callback\_register(struct mgmt\_callback \*callback)

Register event callback function.

[mgmt\_evt\_get\_index](group__mcumgr__callback__api.md#gab309008a29ddcde95654ad812463d3bc)

uint8\_t mgmt\_evt\_get\_index(uint32\_t event)

Get event ID index from event.

[mgmt\_cb](group__mcumgr__callback__api.md#gae61f705224a859776ee5161dfda5ed7d)

enum mgmt\_cb\_return(\* mgmt\_cb)(uint32\_t event, enum mgmt\_cb\_return prev\_status, int32\_t \*rc, uint16\_t \*group, bool \*abort\_more, void \*data, size\_t data\_size)

Function to be called on MGMT notification/event.

**Definition** callbacks.h:108

[mgmt\_callback\_notify](group__mcumgr__callback__api.md#gaf9308502f8137f7fb80667941cdd46ca)

enum mgmt\_cb\_return mgmt\_callback\_notify(uint32\_t event, void \*data, size\_t data\_size, int32\_t \*err\_rc, uint16\_t \*err\_group)

This function is called to notify registered callbacks about mcumgr notifications/events.

[MGMT\_EVT\_OP\_SETTINGS\_MGMT\_ACCESS](group__mcumgr__callback__api.md#gga1711bc9f45a8114a6b0c89db4a40e3dea65c675aa2e807d9977a5ff13a97c75a0)

@ MGMT\_EVT\_OP\_SETTINGS\_MGMT\_ACCESS

Callback when a setting is read/written/deleted.

**Definition** callbacks.h:241

[MGMT\_EVT\_OP\_SETTINGS\_MGMT\_ALL](group__mcumgr__callback__api.md#gga1711bc9f45a8114a6b0c89db4a40e3deac91ef1ec87aabb0b3f3587a9303bdbf2)

@ MGMT\_EVT\_OP\_SETTINGS\_MGMT\_ALL

Used to enable all settings\_mgmt\_group events.

**Definition** callbacks.h:244

[MGMT\_CB\_ERROR\_RC](group__mcumgr__callback__api.md#gga1ba636c0efb7a91630ed9743e6fd4d6ca6ca7c4ba7dc1c300489da4a935b7d990)

@ MGMT\_CB\_ERROR\_RC

SMP protocol error and err\_rc contains the mcumgr\_err\_t error code.

**Definition** callbacks.h:70

[MGMT\_CB\_OK](group__mcumgr__callback__api.md#gga1ba636c0efb7a91630ed9743e6fd4d6cac9a6240975af04d413048d762ca1b0da)

@ MGMT\_CB\_OK

No error.

**Definition** callbacks.h:67

[MGMT\_CB\_ERROR\_ERR](group__mcumgr__callback__api.md#gga1ba636c0efb7a91630ed9743e6fd4d6cad88f720a1d62658c346e8bebfb81d66d)

@ MGMT\_CB\_ERROR\_ERR

Group (application-level) error and err\_group contains the group ID that caused the error and err\_rc ...

**Definition** callbacks.h:76

[MGMT\_EVT\_OP\_OS\_MGMT\_DATETIME\_GET](group__mcumgr__callback__api.md#gga261346c700a2522542d8282ca76f88a5a06b0f21e6905a28251f04ec544095a2d)

@ MGMT\_EVT\_OP\_OS\_MGMT\_DATETIME\_GET

Callback when a datetime get command has been received.

**Definition** callbacks.h:221

[MGMT\_EVT\_OP\_OS\_MGMT\_DATETIME\_SET](group__mcumgr__callback__api.md#gga261346c700a2522542d8282ca76f88a5a3cd3ee81f3c691c81a11de2dc6ccf98b)

@ MGMT\_EVT\_OP\_OS\_MGMT\_DATETIME\_SET

Callback when a datetime set command has been received, data is struct rtc\_time().

**Definition** callbacks.h:224

[MGMT\_EVT\_OP\_OS\_MGMT\_INFO\_CHECK](group__mcumgr__callback__api.md#gga261346c700a2522542d8282ca76f88a5a60756021758616ee8d90b5508cb34ba5)

@ MGMT\_EVT\_OP\_OS\_MGMT\_INFO\_CHECK

Callback when an info command is processed, data is os\_mgmt\_info\_check().

**Definition** callbacks.h:215

[MGMT\_EVT\_OP\_OS\_MGMT\_BOOTLOADER\_INFO](group__mcumgr__callback__api.md#gga261346c700a2522542d8282ca76f88a5a683d22d5d17a493a2f0732371dc116bf)

@ MGMT\_EVT\_OP\_OS\_MGMT\_BOOTLOADER\_INFO

Callback when a bootloader info command has been received, data is os\_mgmt\_bootloader\_info\_data().

**Definition** callbacks.h:230

[MGMT\_EVT\_OP\_OS\_MGMT\_RESET](group__mcumgr__callback__api.md#gga261346c700a2522542d8282ca76f88a5a9feea9f8cfcca803a18be03e08583c52)

@ MGMT\_EVT\_OP\_OS\_MGMT\_RESET

Callback when a reset command has been received, data is os\_mgmt\_reset\_data().

**Definition** callbacks.h:212

[MGMT\_EVT\_OP\_OS\_MGMT\_INFO\_APPEND](group__mcumgr__callback__api.md#gga261346c700a2522542d8282ca76f88a5ac931d11c7cc4160a9f93c3f011a26f0f)

@ MGMT\_EVT\_OP\_OS\_MGMT\_INFO\_APPEND

Callback when an info command needs to output data, data is os\_mgmt\_info\_append().

**Definition** callbacks.h:218

[MGMT\_EVT\_OP\_OS\_MGMT\_ALL](group__mcumgr__callback__api.md#gga261346c700a2522542d8282ca76f88a5ae5e0c2779b106a03a675ee2f9b1c389a)

@ MGMT\_EVT\_OP\_OS\_MGMT\_ALL

Used to enable all os\_mgmt\_group events.

**Definition** callbacks.h:233

[MGMT\_EVT\_OP\_FS\_MGMT\_FILE\_ACCESS](group__mcumgr__callback__api.md#gga324223c20cbefe3400272e2789082c79a0475953c86b97afa8e4ed30da3f736d3)

@ MGMT\_EVT\_OP\_FS\_MGMT\_FILE\_ACCESS

Callback when a file has been accessed, data is fs\_mgmt\_file\_access().

**Definition** callbacks.h:157

[MGMT\_EVT\_OP\_FS\_MGMT\_ALL](group__mcumgr__callback__api.md#gga324223c20cbefe3400272e2789082c79a9d0806e3d6f0276930af97370ae23b53)

@ MGMT\_EVT\_OP\_FS\_MGMT\_ALL

Used to enable all fs\_mgmt\_group events.

**Definition** callbacks.h:160

[MGMT\_EVT\_OP\_IMG\_MGMT\_ALL](group__mcumgr__callback__api.md#gga3fa2c42bade08cca1122e32f6315f107a0ba2354ef268ed22c51df7e5708c50bf)

@ MGMT\_EVT\_OP\_IMG\_MGMT\_ALL

Used to enable all img\_mgmt\_group events.

**Definition** callbacks.h:204

[MGMT\_EVT\_OP\_IMG\_MGMT\_DFU\_CHUNK](group__mcumgr__callback__api.md#gga3fa2c42bade08cca1122e32f6315f107a19d53f0c0f6649858e97fbcecfbaf24c)

@ MGMT\_EVT\_OP\_IMG\_MGMT\_DFU\_CHUNK

Callback when a client sends a file upload chunk, data is img\_mgmt\_upload\_check().

**Definition** callbacks.h:168

[MGMT\_EVT\_OP\_IMG\_MGMT\_DFU\_PENDING](group__mcumgr__callback__api.md#gga3fa2c42bade08cca1122e32f6315f107a2ff64450efa47d0d460c866f5634bce4)

@ MGMT\_EVT\_OP\_IMG\_MGMT\_DFU\_PENDING

Callback when a DFU operation has finished being transferred.

**Definition** callbacks.h:177

[MGMT\_EVT\_OP\_IMG\_MGMT\_DFU\_CONFIRMED](group__mcumgr__callback__api.md#gga3fa2c42bade08cca1122e32f6315f107a36e486e194d0d6013d188b4ed70a95fb)

@ MGMT\_EVT\_OP\_IMG\_MGMT\_DFU\_CONFIRMED

Callback when an image has been confirmed.

**Definition** callbacks.h:180

[MGMT\_EVT\_OP\_IMG\_MGMT\_DFU\_CHUNK\_WRITE\_COMPLETE](group__mcumgr__callback__api.md#gga3fa2c42bade08cca1122e32f6315f107a4204cb29c7308f103644162839abcb88)

@ MGMT\_EVT\_OP\_IMG\_MGMT\_DFU\_CHUNK\_WRITE\_COMPLETE

Callback when an image write command has finished writing to flash.

**Definition** callbacks.h:183

[MGMT\_EVT\_OP\_IMG\_MGMT\_IMAGE\_SLOT\_STATE](group__mcumgr__callback__api.md#gga3fa2c42bade08cca1122e32f6315f107a52a1b8f3d4dae7bab74fd6187500acc7)

@ MGMT\_EVT\_OP\_IMG\_MGMT\_IMAGE\_SLOT\_STATE

Callback when an image slot's state is encoded for a response, data is img\_mgmt\_state\_slot\_encode().

**Definition** callbacks.h:189

[MGMT\_EVT\_OP\_IMG\_MGMT\_SLOT\_INFO\_SLOT](group__mcumgr__callback__api.md#gga3fa2c42bade08cca1122e32f6315f107a9e1b6d2ae97ef43edc7ad4749b7ac9b0)

@ MGMT\_EVT\_OP\_IMG\_MGMT\_SLOT\_INFO\_SLOT

Callback when a slot list command outputs fields for a slot of an image, data is img\_mgmt\_slot\_info\_s...

**Definition** callbacks.h:201

[MGMT\_EVT\_OP\_IMG\_MGMT\_SLOT\_INFO\_IMAGE](group__mcumgr__callback__api.md#gga3fa2c42bade08cca1122e32f6315f107acd93051e050127a961843e3a8650fda3)

@ MGMT\_EVT\_OP\_IMG\_MGMT\_SLOT\_INFO\_IMAGE

Callback when a slot list command outputs fields for an image, data is img\_mgmt\_slot\_info\_image().

**Definition** callbacks.h:195

[MGMT\_EVT\_OP\_IMG\_MGMT\_DFU\_STOPPED](group__mcumgr__callback__api.md#gga3fa2c42bade08cca1122e32f6315f107af6424b9e8f800bde22a764da459a50a8)

@ MGMT\_EVT\_OP\_IMG\_MGMT\_DFU\_STOPPED

Callback when a DFU operation is stopped.

**Definition** callbacks.h:171

[MGMT\_EVT\_OP\_IMG\_MGMT\_DFU\_STARTED](group__mcumgr__callback__api.md#gga3fa2c42bade08cca1122e32f6315f107af8836c552e137e15d5e859515f067bbf)

@ MGMT\_EVT\_OP\_IMG\_MGMT\_DFU\_STARTED

Callback when a DFU operation is started.

**Definition** callbacks.h:174

[MGMT\_EVT\_GRP\_ALL](group__mcumgr__callback__api.md#gga40ecf8933112abe76d7fedb3dcc7cdbea0529ffba74faffdc8f0ad33ab3c4786a)

@ MGMT\_EVT\_GRP\_ALL

**Definition** callbacks.h:116

[MGMT\_EVT\_GRP\_SMP](group__mcumgr__callback__api.md#gga40ecf8933112abe76d7fedb3dcc7cdbea18b3bfbd15159108bf60fd8e0569658c)

@ MGMT\_EVT\_GRP\_SMP

**Definition** callbacks.h:117

[MGMT\_EVT\_GRP\_OS](group__mcumgr__callback__api.md#gga40ecf8933112abe76d7fedb3dcc7cdbea34df22b866cd61f81bdc7d743edce2ae)

@ MGMT\_EVT\_GRP\_OS

**Definition** callbacks.h:118

[MGMT\_EVT\_GRP\_SETTINGS](group__mcumgr__callback__api.md#gga40ecf8933112abe76d7fedb3dcc7cdbea541b2a1541ad78bdfb3d26dc314ba536)

@ MGMT\_EVT\_GRP\_SETTINGS

**Definition** callbacks.h:121

[MGMT\_EVT\_GRP\_FS](group__mcumgr__callback__api.md#gga40ecf8933112abe76d7fedb3dcc7cdbea5504e38868b808ea6e46965bf3e6da48)

@ MGMT\_EVT\_GRP\_FS

**Definition** callbacks.h:120

[MGMT\_EVT\_GRP\_USER\_CUSTOM\_START](group__mcumgr__callback__api.md#gga40ecf8933112abe76d7fedb3dcc7cdbea66361c0b52e996d2feb0a7c84532594d)

@ MGMT\_EVT\_GRP\_USER\_CUSTOM\_START

**Definition** callbacks.h:124

[MGMT\_EVT\_GRP\_ENUM](group__mcumgr__callback__api.md#gga40ecf8933112abe76d7fedb3dcc7cdbeac23aa88bc1047404e2d75f7c5de7a6a3)

@ MGMT\_EVT\_GRP\_ENUM

**Definition** callbacks.h:122

[MGMT\_EVT\_GRP\_IMG](group__mcumgr__callback__api.md#gga40ecf8933112abe76d7fedb3dcc7cdbeaf55a2f10814a24eb11660ffe4bb930e1)

@ MGMT\_EVT\_GRP\_IMG

**Definition** callbacks.h:119

[MGMT\_EVT\_OP\_CMD\_RECV](group__mcumgr__callback__api.md#gga590788274b4508c6203685d9e9252184a933f494aa22d52d536bb6c3de0dbeb28)

@ MGMT\_EVT\_OP\_CMD\_RECV

Callback when a command is received, data is mgmt\_evt\_op\_cmd\_arg().

**Definition** callbacks.h:140

[MGMT\_EVT\_OP\_CMD\_ALL](group__mcumgr__callback__api.md#gga590788274b4508c6203685d9e9252184aa447c50326ec3f90c66314e744de0e70)

@ MGMT\_EVT\_OP\_CMD\_ALL

Used to enable all smp\_group events.

**Definition** callbacks.h:149

[MGMT\_EVT\_OP\_CMD\_DONE](group__mcumgr__callback__api.md#gga590788274b4508c6203685d9e9252184adb820d1a8cdea6c74a5a39f096deab12)

@ MGMT\_EVT\_OP\_CMD\_DONE

Callback when a command has been processed, data is mgmt\_evt\_op\_cmd\_arg().

**Definition** callbacks.h:146

[MGMT\_EVT\_OP\_CMD\_STATUS](group__mcumgr__callback__api.md#gga590788274b4508c6203685d9e9252184afc1cee09954cdc6dfaee196dd7518770)

@ MGMT\_EVT\_OP\_CMD\_STATUS

Callback when a status is updated, data is mgmt\_evt\_op\_cmd\_arg().

**Definition** callbacks.h:143

[MGMT\_EVT\_OP\_ENUM\_MGMT\_ALL](group__mcumgr__callback__api.md#gga7ddc4c031948a2fee56fcbdb7d675a1da5f19a62b627e602db48748c91ce2354b)

@ MGMT\_EVT\_OP\_ENUM\_MGMT\_ALL

Used to enable all enum\_mgmt\_group events.

**Definition** callbacks.h:255

[MGMT\_EVT\_OP\_ENUM\_MGMT\_DETAILS](group__mcumgr__callback__api.md#gga7ddc4c031948a2fee56fcbdb7d675a1da749daeaef01327a881f91671b9222abf)

@ MGMT\_EVT\_OP\_ENUM\_MGMT\_DETAILS

Callback when fetching details on supported command groups.

**Definition** callbacks.h:252

[MGMT\_EVT\_OP\_ALL](group__mcumgr__callback__api.md#ggaab6470007be89e5aab88838456f9561aaf9e289ad5f7e0fd8bec581f67951813a)

@ MGMT\_EVT\_OP\_ALL

Used to enable all events.

**Definition** callbacks.h:132

[MGMT\_GROUP\_ID\_PERUSER](group__mcumgr__mgmt__api.md#gga81f98b9a0c3810f7d607b783f8e259b5af2504389290c7b2a3537f4ebfb730726)

@ MGMT\_GROUP\_ID\_PERUSER

User groups defined from 64 onwards.

**Definition** mgmt\_defines.h:84

[sys\_snode\_t](group__single-linked-list__apis.md#ga69bf43aad81e3ee2d55250c59b857493)

struct \_snode sys\_snode\_t

Single-linked list node structure.

**Definition** slist.h:39

[img\_mgmt\_callbacks.h](img__mgmt__callbacks_8h.md)

[inttypes.h](inttypes_8h.md)

[mgmt.h](mgmt_8h.md)

[os\_mgmt\_callbacks.h](os__mgmt__callbacks_8h.md)

[settings\_mgmt\_callbacks.h](settings__mgmt__callbacks_8h.md)

[slist.h](slist_8h.md)

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2)

\_\_INT32\_TYPE\_\_ int32\_t

**Definition** stdint.h:74

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e)

\_\_UINT16\_TYPE\_\_ uint16\_t

**Definition** stdint.h:89

[group](structgroup.md)

Group structure.

**Definition** grp.h:18

[mgmt\_callback](structmgmt__callback.md)

MGMT callback struct.

**Definition** callbacks.h:261

[mgmt\_callback::event\_id](structmgmt__callback.md#a3dc18e5f7e3e00c1c05cc104bb1f3ab1)

uint32\_t event\_id

MGMT\_EVT\_[...] Event ID for handler to be called on.

**Definition** callbacks.h:277

[mgmt\_callback::node](structmgmt__callback.md#a4595cb6a72ebf8b9396e63a8f31c497f)

sys\_snode\_t node

Entry list node.

**Definition** callbacks.h:263

[mgmt\_callback::callback](structmgmt__callback.md#acd79e73a2a3d44697bbda2b401d1e7df)

mgmt\_cb callback

Callback that will be called.

**Definition** callbacks.h:266

[mgmt\_evt\_op\_cmd\_arg](structmgmt__evt__op__cmd__arg.md)

Arguments for MGMT\_EVT\_OP\_CMD\_RECV, MGMT\_EVT\_OP\_CMD\_STATUS and MGMT\_EVT\_OP\_CMD\_DONE.

**Definition** callbacks.h:283

[mgmt\_evt\_op\_cmd\_arg::group](structmgmt__evt__op__cmd__arg.md#a0607126986dc0a1e9a0dae348d278741)

uint16\_t group

mcumgr\_group\_t

**Definition** callbacks.h:285

[mgmt\_evt\_op\_cmd\_arg::status](structmgmt__evt__op__cmd__arg.md#a4d08fca41a60aee6c458d510d528a307)

int status

img\_mgmt\_id\_upload\_t, used in MGMT\_EVT\_OP\_CMD\_STATUS

**Definition** callbacks.h:298

[mgmt\_evt\_op\_cmd\_arg::err](structmgmt__evt__op__cmd__arg.md#a7e7a469f944d27d92e25e42d56fa32d2)

int err

mcumgr\_err\_t, used in MGMT\_EVT\_OP\_CMD\_DONE

**Definition** callbacks.h:295

[mgmt\_evt\_op\_cmd\_arg::id](structmgmt__evt__op__cmd__arg.md#ac461e832ea0997ae19be72df4caf0bb7)

uint8\_t id

Message ID within group.

**Definition** callbacks.h:288

[mgmt\_evt\_op\_cmd\_arg::op](structmgmt__evt__op__cmd__arg.md#acbd58ae2efe86685df33e58450753fe1)

uint8\_t op

mcumgr\_op\_t used in MGMT\_EVT\_OP\_CMD\_RECV

**Definition** callbacks.h:292

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [mgmt](dir_ebeee477af3ac5faaeebf82454c7c7cb.md)
- [mcumgr](dir_9fcc4c99bd235bcb56fa133fdd1138d7.md)
- [mgmt](dir_138c477f5f1e916a824d5e5e3c2b43b2.md)
- [callbacks.h](callbacks_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/doxygen/html/sip__svc__controller_8h_source.html
original_path: doxygen/html/sip__svc__controller_8h_source.html
---

| Logo | Zephyr API Documentation 4.1.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

sip\_svc\_controller.h

[Go to the documentation of this file.](sip__svc__controller_8h.md)

1/\*

2 \* Copyright (c) 2023, Intel Corporation.

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef ZEPHYR\_SIP\_SVC\_CONTROLLER\_H\_

8#define ZEPHYR\_SIP\_SVC\_CONTROLLER\_H\_

9

13

14#ifdef CONFIG\_ARM\_SIP\_SVC\_SUBSYS

15

16#include <[zephyr/sys/atomic.h](sys_2atomic_8h.md)>

17

22#define SIP\_SVC\_SUBSYS\_CONDUIT\_NAME\_LENGTH (4U)

23

27enum open\_state {

28 SIP\_SVC\_OPEN\_UNLOCKED = 0,

29 SIP\_SVC\_OPEN\_LOCKED

30};

31

36struct sip\_svc\_client {

37

38 /\* Client id internal to sip\_svc\*/

39 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) id;

40 /\* Client's token id provided back to client during sip\_svc\_register() \*/

41 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) token;

42 /\* Client's state \*/

43 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90);

44 /\* Total Number of on-going transaction of the client \*/

45 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) active\_trans\_cnt;

46 /\* Private data of each client , Provided during sip\_svc\_register() \*/

47 void \*priv\_data;

48 /\* Transaction id pool for each client \*/

49 struct sip\_svc\_id\_pool \*trans\_idx\_pool;

50};

51

56struct sip\_svc\_controller {

57

58 /\* Initialization status\*/

59 bool init;

60 /\* Total number of clients\*/

61 const [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) num\_clients;

62 /\* Maximum allowable transactions in the system per controller\*/

63 const [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) max\_transactions;

64 /\* Response size of buffer used for ASYNC transaction\*/

65 const [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) resp\_size;

66 /\* Total Number of active transactions \*/

67 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) active\_job\_cnt;

68 /\* Active ASYNC transactions \*/

69 [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) active\_async\_job\_cnt;

70 /\* Supervisory call name , got from dts entry \*/

71 char method[SIP\_SVC\_SUBSYS\_CONDUIT\_NAME\_LENGTH];

72 /\* Pointer to driver instance \*/

73 const struct device \*dev;

74 /\* Pointer to client id pool \*/

75 struct sip\_svc\_id\_pool \*client\_id\_pool;

76 /\* Pointer to database for storing arguments from sip\_svc\_send() \*/

77 struct sip\_svc\_id\_map \*trans\_id\_map;

78 /\* Pointer to client array \*/

79 struct sip\_svc\_client \*clients;

80 /\* Pointer to Buffer used for storing response from lower layers \*/

81 [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*async\_resp\_data;

82 /\* Thread id of sip\_svc thread \*/

83 [k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647) tid;

84

85#if CONFIG\_ARM\_SIP\_SVC\_SUBSYS\_SINGLY\_OPEN

86 /\* Atomic variable to restrict one client access \*/

87 [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) open\_lock;

88#endif

89 /\* Mutex for protecting database access \*/

90 struct k\_mutex data\_mutex;

91 /\* msgq for sending sip\_svc\_request to sip\_svc thread \*/

92 struct k\_msgq req\_msgq;

93 /\* sip\_svc thread object \*/

94 struct k\_thread thread;

95 /\* Stack object of sip\_svc thread \*/

96 [K\_KERNEL\_STACK\_MEMBER](group__thread__stack__api.md#ga600162959def399e70310b944834711f)(stack, CONFIG\_ARM\_SIP\_SVC\_SUBSYS\_THREAD\_STACK\_SIZE);

97};

98

104#define SIP\_SVC\_CONTROLLER\_DEFINE(inst, conduit\_name, sip\_dev, sip\_num\_clients, \

105 sip\_max\_transactions, sip\_resp\_size) \

106 BUILD\_ASSERT( \

107 ((sip\_num\_clients <= CONFIG\_ARM\_SIP\_SVC\_SUBSYS\_MAX\_CLIENT\_COUNT) && \

108 (sip\_num\_clients > 0)), \

109 "Number of client should be within 1 and ARM\_SIP\_SVC\_SUBSYS\_MAX\_CLIENT\_COUNT"); \

110 static STRUCT\_SECTION\_ITERABLE(sip\_svc\_controller, sip\_svc\_##inst) = { \

111 .method = conduit\_name, \

112 .dev = sip\_dev, \

113 .num\_clients = sip\_num\_clients, \

114 .max\_transactions = sip\_max\_transactions, \

115 .resp\_size = sip\_resp\_size, \

116 }

117

118#else

[ 119](sip__svc__controller_8h.md#a5d20a93f779ed0023bd8f993c712632a)#define SIP\_SVC\_CONTROLLER\_DEFINE(inst, conduit\_name, sip\_dev, sip\_num\_clients, \

120 sip\_max\_transactions, sip\_resp\_size)

121#endif

122

123#endif /\* ZEPHYR\_SIP\_SVC\_CONTROLLER\_H\_ \*/

[atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8)

long atomic\_t

**Definition** atomic\_types.h:15

[K\_KERNEL\_STACK\_MEMBER](group__thread__stack__api.md#ga600162959def399e70310b944834711f)

#define K\_KERNEL\_STACK\_MEMBER(sym, size)

Define an embedded stack memory region.

**Definition** thread\_stack.h:279

[k\_tid\_t](kernel_2thread_8h.md#a6379f5a1f19ffbc262a6877c4f6e3647)

struct k\_thread \* k\_tid\_t

**Definition** thread.h:380

[state](parser__state_8h.md#adc6e5733fc3c22f0a7b2914188c49c90)

state

**Definition** parser\_state.h:29

[uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f)

\_\_UINT32\_TYPE\_\_ uint32\_t

**Definition** stdint.h:90

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[atomic.h](sys_2atomic_8h.md)

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [sip\_svc](dir_8cbf67ac7d7b628e7429e25a66b76887.md)
- [sip\_svc\_controller.h](sip__svc__controller_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

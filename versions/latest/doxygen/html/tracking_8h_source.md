---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/tracking_8h_source.html
original_path: doxygen/html/tracking_8h_source.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

tracking.h

[Go to the documentation of this file.](tracking_8h.md)

1/\*

2 \* Copyright (c) 2021 Intel Corporation

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6#ifndef ZEPHYR\_INCLUDE\_TRACING\_TRACKING\_H\_

7#define ZEPHYR\_INCLUDE\_TRACING\_TRACKING\_H\_

8

9#include <[zephyr/kernel.h](include_2zephyr_2kernel_8h.md)>

10#include <[zephyr/kernel\_structs.h](kernel__structs_8h.md)>

11

12#if defined(CONFIG\_TRACING\_OBJECT\_TRACKING) || defined(\_\_DOXYGEN\_\_)

13

36

37extern struct k\_timer \*\_track\_list\_k\_timer;

38extern struct k\_mem\_slab \*\_track\_list\_k\_mem\_slab;

39extern struct k\_sem \*\_track\_list\_k\_sem;

40extern struct [k\_mutex](structk__mutex.md) \*\_track\_list\_k\_mutex;

41extern struct k\_stack \*\_track\_list\_k\_stack;

42extern struct [k\_msgq](structk__msgq.md) \*\_track\_list\_k\_msgq;

43extern struct [k\_mbox](structk__mbox.md) \*\_track\_list\_k\_mbox;

44extern struct [k\_pipe](structk__pipe.md) \*\_track\_list\_k\_pipe;

45extern struct [k\_queue](structk__queue.md) \*\_track\_list\_k\_queue;

46extern struct [k\_event](structk__event.md) \*\_track\_list\_k\_event;

47

[ 53](group__subsys__tracing__object__tracking.md#ga6c7340c07c55f462c00d9bca7fc00a58)#define SYS\_PORT\_TRACK\_NEXT(list)((list)->\_obj\_track\_next)

54

56

57#define sys\_port\_track\_k\_thread\_start(thread)

58#define sys\_port\_track\_k\_thread\_create(new\_thread)

59#define sys\_port\_track\_k\_thread\_sched\_ready(thread)

60#define sys\_port\_track\_k\_thread\_wakeup(thread)

61#define sys\_port\_track\_k\_thread\_sched\_priority\_set(thread, prio)

62#define sys\_port\_track\_k\_work\_delayable\_init(dwork)

63#define sys\_port\_track\_k\_work\_queue\_init(queue)

64#define sys\_port\_track\_k\_work\_init(work)

65#define sys\_port\_track\_k\_mutex\_init(mutex, ret) \

66 sys\_track\_k\_mutex\_init(mutex)

67#define sys\_port\_track\_k\_timer\_stop(timer)

68#define sys\_port\_track\_k\_timer\_start(timer, duration, period)

69#define sys\_port\_track\_k\_timer\_init(timer) \

70 sys\_track\_k\_timer\_init(timer)

71#define sys\_port\_track\_k\_queue\_peek\_tail(queue, ret)

72#define sys\_port\_track\_k\_queue\_peek\_head(queue, ret)

73#define sys\_port\_track\_k\_queue\_cancel\_wait(queue)

74#define sys\_port\_track\_k\_queue\_init(queue) \

75 sys\_track\_k\_queue\_init(queue)

76#define sys\_port\_track\_k\_pipe\_init(pipe) \

77 sys\_track\_k\_pipe\_init(pipe)

78#define sys\_port\_track\_k\_condvar\_init(condvar, ret)

79#define sys\_port\_track\_k\_stack\_init(stack) \

80 sys\_track\_k\_stack\_init(stack)

81#define sys\_port\_track\_k\_thread\_name\_set(thread, ret)

82#define sys\_port\_track\_k\_sem\_reset(sem)

83#define sys\_port\_track\_k\_sem\_init(sem, ret) \

84 sys\_track\_k\_sem\_init(sem)

85#define sys\_port\_track\_k\_msgq\_purge(msgq)

86#define sys\_port\_track\_k\_msgq\_peek(msgq, ret)

87#define sys\_port\_track\_k\_msgq\_init(msgq) \

88 sys\_track\_k\_msgq\_init(msgq)

89#define sys\_port\_track\_k\_mbox\_init(mbox) \

90 sys\_track\_k\_mbox\_init(mbox)

91#define sys\_port\_track\_k\_mem\_slab\_init(slab, rc) \

92 sys\_track\_k\_mem\_slab\_init(slab)

93#define sys\_port\_track\_k\_heap\_free(h)

94#define sys\_port\_track\_k\_heap\_init(h)

95#define sys\_port\_track\_k\_event\_init(event) \

96 sys\_track\_k\_event\_init(event);

97

98void sys\_track\_k\_timer\_init(struct k\_timer \*timer);

99void sys\_track\_k\_mem\_slab\_init(struct k\_mem\_slab \*slab);

100void sys\_track\_k\_sem\_init(struct k\_sem \*sem);

101void sys\_track\_k\_mutex\_init(struct [k\_mutex](structk__mutex.md) \*mutex);

102void sys\_track\_k\_stack\_init(struct k\_stack \*stack);

103void sys\_track\_k\_msgq\_init(struct [k\_msgq](structk__msgq.md) \*msgq);

104void sys\_track\_k\_mbox\_init(struct [k\_mbox](structk__mbox.md) \*mbox);

105void sys\_track\_k\_pipe\_init(struct [k\_pipe](structk__pipe.md) \*pipe);

106void sys\_track\_k\_queue\_init(struct [k\_queue](structk__queue.md) \*queue);

107void sys\_track\_k\_event\_init(struct [k\_event](structk__event.md) \*event);

108

110 /\* end of subsys\_tracing\_object\_tracking \*/

112

113#else

114

115#define sys\_port\_track\_k\_thread\_start(thread)

116#define sys\_port\_track\_k\_thread\_create(new\_thread)

117#define sys\_port\_track\_k\_thread\_sched\_ready(thread)

118#define sys\_port\_track\_k\_thread\_wakeup(thread)

119#define sys\_port\_track\_k\_thread\_sched\_priority\_set(thread, prio)

120#define sys\_port\_track\_k\_work\_delayable\_init(dwork)

121#define sys\_port\_track\_k\_work\_queue\_init(queue)

122#define sys\_port\_track\_k\_work\_init(work)

123#define sys\_port\_track\_k\_mutex\_init(mutex, ret)

124#define sys\_port\_track\_k\_timer\_stop(timer)

125#define sys\_port\_track\_k\_timer\_start(timer, duration, period)

126#define sys\_port\_track\_k\_timer\_init(timer)

127#define sys\_port\_track\_k\_queue\_peek\_tail(queue, ret)

128#define sys\_port\_track\_k\_queue\_peek\_head(queue, ret)

129#define sys\_port\_track\_k\_queue\_cancel\_wait(queue)

130#define sys\_port\_track\_k\_queue\_init(queue)

131#define sys\_port\_track\_k\_pipe\_init(pipe)

132#define sys\_port\_track\_k\_condvar\_init(condvar, ret)

133#define sys\_port\_track\_k\_stack\_init(stack)

134#define sys\_port\_track\_k\_thread\_name\_set(thread, ret)

135#define sys\_port\_track\_k\_sem\_reset(sem)

136#define sys\_port\_track\_k\_sem\_init(sem, ret)

137#define sys\_port\_track\_k\_msgq\_purge(msgq)

138#define sys\_port\_track\_k\_msgq\_peek(msgq, ret)

139#define sys\_port\_track\_k\_msgq\_init(msgq)

140#define sys\_port\_track\_k\_mbox\_init(mbox)

141#define sys\_port\_track\_k\_mem\_slab\_init(slab, rc)

142#define sys\_port\_track\_k\_heap\_free(h)

143#define sys\_port\_track\_k\_heap\_init(h)

144#define sys\_port\_track\_k\_event\_init(event)

145

146#endif

147

148#endif /\* ZEPHYR\_INCLUDE\_TRACING\_TRACKING\_H\_ \*/

[kernel.h](include_2zephyr_2kernel_8h.md)

Public kernel APIs.

[kernel\_structs.h](kernel__structs_8h.md)

[k\_event](structk__event.md)

Event Structure.

**Definition** kernel.h:2207

[k\_mbox](structk__mbox.md)

Mailbox Structure.

**Definition** kernel.h:4716

[k\_msgq](structk__msgq.md)

Message Queue Structure.

**Definition** kernel.h:4402

[k\_mutex](structk__mutex.md)

Mutex Structure.

**Definition** kernel.h:2900

[k\_pipe](structk__pipe.md)

Pipe Structure.

**Definition** kernel.h:4847

[k\_queue](structk__queue.md)

**Definition** kernel.h:1835

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [tracing](dir_c5f5a3ad31e756e37640fc6557a06392.md)
- [tracking.h](tracking_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

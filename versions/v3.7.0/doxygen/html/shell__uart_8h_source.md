---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/doxygen/html/shell__uart_8h_source.html
original_path: doxygen/html/shell__uart_8h_source.html
---

| Logo | Zephyr API Documentation  3.7.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

shell\_uart.h

[Go to the documentation of this file.](shell__uart_8h.md)

1/\*

2 \* Copyright (c) 2018 Nordic Semiconductor ASA

3 \*

4 \* SPDX-License-Identifier: Apache-2.0

5 \*/

6

7#ifndef SHELL\_UART\_H\_\_

8#define SHELL\_UART\_H\_\_

9

10#include <[zephyr/drivers/serial/uart\_async\_rx.h](uart__async__rx_8h.md)>

11#include <[zephyr/mgmt/mcumgr/transport/smp\_shell.h](smp__shell_8h.md)>

12#include <[zephyr/shell/shell.h](shell_2shell_8h.md)>

13

14#ifdef \_\_cplusplus

15extern "C" {

16#endif

17

18extern const struct [shell\_transport\_api](structshell__transport__api.md) [shell\_uart\_transport\_api](shell__uart_8h.md#ab69d50c56e978e985781b8bc03ddd9e1);

19

20#ifndef CONFIG\_SHELL\_BACKEND\_SERIAL\_RX\_RING\_BUFFER\_SIZE

[ 21](shell__uart_8h.md#a88ad87f38e73f4509aece54ee239c317)#define CONFIG\_SHELL\_BACKEND\_SERIAL\_RX\_RING\_BUFFER\_SIZE 0

22#endif

23

24#ifndef CONFIG\_SHELL\_BACKEND\_SERIAL\_TX\_RING\_BUFFER\_SIZE

[ 25](shell__uart_8h.md#a2a3edcda2c2fcabcbcacc1cf33e60279)#define CONFIG\_SHELL\_BACKEND\_SERIAL\_TX\_RING\_BUFFER\_SIZE 0

26#endif

27

28#ifndef CONFIG\_SHELL\_BACKEND\_SERIAL\_ASYNC\_RX\_BUFFER\_COUNT

[ 29](shell__uart_8h.md#a14ed6d5f2c998309503c28d9618f1a1d)#define CONFIG\_SHELL\_BACKEND\_SERIAL\_ASYNC\_RX\_BUFFER\_COUNT 0

30#endif

31

32#ifndef CONFIG\_SHELL\_BACKEND\_SERIAL\_ASYNC\_RX\_BUFFER\_SIZE

[ 33](shell__uart_8h.md#ae358d3286d11a4cbc1c1d9f77dde23b7)#define CONFIG\_SHELL\_BACKEND\_SERIAL\_ASYNC\_RX\_BUFFER\_SIZE 0

34#endif

35

[ 36](shell__uart_8h.md#a4665a2c895ab7f1d51c2a206bbeae24a)#define ASYNC\_RX\_BUF\_SIZE (CONFIG\_SHELL\_BACKEND\_SERIAL\_ASYNC\_RX\_BUFFER\_COUNT \* \

37 (CONFIG\_SHELL\_BACKEND\_SERIAL\_ASYNC\_RX\_BUFFER\_SIZE + \

38 UART\_ASYNC\_RX\_BUF\_OVERHEAD))

39

[ 40](structshell__uart__common.md)struct [shell\_uart\_common](structshell__uart__common.md) {

[ 41](structshell__uart__common.md#aafd4af76bd836a743598239066feb445) const struct [device](structdevice.md) \*[dev](structshell__uart__common.md#aafd4af76bd836a743598239066feb445);

[ 42](structshell__uart__common.md#a3e03f9052e91edcca5d6a9c8887446da) [shell\_transport\_handler\_t](group__shell__api.md#ga265807c2d8eba7b9ea633968627e085d) [handler](structshell__uart__common.md#a3e03f9052e91edcca5d6a9c8887446da);

[ 43](structshell__uart__common.md#a6599ee312e34eaafa71e706df5687e28) void \*[context](structshell__uart__common.md#a6599ee312e34eaafa71e706df5687e28);

[ 44](structshell__uart__common.md#ad166c0c136082334b19b403e2cbaa4a9) bool [blocking\_tx](structshell__uart__common.md#ad166c0c136082334b19b403e2cbaa4a9);

45#ifdef CONFIG\_MCUMGR\_TRANSPORT\_SHELL

46 struct [smp\_shell\_data](structsmp__shell__data.md) smp;

47#endif /\* CONFIG\_MCUMGR\_TRANSPORT\_SHELL \*/

48};

49

[ 50](structshell__uart__int__driven.md)struct [shell\_uart\_int\_driven](structshell__uart__int__driven.md) {

[ 51](structshell__uart__int__driven.md#a524615d1e41ed52429a3f1541f39f977) struct [shell\_uart\_common](structshell__uart__common.md) [common](structshell__uart__int__driven.md#a524615d1e41ed52429a3f1541f39f977);

[ 52](structshell__uart__int__driven.md#a308d6b1f53e1c58a6368e9c11a7fedce) struct [ring\_buf](structring__buf.md) [tx\_ringbuf](structshell__uart__int__driven.md#a308d6b1f53e1c58a6368e9c11a7fedce);

[ 53](structshell__uart__int__driven.md#aa099ed76b8ca37637588609fdfbf469d) struct [ring\_buf](structring__buf.md) [rx\_ringbuf](structshell__uart__int__driven.md#aa099ed76b8ca37637588609fdfbf469d);

[ 54](structshell__uart__int__driven.md#a29fe5ca8668a6db73f5478bad912f37a) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [tx\_buf](structshell__uart__int__driven.md#a29fe5ca8668a6db73f5478bad912f37a)[[CONFIG\_SHELL\_BACKEND\_SERIAL\_TX\_RING\_BUFFER\_SIZE](shell__uart_8h.md#a2a3edcda2c2fcabcbcacc1cf33e60279)];

[ 55](structshell__uart__int__driven.md#aec5209bcb1b41935934f1638f80d676c) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [rx\_buf](structshell__uart__int__driven.md#aec5209bcb1b41935934f1638f80d676c)[[CONFIG\_SHELL\_BACKEND\_SERIAL\_RX\_RING\_BUFFER\_SIZE](shell__uart_8h.md#a88ad87f38e73f4509aece54ee239c317)];

[ 56](structshell__uart__int__driven.md#ad0ca48ecfcc0c333e3854b656b89b3d3) struct k\_timer [dtr\_timer](structshell__uart__int__driven.md#ad0ca48ecfcc0c333e3854b656b89b3d3);

[ 57](structshell__uart__int__driven.md#ad685a823847bdc230071e1898ebf9562) [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) [tx\_busy](structshell__uart__int__driven.md#ad685a823847bdc230071e1898ebf9562);

58};

59

[ 60](structshell__uart__async.md)struct [shell\_uart\_async](structshell__uart__async.md) {

[ 61](structshell__uart__async.md#acb159e579d504b40c574c811c433b307) struct [shell\_uart\_common](structshell__uart__common.md) [common](structshell__uart__async.md#acb159e579d504b40c574c811c433b307);

[ 62](structshell__uart__async.md#a0d6fa4de1d68adafcf2937e2fdb8119e) struct k\_sem [tx\_sem](structshell__uart__async.md#a0d6fa4de1d68adafcf2937e2fdb8119e);

[ 63](structshell__uart__async.md#a2410eaa1860e6f00ed12ceab5927bbed) struct [uart\_async\_rx](structuart__async__rx.md) [async\_rx](structshell__uart__async.md#a2410eaa1860e6f00ed12ceab5927bbed);

[ 64](structshell__uart__async.md#a96f02b1cd55c7ee2edba7277e105c32d) struct [uart\_async\_rx\_config](structuart__async__rx__config.md) [async\_rx\_config](structshell__uart__async.md#a96f02b1cd55c7ee2edba7277e105c32d);

[ 65](structshell__uart__async.md#a2d13bc10a0150623a10a8e76fb61d526) [atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8) [pending\_rx\_req](structshell__uart__async.md#a2d13bc10a0150623a10a8e76fb61d526);

[ 66](structshell__uart__async.md#adca67272c56eaebcc1ddde44bb5ec774) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [rx\_data](structshell__uart__async.md#adca67272c56eaebcc1ddde44bb5ec774)[[ASYNC\_RX\_BUF\_SIZE](shell__uart_8h.md#a4665a2c895ab7f1d51c2a206bbeae24a)];

67};

68

[ 69](structshell__uart__polling.md)struct [shell\_uart\_polling](structshell__uart__polling.md) {

[ 70](structshell__uart__polling.md#af53998508fe666d61327cb5340c76354) struct [shell\_uart\_common](structshell__uart__common.md) [common](structshell__uart__polling.md#af53998508fe666d61327cb5340c76354);

[ 71](structshell__uart__polling.md#ae05061fbe7ea7ea926893c695280698e) struct [ring\_buf](structring__buf.md) [rx\_ringbuf](structshell__uart__polling.md#ae05061fbe7ea7ea926893c695280698e);

[ 72](structshell__uart__polling.md#ad6c0d8d792df20fe2b9f5a1608cd0cfd) [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) [rx\_buf](structshell__uart__polling.md#ad6c0d8d792df20fe2b9f5a1608cd0cfd)[[CONFIG\_SHELL\_BACKEND\_SERIAL\_RX\_RING\_BUFFER\_SIZE](shell__uart_8h.md#a88ad87f38e73f4509aece54ee239c317)];

[ 73](structshell__uart__polling.md#a4cd8ddcbea91c6ee4994fbe5898537ea) struct k\_timer [rx\_timer](structshell__uart__polling.md#a4cd8ddcbea91c6ee4994fbe5898537ea);

74};

75

76#ifdef CONFIG\_SHELL\_BACKEND\_SERIAL\_API\_POLLING

77#define SHELL\_UART\_STRUCT struct shell\_uart\_polling

78#elif defined(CONFIG\_SHELL\_BACKEND\_SERIAL\_API\_ASYNC)

79#define SHELL\_UART\_STRUCT struct shell\_uart\_async

80#else

[ 81](shell__uart_8h.md#a54f2edea6a734fc5f18cb28fa168b4b9)#define SHELL\_UART\_STRUCT struct shell\_uart\_int\_driven

82#endif

83

[ 90](shell__uart_8h.md#a9844dc8d28b8d55529af7718d9f78e12)#define SHELL\_UART\_DEFINE(\_name, ...) \

91 static SHELL\_UART\_STRUCT \_name##\_shell\_uart; \

92 struct shell\_transport \_name = { \

93 .api = &shell\_uart\_transport\_api, \

94 .ctx = (struct shell\_telnet \*)&\_name##\_shell\_uart, \

95 }

96

[ 105](shell__uart_8h.md#a633a97c0298e35127e332df5a9490b0c)const struct [shell](structshell.md) \*[shell\_backend\_uart\_get\_ptr](shell__uart_8h.md#a633a97c0298e35127e332df5a9490b0c)(void);

106

[ 112](shell__uart_8h.md#a1387a797a3940ff66bfba4af9e48e8d6)struct [smp\_shell\_data](structsmp__shell__data.md) \*[shell\_uart\_smp\_shell\_data\_get\_ptr](shell__uart_8h.md#a1387a797a3940ff66bfba4af9e48e8d6)(void);

113

114#ifdef \_\_cplusplus

115}

116#endif

117

118#endif /\* SHELL\_UART\_H\_\_ \*/

[atomic\_t](atomic__types_8h.md#a124f07c3a788e53c3a40e4e1c06d8af8)

long atomic\_t

**Definition** atomic\_types.h:15

[shell\_transport\_handler\_t](group__shell__api.md#ga265807c2d8eba7b9ea633968627e085d)

void(\* shell\_transport\_handler\_t)(enum shell\_transport\_evt evt, void \*context)

**Definition** shell.h:624

[shell.h](shell_2shell_8h.md)

[shell\_uart\_smp\_shell\_data\_get\_ptr](shell__uart_8h.md#a1387a797a3940ff66bfba4af9e48e8d6)

struct smp\_shell\_data \* shell\_uart\_smp\_shell\_data\_get\_ptr(void)

This function provides pointer to the smp shell data of the UART shell transport.

[CONFIG\_SHELL\_BACKEND\_SERIAL\_TX\_RING\_BUFFER\_SIZE](shell__uart_8h.md#a2a3edcda2c2fcabcbcacc1cf33e60279)

#define CONFIG\_SHELL\_BACKEND\_SERIAL\_TX\_RING\_BUFFER\_SIZE

**Definition** shell\_uart.h:25

[ASYNC\_RX\_BUF\_SIZE](shell__uart_8h.md#a4665a2c895ab7f1d51c2a206bbeae24a)

#define ASYNC\_RX\_BUF\_SIZE

**Definition** shell\_uart.h:36

[shell\_backend\_uart\_get\_ptr](shell__uart_8h.md#a633a97c0298e35127e332df5a9490b0c)

const struct shell \* shell\_backend\_uart\_get\_ptr(void)

This function provides pointer to the shell UART backend instance.

[CONFIG\_SHELL\_BACKEND\_SERIAL\_RX\_RING\_BUFFER\_SIZE](shell__uart_8h.md#a88ad87f38e73f4509aece54ee239c317)

#define CONFIG\_SHELL\_BACKEND\_SERIAL\_RX\_RING\_BUFFER\_SIZE

**Definition** shell\_uart.h:21

[shell\_uart\_transport\_api](shell__uart_8h.md#ab69d50c56e978e985781b8bc03ddd9e1)

const struct shell\_transport\_api shell\_uart\_transport\_api

[smp\_shell.h](smp__shell_8h.md)

Shell transport for the mcumgr SMP protocol.

[uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

\_\_UINT8\_TYPE\_\_ uint8\_t

**Definition** stdint.h:88

[device](structdevice.md)

Runtime device structure (in ROM) per driver instance.

**Definition** device.h:403

[ring\_buf](structring__buf.md)

A structure to represent a ring buffer.

**Definition** ring\_buffer.h:41

[shell\_transport\_api](structshell__transport__api.md)

Unified shell transport interface.

**Definition** shell.h:646

[shell\_uart\_async](structshell__uart__async.md)

**Definition** shell\_uart.h:60

[shell\_uart\_async::tx\_sem](structshell__uart__async.md#a0d6fa4de1d68adafcf2937e2fdb8119e)

struct k\_sem tx\_sem

**Definition** shell\_uart.h:62

[shell\_uart\_async::async\_rx](structshell__uart__async.md#a2410eaa1860e6f00ed12ceab5927bbed)

struct uart\_async\_rx async\_rx

**Definition** shell\_uart.h:63

[shell\_uart\_async::pending\_rx\_req](structshell__uart__async.md#a2d13bc10a0150623a10a8e76fb61d526)

atomic\_t pending\_rx\_req

**Definition** shell\_uart.h:65

[shell\_uart\_async::async\_rx\_config](structshell__uart__async.md#a96f02b1cd55c7ee2edba7277e105c32d)

struct uart\_async\_rx\_config async\_rx\_config

**Definition** shell\_uart.h:64

[shell\_uart\_async::common](structshell__uart__async.md#acb159e579d504b40c574c811c433b307)

struct shell\_uart\_common common

**Definition** shell\_uart.h:61

[shell\_uart\_async::rx\_data](structshell__uart__async.md#adca67272c56eaebcc1ddde44bb5ec774)

uint8\_t rx\_data[(0 \*(0+UART\_ASYNC\_RX\_BUF\_OVERHEAD))]

**Definition** shell\_uart.h:66

[shell\_uart\_common](structshell__uart__common.md)

**Definition** shell\_uart.h:40

[shell\_uart\_common::handler](structshell__uart__common.md#a3e03f9052e91edcca5d6a9c8887446da)

shell\_transport\_handler\_t handler

**Definition** shell\_uart.h:42

[shell\_uart\_common::context](structshell__uart__common.md#a6599ee312e34eaafa71e706df5687e28)

void \* context

**Definition** shell\_uart.h:43

[shell\_uart\_common::dev](structshell__uart__common.md#aafd4af76bd836a743598239066feb445)

const struct device \* dev

**Definition** shell\_uart.h:41

[shell\_uart\_common::blocking\_tx](structshell__uart__common.md#ad166c0c136082334b19b403e2cbaa4a9)

bool blocking\_tx

**Definition** shell\_uart.h:44

[shell\_uart\_int\_driven](structshell__uart__int__driven.md)

**Definition** shell\_uart.h:50

[shell\_uart\_int\_driven::tx\_buf](structshell__uart__int__driven.md#a29fe5ca8668a6db73f5478bad912f37a)

uint8\_t tx\_buf[0]

**Definition** shell\_uart.h:54

[shell\_uart\_int\_driven::tx\_ringbuf](structshell__uart__int__driven.md#a308d6b1f53e1c58a6368e9c11a7fedce)

struct ring\_buf tx\_ringbuf

**Definition** shell\_uart.h:52

[shell\_uart\_int\_driven::common](structshell__uart__int__driven.md#a524615d1e41ed52429a3f1541f39f977)

struct shell\_uart\_common common

**Definition** shell\_uart.h:51

[shell\_uart\_int\_driven::rx\_ringbuf](structshell__uart__int__driven.md#aa099ed76b8ca37637588609fdfbf469d)

struct ring\_buf rx\_ringbuf

**Definition** shell\_uart.h:53

[shell\_uart\_int\_driven::dtr\_timer](structshell__uart__int__driven.md#ad0ca48ecfcc0c333e3854b656b89b3d3)

struct k\_timer dtr\_timer

**Definition** shell\_uart.h:56

[shell\_uart\_int\_driven::tx\_busy](structshell__uart__int__driven.md#ad685a823847bdc230071e1898ebf9562)

atomic\_t tx\_busy

**Definition** shell\_uart.h:57

[shell\_uart\_int\_driven::rx\_buf](structshell__uart__int__driven.md#aec5209bcb1b41935934f1638f80d676c)

uint8\_t rx\_buf[0]

**Definition** shell\_uart.h:55

[shell\_uart\_polling](structshell__uart__polling.md)

**Definition** shell\_uart.h:69

[shell\_uart\_polling::rx\_timer](structshell__uart__polling.md#a4cd8ddcbea91c6ee4994fbe5898537ea)

struct k\_timer rx\_timer

**Definition** shell\_uart.h:73

[shell\_uart\_polling::rx\_buf](structshell__uart__polling.md#ad6c0d8d792df20fe2b9f5a1608cd0cfd)

uint8\_t rx\_buf[0]

**Definition** shell\_uart.h:72

[shell\_uart\_polling::rx\_ringbuf](structshell__uart__polling.md#ae05061fbe7ea7ea926893c695280698e)

struct ring\_buf rx\_ringbuf

**Definition** shell\_uart.h:71

[shell\_uart\_polling::common](structshell__uart__polling.md#af53998508fe666d61327cb5340c76354)

struct shell\_uart\_common common

**Definition** shell\_uart.h:70

[shell](structshell.md)

Shell instance internals.

**Definition** shell.h:890

[smp\_shell\_data](structsmp__shell__data.md)

Data used by SMP shell.

**Definition** smp\_shell.h:23

[uart\_async\_rx\_config](structuart__async__rx__config.md)

UART asynchronous RX helper configuration structure.

**Definition** uart\_async\_rx.h:62

[uart\_async\_rx](structuart__async__rx.md)

UART asynchronous RX helper structure.

**Definition** uart\_async\_rx.h:36

[uart\_async\_rx.h](uart__async__rx_8h.md)

Helper module for receiving using UART Asynchronous API.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [shell](dir_a00401f9c4a77a4264f18025172f9ea7.md)
- [shell\_uart.h](shell__uart_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

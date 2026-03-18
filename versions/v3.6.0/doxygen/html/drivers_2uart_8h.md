---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/doxygen/html/drivers_2uart_8h.html
original_path: doxygen/html/drivers_2uart_8h.html
---

| Logo | Zephyr API Documentation  3.6.0  A Scalable Open Source RTOS |
| --- | --- |

Loading...

Searching...

No Matches

uart.h File Reference

Public APIs for UART drivers.
[More...](#details)

`#include <[errno.h](errno_8h_source.md)>`  
`#include <stddef.h>`  
`#include <[zephyr/device.h](device_8h_source.md)>`  
`#include <syscalls/uart.h>`

[Go to the source code of this file.](drivers_2uart_8h_source.md)

| Data Structures | |
| --- | --- |
| struct | [uart\_config](structuart__config.md) |
|  | UART controller configuration structure. [More...](structuart__config.md#details) |
| struct | [uart\_event\_tx](structuart__event__tx.md) |
|  | UART TX event data. [More...](structuart__event__tx.md#details) |
| struct | [uart\_event\_rx](structuart__event__rx.md) |
|  | UART RX event data. [More...](structuart__event__rx.md#details) |
| struct | [uart\_event\_rx\_buf](structuart__event__rx__buf.md) |
|  | UART RX buffer released event data. [More...](structuart__event__rx__buf.md#details) |
| struct | [uart\_event\_rx\_stop](structuart__event__rx__stop.md) |
|  | UART RX stopped data. [More...](structuart__event__rx__stop.md#details) |
| struct | [uart\_event](structuart__event.md) |
|  | Structure containing information about current event. [More...](structuart__event.md#details) |
| union | [uart\_event::uart\_event\_data](unionuart__event_1_1uart__event__data.md) |
|  | Event data. [More...](unionuart__event_1_1uart__event__data.md#details) |

| Typedefs | |
| --- | --- |
| typedef void(\* | [uart\_irq\_callback\_user\_data\_t](group__uart__interrupt.md#gad7a26b1a1d6212d7d39c05c8ad4ec926)) (const struct [device](structdevice.md) \*dev, void \*user\_data) |
|  | Define the application callback function signature for [uart\_irq\_callback\_user\_data\_set()](group__uart__interrupt.md#gaf469966a56d1fc9f50108201597ee0a0 "Set the IRQ callback function pointer.") function. |
| typedef void(\* | [uart\_irq\_config\_func\_t](group__uart__interrupt.md#ga6750414923953c84fb1e19177ec74ae0)) (const struct [device](structdevice.md) \*dev) |
|  | For configuring IRQ on each individual UART device. |
| typedef void(\* | [uart\_callback\_t](group__uart__async.md#ga00b7c98a4da3ea3675d0a40c5dacb136)) (const struct [device](structdevice.md) \*dev, struct [uart\_event](structuart__event.md) \*evt, void \*user\_data) |
|  | Define the application callback function signature for [uart\_callback\_set()](group__uart__async.md#gad33e627ed8729409b14e92453e53459c "Set event handler function.") function. |

| Enumerations | |
| --- | --- |
| enum | [uart\_line\_ctrl](group__uart__interface.md#ga02552532e171e789efc1b000917a9be0) {     [UART\_LINE\_CTRL\_BAUD\_RATE](group__uart__interface.md#gga02552532e171e789efc1b000917a9be0a3fdd02679f4f103190f3c12ab3cda00b) = BIT(0) , [UART\_LINE\_CTRL\_RTS](group__uart__interface.md#gga02552532e171e789efc1b000917a9be0a205d22bd797ab1c55323dc1ffda75f0d) = BIT(1) , [UART\_LINE\_CTRL\_DTR](group__uart__interface.md#gga02552532e171e789efc1b000917a9be0a19e76af9901fc0274a9e27ff40e29e23) = BIT(2) , [UART\_LINE\_CTRL\_DCD](group__uart__interface.md#gga02552532e171e789efc1b000917a9be0a6d2c438044dd64f5cef07bbe4c6b3e97) = BIT(3) ,     [UART\_LINE\_CTRL\_DSR](group__uart__interface.md#gga02552532e171e789efc1b000917a9be0a87d8bedb5c918c182b271884ee42d75c) = BIT(4)   } |
|  | Line control signals. [More...](group__uart__interface.md#ga02552532e171e789efc1b000917a9be0) |
| enum | [uart\_rx\_stop\_reason](group__uart__interface.md#gadeba6c5485e01dfc1c8a6e1c21668a88) {     [UART\_ERROR\_OVERRUN](group__uart__interface.md#ggadeba6c5485e01dfc1c8a6e1c21668a88a442beffc51cdf265bbcb40810a9a6e54) = (1 << 0) , [UART\_ERROR\_PARITY](group__uart__interface.md#ggadeba6c5485e01dfc1c8a6e1c21668a88a86d38eac5a46e6659aa765164b833eb5) = (1 << 1) , [UART\_ERROR\_FRAMING](group__uart__interface.md#ggadeba6c5485e01dfc1c8a6e1c21668a88af13f72a8c615b4bc570b5a4df573407b) = (1 << 2) , [UART\_BREAK](group__uart__interface.md#ggadeba6c5485e01dfc1c8a6e1c21668a88a4986147e23cc46ab8c2aa7e151d09571) = (1 << 3) ,     [UART\_ERROR\_COLLISION](group__uart__interface.md#ggadeba6c5485e01dfc1c8a6e1c21668a88aad8ca4dca9a846560293df71e6b39786) = (1 << 4) , [UART\_ERROR\_NOISE](group__uart__interface.md#ggadeba6c5485e01dfc1c8a6e1c21668a88a412058adbf7668b7051efb8419984d60) = (1 << 5)   } |
|  | Reception stop reasons. [More...](group__uart__interface.md#gadeba6c5485e01dfc1c8a6e1c21668a88) |
| enum | [uart\_config\_parity](group__uart__interface.md#gab2ab6aacb6e3c43bb26d4274157e5711) {     [UART\_CFG\_PARITY\_NONE](group__uart__interface.md#ggab2ab6aacb6e3c43bb26d4274157e5711a6a23a2ef22fb3b144648b244fff82b8d) , [UART\_CFG\_PARITY\_ODD](group__uart__interface.md#ggab2ab6aacb6e3c43bb26d4274157e5711a8a618b0a531c8d62809e39eb56eaf5ed) , [UART\_CFG\_PARITY\_EVEN](group__uart__interface.md#ggab2ab6aacb6e3c43bb26d4274157e5711ac3a4310efe198a1fa7d977a5531486ba) , [UART\_CFG\_PARITY\_MARK](group__uart__interface.md#ggab2ab6aacb6e3c43bb26d4274157e5711a5ee61c29a32447644ff70385158a11ca) ,     [UART\_CFG\_PARITY\_SPACE](group__uart__interface.md#ggab2ab6aacb6e3c43bb26d4274157e5711a8dc5306c8ca26321431bcf22ce9b036c)   } |
|  | Parity modes. [More...](group__uart__interface.md#gab2ab6aacb6e3c43bb26d4274157e5711) |
| enum | [uart\_config\_stop\_bits](group__uart__interface.md#gafc1aecb863e2456d73b78a49fcbad72e) { [UART\_CFG\_STOP\_BITS\_0\_5](group__uart__interface.md#ggafc1aecb863e2456d73b78a49fcbad72ea308c660590a9fd16143806e8bef002af) , [UART\_CFG\_STOP\_BITS\_1](group__uart__interface.md#ggafc1aecb863e2456d73b78a49fcbad72ea73024f1618eb04385bf488214c635e58) , [UART\_CFG\_STOP\_BITS\_1\_5](group__uart__interface.md#ggafc1aecb863e2456d73b78a49fcbad72ea1da47ec95b6a6eee65abef3d6d84f9ad) , [UART\_CFG\_STOP\_BITS\_2](group__uart__interface.md#ggafc1aecb863e2456d73b78a49fcbad72eae180ecebc76516e89669e1d16bfb31c6) } |
|  | Number of stop bits. [More...](group__uart__interface.md#gafc1aecb863e2456d73b78a49fcbad72e) |
| enum | [uart\_config\_data\_bits](group__uart__interface.md#gab9f7de744a68a311330576d7da02c44a) {     [UART\_CFG\_DATA\_BITS\_5](group__uart__interface.md#ggab9f7de744a68a311330576d7da02c44aa1b0545c2d1970e67d697b62510bfbe27) , [UART\_CFG\_DATA\_BITS\_6](group__uart__interface.md#ggab9f7de744a68a311330576d7da02c44aac6e0f3c0479164c34144d0e6e28298e4) , [UART\_CFG\_DATA\_BITS\_7](group__uart__interface.md#ggab9f7de744a68a311330576d7da02c44aa6120eb8f668b257c8c2dd0dc9cf0c913) , [UART\_CFG\_DATA\_BITS\_8](group__uart__interface.md#ggab9f7de744a68a311330576d7da02c44aa23f55bdb24b4016c8c23c518e981df97) ,     [UART\_CFG\_DATA\_BITS\_9](group__uart__interface.md#ggab9f7de744a68a311330576d7da02c44aaf3b601af696d8841fe79871ca3e41e5f)   } |
|  | Number of data bits. [More...](group__uart__interface.md#gab9f7de744a68a311330576d7da02c44a) |
| enum | [uart\_config\_flow\_control](group__uart__interface.md#ga8e2f1b4a8d60d7a6c24835d1b26f99e8) { [UART\_CFG\_FLOW\_CTRL\_NONE](group__uart__interface.md#gga8e2f1b4a8d60d7a6c24835d1b26f99e8a546b28db6f8bfc26266e8f7d6b8ff973) , [UART\_CFG\_FLOW\_CTRL\_RTS\_CTS](group__uart__interface.md#gga8e2f1b4a8d60d7a6c24835d1b26f99e8ad682bfe14a9f0860d1fdc3e8e9d56f86) , [UART\_CFG\_FLOW\_CTRL\_DTR\_DSR](group__uart__interface.md#gga8e2f1b4a8d60d7a6c24835d1b26f99e8a0efc5de86bf80119f750cf372814309f) , [UART\_CFG\_FLOW\_CTRL\_RS485](group__uart__interface.md#gga8e2f1b4a8d60d7a6c24835d1b26f99e8a9675cc80d44e980b66e99bc8548f085c) } |
|  | Hardware flow control options. [More...](group__uart__interface.md#ga8e2f1b4a8d60d7a6c24835d1b26f99e8) |
| enum | [uart\_event\_type](group__uart__async.md#gaf0c9513cbafa36d86b4c83f2b6a03dcd) {     [UART\_TX\_DONE](group__uart__async.md#ggaf0c9513cbafa36d86b4c83f2b6a03dcda4b5cdf863d8b6e5cd7b58f611808a6e4) , [UART\_TX\_ABORTED](group__uart__async.md#ggaf0c9513cbafa36d86b4c83f2b6a03dcda0abcf565ba1011815285bb3845f8d5a1) , [UART\_RX\_RDY](group__uart__async.md#ggaf0c9513cbafa36d86b4c83f2b6a03dcda7c70c3a56f64602f3d808b46e7b047f7) , [UART\_RX\_BUF\_REQUEST](group__uart__async.md#ggaf0c9513cbafa36d86b4c83f2b6a03dcda0d250f372702526f1bce6d4dfe166abe) ,     [UART\_RX\_BUF\_RELEASED](group__uart__async.md#ggaf0c9513cbafa36d86b4c83f2b6a03dcdab2d152bd84f659d4fc4060df29811b48) , [UART\_RX\_DISABLED](group__uart__async.md#ggaf0c9513cbafa36d86b4c83f2b6a03dcdaa8ff5629c002a61bc3bdf5baa2ebc203) , [UART\_RX\_STOPPED](group__uart__async.md#ggaf0c9513cbafa36d86b4c83f2b6a03dcda05b81ddf74d208aeabace6ac90ae52dd)   } |
|  | Types of events passed to callback in UART\_ASYNC\_API. [More...](group__uart__async.md#gaf0c9513cbafa36d86b4c83f2b6a03dcd) |

| Functions | |
| --- | --- |
| int | [uart\_err\_check](group__uart__interface.md#ga22ea20fd8e07153b3b71cc9416f5462f) (const struct [device](structdevice.md) \*dev) |
|  | Check whether an error was detected. |
| int | [uart\_poll\_in](group__uart__polling.md#gae81ac8cc976a20d774cfbda09e9c983d) (const struct [device](structdevice.md) \*dev, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) char \*p\_char) |
|  | Read a character from the device for input. |
| int | [uart\_poll\_in\_u16](group__uart__polling.md#gaad39c1358019bfdcb919da7982743553) (const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*p\_u16) |
|  | Read a 16-bit datum from the device for input. |
| void | [uart\_poll\_out](group__uart__polling.md#ga06ba27ba772a7a18462b8cdbc7f9353c) (const struct [device](structdevice.md) \*dev, [unsigned](lib_2libc_2minimal_2include_2sys_2types_8h.md#a4089fb16419d359081465355db05f846) char out\_char) |
|  | Write a character to the device for output. |
| void | [uart\_poll\_out\_u16](group__uart__polling.md#ga8faa3f58b9098c97e288e9c5f3367fd9) (const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) out\_u16) |
|  | Write a 16-bit datum to the device for output. |
| int | [uart\_configure](group__uart__interface.md#gaa0b75777b879af10543f7e8f463ff9a2) (const struct [device](structdevice.md) \*dev, const struct [uart\_config](structuart__config.md) \*cfg) |
|  | Set UART configuration. |
| int | [uart\_config\_get](group__uart__interface.md#ga81dfc5f2134de8e4acb5f063512cf703) (const struct [device](structdevice.md) \*dev, struct [uart\_config](structuart__config.md) \*cfg) |
|  | Get UART configuration. |
| static int | [uart\_fifo\_fill](group__uart__interrupt.md#gafe42e4719eada7e25904bc9ebfe87791) (const struct [device](structdevice.md) \*dev, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*tx\_data, int size) |
|  | Fill FIFO with data. |
| static int | [uart\_fifo\_fill\_u16](group__uart__interrupt.md#gaa89f58818d8428ad6a11abf692c54c0d) (const struct [device](structdevice.md) \*dev, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*tx\_data, int size) |
|  | Fill FIFO with wide data. |
| static int | [uart\_fifo\_read](group__uart__interrupt.md#gab10942076ac47ecff29e924098049398) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*rx\_data, const int size) |
|  | Read data from FIFO. |
| static int | [uart\_fifo\_read\_u16](group__uart__interrupt.md#ga4a3c25dad2290f1f40e4b847e3b83f64) (const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*rx\_data, const int size) |
|  | Read wide data from FIFO. |
| void | [uart\_irq\_tx\_enable](group__uart__interrupt.md#ga9cbd6e33dce6a5b06233cf10077e19cc) (const struct [device](structdevice.md) \*dev) |
|  | Enable TX interrupt in IER. |
| void | [uart\_irq\_tx\_disable](group__uart__interrupt.md#gaf8a5bc26cd7c32e7bc6516c6f873c45a) (const struct [device](structdevice.md) \*dev) |
|  | Disable TX interrupt in IER. |
| static int | [uart\_irq\_tx\_ready](group__uart__interrupt.md#ga5e126b5f19549eb7f5b785b98ebe7638) (const struct [device](structdevice.md) \*dev) |
|  | Check if UART TX buffer can accept a new char. |
| void | [uart\_irq\_rx\_enable](group__uart__interrupt.md#ga4ec3ae3974da2b3ab94ae7b835d17bad) (const struct [device](structdevice.md) \*dev) |
|  | Enable RX interrupt. |
| void | [uart\_irq\_rx\_disable](group__uart__interrupt.md#gaa759d7935fdd9ab6ca0761f161389a29) (const struct [device](structdevice.md) \*dev) |
|  | Disable RX interrupt. |
| static int | [uart\_irq\_tx\_complete](group__uart__interrupt.md#ga917935a13bf6a5d1e32ef34339e96455) (const struct [device](structdevice.md) \*dev) |
|  | Check if UART TX block finished transmission. |
| static int | [uart\_irq\_rx\_ready](group__uart__interrupt.md#gad04073b1b8e3de13b43ae1194561377b) (const struct [device](structdevice.md) \*dev) |
|  | Check if UART RX buffer has a received char. |
| void | [uart\_irq\_err\_enable](group__uart__interrupt.md#ga7c24daae3326bc2959ea13a2be79969f) (const struct [device](structdevice.md) \*dev) |
|  | Enable error interrupt. |
| void | [uart\_irq\_err\_disable](group__uart__interrupt.md#gaaf8a88361807e204f7227fbd1d0e75b2) (const struct [device](structdevice.md) \*dev) |
|  | Disable error interrupt. |
| int | [uart\_irq\_is\_pending](group__uart__interrupt.md#ga11ccae917c8b5fd76aaabdb047125f6a) (const struct [device](structdevice.md) \*dev) |
|  | Check if any IRQs is pending. |
| int | [uart\_irq\_update](group__uart__interrupt.md#gac5241e000d482c40b2a4856c58c106a6) (const struct [device](structdevice.md) \*dev) |
|  | Start processing interrupts in ISR. |
| static int | [uart\_irq\_callback\_user\_data\_set](group__uart__interrupt.md#gaf469966a56d1fc9f50108201597ee0a0) (const struct [device](structdevice.md) \*dev, [uart\_irq\_callback\_user\_data\_t](group__uart__interrupt.md#gad7a26b1a1d6212d7d39c05c8ad4ec926) cb, void \*user\_data) |
|  | Set the IRQ callback function pointer. |
| static int | [uart\_irq\_callback\_set](group__uart__interrupt.md#ga5f7af3f7f0d9155349ea3b4fad78956c) (const struct [device](structdevice.md) \*dev, [uart\_irq\_callback\_user\_data\_t](group__uart__interrupt.md#gad7a26b1a1d6212d7d39c05c8ad4ec926) cb) |
|  | Set the IRQ callback function pointer (legacy). |
| static int | [uart\_callback\_set](group__uart__async.md#gad33e627ed8729409b14e92453e53459c) (const struct [device](structdevice.md) \*dev, [uart\_callback\_t](group__uart__async.md#ga00b7c98a4da3ea3675d0a40c5dacb136) callback, void \*user\_data) |
|  | Set event handler function. |
| int | [uart\_tx](group__uart__async.md#gaf99f32ce2e2d9beb32a2f2e5a26320dc) (const struct [device](structdevice.md) \*dev, const [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout) |
|  | Send given number of bytes from buffer through UART. |
| int | [uart\_tx\_u16](group__uart__async.md#gab0ea611cd072fa459a6f1780ce62c9e3) (const struct [device](structdevice.md) \*dev, const [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout) |
|  | Send given number of datum from buffer through UART. |
| int | [uart\_tx\_abort](group__uart__async.md#gaa8a26d3ea685fb98030ea03613be6280) (const struct [device](structdevice.md) \*dev) |
|  | Abort current TX transmission. |
| int | [uart\_rx\_enable](group__uart__async.md#ga902e18c2a727ed2988e1b6caa6a444b8) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout) |
|  | Start receiving data through UART. |
| int | [uart\_rx\_enable\_u16](group__uart__async.md#ga12d91846133351a85fa471fa90f2a0fd) (const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len, [int32\_t](stdint_8h.md#a0c18914b3041c2f583aba76f418399c2) timeout) |
|  | Start receiving wide data through UART. |
| static int | [uart\_rx\_buf\_rsp](group__uart__async.md#ga3970fe2818e214b0814ea8b73a816a6a) (const struct [device](structdevice.md) \*dev, [uint8\_t](stdint_8h.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d) \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Provide receive buffer in response to [UART\_RX\_BUF\_REQUEST](group__uart__async.md#ggaf0c9513cbafa36d86b4c83f2b6a03dcda0d250f372702526f1bce6d4dfe166abe "Driver requests next buffer for continuous reception.") event. |
| static int | [uart\_rx\_buf\_rsp\_u16](group__uart__async.md#ga778bcfc30be853c8d320f295b34c17c0) (const struct [device](structdevice.md) \*dev, [uint16\_t](stdint_8h.md#a5debae8b2a1ec20a6694c0c443ee399e) \*buf, [size\_t](retained__mem_8h.md#a36713c339c3c5ec6d6bd481480bdb6f9) len) |
|  | Provide wide data receive buffer in response to [UART\_RX\_BUF\_REQUEST](group__uart__async.md#ggaf0c9513cbafa36d86b4c83f2b6a03dcda0d250f372702526f1bce6d4dfe166abe "Driver requests next buffer for continuous reception.") event. |
| int | [uart\_rx\_disable](group__uart__async.md#gafd4753bee51b230091a3c6ddb26ea734) (const struct [device](structdevice.md) \*dev) |
|  | Disable RX. |
| int | [uart\_line\_ctrl\_set](group__uart__interface.md#gab039414b41145dc8d31349836da91263) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ctrl, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) val) |
|  | Manipulate line control for UART. |
| int | [uart\_line\_ctrl\_get](group__uart__interface.md#gafda8a550284a54c8e1d6b6638de978e5) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) ctrl, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) \*val) |
|  | Retrieve line control for UART. |
| int | [uart\_drv\_cmd](group__uart__interface.md#gaa8683398e5d709b513509d08841ed51b) (const struct [device](structdevice.md) \*dev, [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) [cmd](group__ft8xx__reference__api.md#gacde1ca3945cbe6c828f65051c5c3a615), [uint32\_t](stdint_8h.md#a0a8582351ac627ee8bde2973c825e47f) p) |
|  | Send extra command to driver. |

## Detailed Description

Public APIs for UART drivers.

- [zephyr](dir_6cbb653dcd0745b39bd039f02ad5bff5.md)
- [drivers](dir_49c63ef737d38af1498bd111c90a6556.md)
- [uart.h](drivers_2uart_8h.md)
- Generated on  for Zephyr API Documentation by [![doxygen](doxygen.svg)](https://www.doxygen.org/index.html) 1.16.1

---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/connectivity/bluetooth/api/data_buffer.html
original_path: connectivity/bluetooth/api/data_buffer.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Data Buffers

## API Reference

*group* bt\_buf
:   Data buffers.

    Defines

    BT\_BUF\_RESERVE

    BT\_BUF\_SIZE(size)
    :   Helper to include reserved HCI data in buffer calculations.

    BT\_BUF\_ACL\_SIZE(size)
    :   Helper to calculate needed buffer size for HCI ACL packets.

    BT\_BUF\_EVT\_SIZE(size)
    :   Helper to calculate needed buffer size for HCI Event packets.

    BT\_BUF\_CMD\_SIZE(size)
    :   Helper to calculate needed buffer size for HCI Command packets.

    BT\_BUF\_ISO\_SIZE(size)
    :   Helper to calculate needed buffer size for HCI ISO packets.

    BT\_BUF\_ACL\_RX\_SIZE
    :   Data size needed for HCI ACL RX buffers.

    BT\_BUF\_EVT\_RX\_SIZE
    :   Data size needed for HCI Event RX buffers.

    BT\_BUF\_ISO\_RX\_SIZE

    BT\_BUF\_ISO\_RX\_COUNT

    BT\_BUF\_RX\_SIZE
    :   Data size needed for HCI ACL, HCI ISO or Event RX buffers.

    BT\_BUF\_RX\_COUNT
    :   Buffer count needed for HCI ACL, HCI ISO or Event RX buffers.

    BT\_BUF\_CMD\_TX\_SIZE
    :   Data size needed for HCI Command buffers.

    Enums

    enum bt\_buf\_type
    :   Possible types of buffers passed around the Bluetooth stack.

        *Values:*

        enumerator BT\_BUF\_CMD
        :   HCI command.

        enumerator BT\_BUF\_EVT
        :   HCI event.

        enumerator BT\_BUF\_ACL\_OUT
        :   Outgoing ACL data.

        enumerator BT\_BUF\_ACL\_IN
        :   Incoming ACL data.

        enumerator BT\_BUF\_ISO\_OUT
        :   Outgoing ISO data.

        enumerator BT\_BUF\_ISO\_IN
        :   Incoming ISO data.

        enumerator BT\_BUF\_H4
        :   H:4 data.

    Functions

    struct [net\_buf](../../networking/api/net_buf.md#c.net_buf "net_buf") \*bt\_buf\_get\_rx(enum [bt\_buf\_type](#c.bt_buf_type) type, [k\_timeout\_t](../../../kernel/services/timing/clocks.md#c.k_timeout_t "k_timeout_t") timeout)
    :   Allocate a buffer for incoming data.

        This will set the buffer type so [bt\_buf\_set\_type()](#group__bt__buf_1gaec645aec3d6fb845f214c07f2a864fec) does not need to be explicitly called before [bt\_recv\_prio()](hci_drivers.md#group__bt__hci__driver_1ga19c61df1660d6049ae6b03afe3554fee).

        Parameters:
        :   - **type** – Type of buffer. Only BT\_BUF\_EVT, BT\_BUF\_ACL\_IN and BT\_BUF\_ISO\_IN are allowed.
            - **timeout** – Non-negative waiting period to obtain a buffer or one of the special values K\_NO\_WAIT and K\_FOREVER.

        Returns:
        :   A new buffer.

    struct [net\_buf](../../networking/api/net_buf.md#c.net_buf "net_buf") \*bt\_buf\_get\_tx(enum [bt\_buf\_type](#c.bt_buf_type) type, [k\_timeout\_t](../../../kernel/services/timing/clocks.md#c.k_timeout_t "k_timeout_t") timeout, const void \*data, size\_t size)
    :   Allocate a buffer for outgoing data.

        This will set the buffer type so [bt\_buf\_set\_type()](#group__bt__buf_1gaec645aec3d6fb845f214c07f2a864fec) does not need to be explicitly called before [bt\_send()](hci_raw.md#group__hci__raw_1ga8de934e01eb9a16a3c9d096151e58313).

        Parameters:
        :   - **type** – Type of buffer. Only BT\_BUF\_CMD, BT\_BUF\_ACL\_OUT or BT\_BUF\_H4, when operating on H:4 mode, are allowed.
            - **timeout** – Non-negative waiting period to obtain a buffer or one of the special values K\_NO\_WAIT and K\_FOREVER.
            - **data** – Initial data to append to buffer.
            - **size** – Initial data size.

        Returns:
        :   A new buffer.

    struct [net\_buf](../../networking/api/net_buf.md#c.net_buf "net_buf") \*bt\_buf\_get\_evt(uint8\_t evt, bool discardable, [k\_timeout\_t](../../../kernel/services/timing/clocks.md#c.k_timeout_t "k_timeout_t") timeout)
    :   Allocate a buffer for an HCI Event.

        This will set the buffer type so [bt\_buf\_set\_type()](#group__bt__buf_1gaec645aec3d6fb845f214c07f2a864fec) does not need to be explicitly called before [bt\_recv\_prio()](hci_drivers.md#group__bt__hci__driver_1ga19c61df1660d6049ae6b03afe3554fee) or [bt\_recv()](hci_drivers.md#group__bt__hci__driver_1gaca80bc9dacc4fa44416bd545bd185ef7).

        Parameters:
        :   - **evt** – HCI event code
            - **discardable** – Whether the driver considers the event discardable.
            - **timeout** – Non-negative waiting period to obtain a buffer or one of the special values K\_NO\_WAIT and K\_FOREVER.

        Returns:
        :   A new buffer.

    static inline void bt\_buf\_set\_type(struct [net\_buf](../../networking/api/net_buf.md#c.net_buf "net_buf") \*buf, enum [bt\_buf\_type](#c.bt_buf_type) type)
    :   Set the buffer type.

        Parameters:
        :   - **buf** – Bluetooth buffer
            - **type** – The BT\_\* type to set the buffer to

    static inline enum [bt\_buf\_type](#c.bt_buf_type) bt\_buf\_get\_type(struct [net\_buf](../../networking/api/net_buf.md#c.net_buf "net_buf") \*buf)
    :   Get the buffer type.

        Parameters:
        :   - **buf** – Bluetooth buffer

        Returns:
        :   The BT\_\* type to of the buffer

    struct bt\_buf\_data
    :   *#include <buf.h>*

        This is a base type for bt\_buf user data.

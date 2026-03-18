---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/connectivity/usb/host/api/uhc.html
original_path: connectivity/usb/host/api/uhc.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# USB host controller (UHC) driver API

The USB host controller driver API is described in
[include/zephyr/drivers/usb/uhc.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/drivers/usb/uhc.h) and referred to
as the `UHC driver` API.

UHC driver API is experimental and is subject to change without notice.

## Driver API reference

*group* USB host controller driver API
:   USB host controller (UHC) driver API.

    Defines

    UHC\_STATUS\_INITIALIZED
    :   Controller is initialized by [uhc\_init()](#group__uhc__api_1gabfee9100a18fdf67c5d4f8f99928d530).

    UHC\_STATUS\_ENABLED
    :   Controller is enabled and all API functions are available.

    Typedefs

    typedef int (\*uhc\_event\_cb\_t)(const struct [device](../../../../kernel/drivers/index.md#c.device "device") \*dev, const struct [uhc\_event](#c.uhc_event) \*const event)
    :   Callback to submit UHC event to higher layer.

        At the higher level, the event is to be inserted into a message queue.

        Param dev:
        :   **[in]** Pointer to device struct of the driver instance

        Param event:
        :   **[in]** Point to event structure

        Return:
        :   0 on success, all other values should be treated as error.

    Enums

    enum uhc\_control\_stage
    :   USB control transfer stage.

        *Values:*

        enumerator UHC\_CONTROL\_STAGE\_SETUP = 0

        enumerator UHC\_CONTROL\_STAGE\_DATA

        enumerator UHC\_CONTROL\_STAGE\_STATUS

    enum uhc\_event\_type
    :   USB host controller event types.

        *Values:*

        enumerator UHC\_EVT\_DEV\_CONNECTED\_LS
        :   Low speed device connected.

        enumerator UHC\_EVT\_DEV\_CONNECTED\_FS
        :   Full speed device connected.

        enumerator UHC\_EVT\_DEV\_CONNECTED\_HS
        :   High speed device connected.

        enumerator UHC\_EVT\_DEV\_REMOVED
        :   Device (peripheral) removed.

        enumerator UHC\_EVT\_RESETED
        :   Bus reset operation finished.

        enumerator UHC\_EVT\_SUSPENDED
        :   Bus suspend operation finished.

        enumerator UHC\_EVT\_RESUMED
        :   Bus resume operation finished.

        enumerator UHC\_EVT\_RWUP
        :   Remote wakeup signal.

        enumerator UHC\_EVT\_EP\_REQUEST
        :   Endpoint request result event.

        enumerator UHC\_EVT\_ERROR
        :   Non-correctable error event, requires attention from higher levels or application.

    Functions

    static inline bool uhc\_is\_initialized(const struct [device](../../../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Checks whether the controller is initialized.

        Parameters:
        :   - **dev** – **[in]** Pointer to device struct of the driver instance

        Returns:
        :   true if controller is initialized, false otherwise

    static inline bool uhc\_is\_enabled(const struct [device](../../../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Checks whether the controller is enabled.

        Parameters:
        :   - **dev** – **[in]** Pointer to device struct of the driver instance

        Returns:
        :   true if controller is enabled, false otherwise

    static inline int uhc\_bus\_reset(const struct [device](../../../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Reset USB bus.

        Perform USB bus reset, controller may emit UHC\_EVT\_RESETED at the end of reset signaling.

        Parameters:
        :   - **dev** – **[in]** Pointer to device struct of the driver instance

        Return values:
        :   **-EBUSY** – if the controller is already performing a bus operation

        Returns:
        :   0 on success, all other values should be treated as error.

    static inline int uhc\_sof\_enable(const struct [device](../../../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Enable Start of Frame generator.

        Enable SOF generator.

        Parameters:
        :   - **dev** – **[in]** Pointer to device struct of the driver instance

        Return values:
        :   **-EALREADY** – if already enabled

        Returns:
        :   0 on success, all other values should be treated as error.

    static inline int uhc\_bus\_suspend(const struct [device](../../../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Suspend USB bus.

        Disable SOF generator and emit UHC\_EVT\_SUSPENDED event when USB bus is suspended.

        Parameters:
        :   - **dev** – **[in]** Pointer to device struct of the driver instance

        Return values:
        :   **-EALREADY** – if already suspended

        Returns:
        :   0 on success, all other values should be treated as error.

    static inline int uhc\_bus\_resume(const struct [device](../../../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Resume USB bus.

        Signal resume for at least 20ms, emit UHC\_EVT\_RESUMED at the end of USB bus resume signaling. The SoF generator should subsequently start within 3ms.

        Parameters:
        :   - **dev** – **[in]** Pointer to device struct of the driver instance

        Return values:
        :   **-EBUSY** – if the controller is already performing a bus operation

        Returns:
        :   0 on success, all other values should be treated as error.

    struct [uhc\_transfer](#c.uhc_transfer) \*uhc\_xfer\_alloc(const struct [device](../../../../kernel/drivers/index.md#c.device "device") \*dev, const uint8\_t addr, const uint8\_t ep, const uint8\_t attrib, const uint16\_t mps, const uint16\_t timeout, void \*const udev, void \*const cb)
    :   Allocate UHC transfer.

        Allocate a new transfer from common transfer pool. Transfer has no buffer after allocation, but can be allocated and added from different pools.

        Parameters:
        :   - **dev** – **[in]** Pointer to device struct of the driver instance
            - **addr** – **[in]** Device (peripheral) address
            - **ep** – **[in]** Endpoint address
            - **attrib** – **[in]** Endpoint attributes
            - **mps** – **[in]** Maximum packet size of the endpoint
            - **timeout** – **[in]** Timeout in number of frames
            - **udev** – **[in]** Opaque pointer to USB device
            - **cb** – **[in]** Transfer completion callback

        Returns:
        :   pointer to allocated transfer or NULL on error.

    struct [uhc\_transfer](#c.uhc_transfer) \*uhc\_xfer\_alloc\_with\_buf(const struct [device](../../../../kernel/drivers/index.md#c.device "device") \*dev, const uint8\_t addr, const uint8\_t ep, const uint8\_t attrib, const uint16\_t mps, const uint16\_t timeout, void \*const udev, void \*const cb, size\_t size)
    :   Allocate UHC transfer with buffer.

        Allocate a new transfer from common transfer pool with buffer.

        Parameters:
        :   - **dev** – **[in]** Pointer to device struct of the driver instance
            - **addr** – **[in]** Device (peripheral) address
            - **ep** – **[in]** Endpoint address
            - **attrib** – **[in]** Endpoint attributes
            - **mps** – **[in]** Maximum packet size of the endpoint
            - **timeout** – **[in]** Timeout in number of frames
            - **udev** – **[in]** Opaque pointer to USB device
            - **cb** – **[in]** Transfer completion callback
            - **size** – **[in]** Size of the buffer

        Returns:
        :   pointer to allocated transfer or NULL on error.

    int uhc\_xfer\_free(const struct [device](../../../../kernel/drivers/index.md#c.device "device") \*dev, struct [uhc\_transfer](#c.uhc_transfer) \*const xfer)
    :   Free UHC transfer and any buffers.

        Free any buffers and put the transfer back into the transfer pool.

        Parameters:
        :   - **dev** – **[in]** Pointer to device struct of the driver instance
            - **xfer** – **[in]** Pointer to UHC transfer

        Returns:
        :   0 on success, all other values should be treated as error.

    int uhc\_xfer\_buf\_add(const struct [device](../../../../kernel/drivers/index.md#c.device "device") \*dev, struct [uhc\_transfer](#c.uhc_transfer) \*const xfer, struct [net\_buf](../../../networking/api/net_buf.md#c.net_buf "net_buf") \*buf)
    :   Add UHC transfer buffer.

        Add a previously allocated buffer to the transfer.

        Parameters:
        :   - **dev** – **[in]** Pointer to device struct of the driver instance
            - **xfer** – **[in]** Pointer to UHC transfer
            - **buf** – **[in]** Pointer to UHC request buffer

        Returns:
        :   pointer to allocated request or NULL on error.

    struct [net\_buf](../../../networking/api/net_buf.md#c.net_buf "net_buf") \*uhc\_xfer\_buf\_alloc(const struct [device](../../../../kernel/drivers/index.md#c.device "device") \*dev, const size\_t size)
    :   Allocate UHC transfer buffer.

        Allocate a new buffer from common request buffer pool and assign it to the transfer if the xfer parameter is not NULL.

        Parameters:
        :   - **dev** – **[in]** Pointer to device struct of the driver instance
            - **size** – **[in]** Size of the request buffer

        Returns:
        :   pointer to allocated request or NULL on error.

    void uhc\_xfer\_buf\_free(const struct [device](../../../../kernel/drivers/index.md#c.device "device") \*dev, struct [net\_buf](../../../networking/api/net_buf.md#c.net_buf "net_buf") \*const buf)
    :   Free UHC request buffer.

        Put the buffer back into the request buffer pool.

        Parameters:
        :   - **dev** – **[in]** Pointer to device struct of the driver instance
            - **buf** – **[in]** Pointer to UHC request buffer

    int uhc\_ep\_enqueue(const struct [device](../../../../kernel/drivers/index.md#c.device "device") \*dev, struct [uhc\_transfer](#c.uhc_transfer) \*const xfer)
    :   Queue USB host controller transfer.

        Add transfer to the queue. If the queue is empty, the transfer can be claimed by the controller immediately.

        Parameters:
        :   - **dev** – **[in]** Pointer to device struct of the driver instance
            - **xfer** – **[in]** Pointer to UHC transfer

        Return values:
        :   **-EPERM** – controller is not initialized

        Returns:
        :   0 on success, all other values should be treated as error.

    int uhc\_ep\_dequeue(const struct [device](../../../../kernel/drivers/index.md#c.device "device") \*dev, struct [uhc\_transfer](#c.uhc_transfer) \*const xfer)
    :   Remove a USB host controller transfers from queue.

        Not implemented yet.

        Parameters:
        :   - **dev** – **[in]** Pointer to device struct of the driver instance
            - **xfer** – **[in]** Pointer to UHC transfer

        Return values:
        :   **-EPERM** – controller is not initialized

        Returns:
        :   0 on success, all other values should be treated as error.

    int uhc\_init(const struct [device](../../../../kernel/drivers/index.md#c.device "device") \*dev, [uhc\_event\_cb\_t](#c.uhc_event_cb_t) event\_cb)
    :   Initialize USB host controller.

        Initialize USB host controller.

        Parameters:
        :   - **dev** – **[in]** Pointer to device struct of the driver instance
            - **event\_cb** – **[in]** Event callback from the higher layer (USB host stack)

        Return values:
        :   - **-EINVAL** – on parameter error (no callback is passed)
            - **-EALREADY** – already initialized

        Returns:
        :   0 on success, all other values should be treated as error.

    int uhc\_enable(const struct [device](../../../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Enable USB host controller.

        Enable powered USB host controller and allow host stack to recognize and enumerate devices.

        Parameters:
        :   - **dev** – **[in]** Pointer to device struct of the driver instance

        Return values:
        :   - **-EPERM** – controller is not initialized
            - **-EALREADY** – already enabled

        Returns:
        :   0 on success, all other values should be treated as error.

    int uhc\_disable(const struct [device](../../../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Disable USB host controller.

        Disable enabled USB host controller.

        Parameters:
        :   - **dev** – **[in]** Pointer to device struct of the driver instance

        Return values:
        :   **-EALREADY** – already disabled

        Returns:
        :   0 on success, all other values should be treated as error.

    int uhc\_shutdown(const struct [device](../../../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Poweroff USB host controller.

        Shut down the controller completely to reduce energy consumption or to change the role of the controller.

        Parameters:
        :   - **dev** – **[in]** Pointer to device struct of the driver instance

        Return values:
        :   **-EALREADY** – controller is already uninitialized

        Returns:
        :   0 on success, all other values should be treated as error.

    static inline struct [uhc\_device\_caps](#c.uhc_device_caps) uhc\_caps(const struct [device](../../../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Get USB host controller capabilities.

        Obtain the capabilities of the controller such as high speed (HS), and more.

        Parameters:
        :   - **dev** – **[in]** Pointer to device struct of the driver instance

        Returns:
        :   USB host controller capabilities.

    struct uhc\_transfer
    :   *#include <uhc.h>*

        UHC endpoint buffer info.

        This structure is mandatory for all UHC request. It contains the meta data about the request and FIFOs to store [net\_buf](../../../networking/api/net_buf.md#structnet__buf) structures for each request.

        The members of this structure should not be used directly by a higher layer (host stack).

        Public Members

        [sys\_dnode\_t](../../../../kernel/data_structures/dlist.md#c.sys_dnode_t "sys_dnode_t") node
        :   dlist node

        uint8\_t setup\_pkt[8]
        :   Control transfer setup packet.

        struct [net\_buf](../../../networking/api/net_buf.md#c.net_buf "net_buf") \*buf
        :   Transfer data buffer.

        uint8\_t addr
        :   Device (peripheral) address.

        uint8\_t ep
        :   Endpoint to which request is associated.

        uint8\_t attrib
        :   Endpoint attributes (TBD).

        uint16\_t mps
        :   Maximum packet size.

        uint16\_t timeout
        :   Timeout in number of frames.

        unsigned int queued
        :   Flag marks request buffer is queued.

        unsigned int stage
        :   Control stage status, up to the driver to use it or not.

        void \*udev
        :   Pointer to USB device (opaque for the UHC).

        void \*cb
        :   Pointer to transfer completion callback (opaque for the UHC).

        int err
        :   Transfer result, 0 on success, other values on error.

    struct uhc\_event
    :   *#include <uhc.h>*

        USB host controller event.

        Common structure for all events that originate from the UHC driver and are passed to higher layer using message queue and a callback ([uhc\_event\_cb\_t](#group__uhc__api_1ga3cda056094ceef79dd62ad9c6852daf9)) provided by higher layer during controller initialization (uhc\_init).

        Public Members

        [sys\_snode\_t](../../../../kernel/data_structures/slist.md#c.sys_snode_t "sys_snode_t") node
        :   slist node for the message queue

        enum [uhc\_event\_type](#c.uhc_event_type) type
        :   Event type.

        int status
        :   Event status value, if any.

        struct [uhc\_transfer](#c.uhc_transfer) \*xfer
        :   Pointer to request used only for UHC\_EVT\_EP\_REQUEST.

        const struct [device](../../../../kernel/drivers/index.md#c.device "device") \*dev
        :   Pointer to controller’s device struct.

    struct uhc\_device\_caps
    :   *#include <uhc.h>*

        USB host controller capabilities.

        This structure is mainly intended for the USB host stack.

        Public Members

        uint32\_t hs
        :   USB high speed capable controller.

    struct uhc\_data
    :   *#include <uhc.h>*

        Common UHC driver data structure.

        Mandatory structure for each UHC controller driver. To be implemented as device’s private data (device->data).

        Public Members

        struct [uhc\_device\_caps](#c.uhc_device_caps) caps
        :   Controller capabilities.

        struct [k\_mutex](../../../../kernel/services/synchronization/mutexes.md#c.k_mutex "k_mutex") mutex
        :   Driver access mutex.

        [sys\_dlist\_t](../../../../kernel/data_structures/dlist.md#c.sys_dlist_t "sys_dlist_t") ctrl\_xfers
        :   dlist for control transfers

        [sys\_dlist\_t](../../../../kernel/data_structures/dlist.md#c.sys_dlist_t "sys_dlist_t") bulk\_xfers
        :   dlist for bulk transfers

        [uhc\_event\_cb\_t](#c.uhc_event_cb_t) event\_cb
        :   Callback to submit an UHC event to upper layer.

        atomic\_t status
        :   USB host controller status.

        void \*priv
        :   Driver private data.

---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/connectivity/usb/device_next/api/usbd.html
original_path: connectivity/usb/device_next/api/usbd.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# USB device stack (next) API

New USB device stack API is experimental and is subject to change without notice.

## API reference

Related code samples

[Console over USB CDC ACM](../../../../samples/subsys/usb/console/README.md#usb-cdc-acm-console "Output "Hello World!" to the console over USB CDC ACM.")
:   Output "Hello World!" to the console over USB CDC ACM.

[USB CDC-ACM](../../../../samples/subsys/usb/cdc_acm/README.md#usb-cdc-acm "Use USB CDC-ACM driver to implement a serial port echo.")
:   Use USB CDC-ACM driver to implement a serial port echo.

[USB CDC-ACM composite](../../../../samples/subsys/usb/cdc_acm_composite/README.md#usb-cdc-acm-composite "Implement a composite USB device exposing two serial ports using USB CDC-ACM driver.")
:   Implement a composite USB device exposing two serial ports using USB CDC-ACM driver.

[USB DFU (Device Firmware Upgrade)](../../../../samples/subsys/usb/dfu/README.md#usb-dfu "Implement device firmware upgrade using the USB DFU class driver.")
:   Implement device firmware upgrade using the USB DFU class driver.

[USB HID (Human Interface Device)](../../../../samples/subsys/usb/hid/README.md#usb-hid "Use USB HID driver to enumerate as a raw HID device.")
:   Use USB HID driver to enumerate as a raw HID device.

[USB Mass Storage](../../../../samples/subsys/usb/mass/README.md#usb-mass "Expose board's RAM or FLASH as a USB disk using USB Mass Storage driver.")
:   Expose board's RAM or FLASH as a USB disk using USB Mass Storage driver.

[USB shell](../../../../samples/subsys/usb/shell/README.md#usb-shell "Use shell commands to interact with USB device stack.")
:   Use shell commands to interact with USB device stack.

[WebUSB](../../../../samples/subsys/usb/webusb/README.md#webusb "Receive and echo data from a web page using WebUSB API.")
:   Receive and echo data from a web page using WebUSB API.

*group* usbd\_api
:   New USB device stack core API.

    Defines

    USB\_BSTRING\_LENGTH(s)

    USB\_STRING\_DESCRIPTOR\_LENGTH(s)

    USBD\_NUMOF\_INTERFACES\_MAX

    USBD\_CCTX\_REGISTERED
    :   USB Class instance registered flag.

    USBD\_DEVICE\_DEFINE(device\_name, uhc\_dev, vid, pid)

    USBD\_CONFIGURATION\_DEFINE(name, attrib, power)

    USBD\_DESC\_LANG\_DEFINE(name)
    :   Create a string descriptor node and language string descriptor.

        This macro defines a descriptor node and a string descriptor that, when added to the device context, is automatically used as the language string descriptor zero. Both descriptor node and descriptor are defined with static-storage-class specifier. Default and currently only supported language ID is 0x0409 English (United States). If string descriptors are used, it is necessary to add this descriptor as the first one to the USB device context.

        Parameters:
        :   - **name** – Language string descriptor node identifier.

    USBD\_DESC\_STRING\_DEFINE(d\_name, d\_string, d\_utype)

    USBD\_DESC\_MANUFACTURER\_DEFINE(d\_name, d\_string)
    :   Create a string descriptor node and manufacturer string descriptor.

        This macro defines a descriptor node and a string descriptor that, when added to the device context, is automatically used as the manufacturer string descriptor. Both descriptor node and descriptor are defined with static-storage-class specifier.

        Parameters:
        :   - **d\_name** – String descriptor node identifier.
            - **d\_string** – ASCII7 encoded manufacturer string literal

    USBD\_DESC\_PRODUCT\_DEFINE(d\_name, d\_string)
    :   Create a string descriptor node and product string descriptor.

        This macro defines a descriptor node and a string descriptor that, when added to the device context, is automatically used as the product string descriptor. Both descriptor node and descriptor are defined with static-storage-class specifier.

        Parameters:
        :   - **d\_name** – String descriptor node identifier.
            - **d\_string** – ASCII7 encoded product string literal

    USBD\_DESC\_SERIAL\_NUMBER\_DEFINE(d\_name, d\_string)
    :   Create a string descriptor node and serial number string descriptor.

        This macro defines a descriptor node and a string descriptor that, when added to the device context, is automatically used as the serial number string descriptor. The string literal parameter is used as a placeholder, the unique number is obtained from hwinfo. Both descriptor node and descriptor are defined with static-storage-class specifier.

        Parameters:
        :   - **d\_name** – String descriptor node identifier.
            - **d\_string** – ASCII7 encoded serial number string literal placeholder

    USBD\_DEFINE\_CLASS(class\_name, class\_api, class\_data)

    VENDOR\_REQ\_DEFINE(\_reqs, \_len)
    :   Helper to declare request table of [usbd\_cctx\_vendor\_req](#structusbd__cctx__vendor__req).

        Parameters:
        :   - **\_reqs** – Pointer to the vendor request field
            - **\_len** – Number of supported vendor requests

    USBD\_VENDOR\_REQ(\_reqs...)
    :   Helper to declare supported vendor requests.

        Parameters:
        :   - **\_reqs** – Variable number of vendor requests

    Enums

    enum usbd\_desc\_usage\_type
    :   *Values:*

        enumerator USBD\_DUT\_STRING\_LANG

        enumerator USBD\_DUT\_STRING\_MANUFACTURER

        enumerator USBD\_DUT\_STRING\_PRODUCT

        enumerator USBD\_DUT\_STRING\_SERIAL\_NUMBER

        enumerator USBD\_DUT\_STRING\_INTERFACE

    enum usbd\_ch9\_state
    :   USB device support middle layer runtime state.

        Part of USB device states without suspended and powered states, as it is better to track them separately.

        *Values:*

        enumerator USBD\_STATE\_DEFAULT = 0

        enumerator USBD\_STATE\_ADDRESS

        enumerator USBD\_STATE\_CONFIGURED

    Functions

    int usbd\_add\_descriptor(struct [usbd\_contex](#c.usbd_contex) \*uds\_ctx, struct [usbd\_desc\_node](#c.usbd_desc_node) \*dn)
    :   Add common USB descriptor.

        Add common descriptor like string or bos.

        Parameters:
        :   - **uds\_ctx** – **[in]** Pointer to USB device support context
            - **dn** – **[in]** Pointer to USB descriptor node

        Returns:
        :   0 on success, other values on fail.

    int usbd\_add\_configuration(struct [usbd\_contex](#c.usbd_contex) \*uds\_ctx, struct [usbd\_config\_node](#c.usbd_config_node) \*cd)
    :   Add a USB device configuration.

        Parameters:
        :   - **uds\_ctx** – **[in]** Pointer to USB device support context
            - **cd** – **[in]** Pointer to USB configuration node

        Returns:
        :   0 on success, other values on fail.

    int usbd\_register\_class(struct [usbd\_contex](#c.usbd_contex) \*uds\_ctx, const char \*name, uint8\_t cfg)
    :   Register an USB class instance.

        An USB class implementation can have one or more instances. To identify the instances we use device drivers API. Device names have a prefix derived from the name of the class, for example CDC\_ACM for CDC ACM class instance, and can also be easily identified in the shell. Class instance can only be registered when the USB device stack is disabled. Registered instances are initialized at initialization of the USB device stack, and the interface descriptors of each instance are adapted to the whole context.

        Parameters:
        :   - **uds\_ctx** – **[in]** Pointer to USB device support context
            - **name** – **[in]** Class instance name
            - **cfg** – **[in]** Configuration value (similar to bConfigurationValue)

        Returns:
        :   0 on success, other values on fail.

    int usbd\_unregister\_class(struct [usbd\_contex](#c.usbd_contex) \*uds\_ctx, const char \*name, uint8\_t cfg)
    :   Unregister an USB class instance.

        USB class instance will be removed and will not appear on the next start of the stack. Instance can only be unregistered when the USB device stack is disabled.

        Parameters:
        :   - **uds\_ctx** – **[in]** Pointer to USB device support context
            - **name** – **[in]** Class instance name
            - **cfg** – **[in]** Configuration value (similar to bConfigurationValue)

        Returns:
        :   0 on success, other values on fail.

    int usbd\_init(struct [usbd\_contex](#c.usbd_contex) \*uds\_ctx)
    :   Initialize USB device.

        Initialize USB device descriptors and configuration, initialize USB device controller. Class instances should be registered before they are involved. However, the stack should also initialize without registered instances, even if the host would complain about missing interfaces.

        Parameters:
        :   - **uds\_ctx** – **[in]** Pointer to USB device support context

        Returns:
        :   0 on success, other values on fail.

    int usbd\_enable(struct [usbd\_contex](#c.usbd_contex) \*uds\_ctx)
    :   Enable the USB device support and registered class instances.

        This function enables the USB device support.

        Parameters:
        :   - **uds\_ctx** – **[in]** Pointer to USB device support context

        Returns:
        :   0 on success, other values on fail.

    int usbd\_disable(struct [usbd\_contex](#c.usbd_contex) \*uds\_ctx)
    :   Disable the USB device support.

        This function disables the USB device support.

        Parameters:
        :   - **uds\_ctx** – **[in]** Pointer to USB device support context

        Returns:
        :   0 on success, other values on fail.

    int usbd\_shutdown(struct [usbd\_contex](#c.usbd_contex) \*const uds\_ctx)
    :   Shutdown the USB device support.

        This function completely disables the USB device support.

        Parameters:
        :   - **uds\_ctx** – **[in]** Pointer to USB device support context

        Returns:
        :   0 on success, other values on fail.

    int usbd\_ep\_set\_halt(struct [usbd\_contex](#c.usbd_contex) \*uds\_ctx, uint8\_t ep)
    :   Halt endpoint.

        Parameters:
        :   - **uds\_ctx** – **[in]** Pointer to USB device support context
            - **ep** – **[in]** Endpoint address

        Returns:
        :   0 on success, or error from [udc\_ep\_set\_halt()](udc.md#group__udc__api_1ga19488ec4c93d81592bb5ffccfc1eadc4)

    int usbd\_ep\_clear\_halt(struct [usbd\_contex](#c.usbd_contex) \*uds\_ctx, uint8\_t ep)
    :   Clear endpoint halt.

        Parameters:
        :   - **uds\_ctx** – **[in]** Pointer to USB device support context
            - **ep** – **[in]** Endpoint address

        Returns:
        :   0 on success, or error from [udc\_ep\_clear\_halt()](udc.md#group__udc__api_1gadec9c8af89b28984028fd8e0b1a8c776)

    bool usbd\_ep\_is\_halted(struct [usbd\_contex](#c.usbd_contex) \*uds\_ctx, uint8\_t ep)
    :   Checks whether the endpoint is halted.

        Parameters:
        :   - **uds\_ctx** – **[in]** Pointer to USB device support context
            - **ep** – **[in]** Endpoint address

        Returns:
        :   true if endpoint is halted, false otherwise

    struct [net\_buf](../../../networking/api/net_buf.md#c.net_buf "net_buf") \*usbd\_ep\_ctrl\_buf\_alloc(struct [usbd\_contex](#c.usbd_contex) \*const uds\_ctx, const uint8\_t ep, const size\_t size)
    :   Allocate buffer for USB device control request.

        Allocate a new buffer from controller’s driver buffer pool.

        Parameters:
        :   - **uds\_ctx** – **[in]** Pointer to USB device support context
            - **ep** – **[in]** Endpoint address
            - **size** – **[in]** Size of the request buffer

        Returns:
        :   pointer to allocated request or NULL on error.

    struct [net\_buf](../../../networking/api/net_buf.md#c.net_buf "net_buf") \*usbd\_ep\_buf\_alloc(const struct [usbd\_class\_node](#c.usbd_class_node) \*const c\_nd, const uint8\_t ep, const size\_t size)
    :   Allocate buffer for USB device request.

        Allocate a new buffer from controller’s driver buffer pool.

        Parameters:
        :   - **c\_nd** – **[in]** Pointer to USB device class node
            - **ep** – **[in]** Endpoint address
            - **size** – **[in]** Size of the request buffer

        Returns:
        :   pointer to allocated request or NULL on error.

    int usbd\_ep\_ctrl\_enqueue(struct [usbd\_contex](#c.usbd_contex) \*const uds\_ctx, struct [net\_buf](../../../networking/api/net_buf.md#c.net_buf "net_buf") \*const buf)
    :   Queue USB device control request.

        Add control request to the queue.

        Parameters:
        :   - **uds\_ctx** – **[in]** Pointer to USB device support context
            - **buf** – **[in]** Pointer to UDC request buffer

        Returns:
        :   0 on success, all other values should be treated as error.

    int usbd\_ep\_enqueue(const struct [usbd\_class\_node](#c.usbd_class_node) \*const c\_nd, struct [net\_buf](../../../networking/api/net_buf.md#c.net_buf "net_buf") \*const buf)
    :   Queue USB device request.

        Add request to the queue.

        Parameters:
        :   - **c\_nd** – **[in]** Pointer to USB device class node
            - **buf** – **[in]** Pointer to UDC request buffer

        Returns:
        :   0 on success, or error from [udc\_ep\_enqueue()](udc.md#group__udc__api_1gacb2dc96353f1cffcc3d5e9710133fc0d)

    int usbd\_ep\_dequeue(struct [usbd\_contex](#c.usbd_contex) \*uds\_ctx, const uint8\_t ep)
    :   Remove all USB device controller requests from endpoint queue.

        Parameters:
        :   - **uds\_ctx** – **[in]** Pointer to USB device support context
            - **ep** – **[in]** Endpoint address

        Returns:
        :   0 on success, or error from [udc\_ep\_dequeue()](udc.md#group__udc__api_1ga6e6fb62fb8ebceca7e8e6b590c32efc2)

    int usbd\_ep\_buf\_free(struct [usbd\_contex](#c.usbd_contex) \*uds\_ctx, struct [net\_buf](../../../networking/api/net_buf.md#c.net_buf "net_buf") \*buf)
    :   Free USB device request buffer.

        Put the buffer back into the request buffer pool.

        Parameters:
        :   - **uds\_ctx** – **[in]** Pointer to USB device support context
            - **buf** – **[in]** Pointer to UDC request buffer

        Returns:
        :   0 on success, all other values should be treated as error.

    bool usbd\_is\_suspended(struct [usbd\_contex](#c.usbd_contex) \*uds\_ctx)
    :   Checks whether the USB device controller is suspended.

        Parameters:
        :   - **uds\_ctx** – **[in]** Pointer to USB device support context

        Returns:
        :   true if endpoint is halted, false otherwise

    int usbd\_wakeup\_request(struct [usbd\_contex](#c.usbd_contex) \*uds\_ctx)
    :   Initiate the USB remote wakeup (TBD).

        Returns:
        :   0 on success, other values on fail.

    int usbd\_device\_set\_bcd(struct [usbd\_contex](#c.usbd_contex) \*const uds\_ctx, const uint16\_t bcd)
    :   Set USB device descriptor value bcdUSB.

        Parameters:
        :   - **uds\_ctx** – **[in]** Pointer to USB device support context
            - **bcd** – **[in]** bcdUSB value

        Returns:
        :   0 on success, other values on fail.

    int usbd\_device\_set\_vid(struct [usbd\_contex](#c.usbd_contex) \*const uds\_ctx, const uint16\_t vid)
    :   Set USB device descriptor value idVendor.

        Parameters:
        :   - **uds\_ctx** – **[in]** Pointer to USB device support context
            - **vid** – **[in]** idVendor value

        Returns:
        :   0 on success, other values on fail.

    int usbd\_device\_set\_pid(struct [usbd\_contex](#c.usbd_contex) \*const uds\_ctx, const uint16\_t pid)
    :   Set USB device descriptor value idProduct.

        Parameters:
        :   - **uds\_ctx** – **[in]** Pointer to USB device support context
            - **pid** – **[in]** idProduct value

        Returns:
        :   0 on success, other values on fail.

    int usbd\_device\_set\_code\_triple(struct [usbd\_contex](#c.usbd_contex) \*const uds\_ctx, const uint8\_t base\_class, const uint8\_t subclass, const uint8\_t protocol)
    :   Set USB device descriptor code triple Base Class, SubClass, and Protocol.

        Parameters:
        :   - **uds\_ctx** – **[in]** Pointer to USB device support context
            - **base\_class** – **[in]** bDeviceClass value
            - **subclass** – **[in]** bDeviceSubClass value
            - **protocol** – **[in]** bDeviceProtocol value

        Returns:
        :   0 on success, other values on fail.

    int usbd\_config\_attrib\_rwup(struct [usbd\_contex](#c.usbd_contex) \*const uds\_ctx, const uint8\_t cfg, const bool enable)
    :   Setup USB device configuration attribute Remote Wakeup.

        Parameters:
        :   - **uds\_ctx** – **[in]** Pointer to USB device support context
            - **cfg** – **[in]** Configuration number
            - **enable** – **[in]** Sets attribute if true, clears it otherwise

        Returns:
        :   0 on success, other values on fail.

    int usbd\_config\_attrib\_self(struct [usbd\_contex](#c.usbd_contex) \*const uds\_ctx, const uint8\_t cfg, const bool enable)
    :   Setup USB device configuration attribute Self-powered.

        Parameters:
        :   - **uds\_ctx** – **[in]** Pointer to USB device support context
            - **cfg** – **[in]** Configuration number
            - **enable** – **[in]** Sets attribute if true, clears it otherwise

        Returns:
        :   0 on success, other values on fail.

    int usbd\_config\_maxpower(struct [usbd\_contex](#c.usbd_contex) \*const uds\_ctx, const uint8\_t cfg, const uint8\_t power)
    :   Setup USB device configuration power consumption.

        Parameters:
        :   - **uds\_ctx** – **[in]** Pointer to USB device support context
            - **cfg** – **[in]** Configuration number
            - **power** – **[in]** Maximum power consumption value (bMaxPower)

        Returns:
        :   0 on success, other values on fail.

    struct usbd\_desc\_node
    :   *#include <usbd.h>*

        Descriptor node.

        Descriptor node is used to manage descriptors that are not directly part of a structure, such as string or bos descriptors.

        Public Members

        [sys\_dnode\_t](../../../../kernel/data_structures/dlist.md#c.sys_dnode_t "sys_dnode_t") node
        :   slist node struct

        unsigned int idx
        :   Descriptor index, required for string descriptors.

        unsigned int utype
        :   Descriptor usage type (not bDescriptorType).

        unsigned int utf16le
        :   If not set, string descriptor must be converted to UTF16LE.

        unsigned int custom\_sn
        :   If not set, device stack obtains SN using the hwinfo API.

        void \*desc
        :   Pointer to a descriptor.

    struct usbd\_config\_node
    :   *#include <usbd.h>*

        Device configuration node.

        Configuration node is used to manage device configurations, at least one configuration is required. It does not have an index, instead bConfigurationValue of the descriptor is used for identification.

        Public Members

        [sys\_snode\_t](../../../../kernel/data_structures/slist.md#c.sys_snode_t "sys_snode_t") node
        :   slist node struct

        void \*desc
        :   Pointer to configuration descriptor.

        [sys\_slist\_t](../../../../kernel/data_structures/slist.md#c.sys_slist_t "sys_slist_t") class\_list
        :   List of registered classes (functions).

    struct usbd\_ch9\_data
    :   *#include <usbd.h>*

        USB device support middle layer runtime data.

        Public Members

        struct usb\_setup\_packet setup
        :   Setup packet, up-to-date for the respective control request.

        int ctrl\_type
        :   Control type, internally used for stage verification.

        enum [usbd\_ch9\_state](#c.usbd_ch9_state) state
        :   Protocol state of the USB device stack.

        uint32\_t ep\_halt
        :   Halted endpoints bitmap.

        uint8\_t configuration
        :   USB device stack selected configuration.

        bool post\_status
        :   Post status stage work required, e.g.

            set new device address

        uint8\_t alternate[16U]
        :   Array to track interfaces alternate settings.

    struct usbd\_status
    :   *#include <usbd.h>*

        USB device support status.

        Public Members

        unsigned int initialized
        :   USB device support is initialized.

        unsigned int enabled
        :   USB device support is enabled.

        unsigned int suspended
        :   USB device is suspended.

        unsigned int rwup
        :   USB remote wake-up feature is enabled.

    struct usbd\_contex
    :   *#include <usbd.h>*

        USB device support runtime context.

        Main structure that organizes all descriptors, configuration, and interfaces. An UDC device must be assigned to this structure.

        Public Members

        const char \*name
        :   Name of the USB device.

        struct [k\_mutex](../../../../kernel/services/synchronization/mutexes.md#c.k_mutex "k_mutex") mutex
        :   Access mutex.

        const struct [device](../../../../kernel/drivers/index.md#c.device "device") \*dev
        :   Pointer to UDC device.

        struct [usbd\_ch9\_data](#c.usbd_ch9_data) ch9\_data
        :   Middle layer runtime data.

        [sys\_dlist\_t](../../../../kernel/data_structures/dlist.md#c.sys_dlist_t "sys_dlist_t") descriptors
        :   slist to manage descriptors like string, bos

        [sys\_slist\_t](../../../../kernel/data_structures/slist.md#c.sys_slist_t "sys_slist_t") configs
        :   slist to manage device configurations

        struct [usbd\_status](#c.usbd_status) status
        :   Status of the USB device support.

        void \*desc
        :   Pointer to device descriptor.

    struct usbd\_cctx\_vendor\_req
    :   *#include <usbd.h>*

        Vendor Requests Table.

        Public Members

        const uint8\_t \*reqs
        :   Array of vendor requests supported by the class.

        uint8\_t len
        :   Length of the array.

    struct usbd\_class\_api
    :   *#include <usbd.h>*

        USB device support class instance API.

        Public Members

        void (\*feature\_halt)(struct [usbd\_class\_node](#c.usbd_class_node) \*const node, uint8\_t ep, bool halted)
        :   Feature halt state update handler.

        void (\*update)(struct [usbd\_class\_node](#c.usbd_class_node) \*const node, uint8\_t iface, uint8\_t alternate)
        :   Configuration update handler.

        int (\*control\_to\_dev)(struct [usbd\_class\_node](#c.usbd_class_node) \*const node, const struct usb\_setup\_packet \*const setup, const struct [net\_buf](../../../networking/api/net_buf.md#c.net_buf "net_buf") \*const buf)
        :   USB control request handler to device.

        int (\*control\_to\_host)(struct [usbd\_class\_node](#c.usbd_class_node) \*const node, const struct usb\_setup\_packet \*const setup, struct [net\_buf](../../../networking/api/net_buf.md#c.net_buf "net_buf") \*const buf)
        :   USB control request handler to host.

        int (\*request)(struct [usbd\_class\_node](#c.usbd_class_node) \*const node, struct [net\_buf](../../../networking/api/net_buf.md#c.net_buf "net_buf") \*buf, int err)
        :   Endpoint request completion event handler.

        void (\*suspended)(struct [usbd\_class\_node](#c.usbd_class_node) \*const node)
        :   USB power management handler suspended.

        void (\*resumed)(struct [usbd\_class\_node](#c.usbd_class_node) \*const node)
        :   USB power management handler resumed.

        void (\*sof)(struct [usbd\_class\_node](#c.usbd_class_node) \*const node)
        :   Start of Frame.

        void (\*enable)(struct [usbd\_class\_node](#c.usbd_class_node) \*const node)
        :   Class associated configuration is selected.

        void (\*disable)(struct [usbd\_class\_node](#c.usbd_class_node) \*const node)
        :   Class associated configuration is disabled.

        int (\*init)(struct [usbd\_class\_node](#c.usbd_class_node) \*const node)
        :   Initialization of the class implementation.

        void (\*shutdown)(struct [usbd\_class\_node](#c.usbd_class_node) \*const node)
        :   Shutdown of the class implementation.

    struct usbd\_class\_data
    :   *#include <usbd.h>*

        USB device support class data.

        Public Members

        struct [usbd\_contex](#c.usbd_contex) \*uds\_ctx
        :   Pointer to USB device stack context structure.

        void \*desc
        :   Pointer to a class implementation descriptor that should end with a nil descriptor (bLength = 0 and bDescriptorType = 0).

        const struct [usbd\_cctx\_vendor\_req](#c.usbd_cctx_vendor_req) \*v\_reqs
        :   Supported vendor request table, can be NULL.

        uint32\_t ep\_assigned
        :   Bitmap of all endpoints assigned to the instance.

            The IN endpoints are mapped in the upper halfword.

        uint32\_t ep\_active
        :   Bitmap of the enabled endpoints of the instance.

            The IN endpoints are mapped in the upper halfword.

        uint32\_t iface\_bm
        :   Bitmap of the bInterfaceNumbers of the class instance.

        atomic\_t state
        :   Variable to store the state of the class instance.

        void \*priv
        :   Pointer to private data.

    struct usbd\_class\_node
    :   *#include <usbd.h>*

        Public Members

        [sys\_snode\_t](../../../../kernel/data_structures/slist.md#c.sys_snode_t "sys_snode_t") node
        :   Node information for the slist.

        const char \*name
        :   Name of the USB device class instance.

        const struct [usbd\_class\_api](#c.usbd_class_api) \*api
        :   Pointer to device support class API.

        struct [usbd\_class\_data](#c.usbd_class_data) \*data
        :   Pointer to USB device support class data.

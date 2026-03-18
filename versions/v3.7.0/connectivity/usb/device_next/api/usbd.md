---
version: v3.7.0
source_url: https://docs.zephyrproject.org/3.7.0/connectivity/usb/device_next/api/usbd.html
original_path: connectivity/usb/device_next/api/usbd.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down list at the bottom of the left panel and select the desired version.

# USB device stack (next) API

New USB device stack API is experimental and is subject to change without notice.

## API reference

Related code samples

[Console over USB CDC ACM](../../../../samples/subsys/usb/console/README.md#usb-cdc-acm-console "Output "Hello World!" to the console over USB CDC ACM.")
:   Output "Hello World!" to the console over USB CDC ACM.

[USB Audio asynchronous explicit feedback sample](../../../../samples/subsys/usb/uac2_explicit_feedback/README.md#uac2-explicit-feedback "USB Audio 2 explicit feedback sample playing audio on I2S.")
:   USB Audio 2 explicit feedback sample playing audio on I2S.

[USB CDC-ACM](../../../../samples/subsys/usb/cdc_acm/README.md#usb-cdc-acm "Use USB CDC-ACM driver to implement a serial port echo.")
:   Use USB CDC-ACM driver to implement a serial port echo.

[USB HID keyboard](../../../../samples/subsys/usb/hid-keyboard/README.md#usb-hid-keyboard "Implement a basic HID keyboard device.")
:   Implement a basic HID keyboard device.

[USB Mass Storage](../../../../samples/subsys/usb/mass/README.md#usb-mass "Expose board's RAM or FLASH as a USB disk using USB Mass Storage driver.")
:   Expose board's RAM or FLASH as a USB disk using USB Mass Storage driver.

[USB shell](../../../../samples/subsys/usb/shell/README.md#usb-shell "Use shell commands to interact with USB device stack.")
:   Use shell commands to interact with USB device stack.

*group* USB device core API
:   New USB device stack core API.

    Defines

    USB\_BSTRING\_LENGTH(s)

    USB\_STRING\_DESCRIPTOR\_LENGTH(s)

    USBD\_NUMOF\_INTERFACES\_MAX

    USBD\_CCTX\_REGISTERED
    :   USB Class instance registered flag.

    USBD\_DEVICE\_DEFINE(device\_name, udc\_dev, vid, pid)
    :   Define USB device context structure.

        Macro defines a USB device structure needed by the stack to manage its properties and runtime data. The `vid` and `pid` parameters can also be changed using [usbd\_device\_set\_vid()](#group__usbd__api_1ga06aa9f954b6765e07494753bb4fa42d4) and [usbd\_device\_set\_pid()](#group__usbd__api_1ga44719fc03a50c70d75ce65e1d2f77a04).

        Example of use:

        ```c
        USBD_DEVICE_DEFINE(sample_usbd,
                           DEVICE_DT_GET(DT_NODELABEL(zephyr_udc0)),
                           YOUR_VID, YOUR_PID);
        ```

        Parameters:
        :   - **device\_name** – USB device context name
            - **udc\_dev** – Pointer to UDC device structure
            - **vid** – Vendor ID
            - **pid** – Product ID

    USBD\_CONFIGURATION\_DEFINE(name, attrib, power)
    :   Define USB device configuration.

        USB device requires at least one configuration instance per supported speed. `attrib` is a combination of `USB_SCD_SELF_POWERED` or `USB_SCD_REMOTE_WAKEUP`, depending on which characteristic the USB device should have in this configuration.

        Parameters:
        :   - **name** – Configuration name
            - **attrib** – Configuration characteristics. Attributes can also be updated with [usbd\_config\_attrib\_rwup()](#group__usbd__api_1ga2b803f8ac10d9375a74949cd2c2f3136) and [usbd\_config\_attrib\_self()](#group__usbd__api_1ga8b0fff68bc6ce9d8ec4a7dfd59f0eade)
            - **power** – bMaxPower value in 2 mA units. This value can also be set with [usbd\_config\_maxpower()](#group__usbd__api_1ga59fc1ea6d943d26b0207bb6060e18f08)

    USBD\_DESC\_LANG\_DEFINE(name)
    :   Create a string descriptor node and language string descriptor.

        This macro defines a descriptor node and a string descriptor that, when added to the device context, is automatically used as the language string descriptor zero. Both descriptor node and descriptor are defined with static-storage-class specifier. Default and currently only supported language ID is 0x0409 English (United States). If string descriptors are used, it is necessary to add this descriptor as the first one to the USB device context.

        Parameters:
        :   - **name** – Language string descriptor node identifier.

    USBD\_DESC\_STRING\_DEFINE(d\_name, d\_string, d\_utype)
    :   Create a string descriptor.

        This macro defines a descriptor node and a string descriptor. The string literal passed to the macro should be in the ASCII7 format. It is converted to UTF16LE format on the host request.

        Parameters:
        :   - **d\_name** – Internal string descriptor node identifier name
            - **d\_string** – ASCII7 encoded string literal
            - **d\_utype** – String descriptor usage type

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

    USBD\_DESC\_SERIAL\_NUMBER\_DEFINE(d\_name)
    :   Create a string descriptor node and serial number string descriptor.

        This macro defines a descriptor node that, when added to the device context, is automatically used as the serial number string descriptor. A valid serial number is generated from HWID (HWINFO= whenever this string descriptor is requested.

        Parameters:
        :   - **d\_name** – String descriptor node identifier.

    USBD\_DESC\_BOS\_DEFINE(name, len, subset)
    :   Define BOS Device Capability descriptor node.

        The application defines a BOS capability descriptor node for descriptors such as USB 2.0 Extension Descriptor.

        Parameters:
        :   - **name** – Descriptor node identifier
            - **len** – Device Capability descriptor length
            - **subset** – Pointer to a Device Capability descriptor

    USBD\_DEFINE\_CLASS(class\_name, class\_api, class\_priv, class\_v\_reqs)
    :   Define USB device support class data.

        Macro defines class (function) data, as well as corresponding node structures used internally by the stack.

        Parameters:
        :   - **class\_name** – Class name
            - **class\_api** – Pointer to struct [usbd\_class\_api](#structusbd__class__api)
            - **class\_priv** – Class private data
            - **class\_v\_reqs** – Pointer to struct [usbd\_cctx\_vendor\_req](#structusbd__cctx__vendor__req)

    VENDOR\_REQ\_DEFINE(\_reqs, \_len)
    :   Helper to declare request table of [usbd\_cctx\_vendor\_req](#structusbd__cctx__vendor__req).

        Parameters:
        :   - **\_reqs** – Pointer to the vendor request field
            - **\_len** – Number of supported vendor requests

    USBD\_VENDOR\_REQ(\_reqs...)
    :   Helper to declare supported vendor requests.

        Parameters:
        :   - **\_reqs** – Variable number of vendor requests

    Typedefs

    typedef void (\*usbd\_msg\_cb\_t)(struct [usbd\_context](#c.usbd_context) \*const ctx, const struct [usbd\_msg](#c.usbd_msg) \*const msg)
    :   Callback type definition for USB device message delivery.

        The implementation uses the system workqueue, and a callback provided and registered by the application. The application callback is called in the context of the system workqueue. Notification messages are stored in a queue and delivered to the callback in sequence.

        Param ctx:
        :   **[in]** Pointer to USB device support context

        Param msg:
        :   **[in]** Pointer to USB device message

    Enums

    enum usbd\_ch9\_state
    :   USB device support middle layer runtime state.

        Part of USB device states without suspended and powered states, as it is better to track them separately.

        *Values:*

        enumerator USBD\_STATE\_DEFAULT = 0

        enumerator USBD\_STATE\_ADDRESS

        enumerator USBD\_STATE\_CONFIGURED

    enum usbd\_speed
    :   USB device speed.

        *Values:*

        enumerator USBD\_SPEED\_FS
        :   Device supports or is connected to a full speed bus.

        enumerator USBD\_SPEED\_HS
        :   Device supports or is connected to a high speed bus.

        enumerator USBD\_SPEED\_SS
        :   Device supports or is connected to a super speed bus.

    Functions

    static inline struct [usbd\_context](#c.usbd_context) \*usbd\_class\_get\_ctx(const struct [usbd\_class\_data](#c.usbd_class_data) \*const c\_data)
    :   Get the USB device runtime context under which the class is registered.

        The class implementation must use this function and not access the members of the struct directly.

        Parameters:
        :   - **c\_data** – **[in]** Pointer to USB device class data

        Returns:
        :   Pointer to USB device runtime context

    static inline void \*usbd\_class\_get\_private(const struct [usbd\_class\_data](#c.usbd_class_data) \*const c\_data)
    :   Get class implementation private data.

        The class implementation must use this function and not access the members of the struct directly.

        Parameters:
        :   - **c\_data** – **[in]** Pointer to USB device class data

        Returns:
        :   Pointer to class implementation private data

    int usbd\_add\_descriptor(struct [usbd\_context](#c.usbd_context) \*uds\_ctx, struct [usbd\_desc\_node](#c.usbd_desc_node) \*dn)
    :   Add common USB descriptor.

        Add common descriptor like string or BOS Device Capability.

        Parameters:
        :   - **uds\_ctx** – **[in]** Pointer to USB device support context
            - **dn** – **[in]** Pointer to USB descriptor node

        Returns:
        :   0 on success, other values on fail.

    uint8\_t usbd\_str\_desc\_get\_idx(const struct [usbd\_desc\_node](#c.usbd_desc_node) \*const desc\_nd)
    :   Get USB string descriptor index from descriptor node.

        Parameters:
        :   - **desc\_nd** – **[in]** Pointer to USB descriptor node

        Returns:
        :   Descriptor index, 0 if descriptor is not part of any device

    void usbd\_remove\_descriptor(struct [usbd\_desc\_node](#c.usbd_desc_node) \*const desc\_nd)
    :   Remove USB string descriptor.

        Remove linked USB string descriptor from any list.

        Parameters:
        :   - **desc\_nd** – **[in]** Pointer to USB descriptor node

    int usbd\_add\_configuration(struct [usbd\_context](#c.usbd_context) \*uds\_ctx, const enum [usbd\_speed](#c.usbd_speed) speed, struct [usbd\_config\_node](#c.usbd_config_node) \*cd)
    :   Add a USB device configuration.

        Parameters:
        :   - **uds\_ctx** – **[in]** Pointer to USB device support context
            - **speed** – **[in]** Speed at which this configuration operates
            - **cd** – **[in]** Pointer to USB configuration node

        Returns:
        :   0 on success, other values on fail.

    int usbd\_register\_class(struct [usbd\_context](#c.usbd_context) \*uds\_ctx, const char \*name, const enum [usbd\_speed](#c.usbd_speed) speed, uint8\_t cfg)
    :   Register an USB class instance.

        An USB class implementation can have one or more instances. To identify the instances we use device drivers API. Device names have a prefix derived from the name of the class, for example CDC\_ACM for CDC ACM class instance, and can also be easily identified in the shell. Class instance can only be registered when the USB device stack is disabled. Registered instances are initialized at initialization of the USB device stack, and the interface descriptors of each instance are adapted to the whole context.

        Parameters:
        :   - **uds\_ctx** – **[in]** Pointer to USB device support context
            - **name** – **[in]** Class instance name
            - **speed** – **[in]** Configuration speed
            - **cfg** – **[in]** Configuration value (bConfigurationValue)

        Returns:
        :   0 on success, other values on fail.

    int usbd\_register\_all\_classes(struct [usbd\_context](#c.usbd_context) \*uds\_ctx, const enum [usbd\_speed](#c.usbd_speed) speed, uint8\_t cfg)
    :   Register all available USB class instances.

        Register all available instances. Like usbd\_register\_class, but does not take the instance name and instead registers all available instances.

        Note

        This cannot be combined. If your application calls usbd\_register\_class for any device, configuration number, or instance, either usbd\_register\_class or this function will fail.

        Parameters:
        :   - **uds\_ctx** – **[in]** Pointer to USB device support context
            - **speed** – **[in]** Configuration speed
            - **cfg** – **[in]** Configuration value (bConfigurationValue)

        Returns:
        :   0 on success, other values on fail.

    int usbd\_unregister\_class(struct [usbd\_context](#c.usbd_context) \*uds\_ctx, const char \*name, const enum [usbd\_speed](#c.usbd_speed) speed, uint8\_t cfg)
    :   Unregister an USB class instance.

        USB class instance will be removed and will not appear on the next start of the stack. Instance can only be unregistered when the USB device stack is disabled.

        Parameters:
        :   - **uds\_ctx** – **[in]** Pointer to USB device support context
            - **name** – **[in]** Class instance name
            - **speed** – **[in]** Configuration speed
            - **cfg** – **[in]** Configuration value (bConfigurationValue)

        Returns:
        :   0 on success, other values on fail.

    int usbd\_unregister\_all\_classes(struct [usbd\_context](#c.usbd_context) \*uds\_ctx, const enum [usbd\_speed](#c.usbd_speed) speed, uint8\_t cfg)
    :   Unregister all available USB class instances.

        Unregister all available instances. Like usbd\_unregister\_class, but does not take the instance name and instead unregisters all available instances.

        Parameters:
        :   - **uds\_ctx** – **[in]** Pointer to USB device support context
            - **speed** – **[in]** Configuration speed
            - **cfg** – **[in]** Configuration value (bConfigurationValue)

        Returns:
        :   0 on success, other values on fail.

    int usbd\_msg\_register\_cb(struct [usbd\_context](#c.usbd_context) \*const uds\_ctx, const [usbd\_msg\_cb\_t](#c.usbd_msg_cb_t) cb)
    :   Register USB notification message callback.

        Parameters:
        :   - **uds\_ctx** – **[in]** Pointer to USB device support context
            - **cb** – **[in]** Pointer to message callback function

        Returns:
        :   0 on success, other values on fail.

    int usbd\_init(struct [usbd\_context](#c.usbd_context) \*uds\_ctx)
    :   Initialize USB device.

        Initialize USB device descriptors and configuration, initialize USB device controller. Class instances should be registered before they are involved. However, the stack should also initialize without registered instances, even if the host would complain about missing interfaces.

        Parameters:
        :   - **uds\_ctx** – **[in]** Pointer to USB device support context

        Returns:
        :   0 on success, other values on fail.

    int usbd\_enable(struct [usbd\_context](#c.usbd_context) \*uds\_ctx)
    :   Enable the USB device support and registered class instances.

        This function enables the USB device support.

        Parameters:
        :   - **uds\_ctx** – **[in]** Pointer to USB device support context

        Returns:
        :   0 on success, other values on fail.

    int usbd\_disable(struct [usbd\_context](#c.usbd_context) \*uds\_ctx)
    :   Disable the USB device support.

        This function disables the USB device support.

        Parameters:
        :   - **uds\_ctx** – **[in]** Pointer to USB device support context

        Returns:
        :   0 on success, other values on fail.

    int usbd\_shutdown(struct [usbd\_context](#c.usbd_context) \*const uds\_ctx)
    :   Shutdown the USB device support.

        This function completely disables the USB device support.

        Parameters:
        :   - **uds\_ctx** – **[in]** Pointer to USB device support context

        Returns:
        :   0 on success, other values on fail.

    int usbd\_ep\_set\_halt(struct [usbd\_context](#c.usbd_context) \*uds\_ctx, uint8\_t ep)
    :   Halt endpoint.

        Parameters:
        :   - **uds\_ctx** – **[in]** Pointer to USB device support context
            - **ep** – **[in]** Endpoint address

        Returns:
        :   0 on success, or error from [udc\_ep\_set\_halt()](udc.md#group__udc__api_1ga19488ec4c93d81592bb5ffccfc1eadc4)

    int usbd\_ep\_clear\_halt(struct [usbd\_context](#c.usbd_context) \*uds\_ctx, uint8\_t ep)
    :   Clear endpoint halt.

        Parameters:
        :   - **uds\_ctx** – **[in]** Pointer to USB device support context
            - **ep** – **[in]** Endpoint address

        Returns:
        :   0 on success, or error from [udc\_ep\_clear\_halt()](udc.md#group__udc__api_1gadec9c8af89b28984028fd8e0b1a8c776)

    bool usbd\_ep\_is\_halted(struct [usbd\_context](#c.usbd_context) \*uds\_ctx, uint8\_t ep)
    :   Checks whether the endpoint is halted.

        Parameters:
        :   - **uds\_ctx** – **[in]** Pointer to USB device support context
            - **ep** – **[in]** Endpoint address

        Returns:
        :   true if endpoint is halted, false otherwise

    struct [net\_buf](../../../networking/api/net_buf.md#c.net_buf "net_buf") \*usbd\_ep\_buf\_alloc(const struct [usbd\_class\_data](#c.usbd_class_data) \*const c\_data, const uint8\_t ep, const size\_t size)
    :   Allocate buffer for USB device request.

        Allocate a new buffer from controller’s driver buffer pool.

        Parameters:
        :   - **c\_data** – **[in]** Pointer to USB device class data
            - **ep** – **[in]** Endpoint address
            - **size** – **[in]** Size of the request buffer

        Returns:
        :   pointer to allocated request or NULL on error.

    int usbd\_ep\_ctrl\_enqueue(struct [usbd\_context](#c.usbd_context) \*const uds\_ctx, struct [net\_buf](../../../networking/api/net_buf.md#c.net_buf "net_buf") \*const buf)
    :   Queue USB device control request.

        Add control request to the queue.

        Parameters:
        :   - **uds\_ctx** – **[in]** Pointer to USB device support context
            - **buf** – **[in]** Pointer to UDC request buffer

        Returns:
        :   0 on success, all other values should be treated as error.

    int usbd\_ep\_enqueue(const struct [usbd\_class\_data](#c.usbd_class_data) \*const c\_data, struct [net\_buf](../../../networking/api/net_buf.md#c.net_buf "net_buf") \*const buf)
    :   Queue USB device request.

        Add request to the queue.

        Parameters:
        :   - **c\_data** – **[in]** Pointer to USB device class data
            - **buf** – **[in]** Pointer to UDC request buffer

        Returns:
        :   0 on success, or error from [udc\_ep\_enqueue()](udc.md#group__udc__api_1gacb2dc96353f1cffcc3d5e9710133fc0d)

    int usbd\_ep\_dequeue(struct [usbd\_context](#c.usbd_context) \*uds\_ctx, const uint8\_t ep)
    :   Remove all USB device controller requests from endpoint queue.

        Parameters:
        :   - **uds\_ctx** – **[in]** Pointer to USB device support context
            - **ep** – **[in]** Endpoint address

        Returns:
        :   0 on success, or error from [udc\_ep\_dequeue()](udc.md#group__udc__api_1ga6e6fb62fb8ebceca7e8e6b590c32efc2)

    int usbd\_ep\_buf\_free(struct [usbd\_context](#c.usbd_context) \*uds\_ctx, struct [net\_buf](../../../networking/api/net_buf.md#c.net_buf "net_buf") \*buf)
    :   Free USB device request buffer.

        Put the buffer back into the request buffer pool.

        Parameters:
        :   - **uds\_ctx** – **[in]** Pointer to USB device support context
            - **buf** – **[in]** Pointer to UDC request buffer

        Returns:
        :   0 on success, all other values should be treated as error.

    bool usbd\_is\_suspended(struct [usbd\_context](#c.usbd_context) \*uds\_ctx)
    :   Checks whether the USB device controller is suspended.

        Parameters:
        :   - **uds\_ctx** – **[in]** Pointer to USB device support context

        Returns:
        :   true if endpoint is halted, false otherwise

    int usbd\_wakeup\_request(struct [usbd\_context](#c.usbd_context) \*uds\_ctx)
    :   Initiate the USB remote wakeup (TBD).

        Returns:
        :   0 on success, other values on fail.

    enum [usbd\_speed](#c.usbd_speed) usbd\_bus\_speed(const struct [usbd\_context](#c.usbd_context) \*const uds\_ctx)
    :   Get actual device speed.

        Parameters:
        :   - **uds\_ctx** – **[in]** Pointer to a device context

        Returns:
        :   Actual device speed

    enum [usbd\_speed](#c.usbd_speed) usbd\_caps\_speed(const struct [usbd\_context](#c.usbd_context) \*const uds\_ctx)
    :   Get highest speed supported by the controller.

        Parameters:
        :   - **uds\_ctx** – **[in]** Pointer to a device context

        Returns:
        :   Highest supported speed

    int usbd\_device\_set\_bcd(struct [usbd\_context](#c.usbd_context) \*const uds\_ctx, const enum [usbd\_speed](#c.usbd_speed) speed, const uint16\_t bcd)
    :   Set USB device descriptor value bcdUSB.

        Parameters:
        :   - **uds\_ctx** – **[in]** Pointer to USB device support context
            - **speed** – **[in]** Speed for which the bcdUSB should be set
            - **bcd** – **[in]** bcdUSB value

        Returns:
        :   0 on success, other values on fail.

    int usbd\_device\_set\_vid(struct [usbd\_context](#c.usbd_context) \*const uds\_ctx, const uint16\_t vid)
    :   Set USB device descriptor value idVendor.

        Parameters:
        :   - **uds\_ctx** – **[in]** Pointer to USB device support context
            - **vid** – **[in]** idVendor value

        Returns:
        :   0 on success, other values on fail.

    int usbd\_device\_set\_pid(struct [usbd\_context](#c.usbd_context) \*const uds\_ctx, const uint16\_t pid)
    :   Set USB device descriptor value idProduct.

        Parameters:
        :   - **uds\_ctx** – **[in]** Pointer to USB device support context
            - **pid** – **[in]** idProduct value

        Returns:
        :   0 on success, other values on fail.

    int usbd\_device\_set\_code\_triple(struct [usbd\_context](#c.usbd_context) \*const uds\_ctx, const enum [usbd\_speed](#c.usbd_speed) speed, const uint8\_t base\_class, const uint8\_t subclass, const uint8\_t protocol)
    :   Set USB device descriptor code triple Base Class, SubClass, and Protocol.

        Parameters:
        :   - **uds\_ctx** – **[in]** Pointer to USB device support context
            - **speed** – **[in]** Speed for which the code triple should be set
            - **base\_class** – **[in]** bDeviceClass value
            - **subclass** – **[in]** bDeviceSubClass value
            - **protocol** – **[in]** bDeviceProtocol value

        Returns:
        :   0 on success, other values on fail.

    int usbd\_config\_attrib\_rwup(struct [usbd\_context](#c.usbd_context) \*const uds\_ctx, const enum [usbd\_speed](#c.usbd_speed) speed, const uint8\_t cfg, const bool enable)
    :   Setup USB device configuration attribute Remote Wakeup.

        Parameters:
        :   - **uds\_ctx** – **[in]** Pointer to USB device support context
            - **speed** – **[in]** Configuration speed
            - **cfg** – **[in]** Configuration number
            - **enable** – **[in]** Sets attribute if true, clears it otherwise

        Returns:
        :   0 on success, other values on fail.

    int usbd\_config\_attrib\_self(struct [usbd\_context](#c.usbd_context) \*const uds\_ctx, const enum [usbd\_speed](#c.usbd_speed) speed, const uint8\_t cfg, const bool enable)
    :   Setup USB device configuration attribute Self-powered.

        Parameters:
        :   - **uds\_ctx** – **[in]** Pointer to USB device support context
            - **speed** – **[in]** Configuration speed
            - **cfg** – **[in]** Configuration number
            - **enable** – **[in]** Sets attribute if true, clears it otherwise

        Returns:
        :   0 on success, other values on fail.

    int usbd\_config\_maxpower(struct [usbd\_context](#c.usbd_context) \*const uds\_ctx, const enum [usbd\_speed](#c.usbd_speed) speed, const uint8\_t cfg, const uint8\_t power)
    :   Setup USB device configuration power consumption.

        Parameters:
        :   - **uds\_ctx** – **[in]** Pointer to USB device support context
            - **speed** – **[in]** Configuration speed
            - **cfg** – **[in]** Configuration number
            - **power** – **[in]** Maximum power consumption value (bMaxPower)

        Returns:
        :   0 on success, other values on fail.

    bool usbd\_can\_detect\_vbus(struct [usbd\_context](#c.usbd_context) \*const uds\_ctx)
    :   Check that the controller can detect the VBUS state change.

        This can be used in a generic application to explicitly handle the VBUS detected event after [usbd\_init()](#group__usbd__api_1ga78e5f07af641f9610cc32255efe1680f). For example, to call [usbd\_enable()](#group__usbd__api_1ga1a40fc13129e9218ca63ab3ca70d8d68) after a short delay to give the PMIC time to detect the bus, or to handle cases where [usbd\_enable()](#group__usbd__api_1ga1a40fc13129e9218ca63ab3ca70d8d68) can only be called after a VBUS detected event.

        Parameters:
        :   - **uds\_ctx** – **[in]** Pointer to USB device support context

        Returns:
        :   true if controller can detect VBUS state change, false otherwise

    struct usbd\_str\_desc\_data
    :   *#include <usbd.h>*

        Used internally to keep descriptors in order.

        USBD string descriptor data

        Public Members

        uint8\_t idx
        :   Descriptor index, required for string descriptors.

        enum usbd\_str\_desc\_utype utype
        :   Descriptor usage type (not bDescriptorType).

        unsigned int ascii7
        :   The string descriptor is in ASCII7 format.

        unsigned int use\_hwinfo
        :   Device stack obtains SerialNumber using the HWINFO API.

    struct usbd\_bos\_desc\_data
    :   *#include <usbd.h>*

        USBD BOS Device Capability descriptor data.

        Public Members

        enum usbd\_bos\_desc\_utype utype
        :   Descriptor usage type (not bDescriptorType).

    struct usbd\_desc\_node
    :   *#include <usbd.h>*

        Descriptor node.

        Descriptor node is used to manage descriptors that are not directly part of a structure, such as string or BOS capability descriptors.

        Public Members

        [sys\_dnode\_t](../../../../kernel/data_structures/dlist.md#c.sys_dnode_t "sys_dnode_t") node
        :   slist node struct

        const void \*const ptr
        :   Opaque pointer to a descriptor payload.

        uint8\_t bLength
        :   Descriptor size in bytes.

        uint8\_t bDescriptorType
        :   Descriptor type.

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

        enum [usbd\_speed](#c.usbd_speed) speed
        :   USB device speed.

    struct usbd\_context
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

        [usbd\_msg\_cb\_t](#c.usbd_msg_cb_t) msg\_cb
        :   Notification message recipient callback.

        struct [usbd\_ch9\_data](#c.usbd_ch9_data) ch9\_data
        :   Middle layer runtime data.

        [sys\_dlist\_t](../../../../kernel/data_structures/dlist.md#c.sys_dlist_t "sys_dlist_t") descriptors
        :   slist to manage descriptors like string, BOS

        [sys\_slist\_t](../../../../kernel/data_structures/slist.md#c.sys_slist_t "sys_slist_t") fs\_configs
        :   slist to manage Full-Speed device configurations

        [sys\_slist\_t](../../../../kernel/data_structures/slist.md#c.sys_slist_t "sys_slist_t") hs\_configs
        :   slist to manage High-Speed device configurations

        struct [usbd\_status](#c.usbd_status) status
        :   Status of the USB device support.

        void \*fs\_desc
        :   Pointer to Full-Speed device descriptor.

        void \*hs\_desc
        :   Pointer to High-Speed device descriptor.

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

        void (\*feature\_halt)(struct [usbd\_class\_data](#c.usbd_class_data) \*const c\_data, uint8\_t ep, bool halted)
        :   Feature halt state update handler.

        void (\*update)(struct [usbd\_class\_data](#c.usbd_class_data) \*const c\_data, uint8\_t iface, uint8\_t alternate)
        :   Configuration update handler.

        int (\*control\_to\_dev)(struct [usbd\_class\_data](#c.usbd_class_data) \*const c\_data, const struct usb\_setup\_packet \*const setup, const struct [net\_buf](../../../networking/api/net_buf.md#c.net_buf "net_buf") \*const buf)
        :   USB control request handler to device.

        int (\*control\_to\_host)(struct [usbd\_class\_data](#c.usbd_class_data) \*const c\_data, const struct usb\_setup\_packet \*const setup, struct [net\_buf](../../../networking/api/net_buf.md#c.net_buf "net_buf") \*const buf)
        :   USB control request handler to host.

        int (\*request)(struct [usbd\_class\_data](#c.usbd_class_data) \*const c\_data, struct [net\_buf](../../../networking/api/net_buf.md#c.net_buf "net_buf") \*buf, int err)
        :   Endpoint request completion event handler.

        void (\*suspended)(struct [usbd\_class\_data](#c.usbd_class_data) \*const c\_data)
        :   USB power management handler suspended.

        void (\*resumed)(struct [usbd\_class\_data](#c.usbd_class_data) \*const c\_data)
        :   USB power management handler resumed.

        void (\*sof)(struct [usbd\_class\_data](#c.usbd_class_data) \*const c\_data)
        :   Start of Frame.

        void (\*enable)(struct [usbd\_class\_data](#c.usbd_class_data) \*const c\_data)
        :   Class associated configuration is selected.

        void (\*disable)(struct [usbd\_class\_data](#c.usbd_class_data) \*const c\_data)
        :   Class associated configuration is disabled.

        int (\*init)(struct [usbd\_class\_data](#c.usbd_class_data) \*const c\_data)
        :   Initialization of the class implementation.

        void (\*shutdown)(struct [usbd\_class\_data](#c.usbd_class_data) \*const c\_data)
        :   Shutdown of the class implementation.

        void \*(\*get\_desc)(struct [usbd\_class\_data](#c.usbd_class_data) \*const c\_data, const enum [usbd\_speed](#c.usbd_speed) speed)
        :   Get function descriptor based on speed parameter.

    struct usbd\_class\_data
    :   *#include <usbd.h>*

        USB device support class data.

        Public Members

        const char \*name
        :   Name of the USB device class instance.

        struct [usbd\_context](#c.usbd_context) \*uds\_ctx
        :   Pointer to USB device stack context structure.

        const struct [usbd\_class\_api](#c.usbd_class_api) \*api
        :   Pointer to device support class API.

        const struct [usbd\_cctx\_vendor\_req](#c.usbd_cctx_vendor_req) \*v\_reqs
        :   Supported vendor request table, can be NULL.

        void \*priv
        :   Pointer to private data.

*group* USB device core API
:   Enums

    enum usbd\_msg\_type
    :   USB device support message types.

        The first set of message types map to event types from the UDC driver API.

        *Values:*

        enumerator USBD\_MSG\_VBUS\_READY
        :   VBUS ready message (optional).

        enumerator USBD\_MSG\_VBUS\_REMOVED
        :   VBUS removed message (optional).

        enumerator USBD\_MSG\_RESUME
        :   Device resume message.

        enumerator USBD\_MSG\_SUSPEND
        :   Device suspended message.

        enumerator USBD\_MSG\_RESET
        :   Bus reset detected.

        enumerator USBD\_MSG\_UDC\_ERROR
        :   Non-correctable UDC error message.

        enumerator USBD\_MSG\_STACK\_ERROR
        :   Unrecoverable device stack error message.

        enumerator USBD\_MSG\_CDC\_ACM\_LINE\_CODING
        :   CDC ACM Line Coding update.

        enumerator USBD\_MSG\_CDC\_ACM\_CONTROL\_LINE\_STATE
        :   CDC ACM Line State update.

        enumerator USBD\_MSG\_MAX\_NUMBER
        :   Maximum number of message types.

    Functions

    static inline const char \*usbd\_msg\_type\_string(const enum [usbd\_msg\_type](#c.usbd_msg_type) type)
    :   Returns the message type as a constant string.

        Parameters:
        :   - **type** – **[in]** USBD message type

        Returns:
        :   Message type as a constant string

    struct usbd\_msg
    :   *#include <usbd\_msg.h>*

        USB device message.

        Public Members

        enum [usbd\_msg\_type](#c.usbd_msg_type) type
        :   Message type.

        union [usbd\_msg](#c.usbd_msg).[anonymous] [anonymous]
        :   Message status, value or data.

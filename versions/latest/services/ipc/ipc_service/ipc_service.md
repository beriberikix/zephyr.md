---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/services/ipc/ipc_service/ipc_service.html
original_path: services/ipc/ipc_service/ipc_service.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# IPC service

The IPC service API provides an interface to exchange data between two domains
or CPUs.

## [Overview](#id2)

An IPC service communication channel consists of one instance and one or
several endpoints associated with the instance.

An instance is the external representation of a physical communication channel
between two domains or CPUs. The actual implementation and internal
representation of the instance is peculiar to each backend.

An individual instance is not used to send data between domains/CPUs. To send
and receive the data, the user must create (register) an endpoint in the
instance. This allows for the connection of the two domains of interest.

It is possible to have zero or multiple endpoints for one single instance,
possibly with different priorities, and to use each to exchange data.
Endpoint prioritization and multi-instance ability highly depend on the backend
used.

The endpoint is an entity the user must use to send and receive data between
two domains (connected by the instance). An endpoint is always associated to an
instance.

The creation of the instances is left to the backend, usually at init time.
The registration of the endpoints is left to the user, usually at run time.

The API does not mandate a way for the backend to create instances but it is
strongly recommended to use the devicetree to retrieve the configuration
parameters for an instance. Currently, each backend defines its own
DT-compatible configuration that is used to configure the interface at boot
time.

The following usage scenarios are supported:

- Simple data exchange.
- Data exchange using the no-copy API.

## [Simple data exchange](#id3)

To send data between domains or CPUs, an endpoint must be registered onto
an instance.

See the following example:

Note

Before registering an endpoint, the instance must be opened using the
[`ipc_service_open_instance()`](#c.ipc_service_open_instance) function.

```c
#include <zephyr/ipc/ipc_service.h>

static void bound_cb(void *priv)
{
   /* Endpoint bounded */
}

static void recv_cb(const void *data, size_t len, void *priv)
{
   /* Data received */
}

static struct ipc_ept_cfg ept0_cfg = {
   .name = "ept0",
   .cb = {
      .bound    = bound_cb,
      .received = recv_cb,
   },
};

int main(void)
{
   const struct device *inst0;
   struct ipc_ept ept0;
   int ret;

   inst0 = DEVICE_DT_GET(DT_NODELABEL(ipc0));
   ret = ipc_service_open_instance(inst0);
   ret = ipc_service_register_endpoint(inst0, &ept0, &ept0_cfg);

   /* Wait for endpoint bound (bound_cb called) */

   unsigned char message[] = "hello world";
   ret = ipc_service_send(&ept0, &message, sizeof(message));
}
```

## [Data exchange using the no-copy API](#id4)

If the backend supports the no-copy API you can use it to directly write and
read to and from shared memory regions.

See the following example:

```c
#include <zephyr/ipc/ipc_service.h>
#include <stdint.h>
#include <string.h>

static struct ipc_ept ept0;

static void bound_cb(void *priv)
{
   /* Endpoint bounded */
}

static void recv_cb_nocopy(const void *data, size_t len, void *priv)
{
   int ret;

   ret = ipc_service_hold_rx_buffer(&ept0, (void *)data);
   /* Process directly or put the buffer somewhere else and release. */
   ret = ipc_service_release_rx_buffer(&ept0, (void *)data);
}

static struct ipc_ept_cfg ept0_cfg = {
   .name = "ept0",
   .cb = {
      .bound    = bound_cb,
      .received = recv_cb,
   },
};

int main(void)
{
   const struct device *inst0;
   int ret;

   inst0 = DEVICE_DT_GET(DT_NODELABEL(ipc0));
   ret = ipc_service_open_instance(inst0);
   ret = ipc_service_register_endpoint(inst0, &ept0, &ept0_cfg);

   /* Wait for endpoint bound (bound_cb called) */
   void *data;
   unsigned char message[] = "hello world";
   uint32_t len = sizeof(message);

   ret = ipc_service_get_tx_buffer(&ept0, &data, &len, K_FOREVER);

   memcpy(data, message, len);

   ret = ipc_service_send_nocopy(&ept0, data, sizeof(message));
}
```

### [Backends](#id5)

The requirements needed for implementing backends give flexibility to the IPC
service. These allow for the addition of dedicated backends having only a
subsets of features for specific use cases.

The backend must support at least the following:

- The init-time creation of instances.
- The run-time registration of an endpoint in an instance.

Additionally, the backend can also support the following:

- The run-time deregistration of an endpoint from the instance.
- The run-time closing of an instance.
- The no-copy API.

Each backend can have its own limitations and features that make the backend
unique and dedicated to a specific use case. The IPC service API can be used
with multiple backends simultaneously, combining the pros and cons of each
backend.

### [API Reference](#id6)

## [IPC service API](#id7)

*group* ipc\_service\_api
:   IPC Service API.

    Functions

    int ipc\_service\_open\_instance(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*instance)
    :   Open an instance.

        Function to be used to open an instance before being able to register a new endpoint on it.

        Parameters:
        :   - **instance** – **[in]** Instance to open.

        Return values:
        :   - **-EINVAL** – when instance configuration is invalid.
            - **-EIO** – when no backend is registered.
            - **-EALREADY** – when the instance is already opened (or being opened).
            - **0** – on success or when not implemented on the backend (not needed).
            - **other** – errno codes depending on the implementation of the backend.

    int ipc\_service\_close\_instance(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*instance)
    :   Close an instance.

        Function to be used to close an instance. All bounded endpoints must be deregistered using ipc\_service\_deregister\_endpoint before this is called.

        Parameters:
        :   - **instance** – **[in]** Instance to close.

        Return values:
        :   - **-EINVAL** – when instance configuration is invalid.
            - **-EIO** – when no backend is registered.
            - **-EALREADY** – when the instance is not already opened.
            - **-EBUSY** – when an endpoint exists that hasn’t been deregistered
            - **0** – on success or when not implemented on the backend (not needed).
            - **other** – errno codes depending on the implementation of the backend.

    int ipc\_service\_register\_endpoint(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*instance, struct [ipc\_ept](#c.ipc_ept) \*ept, const struct [ipc\_ept\_cfg](#c.ipc_ept_cfg) \*cfg)
    :   Register IPC endpoint onto an instance.

        Registers IPC endpoint onto an instance to enable communication with a remote device.

        The same function registers endpoints for both host and remote devices.

        Note

        Keep the variable pointed by `cfg` alive when endpoint is in use.

        Parameters:
        :   - **instance** – **[in]** Instance to register the endpoint onto.
            - **ept** – **[in]** Endpoint object.
            - **cfg** – **[in]** Endpoint configuration.

        Return values:
        :   - **-EIO** – when no backend is registered.
            - **-EINVAL** – when instance, endpoint or configuration is invalid.
            - **-EBUSY** – when the instance is busy.
            - **0** – on success.
            - **other** – errno codes depending on the implementation of the backend.

    int ipc\_service\_deregister\_endpoint(struct [ipc\_ept](#c.ipc_ept) \*ept)
    :   Deregister an IPC endpoint from its instance.

        Deregisters an IPC endpoint from its instance.

        The same function deregisters endpoints for both host and remote devices.

        Parameters:
        :   - **ept** – **[in]** Endpoint object.

        Return values:
        :   - **-EIO** – when no backend is registered.
            - **-EINVAL** – when instance, endpoint or configuration is invalid.
            - **-ENOENT** – when the endpoint is not registered with the instance.
            - **-EBUSY** – when the instance is busy.
            - **0** – on success.
            - **other** – errno codes depending on the implementation of the backend.

    int ipc\_service\_send(struct [ipc\_ept](#c.ipc_ept) \*ept, const void \*data, size\_t len)
    :   Send data using given IPC endpoint.

        Parameters:
        :   - **ept** – **[in]** Registered endpoint by [ipc\_service\_register\_endpoint](#group__ipc__service__api_1gabfb8bab2e2e8cfe8908a050d4844666b).
            - **data** – **[in]** Pointer to the buffer to send.
            - **len** – **[in]** Number of bytes to send.

        Return values:
        :   - **-EIO** – when no backend is registered or send hook is missing from backend.
            - **-EINVAL** – when instance or endpoint is invalid.
            - **-ENOENT** – when the endpoint is not registered with the instance.
            - **-EBADMSG** – when the data is invalid (i.e. invalid data format, invalid length, …)
            - **-EBUSY** – when the instance is busy.
            - **-ENOMEM** – when no memory / buffers are available.
            - **bytes** – number of bytes sent.
            - **other** – errno codes depending on the implementation of the backend.

    int ipc\_service\_get\_tx\_buffer\_size(struct [ipc\_ept](#c.ipc_ept) \*ept)
    :   Get the TX buffer size.

        Get the maximal size of a buffer which can be obtained by [ipc\_service\_get\_tx\_buffer](#group__ipc__service__api_1gab2371bd26ad85b5dffac3b4000e51191)

        Parameters:
        :   - **ept** – **[in]** Registered endpoint by [ipc\_service\_register\_endpoint](#group__ipc__service__api_1gabfb8bab2e2e8cfe8908a050d4844666b).

        Return values:
        :   - **-EIO** – when no backend is registered or send hook is missing from backend.
            - **-EINVAL** – when instance or endpoint is invalid.
            - **-ENOENT** – when the endpoint is not registered with the instance.
            - **-ENOTSUP** – when the operation is not supported by backend.
            - **size** – TX buffer size on success.
            - **other** – errno codes depending on the implementation of the backend.

    int ipc\_service\_get\_tx\_buffer(struct [ipc\_ept](#c.ipc_ept) \*ept, void \*\*data, uint32\_t \*size, [k\_timeout\_t](../../../kernel/services/timing/clocks.md#c.k_timeout_t "k_timeout_t") wait)
    :   Get an empty TX buffer to be sent using [ipc\_service\_send\_nocopy](#group__ipc__service__api_1ga72aa5da1530908230478c49b5a012dc1).

        This function can be called to get an empty TX buffer so that the application can directly put its data into the sending buffer without copy from an application buffer.

        It is the application responsibility to correctly fill the allocated TX buffer with data and passing correct parameters to [ipc\_service\_send\_nocopy](#group__ipc__service__api_1ga72aa5da1530908230478c49b5a012dc1) function to perform data no-copy-send mechanism.

        The size parameter can be used to request a buffer with a certain size:

        - if the size can be accommodated the function returns no errors and the buffer is allocated
        - if the requested size is too big, the function returns -ENOMEM and the the buffer is not allocated.
        - if the requested size is ‘0’ the buffer is allocated with the maximum allowed size.

        In all the cases on return the size parameter contains the maximum size for the returned buffer.

        When the function returns no errors, the buffer is intended as allocated and it is released under two conditions: (1) when sending the buffer using [ipc\_service\_send\_nocopy](#group__ipc__service__api_1ga72aa5da1530908230478c49b5a012dc1) (and in this case the buffer is automatically released by the backend), (2) when using [ipc\_service\_drop\_tx\_buffer](#group__ipc__service__api_1ga3eb7168f73f5bc45fdced3af6d374860) on a buffer not sent.

        Parameters:
        :   - **ept** – **[in]** Registered endpoint by [ipc\_service\_register\_endpoint](#group__ipc__service__api_1gabfb8bab2e2e8cfe8908a050d4844666b).
            - **data** – **[out]** Pointer to the empty TX buffer.
            - **size** – **[inout]** Pointer to store the requested TX buffer size. If the function returns -ENOMEM, this parameter returns the maximum allowed size.
            - **wait** – **[in]** Timeout waiting for an available TX buffer.

        Return values:
        :   - **-EIO** – when no backend is registered or send hook is missing from backend.
            - **-EINVAL** – when instance or endpoint is invalid.
            - **-ENOENT** – when the endpoint is not registered with the instance.
            - **-ENOTSUP** – when the operation or the timeout is not supported by backend.
            - **-ENOBUFS** – when there are no TX buffers available.
            - **-EALREADY** – when a buffer was already claimed and not yet released.
            - **-ENOMEM** – when the requested size is too big (and the size parameter contains the maximum allowed size).
            - **0** – on success.
            - **other** – errno codes depending on the implementation of the backend.

    int ipc\_service\_drop\_tx\_buffer(struct [ipc\_ept](#c.ipc_ept) \*ept, const void \*data)
    :   Drop and release a TX buffer.

        Drop and release a TX buffer. It is possible to drop only TX buffers obtained by using [ipc\_service\_get\_tx\_buffer](#group__ipc__service__api_1gab2371bd26ad85b5dffac3b4000e51191).

        Parameters:
        :   - **ept** – **[in]** Registered endpoint by [ipc\_service\_register\_endpoint](#group__ipc__service__api_1gabfb8bab2e2e8cfe8908a050d4844666b).
            - **data** – **[in]** Pointer to the TX buffer.

        Return values:
        :   - **-EIO** – when no backend is registered or send hook is missing from backend.
            - **-EINVAL** – when instance or endpoint is invalid.
            - **-ENOENT** – when the endpoint is not registered with the instance.
            - **-ENOTSUP** – when this is not supported by backend.
            - **-EALREADY** – when the buffer was already dropped.
            - **-ENXIO** – when the buffer was not obtained using [ipc\_service\_get\_tx\_buffer](#group__ipc__service__api_1gab2371bd26ad85b5dffac3b4000e51191)
            - **0** – on success.
            - **other** – errno codes depending on the implementation of the backend.

    int ipc\_service\_send\_nocopy(struct [ipc\_ept](#c.ipc_ept) \*ept, const void \*data, size\_t len)
    :   Send data in a TX buffer reserved by [ipc\_service\_get\_tx\_buffer](#group__ipc__service__api_1gab2371bd26ad85b5dffac3b4000e51191) using the given IPC endpoint.

        This is equivalent to [ipc\_service\_send](#group__ipc__service__api_1gac002253b7436902c6a3e0c93933d23fc) but in this case the TX buffer has been obtained by using [ipc\_service\_get\_tx\_buffer](#group__ipc__service__api_1gab2371bd26ad85b5dffac3b4000e51191).

        The application has to take the responsibility for getting the TX buffer using [ipc\_service\_get\_tx\_buffer](#group__ipc__service__api_1gab2371bd26ad85b5dffac3b4000e51191) and filling the TX buffer with the data.

        After the [ipc\_service\_send\_nocopy](#group__ipc__service__api_1ga72aa5da1530908230478c49b5a012dc1) function is issued the TX buffer is no more owned by the sending task and must not be touched anymore unless the function fails and returns an error.

        If this function returns an error, [ipc\_service\_drop\_tx\_buffer](#group__ipc__service__api_1ga3eb7168f73f5bc45fdced3af6d374860) can be used to drop the TX buffer.

        Parameters:
        :   - **ept** – **[in]** Registered endpoint by [ipc\_service\_register\_endpoint](#group__ipc__service__api_1gabfb8bab2e2e8cfe8908a050d4844666b).
            - **data** – **[in]** Pointer to the buffer to send obtained by [ipc\_service\_get\_tx\_buffer](#group__ipc__service__api_1gab2371bd26ad85b5dffac3b4000e51191).
            - **len** – **[in]** Number of bytes to send.

        Return values:
        :   - **-EIO** – when no backend is registered or send hook is missing from backend.
            - **-EINVAL** – when instance or endpoint is invalid.
            - **-ENOENT** – when the endpoint is not registered with the instance.
            - **-EBADMSG** – when the data is invalid (i.e. invalid data format, invalid length, …)
            - **-EBUSY** – when the instance is busy.
            - **bytes** – number of bytes sent.
            - **other** – errno codes depending on the implementation of the backend.

    int ipc\_service\_hold\_rx\_buffer(struct [ipc\_ept](#c.ipc_ept) \*ept, void \*data)
    :   Holds the RX buffer for usage outside the receive callback.

        Calling this function prevents the receive buffer from being released back to the pool of shmem buffers. This function can be called in the receive callback when the user does not want to copy the message out in the callback itself.

        After the message is processed, the application must release the buffer using the [ipc\_service\_release\_rx\_buffer](#group__ipc__service__api_1gaf4fd99716e7c83006a76f7f1bc85f228) function.

        Parameters:
        :   - **ept** – **[in]** Registered endpoint by [ipc\_service\_register\_endpoint](#group__ipc__service__api_1gabfb8bab2e2e8cfe8908a050d4844666b).
            - **data** – **[in]** Pointer to the RX buffer to hold.

        Return values:
        :   - **-EIO** – when no backend is registered or release hook is missing from backend.
            - **-EINVAL** – when instance or endpoint is invalid.
            - **-ENOENT** – when the endpoint is not registered with the instance.
            - **-EALREADY** – when the buffer data has been hold already.
            - **-ENOTSUP** – when this is not supported by backend.
            - **0** – on success.
            - **other** – errno codes depending on the implementation of the backend.

    int ipc\_service\_release\_rx\_buffer(struct [ipc\_ept](#c.ipc_ept) \*ept, void \*data)
    :   Release the RX buffer for future reuse.

        When supported by the backend, this function can be called after the received message has been processed and the buffer can be marked as reusable again.

        It is possible to release only RX buffers on which [ipc\_service\_hold\_rx\_buffer](#group__ipc__service__api_1gadd957653c3e2bc32c494a9d643c0a0bd) was previously used.

        Parameters:
        :   - **ept** – **[in]** Registered endpoint by [ipc\_service\_register\_endpoint](#group__ipc__service__api_1gabfb8bab2e2e8cfe8908a050d4844666b).
            - **data** – **[in]** Pointer to the RX buffer to release.

        Return values:
        :   - **-EIO** – when no backend is registered or release hook is missing from backend.
            - **-EINVAL** – when instance or endpoint is invalid.
            - **-ENOENT** – when the endpoint is not registered with the instance.
            - **-EALREADY** – when the buffer data has been already released.
            - **-ENOTSUP** – when this is not supported by backend.
            - **-ENXIO** – when the buffer was not hold before using [ipc\_service\_hold\_rx\_buffer](#group__ipc__service__api_1gadd957653c3e2bc32c494a9d643c0a0bd)
            - **0** – on success.
            - **other** – errno codes depending on the implementation of the backend.

    struct ipc\_service\_cb
    :   *#include <ipc\_service.h>*

        Event callback structure.

        It is registered during endpoint registration. This structure is part of the endpoint configuration.

        Public Members

        void (\*bound)(void \*priv)
        :   Bind was successful.

            This callback is called when the endpoint binding is successful.

            Param priv:
            :   **[in]** Private user data.

        void (\*received)(const void \*data, size\_t len, void \*priv)
        :   New packet arrived.

            This callback is called when new data is received.

            Note

            When [ipc\_service\_hold\_rx\_buffer](#group__ipc__service__api_1gadd957653c3e2bc32c494a9d643c0a0bd) is not used, the data buffer is to be considered released and available again only when this callback returns.

            Param data:
            :   **[in]** Pointer to data buffer.

            Param len:
            :   **[in]** Length of *data*.

            Param priv:
            :   **[in]** Private user data.

        void (\*error)(const char \*message, void \*priv)
        :   An error occurred.

            Param message:
            :   **[in]** Error message.

            Param priv:
            :   **[in]** Private user data.

    struct ipc\_ept
    :   *#include <ipc\_service.h>*

        Endpoint instance.

        Token is not important for user of the API. It is implemented in a specific backend.

        Public Members

        const struct [device](../../../kernel/drivers/index.md#c.device "device") \*instance
        :   Instance this endpoint belongs to.

        void \*token
        :   Backend-specific token used to identify an endpoint in an instance.

    struct ipc\_ept\_cfg
    :   *#include <ipc\_service.h>*

        Endpoint configuration structure.

        Public Members

        const char \*name
        :   Name of the endpoint.

        int prio
        :   Endpoint priority.

            If the backend supports priorities.

        struct [ipc\_service\_cb](#c.ipc_service_cb) cb
        :   Event callback structure.

        void \*priv
        :   Private user data.

## [IPC service backend API](#id8)

*group* ipc\_service\_backend
:   IPC service backend.

    struct ipc\_service\_backend
    :   *#include <ipc\_service\_backend.h>*

        IPC backend configuration structure.

        This structure is used for configuration backend during registration.

        Public Members

        int (\*open\_instance)(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*instance)
        :   Pointer to the function that will be used to open an instance.

            Param instance:
            :   **[in]** Instance pointer.

            Retval -EALREADY:
            :   when the instance is already opened.

            Retval 0:
            :   on success

            Retval other:
            :   errno codes depending on the implementation of the backend.

        int (\*close\_instance)(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*instance)
        :   Pointer to the function that will be used to close an instance.

            Param instance:
            :   **[in]** Instance pointer.

            Retval -EALREADY:
            :   when the instance is not already inited.

            Retval 0:
            :   on success

            Retval other:
            :   errno codes depending on the implementation of the backend.

        int (\*send)(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*instance, void \*token, const void \*data, size\_t len)
        :   Pointer to the function that will be used to send data to the endpoint.

            Param instance:
            :   **[in]** Instance pointer.

            Param token:
            :   **[in]** Backend-specific token.

            Param data:
            :   **[in]** Pointer to the buffer to send.

            Param len:
            :   **[in]** Number of bytes to send.

            Retval -EINVAL:
            :   when instance is invalid.

            Retval -ENOENT:
            :   when the endpoint is not registered with the instance.

            Retval -EBADMSG:
            :   when the message is invalid.

            Retval -EBUSY:
            :   when the instance is busy or not ready.

            Retval -ENOMEM:
            :   when no memory / buffers are available.

            Retval bytes:
            :   number of bytes sent.

            Retval other:
            :   errno codes depending on the implementation of the backend.

        int (\*register\_endpoint)(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*instance, void \*\*token, const struct [ipc\_ept\_cfg](#c.ipc_ept_cfg) \*cfg)
        :   Pointer to the function that will be used to register endpoints.

            Param instance:
            :   **[in]** Instance to register the endpoint onto.

            Param token:
            :   **[out]** Backend-specific token.

            Param cfg:
            :   **[in]** Endpoint configuration.

            Retval -EINVAL:
            :   when the endpoint configuration or instance is invalid.

            Retval -EBUSY:
            :   when the instance is busy or not ready.

            Retval 0:
            :   on success

            Retval other:
            :   errno codes depending on the implementation of the backend.

        int (\*deregister\_endpoint)(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*instance, void \*token)
        :   Pointer to the function that will be used to deregister endpoints.

            Param instance:
            :   **[in]** Instance from which to deregister the endpoint.

            Param token:
            :   **[in]** Backend-specific token.

            Retval -EINVAL:
            :   when the endpoint configuration or instance is invalid.

            Retval -ENOENT:
            :   when the endpoint is not registered with the instance.

            Retval -EBUSY:
            :   when the instance is busy or not ready.

            Retval 0:
            :   on success

            Retval other:
            :   errno codes depending on the implementation of the backend.

        int (\*get\_tx\_buffer\_size)(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*instance, void \*token)
        :   Pointer to the function that will return the TX buffer size.

            Param instance:
            :   **[in]** Instance pointer.

            Param token:
            :   **[in]** Backend-specific token.

            Retval -EINVAL:
            :   when instance is invalid.

            Retval -ENOENT:
            :   when the endpoint is not registered with the instance.

            Retval -ENOTSUP:
            :   when the operation is not supported.

            Retval size:
            :   TX buffer size on success.

            Retval other:
            :   errno codes depending on the implementation of the backend.

        int (\*get\_tx\_buffer)(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*instance, void \*token, void \*\*data, uint32\_t \*len, [k\_timeout\_t](../../../kernel/services/timing/clocks.md#c.k_timeout_t "k_timeout_t") wait)
        :   Pointer to the function that will return an empty TX buffer.

            Param instance:
            :   **[in]** Instance pointer.

            Param token:
            :   **[in]** Backend-specific token.

            Param data:
            :   **[out]** Pointer to the empty TX buffer.

            Param len:
            :   **[inout]** Pointer to store the TX buffer size.

            Param wait:
            :   **[in]** Timeout waiting for an available TX buffer.

            Retval -EINVAL:
            :   when instance is invalid.

            Retval -ENOENT:
            :   when the endpoint is not registered with the instance.

            Retval -ENOTSUP:
            :   when the operation or the timeout is not supported.

            Retval -ENOBUFS:
            :   when there are no TX buffers available.

            Retval -EALREADY:
            :   when a buffer was already claimed and not yet released.

            Retval -ENOMEM:
            :   when the requested size is too big (and the size parameter contains the maximum allowed size).

            Retval 0:
            :   on success

            Retval other:
            :   errno codes depending on the implementation of the backend.

        int (\*drop\_tx\_buffer)(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*instance, void \*token, const void \*data)
        :   Pointer to the function that will drop a TX buffer.

            Param instance:
            :   **[in]** Instance pointer.

            Param token:
            :   **[in]** Backend-specific token.

            Param data:
            :   **[in]** Pointer to the TX buffer.

            Retval -EINVAL:
            :   when instance is invalid.

            Retval -ENOENT:
            :   when the endpoint is not registered with the instance.

            Retval -ENOTSUP:
            :   when this function is not supported.

            Retval -EALREADY:
            :   when the buffer was already dropped.

            Retval 0:
            :   on success

            Retval other:
            :   errno codes depending on the implementation of the backend.

        int (\*send\_nocopy)(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*instance, void \*token, const void \*data, size\_t len)
        :   Pointer to the function that will be used to send data to the endpoint when the TX buffer has been obtained using [ipc\_service\_get\_tx\_buffer](#group__ipc__service__api_1gab2371bd26ad85b5dffac3b4000e51191).

            Param instance:
            :   **[in]** Instance pointer.

            Param token:
            :   **[in]** Backend-specific token.

            Param data:
            :   **[in]** Pointer to the buffer to send.

            Param len:
            :   **[in]** Number of bytes to send.

            Retval -EINVAL:
            :   when instance is invalid.

            Retval -ENOENT:
            :   when the endpoint is not registered with the instance.

            Retval -EBADMSG:
            :   when the data is invalid (i.e. invalid data format, invalid length, …)

            Retval -EBUSY:
            :   when the instance is busy or not ready.

            Retval bytes:
            :   number of bytes sent.

            Retval other:
            :   errno codes depending on the implementation of the backend.

        int (\*hold\_rx\_buffer)(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*instance, void \*token, void \*data)
        :   Pointer to the function that will hold the RX buffer.

            Param instance:
            :   **[in]** Instance pointer.

            Param token:
            :   **[in]** Backend-specific token.

            Param data:
            :   **[in]** Pointer to the RX buffer to hold.

            Retval -EINVAL:
            :   when instance is invalid.

            Retval -ENOENT:
            :   when the endpoint is not registered with the instance.

            Retval -EALREADY:
            :   when the buffer data has been already hold.

            Retval -ENOTSUP:
            :   when this function is not supported.

            Retval 0:
            :   on success

            Retval other:
            :   errno codes depending on the implementation of the backend.

        int (\*release\_rx\_buffer)(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*instance, void \*token, void \*data)
        :   Pointer to the function that will release the RX buffer.

            Param instance:
            :   **[in]** Instance pointer.

            Param token:
            :   **[in]** Backend-specific token.

            Param data:
            :   **[in]** Pointer to the RX buffer to release.

            Retval -EINVAL:
            :   when instance is invalid.

            Retval -ENOENT:
            :   when the endpoint is not registered with the instance.

            Retval -EALREADY:
            :   when the buffer data has been already released.

            Retval -ENOTSUP:
            :   when this function is not supported.

            Retval 0:
            :   on success

            Retval other:
            :   errno codes depending on the implementation of the backend.

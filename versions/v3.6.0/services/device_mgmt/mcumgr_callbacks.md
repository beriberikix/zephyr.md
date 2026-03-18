---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/services/device_mgmt/mcumgr_callbacks.html
original_path: services/device_mgmt/mcumgr_callbacks.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# MCUmgr Callbacks

## Overview

MCUmgr has a customisable callback/notification system that allows application
(and module) code to receive callbacks for MCUmgr events that they are
interested in and react to them or return a status code to the calling function
that provides control over if the action should be allowed or not. An example
of this is with the fs\_mgmt group, whereby file access can be gated, the
callback allows the application to inspect the request path and allow or deny
access to said file, or it can rewrite the provided path to a different path
for transparent file redirection support.

## Implementation

### Enabling

The base callback/notification system can be enabled using
[`CONFIG_MCUMGR_MGMT_NOTIFICATION_HOOKS`](../../kconfig.md#CONFIG_MCUMGR_MGMT_NOTIFICATION_HOOKS "CONFIG_MCUMGR_MGMT_NOTIFICATION_HOOKS") which will compile the
registration and notification system into the code. This will not provide any
callbacks by default as the callbacks that are supported by a build must also
be selected by enabling the Kconfig’s for the required callbacks (see
[Events](#mcumgr-cb-events) for further details). A callback function with the
[`mgmt_cb`](#c.mgmt_cb) type definition can then be declared and registered by
calling [`mgmt_callback_register()`](#c.mgmt_callback_register) for the desired event inside of a
:c:struct`mgmt\_callback` structure. Handlers are called in the order that they
were registered.

With the system enabled, a basic handler can be set up and defined in
application code as per:

```c
#include <zephyr/kernel.h>
#include <zephyr/mgmt/mcumgr/mgmt/mgmt.h>
#include <zephyr/mgmt/mcumgr/mgmt/callbacks.h>

struct mgmt_callback my_callback;

enum mgmt_cb_return my_function(uint32_t event, enum mgmt_cb_return prev_status,
                                int32_t *rc, uint16_t *group, bool *abort_more,
                                void *data, size_t data_size)
{
    if (event == MGMT_EVT_OP_CMD_DONE) {
        /* This is the event we registered for */
    }

    /* Return OK status code to continue with acceptance to underlying handler */
    return MGMT_CB_OK;
}

int main()
{
    my_callback.callback = my_function;
    my_callback.event_id = MGMT_EVT_OP_CMD_DONE;
    mgmt_callback_register(&my_callback);
}
```

This code registers a handler for the [`MGMT_EVT_OP_CMD_DONE`](#c.smp_group_events.MGMT_EVT_OP_CMD_DONE)
event, which will be called after a MCUmgr command has been processed and
output generated, note that this requires that
[`CONFIG_MCUMGR_SMP_COMMAND_STATUS_HOOKS`](../../kconfig.md#CONFIG_MCUMGR_SMP_COMMAND_STATUS_HOOKS "CONFIG_MCUMGR_SMP_COMMAND_STATUS_HOOKS") be enabled to receive
this callback.

Multiple callbacks can be setup to use a single function as a common callback,
and many different functions can be used for each event by registering each
group once, or all notifications for a whole group can be enabled by using one
of the `MGMT_EVT_OP_*_ALL` events, alternatively a handler can setup for
every notification by using [`MGMT_EVT_OP_ALL`](#c.smp_all_events.MGMT_EVT_OP_ALL). When setting up
handlers, events can be combined that are in the same group only, for example
5 img\_mgmt callbacks can be setup with a single registration call, but to also
setup a callback for an os\_mgmt callback, this must be done as a separate
registration. Group IDs are numerical increments, event IDs are bitmask values,
hence the restriction.

As an example, the following registration is allowed, which will register for 3
SMP events with a single callback function in a single registration:

```c
my_callback.callback = my_function;
my_callback.event_id = (MGMT_EVT_OP_CMD_RECV |
                        MGMT_EVT_OP_CMD_STATUS |
                        MGMT_EVT_OP_CMD_DONE);
mgmt_callback_register(&my_callback);
```

The following code is not allowed, and will cause undefined operation, because
it mixes the IMG management group with the OS management group whereby the
group is **not** a bitmask value, only the event is:

```c
my_callback.callback = my_function;
my_callback.event_id = (MGMT_EVT_OP_IMG_MGMT_DFU_STARTED |
                        MGMT_EVT_OP_OS_MGMT_RESET);
mgmt_callback_register(&my_callback);
```

### Events

Events can be selected by enabling their corresponding Kconfig option:

> - [`CONFIG_MCUMGR_SMP_COMMAND_STATUS_HOOKS`](../../kconfig.md#CONFIG_MCUMGR_SMP_COMMAND_STATUS_HOOKS "CONFIG_MCUMGR_SMP_COMMAND_STATUS_HOOKS")
>   :   MCUmgr command status ([`MGMT_EVT_OP_CMD_RECV`](#c.smp_group_events.MGMT_EVT_OP_CMD_RECV),
>       [`MGMT_EVT_OP_CMD_STATUS`](#c.smp_group_events.MGMT_EVT_OP_CMD_STATUS),
>       [`MGMT_EVT_OP_CMD_DONE`](#c.smp_group_events.MGMT_EVT_OP_CMD_DONE))
> - [`CONFIG_MCUMGR_GRP_FS_FILE_ACCESS_HOOK`](../../kconfig.md#CONFIG_MCUMGR_GRP_FS_FILE_ACCESS_HOOK "CONFIG_MCUMGR_GRP_FS_FILE_ACCESS_HOOK")
>   :   fs\_mgmt file access ([`MGMT_EVT_OP_FS_MGMT_FILE_ACCESS`](#c.fs_mgmt_group_events.MGMT_EVT_OP_FS_MGMT_FILE_ACCESS))
> - [`CONFIG_MCUMGR_GRP_IMG_UPLOAD_CHECK_HOOK`](../../kconfig.md#CONFIG_MCUMGR_GRP_IMG_UPLOAD_CHECK_HOOK "CONFIG_MCUMGR_GRP_IMG_UPLOAD_CHECK_HOOK")
>   :   img\_mgmt upload check ([`MGMT_EVT_OP_IMG_MGMT_DFU_CHUNK`](#c.img_mgmt_group_events.MGMT_EVT_OP_IMG_MGMT_DFU_CHUNK))
> - [`CONFIG_MCUMGR_GRP_IMG_STATUS_HOOKS`](../../kconfig.md#CONFIG_MCUMGR_GRP_IMG_STATUS_HOOKS "CONFIG_MCUMGR_GRP_IMG_STATUS_HOOKS")
>   :   img\_mgmt upload status ([`MGMT_EVT_OP_IMG_MGMT_DFU_STOPPED`](#c.img_mgmt_group_events.MGMT_EVT_OP_IMG_MGMT_DFU_STOPPED),
>       [`MGMT_EVT_OP_IMG_MGMT_DFU_STARTED`](#c.img_mgmt_group_events.MGMT_EVT_OP_IMG_MGMT_DFU_STARTED),
>       [`MGMT_EVT_OP_IMG_MGMT_DFU_PENDING`](#c.img_mgmt_group_events.MGMT_EVT_OP_IMG_MGMT_DFU_PENDING),
>       [`MGMT_EVT_OP_IMG_MGMT_DFU_CONFIRMED`](#c.img_mgmt_group_events.MGMT_EVT_OP_IMG_MGMT_DFU_CONFIRMED))
> - [`CONFIG_MCUMGR_GRP_OS_RESET_HOOK`](../../kconfig.md#CONFIG_MCUMGR_GRP_OS_RESET_HOOK "CONFIG_MCUMGR_GRP_OS_RESET_HOOK")
>   :   os\_mgmt reset check ([`MGMT_EVT_OP_OS_MGMT_RESET`](#c.os_mgmt_group_events.MGMT_EVT_OP_OS_MGMT_RESET))
> - [`CONFIG_MCUMGR_GRP_SETTINGS_ACCESS_HOOK`](../../kconfig.md#CONFIG_MCUMGR_GRP_SETTINGS_ACCESS_HOOK "CONFIG_MCUMGR_GRP_SETTINGS_ACCESS_HOOK")
>   :   settings\_mgmt access ([`MGMT_EVT_OP_SETTINGS_MGMT_ACCESS`](#c.settings_mgmt_group_events.MGMT_EVT_OP_SETTINGS_MGMT_ACCESS))

### Actions

Some callbacks expect a return status to either allow or disallow an operation,
an example is the fs\_mgmt access hook which allows for access to files to be
allowed or denied. With these handlers, the first non-OK error code returned
by a handler will be returned to the MCUmgr client.

An example of selectively denying file access:

```c
#include <zephyr/kernel.h>
#include <zephyr/mgmt/mcumgr/mgmt/mgmt.h>
#include <zephyr/mgmt/mcumgr/mgmt/callbacks.h>
#include <string.h>

struct mgmt_callback my_callback;

enum mgmt_cb_return my_function(uint32_t event, enum mgmt_cb_return prev_status,
                                int32_t *rc, uint16_t *group, bool *abort_more,
                                void *data, size_t data_size)
{
    /* Only run this handler if a previous handler has not failed */
    if (event == MGMT_EVT_OP_FS_MGMT_FILE_ACCESS && prev_status == MGMT_CB_OK) {
        struct fs_mgmt_file_access *fs_data = (struct fs_mgmt_file_access *)data;

        /* Check if this is an upload and deny access if it is, otherwise check
         * the path and deny if is matches a name
         */
        if (fs_data->access == FS_MGMT_FILE_ACCESS_WRITE) {
            /* Return an access denied error code to the client and abort calling
             * further handlers
             */
            *abort_more = true;
            *rc = MGMT_ERR_EACCESSDENIED;

            return MGMT_CB_ERROR_RC;
        } else if (strcmp(fs_data->filename, "/lfs1/false_deny.txt") == 0) {
            /* Return a no entry error code to the client, call additional handlers
             * (which will have failed set to true)
             */
            *rc = MGMT_ERR_ENOENT;

            return MGMT_CB_ERROR_RC;
        }
    }

    /* Return OK status code to continue with acceptance to underlying handler */
    return MGMT_CB_OK;
}

int main()
{
    my_callback.callback = my_function;
    my_callback.event_id = MGMT_EVT_OP_FS_MGMT_FILE_ACCESS;
    mgmt_callback_register(&my_callback);
}
```

This code registers a handler for the
[`MGMT_EVT_OP_FS_MGMT_FILE_ACCESS`](#c.fs_mgmt_group_events.MGMT_EVT_OP_FS_MGMT_FILE_ACCESS) event, which will be called
after a fs\_mgmt file read/write command has been received to check if access to
the file should be allowed or not, note that this requires that
[`CONFIG_MCUMGR_GRP_FS_FILE_ACCESS_HOOK`](../../kconfig.md#CONFIG_MCUMGR_GRP_FS_FILE_ACCESS_HOOK "CONFIG_MCUMGR_GRP_FS_FILE_ACCESS_HOOK") be enabled to receive
this callback.
Two types of errors can be returned, the `rc` parameter can be set to an
[`mcumgr_err_t`](mcumgr.md#c.mcumgr_err_t "mcumgr_err_t") error code and [`MGMT_CB_ERROR_RC`](#c.mgmt_cb_return.MGMT_CB_ERROR_RC)
can be returned, or a group error code (introduced with version 2 of the MCUmgr
protocol) can be set by setting the `group` value to the group and `rc`
value to the group error code and returning [`MGMT_CB_ERROR_ERR`](#c.mgmt_cb_return.MGMT_CB_ERROR_ERR).

### MCUmgr Command Callback Usage/Adding New Event Types

To add a callback to a MCUmgr command, [`mgmt_callback_notify()`](#c.mgmt_callback_notify) can be
called with the event ID and, optionally, a data struct to pass to the callback
(which can be modified by handlers). If no data needs to be passed back,
`NULL` can be used instead, and size of the data set to 0.

An example MCUmgr command handler:

```c
#include <zephyr/kernel.h>
#include <zcbor_common.h>
#include <zcbor_encode.h>
#include <zephyr/mgmt/mcumgr/smp/smp.h>
#include <zephyr/mgmt/mcumgr/mgmt/mgmt.h>
#include <zephyr/mgmt/mcumgr/mgmt/callbacks.h>

#define MGMT_EVT_GRP_USER_ONE MGMT_EVT_GRP_USER_CUSTOM_START

enum user_one_group_events {
    /** Callback on first post, data is test_struct. */
    MGMT_EVT_OP_USER_ONE_FIRST  = MGMT_DEF_EVT_OP_ID(MGMT_EVT_GRP_USER_ONE, 0),

    /** Callback on second post, data is test_struct. */
    MGMT_EVT_OP_USER_ONE_SECOND = MGMT_DEF_EVT_OP_ID(MGMT_EVT_GRP_USER_ONE, 1),

    /** Used to enable all user_one events. */
    MGMT_EVT_OP_USER_ONE_ALL    = MGMT_DEF_EVT_OP_ALL(MGMT_EVT_GRP_USER_ONE),
};

struct test_struct {
    uint8_t some_value;
};

static int test_command(struct mgmt_ctxt *ctxt)
{
    int rc;
    int err_rc;
    uint16_t err_group;
    zcbor_state_t *zse = ctxt->cnbe->zs;
    bool ok;
    struct test_struct test_data = {
        .some_value = 8,
    };

    rc = mgmt_callback_notify(MGMT_EVT_OP_USER_ONE_FIRST, &test_data,
                              sizeof(test_data), &err_rc, &err_group);

    if (rc != MGMT_CB_OK) {
        /* A handler returned a failure code */
        if (rc == MGMT_CB_ERROR_RC) {
            /* The failure code is the RC value */
            return err_rc;
        }

        /* The failure is a group and ID error value */
        ok = smp_add_cmd_err(zse, err_group, (uint16_t)err_rc);
        goto end;
    }

    /* All handlers returned success codes */
    ok = zcbor_tstr_put_lit(zse, "output_value") &&
         zcbor_int32_put(zse, 1234);

end:
    rc = (ok ? MGMT_ERR_EOK : MGMT_ERR_EMSGSIZE);

    return rc;
}
```

If no response is required for the callback, the function call be called and
casted to void.

## Migration

If there is existing code using the previous callback system(s) in Zephyr 3.2
or earlier, then it will need to be migrated to the new system. To migrate
code, the following callback registration functions will need to be migrated
to register for callbacks using [`mgmt_callback_register()`](#c.mgmt_callback_register) (note that
[`CONFIG_MCUMGR_MGMT_NOTIFICATION_HOOKS`](../../kconfig.md#CONFIG_MCUMGR_MGMT_NOTIFICATION_HOOKS "CONFIG_MCUMGR_MGMT_NOTIFICATION_HOOKS") will need to be set to
enable the new notification system in addition to any migrations):

> - mgmt\_evt
>   :   Using [`MGMT_EVT_OP_CMD_RECV`](#c.smp_group_events.MGMT_EVT_OP_CMD_RECV),
>       [`MGMT_EVT_OP_CMD_STATUS`](#c.smp_group_events.MGMT_EVT_OP_CMD_STATUS), or
>       [`MGMT_EVT_OP_CMD_DONE`](#c.smp_group_events.MGMT_EVT_OP_CMD_DONE) as drop-in replacements for events of
>       the same name, where the provided data is [`mgmt_evt_op_cmd_arg`](#c.mgmt_evt_op_cmd_arg).
>       [`CONFIG_MCUMGR_SMP_COMMAND_STATUS_HOOKS`](../../kconfig.md#CONFIG_MCUMGR_SMP_COMMAND_STATUS_HOOKS "CONFIG_MCUMGR_SMP_COMMAND_STATUS_HOOKS") needs to be set.
> - fs\_mgmt\_register\_evt\_cb
>   :   Using [`MGMT_EVT_OP_FS_MGMT_FILE_ACCESS`](#c.fs_mgmt_group_events.MGMT_EVT_OP_FS_MGMT_FILE_ACCESS) where the provided
>       data is [`fs_mgmt_file_access`](#c.fs_mgmt_file_access). Instead of returning true to allow
>       the action or false to deny, a MCUmgr result code needs to be returned,
>       [`MGMT_ERR_EOK`](mcumgr.md#c.mcumgr_err_t.MGMT_ERR_EOK "MGMT_ERR_EOK") will allow the action, any other return code
>       will disallow it and return that code to the client
>       ([`MGMT_ERR_EACCESSDENIED`](mcumgr.md#c.mcumgr_err_t.MGMT_ERR_EACCESSDENIED "MGMT_ERR_EACCESSDENIED") can be used for an access denied
>       error). [`CONFIG_MCUMGR_GRP_IMG_STATUS_HOOKS`](../../kconfig.md#CONFIG_MCUMGR_GRP_IMG_STATUS_HOOKS "CONFIG_MCUMGR_GRP_IMG_STATUS_HOOKS") needs to be
>       set.
> - img\_mgmt\_register\_callbacks
>   :   Using [`MGMT_EVT_OP_IMG_MGMT_DFU_STARTED`](#c.img_mgmt_group_events.MGMT_EVT_OP_IMG_MGMT_DFU_STARTED) if
>       `dfu_started_cb` was used,
>       [`MGMT_EVT_OP_IMG_MGMT_DFU_STOPPED`](#c.img_mgmt_group_events.MGMT_EVT_OP_IMG_MGMT_DFU_STOPPED) if `dfu_stopped_cb` was
>       used, [`MGMT_EVT_OP_IMG_MGMT_DFU_PENDING`](#c.img_mgmt_group_events.MGMT_EVT_OP_IMG_MGMT_DFU_PENDING) if
>       `dfu_pending_cb` was used or
>       [`MGMT_EVT_OP_IMG_MGMT_DFU_CONFIRMED`](#c.img_mgmt_group_events.MGMT_EVT_OP_IMG_MGMT_DFU_CONFIRMED) if `dfu_confirmed_cb`
>       was used. These callbacks do not have any return status.
>       [`CONFIG_MCUMGR_GRP_IMG_STATUS_HOOKS`](../../kconfig.md#CONFIG_MCUMGR_GRP_IMG_STATUS_HOOKS "CONFIG_MCUMGR_GRP_IMG_STATUS_HOOKS") needs to be set.
> - img\_mgmt\_set\_upload\_cb
>   :   Using [`MGMT_EVT_OP_IMG_MGMT_DFU_CHUNK`](#c.img_mgmt_group_events.MGMT_EVT_OP_IMG_MGMT_DFU_CHUNK) where the provided
>       data is [`img_mgmt_upload_check`](#c.img_mgmt_upload_check). Instead of returning true to
>       allow the action or false to deny, a MCUmgr result code needs to be
>       returned, [`MGMT_ERR_EOK`](mcumgr.md#c.mcumgr_err_t.MGMT_ERR_EOK "MGMT_ERR_EOK") will allow the action, any other
>       return code will disallow it and return that code to the client
>       ([`MGMT_ERR_EACCESSDENIED`](mcumgr.md#c.mcumgr_err_t.MGMT_ERR_EACCESSDENIED "MGMT_ERR_EACCESSDENIED") can be used for an access denied
>       error). [`CONFIG_MCUMGR_GRP_IMG_UPLOAD_CHECK_HOOK`](../../kconfig.md#CONFIG_MCUMGR_GRP_IMG_UPLOAD_CHECK_HOOK "CONFIG_MCUMGR_GRP_IMG_UPLOAD_CHECK_HOOK") needs to
>       be set.
> - os\_mgmt\_register\_reset\_evt\_cb
>   :   Using [`MGMT_EVT_OP_OS_MGMT_RESET`](#c.os_mgmt_group_events.MGMT_EVT_OP_OS_MGMT_RESET). Instead of returning
>       true to allow the action or false to deny, a MCUmgr result code needs to be
>       returned, [`MGMT_ERR_EOK`](mcumgr.md#c.mcumgr_err_t.MGMT_ERR_EOK "MGMT_ERR_EOK") will allow the action, any other
>       return code will disallow it and return that code to the client
>       ([`MGMT_ERR_EACCESSDENIED`](mcumgr.md#c.mcumgr_err_t.MGMT_ERR_EACCESSDENIED "MGMT_ERR_EACCESSDENIED") can be used for an access denied
>       error). [`CONFIG_MCUMGR_SMP_COMMAND_STATUS_HOOKS`](../../kconfig.md#CONFIG_MCUMGR_SMP_COMMAND_STATUS_HOOKS "CONFIG_MCUMGR_SMP_COMMAND_STATUS_HOOKS") needs to
>       be set.

## API Reference

*group* mcumgr\_callback\_api
:   MCUmgr callback API.

    Defines

    MGMT\_EVT\_GET\_GROUP(event)
    :   Get group from event.

    MGMT\_EVT\_GET\_ID(event)
    :   Get event ID from event.

    MGMT\_CB\_ERROR\_RET

    Typedefs

    typedef enum [mgmt\_cb\_return](#c.mgmt_cb_return) (\*mgmt\_cb)(uint32\_t event, enum [mgmt\_cb\_return](#c.mgmt_cb_return) prev\_status, int32\_t \*rc, uint16\_t \*group, bool \*abort\_more, void \*data, size\_t data\_size)
    :   Function to be called on MGMT notification/event.

        This callback function is used to notify an application or system about a MCUmgr mgmt event.

        Param event:
        :   [mcumgr\_op\_t](mcumgr.md#group__mcumgr__mgmt__api_1gae06a618f492f18e856742b4affab80dd).

        Param prev\_status:
        :   [mgmt\_cb\_return](#group__mcumgr__callback__api_1ga1ba636c0efb7a91630ed9743e6fd4d6c) of the previous handler calls, if it is an error then it will be the first error that was returned by a handler (i.e. this handler is being called for a notification only, the return code will be ignored).

        Param rc:
        :   If `prev_status` is [MGMT\_CB\_ERROR\_RC](#group__mcumgr__callback__api_1gga1ba636c0efb7a91630ed9743e6fd4d6ca6ca7c4ba7dc1c300489da4a935b7d990) then this is the SMP error that was returned by the first handler that failed. If `prev_status` is [MGMT\_CB\_ERROR\_ERR](#group__mcumgr__callback__api_1gga1ba636c0efb7a91630ed9743e6fd4d6cad88f720a1d62658c346e8bebfb81d66d) then this will be the group error rc code returned by the first handler that failed. If the handler wishes to raise an SMP error, this must be set to the [mcumgr\_err\_t](mcumgr.md#group__mcumgr__mgmt__api_1gac5d8757a7ca945c77f405764b85ad5c5) status and [MGMT\_CB\_ERROR\_RC](#group__mcumgr__callback__api_1gga1ba636c0efb7a91630ed9743e6fd4d6ca6ca7c4ba7dc1c300489da4a935b7d990) must be returned by the function, if the handler wishes to raise a ret error, this must be set to the group ret status and [MGMT\_CB\_ERROR\_ERR](#group__mcumgr__callback__api_1gga1ba636c0efb7a91630ed9743e6fd4d6cad88f720a1d62658c346e8bebfb81d66d) must be returned by the function.

        Param group:
        :   If `prev_status` is [MGMT\_CB\_ERROR\_ERR](#group__mcumgr__callback__api_1gga1ba636c0efb7a91630ed9743e6fd4d6cad88f720a1d62658c346e8bebfb81d66d) then this is the group of the ret error that was returned by the first handler that failed. If the handler wishes to raise a ret error, this must be set to the group ret status and [MGMT\_CB\_ERROR\_ERR](#group__mcumgr__callback__api_1gga1ba636c0efb7a91630ed9743e6fd4d6cad88f720a1d62658c346e8bebfb81d66d) must be returned by the function.

        Param abort\_more:
        :   Set to true to abort further processing by additional handlers.

        Param data:
        :   Optional event argument.

        Param data\_size:
        :   Size of optional event argument (0 if no data is provided).

        Return:
        :   [mgmt\_cb\_return](#group__mcumgr__callback__api_1ga1ba636c0efb7a91630ed9743e6fd4d6c) indicating the status to return to the calling code (only checked when this is the first failure reported by a handler).

    Enums

    enum mgmt\_cb\_return
    :   MGMT event callback return value.

        *Values:*

        enumerator MGMT\_CB\_OK
        :   No error.

        enumerator MGMT\_CB\_ERROR\_RC
        :   SMP protocol error and `err_rc` contains the [mcumgr\_err\_t](mcumgr.md#group__mcumgr__mgmt__api_1gac5d8757a7ca945c77f405764b85ad5c5) error code.

        enumerator MGMT\_CB\_ERROR\_ERR
        :   Group (application-level) error and `err_group` contains the group ID that caused the error and `err_rc` contians the error code of that group to return.

    enum mgmt\_cb\_groups
    :   MGMT event callback group IDs.

        Note that this is not a 1:1 mapping with [mcumgr\_group\_t](mcumgr.md#group__mcumgr__mgmt__api_1ga81f98b9a0c3810f7d607b783f8e259b5) values.

        *Values:*

        enumerator MGMT\_EVT\_GRP\_ALL = 0

        enumerator MGMT\_EVT\_GRP\_SMP

        enumerator MGMT\_EVT\_GRP\_OS

        enumerator MGMT\_EVT\_GRP\_IMG

        enumerator MGMT\_EVT\_GRP\_FS

        enumerator MGMT\_EVT\_GRP\_SETTINGS

        enumerator MGMT\_EVT\_GRP\_USER\_CUSTOM\_START = [MGMT\_GROUP\_ID\_PERUSER](mcumgr.md#c.mcumgr_group_t.MGMT_GROUP_ID_PERUSER "MGMT_GROUP_ID_PERUSER")

    enum smp\_all\_events
    :   MGMT event opcodes for all command processing.

        *Values:*

        enumerator MGMT\_EVT\_OP\_ALL = MGMT\_DEF\_EVT\_OP\_ALL([MGMT\_EVT\_GRP\_ALL](#c.mgmt_cb_groups.MGMT_EVT_GRP_ALL))
        :   Used to enable all events.

    enum smp\_group\_events
    :   MGMT event opcodes for base SMP command processing.

        *Values:*

        enumerator MGMT\_EVT\_OP\_CMD\_RECV = MGMT\_DEF\_EVT\_OP\_ID([MGMT\_EVT\_GRP\_SMP](#c.mgmt_cb_groups.MGMT_EVT_GRP_SMP), 0)
        :   Callback when a command is received, data is [mgmt\_evt\_op\_cmd\_arg()](#structmgmt__evt__op__cmd__arg).

        enumerator MGMT\_EVT\_OP\_CMD\_STATUS = MGMT\_DEF\_EVT\_OP\_ID([MGMT\_EVT\_GRP\_SMP](#c.mgmt_cb_groups.MGMT_EVT_GRP_SMP), 1)
        :   Callback when a a status is updated, data is [mgmt\_evt\_op\_cmd\_arg()](#structmgmt__evt__op__cmd__arg).

        enumerator MGMT\_EVT\_OP\_CMD\_DONE = MGMT\_DEF\_EVT\_OP\_ID([MGMT\_EVT\_GRP\_SMP](#c.mgmt_cb_groups.MGMT_EVT_GRP_SMP), 2)
        :   Callback when a command has been processed, data is [mgmt\_evt\_op\_cmd\_arg()](#structmgmt__evt__op__cmd__arg).

        enumerator MGMT\_EVT\_OP\_CMD\_ALL = MGMT\_DEF\_EVT\_OP\_ALL([MGMT\_EVT\_GRP\_SMP](#c.mgmt_cb_groups.MGMT_EVT_GRP_SMP))
        :   Used to enable all smp\_group events.

    enum fs\_mgmt\_group\_events
    :   MGMT event opcodes for filesystem management group.

        *Values:*

        enumerator MGMT\_EVT\_OP\_FS\_MGMT\_FILE\_ACCESS = MGMT\_DEF\_EVT\_OP\_ID([MGMT\_EVT\_GRP\_FS](#c.mgmt_cb_groups.MGMT_EVT_GRP_FS), 0)
        :   Callback when a file has been accessed, data is [fs\_mgmt\_file\_access()](#structfs__mgmt__file__access).

        enumerator MGMT\_EVT\_OP\_FS\_MGMT\_ALL = MGMT\_DEF\_EVT\_OP\_ALL([MGMT\_EVT\_GRP\_FS](#c.mgmt_cb_groups.MGMT_EVT_GRP_FS))
        :   Used to enable all fs\_mgmt\_group events.

    enum img\_mgmt\_group\_events
    :   MGMT event opcodes for image management group.

        *Values:*

        enumerator MGMT\_EVT\_OP\_IMG\_MGMT\_DFU\_CHUNK = MGMT\_DEF\_EVT\_OP\_ID([MGMT\_EVT\_GRP\_IMG](#c.mgmt_cb_groups.MGMT_EVT_GRP_IMG), 0)
        :   Callback when a client sends a file upload chunk, data is [img\_mgmt\_upload\_check()](#structimg__mgmt__upload__check).

        enumerator MGMT\_EVT\_OP\_IMG\_MGMT\_DFU\_STOPPED = MGMT\_DEF\_EVT\_OP\_ID([MGMT\_EVT\_GRP\_IMG](#c.mgmt_cb_groups.MGMT_EVT_GRP_IMG), 1)
        :   Callback when a DFU operation is stopped.

        enumerator MGMT\_EVT\_OP\_IMG\_MGMT\_DFU\_STARTED = MGMT\_DEF\_EVT\_OP\_ID([MGMT\_EVT\_GRP\_IMG](#c.mgmt_cb_groups.MGMT_EVT_GRP_IMG), 2)
        :   Callback when a DFU operation is started.

        enumerator MGMT\_EVT\_OP\_IMG\_MGMT\_DFU\_PENDING = MGMT\_DEF\_EVT\_OP\_ID([MGMT\_EVT\_GRP\_IMG](#c.mgmt_cb_groups.MGMT_EVT_GRP_IMG), 3)
        :   Callback when a DFU operation has finished being transferred.

        enumerator MGMT\_EVT\_OP\_IMG\_MGMT\_DFU\_CONFIRMED = MGMT\_DEF\_EVT\_OP\_ID([MGMT\_EVT\_GRP\_IMG](#c.mgmt_cb_groups.MGMT_EVT_GRP_IMG), 4)
        :   Callback when an image has been confirmed.

        enumerator MGMT\_EVT\_OP\_IMG\_MGMT\_DFU\_CHUNK\_WRITE\_COMPLETE = MGMT\_DEF\_EVT\_OP\_ID([MGMT\_EVT\_GRP\_IMG](#c.mgmt_cb_groups.MGMT_EVT_GRP_IMG), 5)
        :   Callback when an image write command has finished writing to flash.

        enumerator MGMT\_EVT\_OP\_IMG\_MGMT\_ALL = MGMT\_DEF\_EVT\_OP\_ALL([MGMT\_EVT\_GRP\_IMG](#c.mgmt_cb_groups.MGMT_EVT_GRP_IMG))
        :   Used to enable all img\_mgmt\_group events.

    enum os\_mgmt\_group\_events
    :   MGMT event opcodes for operating system management group.

        *Values:*

        enumerator MGMT\_EVT\_OP\_OS\_MGMT\_RESET = MGMT\_DEF\_EVT\_OP\_ID([MGMT\_EVT\_GRP\_OS](#c.mgmt_cb_groups.MGMT_EVT_GRP_OS), 0)
        :   Callback when a reset command has been received, data is [os\_mgmt\_reset\_data](#structos__mgmt__reset__data).

        enumerator MGMT\_EVT\_OP\_OS\_MGMT\_INFO\_CHECK = MGMT\_DEF\_EVT\_OP\_ID([MGMT\_EVT\_GRP\_OS](#c.mgmt_cb_groups.MGMT_EVT_GRP_OS), 1)
        :   Callback when an info command is processed, data is os\_mgmt\_info\_check.

        enumerator MGMT\_EVT\_OP\_OS\_MGMT\_INFO\_APPEND = MGMT\_DEF\_EVT\_OP\_ID([MGMT\_EVT\_GRP\_OS](#c.mgmt_cb_groups.MGMT_EVT_GRP_OS), 2)
        :   Callback when an info command needs to output data, data is os\_mgmt\_info\_append.

        enumerator MGMT\_EVT\_OP\_OS\_MGMT\_DATETIME\_GET = MGMT\_DEF\_EVT\_OP\_ID([MGMT\_EVT\_GRP\_OS](#c.mgmt_cb_groups.MGMT_EVT_GRP_OS), 3)
        :   Callback when a datetime get command has been received.

        enumerator MGMT\_EVT\_OP\_OS\_MGMT\_DATETIME\_SET = MGMT\_DEF\_EVT\_OP\_ID([MGMT\_EVT\_GRP\_OS](#c.mgmt_cb_groups.MGMT_EVT_GRP_OS), 4)
        :   Callback when a datetime set command has been received, data is struct [rtc\_time()](../../hardware/peripherals/rtc.md#structrtc__time).

        enumerator MGMT\_EVT\_OP\_OS\_MGMT\_ALL = MGMT\_DEF\_EVT\_OP\_ALL([MGMT\_EVT\_GRP\_OS](#c.mgmt_cb_groups.MGMT_EVT_GRP_OS))
        :   Used to enable all os\_mgmt\_group events.

    enum settings\_mgmt\_group\_events
    :   MGMT event opcodes for settings management group.

        *Values:*

        enumerator MGMT\_EVT\_OP\_SETTINGS\_MGMT\_ACCESS = MGMT\_DEF\_EVT\_OP\_ID([MGMT\_EVT\_GRP\_SETTINGS](#c.mgmt_cb_groups.MGMT_EVT_GRP_SETTINGS), 0)
        :   Callback when a setting is read/written/deleted.

        enumerator MGMT\_EVT\_OP\_SETTINGS\_MGMT\_ALL = MGMT\_DEF\_EVT\_OP\_ALL([MGMT\_EVT\_GRP\_SETTINGS](#c.mgmt_cb_groups.MGMT_EVT_GRP_SETTINGS))
        :   Used to enable all settings\_mgmt\_group events.

    Functions

    uint8\_t mgmt\_evt\_get\_index(uint32\_t event)
    :   Get event ID index from event.

        Parameters:
        :   - **event** – Event to get ID index from.

        Returns:
        :   Event index.

    enum [mgmt\_cb\_return](#c.mgmt_cb_return) mgmt\_callback\_notify(uint32\_t event, void \*data, size\_t data\_size, int32\_t \*err\_rc, uint16\_t \*err\_group)
    :   This function is called to notify registered callbacks about mcumgr notifications/events.

        Parameters:
        :   - **event** – [mcumgr\_op\_t](mcumgr.md#group__mcumgr__mgmt__api_1gae06a618f492f18e856742b4affab80dd).
            - **data** – Optional event argument.
            - **data\_size** – Size of optional event argument (0 if none).
            - **err\_rc** – Pointer to rc value.
            - **err\_group** – Pointer to group value.

        Returns:
        :   [mgmt\_cb\_return](#group__mcumgr__callback__api_1ga1ba636c0efb7a91630ed9743e6fd4d6c) either [MGMT\_CB\_OK](#group__mcumgr__callback__api_1gga1ba636c0efb7a91630ed9743e6fd4d6cac9a6240975af04d413048d762ca1b0da) if all handlers returned it, or [MGMT\_CB\_ERROR\_RC](#group__mcumgr__callback__api_1gga1ba636c0efb7a91630ed9743e6fd4d6ca6ca7c4ba7dc1c300489da4a935b7d990) if the first failed handler returned an SMP error (in which case `err_rc` will be updated with the SMP error) or [MGMT\_CB\_ERROR\_ERR](#group__mcumgr__callback__api_1gga1ba636c0efb7a91630ed9743e6fd4d6cad88f720a1d62658c346e8bebfb81d66d) if the first failed handler returned a ret group and error (in which case `err_group` will be updated with the failed group ID and `err_rc` will be updated with the group-specific error code).

    void mgmt\_callback\_register(struct [mgmt\_callback](#c.mgmt_callback) \*callback)
    :   Register event callback function.

        Parameters:
        :   - **callback** – Callback struct.

    void mgmt\_callback\_unregister(struct [mgmt\_callback](#c.mgmt_callback) \*callback)
    :   Unregister event callback function.

        Parameters:
        :   - **callback** – Callback struct.

    struct mgmt\_callback
    :   *#include <callbacks.h>*

        MGMT callback struct.

        Public Members

        [sys\_snode\_t](../../kernel/data_structures/slist.md#c.sys_snode_t "sys_snode_t") node
        :   Entry list node.

        [mgmt\_cb](#c.mgmt_cb) callback
        :   Callback that will be called.

        uint32\_t event\_id
        :   MGMT\_EVT\_[…] Event ID for handler to be called on.

            This has special meaning if [MGMT\_EVT\_OP\_ALL](#group__mcumgr__callback__api_1ggaab6470007be89e5aab88838456f9561aaf9e289ad5f7e0fd8bec581f67951813a) is used (which will cover all events for all groups), or MGMT\_EVT\_OP\_\*\_MGMT\_ALL (which will cover all events for a single group). For events that are part of a single group, they can be or’d together for this to have one registration trigger on multiple events, please note that this will only work for a single group, to register for events in different groups, they must be registered separately.

    struct mgmt\_evt\_op\_cmd\_arg
    :   *#include <callbacks.h>*

        Arguments for [MGMT\_EVT\_OP\_CMD\_RECV](#group__mcumgr__callback__api_1gga590788274b4508c6203685d9e9252184a933f494aa22d52d536bb6c3de0dbeb28), [MGMT\_EVT\_OP\_CMD\_STATUS](#group__mcumgr__callback__api_1gga590788274b4508c6203685d9e9252184afc1cee09954cdc6dfaee196dd7518770) and [MGMT\_EVT\_OP\_CMD\_DONE](#group__mcumgr__callback__api_1gga590788274b4508c6203685d9e9252184adb820d1a8cdea6c74a5a39f096deab12).

        Public Members

        uint16\_t group
        :   [mcumgr\_group\_t](mcumgr.md#group__mcumgr__mgmt__api_1ga81f98b9a0c3810f7d607b783f8e259b5)

        uint8\_t id
        :   Message ID within group.

        uint8\_t op
        :   [mcumgr\_op\_t](mcumgr.md#group__mcumgr__mgmt__api_1gae06a618f492f18e856742b4affab80dd) used in [MGMT\_EVT\_OP\_CMD\_RECV](#group__mcumgr__callback__api_1gga590788274b4508c6203685d9e9252184a933f494aa22d52d536bb6c3de0dbeb28)

        int err
        :   [mcumgr\_err\_t](mcumgr.md#group__mcumgr__mgmt__api_1gac5d8757a7ca945c77f405764b85ad5c5), used in [MGMT\_EVT\_OP\_CMD\_DONE](#group__mcumgr__callback__api_1gga590788274b4508c6203685d9e9252184adb820d1a8cdea6c74a5a39f096deab12)

        int status
        :   img\_mgmt\_id\_upload\_t, used in [MGMT\_EVT\_OP\_CMD\_STATUS](#group__mcumgr__callback__api_1gga590788274b4508c6203685d9e9252184afc1cee09954cdc6dfaee196dd7518770)

    MCUmgr fs\_mgmt callback API.

    Enums

    enum fs\_mgmt\_file\_access\_types
    :   The type of operation that is being requested for a given file access callback.

        *Values:*

        enumerator FS\_MGMT\_FILE\_ACCESS\_READ
        :   Access to read file (file upload).

        enumerator FS\_MGMT\_FILE\_ACCESS\_WRITE
        :   Access to write file (file download).

        enumerator FS\_MGMT\_FILE\_ACCESS\_STATUS
        :   Access to get status of file.

        enumerator FS\_MGMT\_FILE\_ACCESS\_HASH\_CHECKSUM
        :   Access to calculate hash or checksum of file.

    struct fs\_mgmt\_file\_access
    :   *#include <fs\_mgmt\_callbacks.h>*

        Structure provided in the [MGMT\_EVT\_OP\_FS\_MGMT\_FILE\_ACCESS](#group__mcumgr__callback__api_1gga324223c20cbefe3400272e2789082c79a0475953c86b97afa8e4ed30da3f736d3) notification callback: This callback function is used to notify the application about a pending file read/write request and to authorise or deny it.

        Access will be allowed so long as all notification handlers return [MGMT\_ERR\_EOK](mcumgr.md#group__mcumgr__mgmt__api_1ggac5d8757a7ca945c77f405764b85ad5c5a4201fc6fbffd1ca9ae99a2e90a40896f), if one returns an error then access will be denied.

        Public Members

        enum [fs\_mgmt\_file\_access\_types](#c.fs_mgmt_file_access_types) access
        :   Specifies the type of the operation that is being requested.

        char \*filename
        :   Path and filename of file be accesses, note that this can be changed by handlers to redirect file access if needed (as long as it does not exceed the maximum path string size).

    MCUmgr img\_mgmt callback API.

    struct img\_mgmt\_upload\_check
    :   *#include <img\_mgmt\_callbacks.h>*

        Structure provided in the [MGMT\_EVT\_OP\_IMG\_MGMT\_DFU\_CHUNK](#group__mcumgr__callback__api_1gga3fa2c42bade08cca1122e32f6315f107a19d53f0c0f6649858e97fbcecfbaf24c) notification callback: This callback function is used to notify the application about a pending firmware upload packet from a client and authorise or deny it.

        Upload will be allowed so long as all notification handlers return [MGMT\_ERR\_EOK](mcumgr.md#group__mcumgr__mgmt__api_1ggac5d8757a7ca945c77f405764b85ad5c5a4201fc6fbffd1ca9ae99a2e90a40896f), if one returns an error then the upload will be denied.

        Public Members

        struct img\_mgmt\_upload\_action \*action
        :   Action to take.

        struct img\_mgmt\_upload\_req \*req
        :   Upload request information.

    MCUmgr os\_mgmt callback API.

    struct os\_mgmt\_reset\_data
    :   *#include <os\_mgmt\_callbacks.h>*

        Structure provided in the [MGMT\_EVT\_OP\_OS\_MGMT\_RESET](#group__mcumgr__callback__api_1gga261346c700a2522542d8282ca76f88a5a9feea9f8cfcca803a18be03e08583c52) notification callback: This callback function is used to notify the application about a pending device reboot request and to authorise or deny it.

        Public Members

        bool force
        :   Contains the value of the force parameter.

    MCUmgr settings\_mgmt callback API.

    Enums

    enum settings\_mgmt\_access\_types
    :   *Values:*

        enumerator SETTINGS\_ACCESS\_READ

        enumerator SETTINGS\_ACCESS\_WRITE

        enumerator SETTINGS\_ACCESS\_DELETE

        enumerator SETTINGS\_ACCESS\_COMMIT

        enumerator SETTINGS\_ACCESS\_LOAD

        enumerator SETTINGS\_ACCESS\_SAVE

    struct settings\_mgmt\_access
    :   *#include <settings\_mgmt\_callbacks.h>*

        Structure provided in the [MGMT\_EVT\_OP\_SETTINGS\_MGMT\_ACCESS](#group__mcumgr__callback__api_1gga1711bc9f45a8114a6b0c89db4a40e3dea65c675aa2e807d9977a5ff13a97c75a0) notification callback: This callback function is used to notify the application about a pending setting read/write/delete/load/save/commit request and to authorise or deny it.

        Access will be allowed so long as no handlers return an error, if one returns an error then access will be denied.

        Public Members

        enum [settings\_mgmt\_access\_types](#c.settings_mgmt_access_types) access
        :   Type of access.

        char \*name
        :   Key name for accesses (only set for SETTINGS\_ACCESS\_READ, SETTINGS\_ACCESS\_WRITE and SETTINGS\_ACCESS\_DELETE).

            Note that this can be changed by handlers to redirect settings access if needed (as long as it does not exceed the maximum setting string size) if CONFIG\_MCUMGR\_GRP\_SETTINGS\_BUFFER\_TYPE\_STACK is selected, of maximum size CONFIG\_MCUMGR\_GRP\_SETTINGS\_NAME\_LEN.

            Note: This string *must* be NULL terminated.

        const uint8\_t \*val
        :   Data provided by the user (only set for SETTINGS\_ACCESS\_WRITE).

        const size\_t \*val\_length
        :   Length of data provided by the user (only set for SETTINGS\_ACCESS\_WRITE).

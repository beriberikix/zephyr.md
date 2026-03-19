---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/services/device_mgmt/mcumgr_callbacks.html
original_path: services/device_mgmt/mcumgr_callbacks.html
---

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
[`mgmt_cb`](../../doxygen/html/group__mcumgr__callback__api.md#gae61f705224a859776ee5161dfda5ed7d) type definition can then be declared and registered by
calling [`mgmt_callback_register()`](../../doxygen/html/group__mcumgr__callback__api.md#gaaf698627904995930784c96fb48a1d7b) for the desired event inside of a
[`mgmt_callback`](../../doxygen/html/structmgmt__callback.md) structure. Handlers are called in the order that they
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

This code registers a handler for the [`MGMT_EVT_OP_CMD_DONE`](../../doxygen/html/group__mcumgr__callback__api.md#gga590788274b4508c6203685d9e9252184adb820d1a8cdea6c74a5a39f096deab12)
event, which will be called after a MCUmgr command has been processed and
output generated, note that this requires that
[`CONFIG_MCUMGR_SMP_COMMAND_STATUS_HOOKS`](../../kconfig.md#CONFIG_MCUMGR_SMP_COMMAND_STATUS_HOOKS "CONFIG_MCUMGR_SMP_COMMAND_STATUS_HOOKS") be enabled to receive
this callback.

Multiple callbacks can be setup to use a single function as a common callback,
and many different functions can be used for each event by registering each
group once, or all notifications for a whole group can be enabled by using one
of the `MGMT_EVT_OP_*_ALL` events, alternatively a handler can setup for
every notification by using [`MGMT_EVT_OP_ALL`](../../doxygen/html/group__mcumgr__callback__api.md#ggaab6470007be89e5aab88838456f9561aaf9e289ad5f7e0fd8bec581f67951813a). When setting up
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
>   :   MCUmgr command status ([`MGMT_EVT_OP_CMD_RECV`](../../doxygen/html/group__mcumgr__callback__api.md#gga590788274b4508c6203685d9e9252184a933f494aa22d52d536bb6c3de0dbeb28),
>       [`MGMT_EVT_OP_CMD_STATUS`](../../doxygen/html/group__mcumgr__callback__api.md#gga590788274b4508c6203685d9e9252184afc1cee09954cdc6dfaee196dd7518770),
>       [`MGMT_EVT_OP_CMD_DONE`](../../doxygen/html/group__mcumgr__callback__api.md#gga590788274b4508c6203685d9e9252184adb820d1a8cdea6c74a5a39f096deab12))
> - [`CONFIG_MCUMGR_GRP_FS_FILE_ACCESS_HOOK`](../../kconfig.md#CONFIG_MCUMGR_GRP_FS_FILE_ACCESS_HOOK "CONFIG_MCUMGR_GRP_FS_FILE_ACCESS_HOOK")
>   :   fs\_mgmt file access ([`MGMT_EVT_OP_FS_MGMT_FILE_ACCESS`](../../doxygen/html/group__mcumgr__callback__api.md#gga324223c20cbefe3400272e2789082c79a0475953c86b97afa8e4ed30da3f736d3))
> - [`CONFIG_MCUMGR_GRP_IMG_UPLOAD_CHECK_HOOK`](../../kconfig.md#CONFIG_MCUMGR_GRP_IMG_UPLOAD_CHECK_HOOK "CONFIG_MCUMGR_GRP_IMG_UPLOAD_CHECK_HOOK")
>   :   img\_mgmt upload check ([`MGMT_EVT_OP_IMG_MGMT_DFU_CHUNK`](../../doxygen/html/group__mcumgr__callback__api.md#gga3fa2c42bade08cca1122e32f6315f107a19d53f0c0f6649858e97fbcecfbaf24c))
> - [`CONFIG_MCUMGR_GRP_IMG_STATUS_HOOKS`](../../kconfig.md#CONFIG_MCUMGR_GRP_IMG_STATUS_HOOKS "CONFIG_MCUMGR_GRP_IMG_STATUS_HOOKS")
>   :   img\_mgmt upload status ([`MGMT_EVT_OP_IMG_MGMT_DFU_STOPPED`](../../doxygen/html/group__mcumgr__callback__api.md#gga3fa2c42bade08cca1122e32f6315f107af6424b9e8f800bde22a764da459a50a8),
>       [`MGMT_EVT_OP_IMG_MGMT_DFU_STARTED`](../../doxygen/html/group__mcumgr__callback__api.md#gga3fa2c42bade08cca1122e32f6315f107af8836c552e137e15d5e859515f067bbf),
>       [`MGMT_EVT_OP_IMG_MGMT_DFU_PENDING`](../../doxygen/html/group__mcumgr__callback__api.md#gga3fa2c42bade08cca1122e32f6315f107a2ff64450efa47d0d460c866f5634bce4),
>       [`MGMT_EVT_OP_IMG_MGMT_DFU_CONFIRMED`](../../doxygen/html/group__mcumgr__callback__api.md#gga3fa2c42bade08cca1122e32f6315f107a36e486e194d0d6013d188b4ed70a95fb))
> - [`CONFIG_MCUMGR_GRP_OS_RESET_HOOK`](../../kconfig.md#CONFIG_MCUMGR_GRP_OS_RESET_HOOK "CONFIG_MCUMGR_GRP_OS_RESET_HOOK")
>   :   os\_mgmt reset check ([`MGMT_EVT_OP_OS_MGMT_RESET`](../../doxygen/html/group__mcumgr__callback__api.md#gga261346c700a2522542d8282ca76f88a5a9feea9f8cfcca803a18be03e08583c52))
> - [`CONFIG_MCUMGR_GRP_SETTINGS_ACCESS_HOOK`](../../kconfig.md#CONFIG_MCUMGR_GRP_SETTINGS_ACCESS_HOOK "CONFIG_MCUMGR_GRP_SETTINGS_ACCESS_HOOK")
>   :   settings\_mgmt access ([`MGMT_EVT_OP_SETTINGS_MGMT_ACCESS`](../../doxygen/html/group__mcumgr__callback__api.md#gga1711bc9f45a8114a6b0c89db4a40e3dea65c675aa2e807d9977a5ff13a97c75a0))

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
[`MGMT_EVT_OP_FS_MGMT_FILE_ACCESS`](../../doxygen/html/group__mcumgr__callback__api.md#gga324223c20cbefe3400272e2789082c79a0475953c86b97afa8e4ed30da3f736d3) event, which will be called
after a fs\_mgmt file read/write command has been received to check if access to
the file should be allowed or not, note that this requires that
[`CONFIG_MCUMGR_GRP_FS_FILE_ACCESS_HOOK`](../../kconfig.md#CONFIG_MCUMGR_GRP_FS_FILE_ACCESS_HOOK "CONFIG_MCUMGR_GRP_FS_FILE_ACCESS_HOOK") be enabled to receive
this callback.
Two types of errors can be returned, the `rc` parameter can be set to an
[`mcumgr_err_t`](../../doxygen/html/group__mcumgr__mgmt__api.md#gac5d8757a7ca945c77f405764b85ad5c5) error code and [`MGMT_CB_ERROR_RC`](../../doxygen/html/group__mcumgr__callback__api.md#gga1ba636c0efb7a91630ed9743e6fd4d6ca6ca7c4ba7dc1c300489da4a935b7d990)
can be returned, or a group error code (introduced with version 2 of the MCUmgr
protocol) can be set by setting the `group` value to the group and `rc`
value to the group error code and returning [`MGMT_CB_ERROR_ERR`](../../doxygen/html/group__mcumgr__callback__api.md#gga1ba636c0efb7a91630ed9743e6fd4d6cad88f720a1d62658c346e8bebfb81d66d).

### MCUmgr Command Callback Usage/Adding New Event Types

To add a callback to a MCUmgr command, [`mgmt_callback_notify()`](../../doxygen/html/group__mcumgr__callback__api.md#gaf9308502f8137f7fb80667941cdd46ca) can be
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
to register for callbacks using [`mgmt_callback_register()`](../../doxygen/html/group__mcumgr__callback__api.md#gaaf698627904995930784c96fb48a1d7b) (note that
[`CONFIG_MCUMGR_MGMT_NOTIFICATION_HOOKS`](../../kconfig.md#CONFIG_MCUMGR_MGMT_NOTIFICATION_HOOKS "CONFIG_MCUMGR_MGMT_NOTIFICATION_HOOKS") will need to be set to
enable the new notification system in addition to any migrations):

> - mgmt\_evt
>   :   Using [`MGMT_EVT_OP_CMD_RECV`](../../doxygen/html/group__mcumgr__callback__api.md#gga590788274b4508c6203685d9e9252184a933f494aa22d52d536bb6c3de0dbeb28),
>       [`MGMT_EVT_OP_CMD_STATUS`](../../doxygen/html/group__mcumgr__callback__api.md#gga590788274b4508c6203685d9e9252184afc1cee09954cdc6dfaee196dd7518770), or
>       [`MGMT_EVT_OP_CMD_DONE`](../../doxygen/html/group__mcumgr__callback__api.md#gga590788274b4508c6203685d9e9252184adb820d1a8cdea6c74a5a39f096deab12) as drop-in replacements for events of
>       the same name, where the provided data is [`mgmt_evt_op_cmd_arg`](../../doxygen/html/structmgmt__evt__op__cmd__arg.md).
>       [`CONFIG_MCUMGR_SMP_COMMAND_STATUS_HOOKS`](../../kconfig.md#CONFIG_MCUMGR_SMP_COMMAND_STATUS_HOOKS "CONFIG_MCUMGR_SMP_COMMAND_STATUS_HOOKS") needs to be set.
> - fs\_mgmt\_register\_evt\_cb
>   :   Using [`MGMT_EVT_OP_FS_MGMT_FILE_ACCESS`](../../doxygen/html/group__mcumgr__callback__api.md#gga324223c20cbefe3400272e2789082c79a0475953c86b97afa8e4ed30da3f736d3) where the provided
>       data is [`fs_mgmt_file_access`](../../doxygen/html/structfs__mgmt__file__access.md). Instead of returning true to allow
>       the action or false to deny, a MCUmgr result code needs to be returned,
>       [`MGMT_ERR_EOK`](../../doxygen/html/group__mcumgr__mgmt__api.md#ggac5d8757a7ca945c77f405764b85ad5c5a4201fc6fbffd1ca9ae99a2e90a40896f) will allow the action, any other return code
>       will disallow it and return that code to the client
>       ([`MGMT_ERR_EACCESSDENIED`](../../doxygen/html/group__mcumgr__mgmt__api.md#ggac5d8757a7ca945c77f405764b85ad5c5aa43ccd2b916bcf346b202a8e0e5e4bde) can be used for an access denied
>       error). [`CONFIG_MCUMGR_GRP_IMG_STATUS_HOOKS`](../../kconfig.md#CONFIG_MCUMGR_GRP_IMG_STATUS_HOOKS "CONFIG_MCUMGR_GRP_IMG_STATUS_HOOKS") needs to be
>       set.
> - img\_mgmt\_register\_callbacks
>   :   Using [`MGMT_EVT_OP_IMG_MGMT_DFU_STARTED`](../../doxygen/html/group__mcumgr__callback__api.md#gga3fa2c42bade08cca1122e32f6315f107af8836c552e137e15d5e859515f067bbf) if
>       `dfu_started_cb` was used,
>       [`MGMT_EVT_OP_IMG_MGMT_DFU_STOPPED`](../../doxygen/html/group__mcumgr__callback__api.md#gga3fa2c42bade08cca1122e32f6315f107af6424b9e8f800bde22a764da459a50a8) if `dfu_stopped_cb` was
>       used, [`MGMT_EVT_OP_IMG_MGMT_DFU_PENDING`](../../doxygen/html/group__mcumgr__callback__api.md#gga3fa2c42bade08cca1122e32f6315f107a2ff64450efa47d0d460c866f5634bce4) if
>       `dfu_pending_cb` was used or
>       [`MGMT_EVT_OP_IMG_MGMT_DFU_CONFIRMED`](../../doxygen/html/group__mcumgr__callback__api.md#gga3fa2c42bade08cca1122e32f6315f107a36e486e194d0d6013d188b4ed70a95fb) if `dfu_confirmed_cb`
>       was used. These callbacks do not have any return status.
>       [`CONFIG_MCUMGR_GRP_IMG_STATUS_HOOKS`](../../kconfig.md#CONFIG_MCUMGR_GRP_IMG_STATUS_HOOKS "CONFIG_MCUMGR_GRP_IMG_STATUS_HOOKS") needs to be set.
> - img\_mgmt\_set\_upload\_cb
>   :   Using [`MGMT_EVT_OP_IMG_MGMT_DFU_CHUNK`](../../doxygen/html/group__mcumgr__callback__api.md#gga3fa2c42bade08cca1122e32f6315f107a19d53f0c0f6649858e97fbcecfbaf24c) where the provided
>       data is [`img_mgmt_upload_check`](../../doxygen/html/structimg__mgmt__upload__check.md). Instead of returning true to
>       allow the action or false to deny, a MCUmgr result code needs to be
>       returned, [`MGMT_ERR_EOK`](../../doxygen/html/group__mcumgr__mgmt__api.md#ggac5d8757a7ca945c77f405764b85ad5c5a4201fc6fbffd1ca9ae99a2e90a40896f) will allow the action, any other
>       return code will disallow it and return that code to the client
>       ([`MGMT_ERR_EACCESSDENIED`](../../doxygen/html/group__mcumgr__mgmt__api.md#ggac5d8757a7ca945c77f405764b85ad5c5aa43ccd2b916bcf346b202a8e0e5e4bde) can be used for an access denied
>       error). [`CONFIG_MCUMGR_GRP_IMG_UPLOAD_CHECK_HOOK`](../../kconfig.md#CONFIG_MCUMGR_GRP_IMG_UPLOAD_CHECK_HOOK "CONFIG_MCUMGR_GRP_IMG_UPLOAD_CHECK_HOOK") needs to
>       be set.
> - os\_mgmt\_register\_reset\_evt\_cb
>   :   Using [`MGMT_EVT_OP_OS_MGMT_RESET`](../../doxygen/html/group__mcumgr__callback__api.md#gga261346c700a2522542d8282ca76f88a5a9feea9f8cfcca803a18be03e08583c52). Instead of returning
>       true to allow the action or false to deny, a MCUmgr result code needs to be
>       returned, [`MGMT_ERR_EOK`](../../doxygen/html/group__mcumgr__mgmt__api.md#ggac5d8757a7ca945c77f405764b85ad5c5a4201fc6fbffd1ca9ae99a2e90a40896f) will allow the action, any other
>       return code will disallow it and return that code to the client
>       ([`MGMT_ERR_EACCESSDENIED`](../../doxygen/html/group__mcumgr__mgmt__api.md#ggac5d8757a7ca945c77f405764b85ad5c5aa43ccd2b916bcf346b202a8e0e5e4bde) can be used for an access denied
>       error). [`CONFIG_MCUMGR_SMP_COMMAND_STATUS_HOOKS`](../../kconfig.md#CONFIG_MCUMGR_SMP_COMMAND_STATUS_HOOKS "CONFIG_MCUMGR_SMP_COMMAND_STATUS_HOOKS") needs to
>       be set.

## API Reference

[MCUmgr callback API](../../doxygen/html/group__mcumgr__callback__api.md)

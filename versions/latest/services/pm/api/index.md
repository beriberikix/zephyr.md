---
version: v3.6.0
source_url: https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/3.6.0/doc/services/pm/api/index.html
original_path: services/pm/api/index.html
---

This is the documentation for the latest (main) development branch of
Zephyr. If you are looking for the documentation of previous releases, use
the drop-down menu on the left and select the desired version.

# Power Management

## System PM APIs

*group* subsys\_pm\_sys
:   System Power Management API.

    Functions

    bool pm\_state\_force(uint8\_t cpu, const struct [pm\_state\_info](#c.pm_state_info) \*info)
    :   Force usage of given power state.

        This function overrides decision made by PM policy forcing usage of given power state upon next entry of the idle thread.

        Note

        This function can only run in thread context

        Parameters:
        :   - **cpu** – CPU index.
            - **info** – Power state which should be used in the ongoing suspend operation.

    void pm\_notifier\_register(struct [pm\_notifier](#c.pm_notifier) \*notifier)
    :   Register a power management notifier.

        Register the given notifier from the power management notification list.

        Parameters:
        :   - **notifier** – [pm\_notifier](#structpm__notifier) object to be registered.

    int pm\_notifier\_unregister(struct [pm\_notifier](#c.pm_notifier) \*notifier)
    :   Unregister a power management notifier.

        Remove the given notifier from the power management notification list. After that this object callbacks will not be called.

        Parameters:
        :   - **notifier** – [pm\_notifier](#structpm__notifier) object to be unregistered.

        Returns:
        :   0 if the notifier was successfully removed, a negative value otherwise.

    const struct [pm\_state\_info](#c.pm_state_info) \*pm\_state\_next\_get(uint8\_t cpu)
    :   Gets the next power state that will be used.

        This function returns the next power state that will be used by the SoC.

        Parameters:
        :   - **cpu** – CPU index.

        Returns:
        :   next [pm\_state\_info](#structpm__state__info) that will be used

    struct pm\_notifier
    :   *#include <pm.h>*

        Power management notifier struct.

        This struct contains callbacks that are called when the target enters and exits power states.

        As currently implemented the entry callback is invoked when transitioning from PM\_STATE\_ACTIVE to another state, and the exit callback is invoked when transitioning from a non-active state to PM\_STATE\_ACTIVE. This behavior may change in the future.

        Note

        These callbacks can be called from the ISR of the event that caused the kernel exit from idling.

        Note

        It is not allowed to call [pm\_notifier\_unregister](#group__subsys__pm__sys_1gab0856d662e50a3847a1b70cb8370849a) or [pm\_notifier\_register](#group__subsys__pm__sys_1ga066945118b8f287ee56aacf41b677a78) from these callbacks because they are called with the spin locked in those functions.

        Public Members

        void (\*state\_entry)(enum [pm\_state](#c.pm_state) state)
        :   Application defined function for doing any target specific operations for power state entry.

        void (\*state\_exit)(enum [pm\_state](#c.pm_state) state)
        :   Application defined function for doing any target specific operations for power state exit.

### States

*group* subsys\_pm\_states
:   System Power Management States.

    Defines

    PM\_STATE\_INFO\_DT\_INIT(node\_id)
    :   Initializer for struct [pm\_state\_info](#structpm__state__info) given a DT node identifier with zephyr,power-state compatible.

        Parameters:
        :   - **node\_id** – A node identifier with compatible zephyr,power-state

    PM\_STATE\_DT\_INIT(node\_id)
    :   Initializer for enum [pm\_state](#group__subsys__pm__states_1ga20e2f5ea9027a3653e5b9cc5aa1e21d5) given a DT node identifier with zephyr,power-state compatible.

        Parameters:
        :   - **node\_id** – A node identifier with compatible zephyr,power-state

    DT\_NUM\_CPU\_POWER\_STATES(node\_id)
    :   Obtain number of CPU power states supported and enabled by the given CPU node identifier.

        Parameters:
        :   - **node\_id** – A CPU node identifier.

        Returns:
        :   Number of supported and enabled CPU power states.

    PM\_STATE\_INFO\_LIST\_FROM\_DT\_CPU(node\_id)
    :   Initialize an array of struct [pm\_state\_info](#structpm__state__info) with information from all the states present and enabled in the given CPU node identifier.

        Example devicetree fragment:

        ```devicetree
        cpus {
           ...
           cpu0: cpu@0 {
                   device_type = "cpu";
                   ...
                   cpu-power-states = <&state0 &state1>;
           };

           power-states {
                   state0: state0 {
                           compatible = "zephyr,power-state";
                           power-state-name = "suspend-to-idle";
                           min-residency-us = <10000>;
                           exit-latency-us = <100>;
                   };

                   state1: state1 {
                           compatible = "zephyr,power-state";
                           power-state-name = "suspend-to-ram";
                           min-residency-us = <50000>;
                           exit-latency-us = <500>;
                   };
           };
        };
        ```

        Example usage:

        ```c
        const struct pm_state_info states[] =
             PM_STATE_INFO_LIST_FROM_DT_CPU(DT_NODELABEL(cpu0));
        ```

        Parameters:
        :   - **node\_id** – A CPU node identifier.

    PM\_STATE\_LIST\_FROM\_DT\_CPU(node\_id)
    :   Initialize an array of struct [pm\_state](#group__subsys__pm__states_1ga20e2f5ea9027a3653e5b9cc5aa1e21d5) with information from all the states present and enabled in the given CPU node identifier.

        Example devicetree fragment:

        ```devicetree
        cpus {
           ...
           cpu0: cpu@0 {
                   device_type = "cpu";
                   ...
                   cpu-power-states = <&state0 &state1>;
           };

           power-states {
                   state0: state0 {
                           compatible = "zephyr,power-state";
                           power-state-name = "suspend-to-idle";
                           min-residency-us = <10000>;
                           exit-latency-us = <100>;
                   };

                   state1: state1 {
                           compatible = "zephyr,power-state";
                           power-state-name = "suspend-to-ram";
                           min-residency-us = <50000>;
                           exit-latency-us = <500>;
                   };
           };
        };
        ```

        Example usage:

        ```c
        const enum pm_state states[] = PM_STATE_LIST_FROM_DT_CPU(DT_NODELABEL(cpu0));
        ```

        Parameters:
        :   - **node\_id** – A CPU node identifier.

    Enums

    enum pm\_state
    :   Power management state.

        *Values:*

        enumerator PM\_STATE\_ACTIVE
        :   Runtime active state.

            The system is fully powered and active.

            Note

            This state is correlated with ACPI G0/S0 state

        enumerator PM\_STATE\_RUNTIME\_IDLE
        :   Runtime idle state.

            Runtime idle is a system sleep state in which all of the cores enter deepest possible idle state and wait for interrupts, no requirements for the devices, leaving them at the states where they are.

            Note

            This state is correlated with ACPI S0ix state

        enumerator PM\_STATE\_SUSPEND\_TO\_IDLE
        :   Suspend to idle state.

            The system goes through a normal platform suspend where it puts all of the cores in deepest possible idle state and *may* puts peripherals into low-power states. No operating state is lost (ie. the cpu core does not lose execution context), so the system can go back to where it left off easily enough.

            Note

            This state is correlated with ACPI S1 state

        enumerator PM\_STATE\_STANDBY
        :   Standby state.

            In addition to putting peripherals into low-power states all non-boot CPUs are powered off. It should allow more energy to be saved relative to suspend to idle, but the resume latency will generally be greater than for that state. But it should be the same state with suspend to idle state on uniprocessor system.

            Note

            This state is correlated with ACPI S2 state

        enumerator PM\_STATE\_SUSPEND\_TO\_RAM
        :   Suspend to ram state.

            This state offers significant energy savings by powering off as much of the system as possible, where memory should be placed into the self-refresh mode to retain its contents. The state of devices and CPUs is saved and held in memory, and it may require some boot- strapping code in ROM to resume the system from it.

            Note

            This state is correlated with ACPI S3 state

        enumerator PM\_STATE\_SUSPEND\_TO\_DISK
        :   Suspend to disk state.

            This state offers significant energy savings by powering off as much of the system as possible, including the memory. The contents of memory are written to disk or other non-volatile storage, and on resume it’s read back into memory with the help of boot-strapping code, restores the system to the same point of execution where it went to suspend to disk.

            Note

            This state is correlated with ACPI S4 state

        enumerator PM\_STATE\_SOFT\_OFF
        :   Soft off state.

            This state consumes a minimal amount of power and requires a large latency in order to return to runtime active state. The contents of system(CPU and memory) will not be preserved, so the system will be restarted as if from initial power-up and kernel boot.

            Note

            This state is correlated with ACPI G2/S5 state

        enumerator PM\_STATE\_COUNT
        :   Number of power management states (internal use).

    Functions

    uint8\_t pm\_state\_cpu\_get\_all(uint8\_t cpu, const struct [pm\_state\_info](#c.pm_state_info) \*\*states)
    :   Obtain information about all supported states by a CPU.

        Parameters:
        :   - **cpu** – CPU index.
            - **states** – Where to store the list of supported states.

        Returns:
        :   Number of supported states.

    struct pm\_state\_info
    :   *#include <state.h>*

        Information about a power management state.

        Public Members

        uint8\_t substate\_id
        :   Some platforms have multiple states that map to one Zephyr power state.

            This property allows the platform distinguish them. e.g:

            ```devicetree
            power-states {
               state0: state0 {
                       compatible = "zephyr,power-state";
                       power-state-name = "suspend-to-idle";
                       substate-id = <1>;
                       min-residency-us = <10000>;
                       exit-latency-us = <100>;
               };
               state1: state1 {
                       compatible = "zephyr,power-state";
                       power-state-name = "suspend-to-idle";
                       substate-id = <2>;
                       min-residency-us = <20000>;
                       exit-latency-us = <200>;
               };
            };
            ```

        uint32\_t min\_residency\_us
        :   Minimum residency duration in microseconds.

            It is the minimum time for a given idle state to be worthwhile energywise.

            Note

            0 means that this property is not available for this state.

        uint32\_t exit\_latency\_us
        :   Worst case latency in microseconds required to exit the idle state.

            Note

            0 means that this property is not available for this state.

### Policy

*group* subsys\_pm\_sys\_policy
:   System Power Management Policy API.

    Defines

    PM\_ALL\_SUBSTATES
    :   Special value for ‘all substates’.

    Typedefs

    typedef void (\*pm\_policy\_latency\_changed\_cb\_t)(int32\_t latency)
    :   Callback to notify when maximum latency changes.

        Param latency:
        :   New maximum latency. Positive value represents latency in microseconds. SYS\_FOREVER\_US value lifts the latency constraint. Other values are forbidden.

    Functions

    void pm\_policy\_state\_lock\_get(enum [pm\_state](#c.pm_state) state, uint8\_t substate\_id)
    :   Increase a power state lock counter.

        A power state will not be allowed on the first call of [pm\_policy\_state\_lock\_get()](#group__subsys__pm__sys__policy_1gabbb379f8572f164addafe93ad3468f3d). Subsequent calls will just increase a reference count, thus meaning this API can be safely used concurrently. A state will be allowed again after [pm\_policy\_state\_lock\_put()](#group__subsys__pm__sys__policy_1ga12f4d121aa8be0eb66381713b481a8b1) is called as many times as [pm\_policy\_state\_lock\_get()](#group__subsys__pm__sys__policy_1gabbb379f8572f164addafe93ad3468f3d).

        Note that the PM\_STATE\_ACTIVE state is always allowed, so calling this API with PM\_STATE\_ACTIVE will have no effect.

        See also

        [pm\_policy\_state\_lock\_put()](#group__subsys__pm__sys__policy_1ga12f4d121aa8be0eb66381713b481a8b1)

        Parameters:
        :   - **state** – Power state.
            - **substate\_id** – Power substate ID. Use PM\_ALL\_SUBSTATES to affect all the substates in the given power state.

    void pm\_policy\_state\_lock\_put(enum [pm\_state](#c.pm_state) state, uint8\_t substate\_id)
    :   Decrease a power state lock counter.

        See also

        [pm\_policy\_state\_lock\_get()](#group__subsys__pm__sys__policy_1gabbb379f8572f164addafe93ad3468f3d)

        Parameters:
        :   - **state** – Power state.
            - **substate\_id** – Power substate ID. Use PM\_ALL\_SUBSTATES to affect all the substates in the given power state.

    bool pm\_policy\_state\_lock\_is\_active(enum [pm\_state](#c.pm_state) state, uint8\_t substate\_id)
    :   Check if a power state lock is active (not allowed).

        Parameters:
        :   - **state** – Power state.
            - **substate\_id** – Power substate ID. Use PM\_ALL\_SUBSTATES to affect all the substates in the given power state.

        Return values:
        :   - **true** – if power state lock is active.
            - **false** – if power state lock is not active.

    void pm\_policy\_latency\_request\_add(struct [pm\_policy\_latency\_request](#c.pm_policy_latency_request) \*req, uint32\_t value\_us)
    :   Add a new latency requirement.

        The system will not enter any power state that would make the system to exceed the given latency value.

        Parameters:
        :   - **req** – Latency request.
            - **value\_us** – Maximum allowed latency in microseconds.

    void pm\_policy\_latency\_request\_update(struct [pm\_policy\_latency\_request](#c.pm_policy_latency_request) \*req, uint32\_t value\_us)
    :   Update a latency requirement.

        Parameters:
        :   - **req** – Latency request.
            - **value\_us** – New maximum allowed latency in microseconds.

    void pm\_policy\_latency\_request\_remove(struct [pm\_policy\_latency\_request](#c.pm_policy_latency_request) \*req)
    :   Remove a latency requirement.

        Parameters:
        :   - **req** – Latency request.

    void pm\_policy\_latency\_changed\_subscribe(struct [pm\_policy\_latency\_subscription](#c.pm_policy_latency_subscription) \*req, [pm\_policy\_latency\_changed\_cb\_t](#c.pm_policy_latency_changed_cb_t) cb)
    :   Subscribe to maximum latency changes.

        Parameters:
        :   - **req** – Subscription request.
            - **cb** – Callback function (NULL to disable).

    void pm\_policy\_latency\_changed\_unsubscribe(struct [pm\_policy\_latency\_subscription](#c.pm_policy_latency_subscription) \*req)
    :   Unsubscribe to maximum latency changes.

        Parameters:
        :   - **req** – Subscription request.

    void pm\_policy\_event\_register(struct [pm\_policy\_event](#c.pm_policy_event) \*evt, uint32\_t time\_us)
    :   Register an event.

        Events in the power-management policy context are defined as any source that will wake up the system at a known time in the future. By registering such event, the policy manager will be able to decide whether certain power states are worth entering or not.

        See also

        [pm\_policy\_event\_unregister](#group__subsys__pm__sys__policy_1ga9448e31e1bd1a8b02defe6d1427197ff)

        Note

        It is mandatory to unregister events once they have happened by using [pm\_policy\_event\_unregister()](#group__subsys__pm__sys__policy_1ga9448e31e1bd1a8b02defe6d1427197ff). Not doing so is an API contract violation, because the system would continue to consider them as valid events in the *far* future, that is, after the cycle counter rollover.

        Parameters:
        :   - **evt** – Event.
            - **time\_us** – When the event will occur, in microseconds from now.

    void pm\_policy\_event\_update(struct [pm\_policy\_event](#c.pm_policy_event) \*evt, uint32\_t time\_us)
    :   Update an event.

        See also

        [pm\_policy\_event\_register](#group__subsys__pm__sys__policy_1gafab2e1484a58131a9c7cefd2b9adb3e9)

        Parameters:
        :   - **evt** – Event.
            - **time\_us** – When the event will occur, in microseconds from now.

    void pm\_policy\_event\_unregister(struct [pm\_policy\_event](#c.pm_policy_event) \*evt)
    :   Unregister an event.

        See also

        [pm\_policy\_event\_register](#group__subsys__pm__sys__policy_1gafab2e1484a58131a9c7cefd2b9adb3e9)

        Parameters:
        :   - **evt** – Event.

    struct pm\_policy\_latency\_subscription
    :   *#include <policy.h>*

        Latency change subscription.

        Note

        All fields in this structure are meant for private usage.

    struct pm\_policy\_latency\_request
    :   *#include <policy.h>*

        Latency request.

        Note

        All fields in this structure are meant for private usage.

    struct pm\_policy\_event
    :   *#include <policy.h>*

        Event.

        Note

        All fields in this structure are meant for private usage.

### Hooks

*group* subsys\_pm\_sys\_hooks
:   System Power Management Hooks.

    Functions

    void pm\_state\_set(enum [pm\_state](#c.pm_state) state, uint8\_t substate\_id)
    :   Put processor into a power state.

        This function implements the SoC specific details necessary to put the processor into available power states.

        Parameters:
        :   - **state** – Power state.
            - **substate\_id** – Power substate id.

    void pm\_state\_exit\_post\_ops(enum [pm\_state](#c.pm_state) state, uint8\_t substate\_id)
    :   Do any SoC or architecture specific post ops after sleep state exits.

        This function is a place holder to do any operations that may be needed to be done after sleep state exits. Currently it enables interrupts after resuming from sleep state. In future, the enabling of interrupts may be moved into the kernel.

        Parameters:
        :   - **state** – Power state.
            - **substate\_id** – Power substate id.

## Device PM APIs

*group* subsys\_pm\_device
:   Device Power Management API.

    Defines

    PM\_DEVICE\_ISR\_SAFE
    :   Flag indicating that runtime PM API for the device can be called from any context.

        If [PM\_DEVICE\_ISR\_SAFE](#group__subsys__pm__device_1ga18bb96fc4d5003516ab2eaf73cb35912) flag is used for device definition, it indicates that PM actions are synchronous and can be executed from any context. This approach can be used for cases where suspending and resuming is short as it is executed in the critical section. This mode requires less resources (~80 byte less RAM) and allows to use device runtime PM from any context (including interrupts).

    PM\_DEVICE\_DEFINE(dev\_id, pm\_action\_cb, ...)
    :   Define device PM resources for the given device name.

        See also

        [PM\_DEVICE\_DT\_DEFINE](#group__subsys__pm__device_1gaa2bd2c490fee99a6fc2b23605e799ef0), [PM\_DEVICE\_DT\_INST\_DEFINE](#group__subsys__pm__device_1ga5b201836d9c19a1c87cdde93631a4b0c)

        Note

        This macro is a no-op if  [`CONFIG_PM_DEVICE`](../../../kconfig.md#CONFIG_PM_DEVICE "CONFIG_PM_DEVICE") is not enabled.

        Parameters:
        :   - **dev\_id** – Device id.
            - **pm\_action\_cb** – PM control callback.
            - **...** – Optional flag to indicate that ISR safe. Use [PM\_DEVICE\_ISR\_SAFE](#group__subsys__pm__device_1ga18bb96fc4d5003516ab2eaf73cb35912) or 0.

    PM\_DEVICE\_DT\_DEFINE(node\_id, pm\_action\_cb, ...)
    :   Define device PM resources for the given node identifier.

        See also

        [PM\_DEVICE\_DT\_INST\_DEFINE](#group__subsys__pm__device_1ga5b201836d9c19a1c87cdde93631a4b0c), [PM\_DEVICE\_DEFINE](#group__subsys__pm__device_1gae85fb5a7c31863a3663cef8dd7229c6c)

        Note

        This macro is a no-op if  [`CONFIG_PM_DEVICE`](../../../kconfig.md#CONFIG_PM_DEVICE "CONFIG_PM_DEVICE") is not enabled.

        Parameters:
        :   - **node\_id** – Node identifier.
            - **pm\_action\_cb** – PM control callback.
            - **...** – Optional flag to indicate that device is isr\_ok. Use [PM\_DEVICE\_ISR\_SAFE](#group__subsys__pm__device_1ga18bb96fc4d5003516ab2eaf73cb35912) or 0.

    PM\_DEVICE\_DT\_INST\_DEFINE(idx, pm\_action\_cb, ...)
    :   Define device PM resources for the given instance.

        See also

        [PM\_DEVICE\_DT\_DEFINE](#group__subsys__pm__device_1gaa2bd2c490fee99a6fc2b23605e799ef0), [PM\_DEVICE\_DEFINE](#group__subsys__pm__device_1gae85fb5a7c31863a3663cef8dd7229c6c)

        Note

        This macro is a no-op if  [`CONFIG_PM_DEVICE`](../../../kconfig.md#CONFIG_PM_DEVICE "CONFIG_PM_DEVICE") is not enabled.

        Parameters:
        :   - **idx** – Instance index.
            - **pm\_action\_cb** – PM control callback.
            - **...** – Optional flag to indicate that device is isr\_ok. Use [PM\_DEVICE\_ISR\_SAFE](#group__subsys__pm__device_1ga18bb96fc4d5003516ab2eaf73cb35912) or 0.

    PM\_DEVICE\_GET(dev\_id)
    :   Obtain a reference to the device PM resources for the given device.

        Parameters:
        :   - **dev\_id** – Device id.

        Returns:
        :   Reference to the device PM resources (NULL if device  [`CONFIG_PM_DEVICE`](../../../kconfig.md#CONFIG_PM_DEVICE "CONFIG_PM_DEVICE") is disabled).

    PM\_DEVICE\_DT\_GET(node\_id)
    :   Obtain a reference to the device PM resources for the given node.

        Parameters:
        :   - **node\_id** – Node identifier.

        Returns:
        :   Reference to the device PM resources (NULL if device  [`CONFIG_PM_DEVICE`](../../../kconfig.md#CONFIG_PM_DEVICE "CONFIG_PM_DEVICE") is disabled).

    PM\_DEVICE\_DT\_INST\_GET(idx)
    :   Obtain a reference to the device PM resources for the given instance.

        Parameters:
        :   - **idx** – Instance index.

        Returns:
        :   Reference to the device PM resources (NULL if device  [`CONFIG_PM_DEVICE`](../../../kconfig.md#CONFIG_PM_DEVICE "CONFIG_PM_DEVICE") is disabled).

    Typedefs

    typedef int (\*pm\_device\_action\_cb\_t)(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, enum [pm\_device\_action](#c.pm_device_action) action)
    :   Device PM action callback.

        Param dev:
        :   Device instance.

        Param action:
        :   Requested action.

        Retval 0:
        :   If successful.

        Retval -ENOTSUP:
        :   If the requested action is not supported.

        Retval Errno:
        :   Other negative errno on failure.

    typedef bool (\*pm\_device\_action\_failed\_cb\_t)(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, int err)
    :   Device PM action failed callback.

        Param dev:
        :   Device that failed the action.

        Param err:
        :   Return code of action failure.

        Return:
        :   True to continue iteration, false to halt iteration.

    Enums

    enum pm\_device\_state
    :   Device power states.

        *Values:*

        enumerator PM\_DEVICE\_STATE\_ACTIVE
        :   Device is in active or regular state.

        enumerator PM\_DEVICE\_STATE\_SUSPENDED
        :   Device is suspended.

            Note

            Device context may be lost.

        enumerator PM\_DEVICE\_STATE\_SUSPENDING
        :   Device is being suspended.

        enumerator PM\_DEVICE\_STATE\_OFF
        :   Device is turned off (power removed).

            Note

            Device context is lost.

    enum pm\_device\_action
    :   Device PM actions.

        *Values:*

        enumerator PM\_DEVICE\_ACTION\_SUSPEND
        :   Suspend.

        enumerator PM\_DEVICE\_ACTION\_RESUME
        :   Resume.

        enumerator PM\_DEVICE\_ACTION\_TURN\_OFF
        :   Turn off.

            Note

            Action triggered only by a power domain.

        enumerator PM\_DEVICE\_ACTION\_TURN\_ON
        :   Turn on.

            Note

            Action triggered only by a power domain.

    Functions

    const char \*pm\_device\_state\_str(enum [pm\_device\_state](#c.pm_device_state) state)
    :   Get name of device PM state.

        Parameters:
        :   - **state** – State id which name should be returned

    int pm\_device\_action\_run(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, enum [pm\_device\_action](#c.pm_device_action) action)
    :   Run a pm action on a device.

        This function calls the device PM control callback so that the device does the necessary operations to execute the given action.

        Parameters:
        :   - **dev** – Device instance.
            - **action** – Device pm action.

        Return values:
        :   - **0** – If successful.
            - **-ENOTSUP** – If requested state is not supported.
            - **-EALREADY** – If device is already at the requested state.
            - **-EBUSY** – If device is changing its state.
            - **-ENOSYS** – If device does not support PM.
            - **-EPERM** – If device has power state locked.
            - **Errno** – Other negative errno on failure.

    void pm\_device\_children\_action\_run(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, enum [pm\_device\_action](#c.pm_device_action) action, [pm\_device\_action\_failed\_cb\_t](#c.pm_device_action_failed_cb_t) failure\_cb)
    :   Run a pm action on all children of a device.

        This function calls all child devices PM control callback so that the device does the necessary operations to execute the given action.

        Parameters:
        :   - **dev** – Device instance.
            - **action** – Device pm action.
            - **failure\_cb** – Function to call if a child fails the action, can be NULL.

    int pm\_device\_state\_get(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, enum [pm\_device\_state](#c.pm_device_state) \*state)
    :   Obtain the power state of a device.

        Parameters:
        :   - **dev** – Device instance.
            - **state** – Pointer where device power state will be stored.

        Return values:
        :   - **0** – If successful.
            - **-ENOSYS** – If device does not implement power management.

    static inline void pm\_device\_init\_suspended(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Initialize a device state to [PM\_DEVICE\_STATE\_SUSPENDED](#group__subsys__pm__device_1gga561c0789071e3c3963f21f4c4a1bb2c6a03f61cb7cd5e4820c1c731500fd053b5).

        By default device state is initialized to [PM\_DEVICE\_STATE\_ACTIVE](#group__subsys__pm__device_1gga561c0789071e3c3963f21f4c4a1bb2c6a54b207e01b4dfc5e1ff56149817120c7). However in order to save power some drivers may choose to only initialize the device to the suspended state, or actively put the device into the suspended state. This function can therefore be used to notify the PM subsystem that the device is in [PM\_DEVICE\_STATE\_SUSPENDED](#group__subsys__pm__device_1gga561c0789071e3c3963f21f4c4a1bb2c6a03f61cb7cd5e4820c1c731500fd053b5) instead of the default.

        Parameters:
        :   - **dev** – Device instance.

    static inline void pm\_device\_init\_off(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Initialize a device state to [PM\_DEVICE\_STATE\_OFF](#group__subsys__pm__device_1gga561c0789071e3c3963f21f4c4a1bb2c6a2456389354b744d4e96847e38f8b61c2).

        By default device state is initialized to [PM\_DEVICE\_STATE\_ACTIVE](#group__subsys__pm__device_1gga561c0789071e3c3963f21f4c4a1bb2c6a54b207e01b4dfc5e1ff56149817120c7). In general, this makes sense because the device initialization function will resume and configure a device, leaving it operational. However, when power domains are enabled, the device may be connected to a switchable power source, in which case it won’t be powered at boot. This function can therefore be used to notify the PM subsystem that the device is in [PM\_DEVICE\_STATE\_OFF](#group__subsys__pm__device_1gga561c0789071e3c3963f21f4c4a1bb2c6a2456389354b744d4e96847e38f8b61c2) instead of the default.

        Parameters:
        :   - **dev** – Device instance.

    void pm\_device\_busy\_set(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Mark a device as busy.

        Devices marked as busy will not be suspended when the system goes into low-power states. This can be useful if, for example, the device is in the middle of a transaction.

        See also

        [pm\_device\_busy\_clear()](#group__subsys__pm__device_1ga8b527314f0c61b85602876b4f5a52275)

        Parameters:
        :   - **dev** – Device instance.

    void pm\_device\_busy\_clear(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Clear a device busy status.

        See also

        [pm\_device\_busy\_set()](#group__subsys__pm__device_1ga7ea002352f3d1c90aecff1d54c255a06)

        Parameters:
        :   - **dev** – Device instance.

    bool pm\_device\_is\_any\_busy(void)
    :   Check if any device is busy.

        Return values:
        :   - **false** – If no device is busy
            - **true** – If one or more devices are busy

    bool pm\_device\_is\_busy(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Check if a device is busy.

        Parameters:
        :   - **dev** – Device instance.

        Return values:
        :   - **false** – If the device is not busy
            - **true** – If the device is busy

    bool pm\_device\_wakeup\_enable(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, bool enable)
    :   Enable or disable a device as a wake up source.

        A device marked as a wake up source will not be suspended when the system goes into low-power modes, thus allowing to use it as a wake up source for the system.

        Parameters:
        :   - **dev** – Device instance.
            - **enable** – `true` to enable or `false` to disable

        Return values:
        :   - **true** – If the wakeup source was successfully enabled.
            - **false** – If the wakeup source was not successfully enabled.

    bool pm\_device\_wakeup\_is\_enabled(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Check if a device is enabled as a wake up source.

        Parameters:
        :   - **dev** – Device instance.

        Return values:
        :   - **true** – if the wakeup source is enabled.
            - **false** – if the wakeup source is not enabled.

    bool pm\_device\_wakeup\_is\_capable(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Check if a device is wake up capable.

        Parameters:
        :   - **dev** – Device instance.

        Return values:
        :   - **true** – If the device is wake up capable.
            - **false** – If the device is not wake up capable.

    void pm\_device\_state\_lock(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Lock current device state.

        This function locks the current device power state. Once locked the device power state will not be changed by system power management or device runtime power management until unlocked.

        See also

        [pm\_device\_state\_unlock](#group__subsys__pm__device_1gaa5d2387a01a4ca4d765b1ea2361155bb)

        Note

        The given device should not have device runtime enabled.

        Parameters:
        :   - **dev** – Device instance.

    void pm\_device\_state\_unlock(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Unlock the current device state.

        Unlocks a previously locked device pm.

        See also

        [pm\_device\_state\_lock](#group__subsys__pm__device_1gaab27e932950e1063b2f1f4c4e19dbf01)

        Parameters:
        :   - **dev** – Device instance.

    bool pm\_device\_state\_is\_locked(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Check if the device pm is locked.

        Parameters:
        :   - **dev** – Device instance.

        Return values:
        :   - **true** – If device is locked.
            - **false** – If device is not locked.

    bool pm\_device\_on\_power\_domain(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Check if the device is on a switchable power domain.

        Parameters:
        :   - **dev** – Device instance.

        Return values:
        :   - **true** – If device is on a switchable power domain.
            - **false** – If device is not on a switchable power domain.

    int pm\_device\_power\_domain\_add(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, const struct [device](../../../kernel/drivers/index.md#c.device "device") \*domain)
    :   Add a device to a power domain.

        This function adds a device to a given power domain.

        Parameters:
        :   - **dev** – Device to be added to the power domain.
            - **domain** – Power domain.

        Return values:
        :   - **0** – If successful.
            - **-EALREADY** – If device is already part of the power domain.
            - **-ENOSYS** – If the application was built without power domain support.
            - **-ENOSPC** – If there is no space available in the power domain to add the device.

    int pm\_device\_power\_domain\_remove(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, const struct [device](../../../kernel/drivers/index.md#c.device "device") \*domain)
    :   Remove a device from a power domain.

        This function removes a device from a given power domain.

        Parameters:
        :   - **dev** – Device to be removed from the power domain.
            - **domain** – Power domain.

        Return values:
        :   - **0** – If successful.
            - **-ENOSYS** – If the application was built without power domain support.
            - **-ENOENT** – If device is not in the given domain.

    bool pm\_device\_is\_powered(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Check if the device is currently powered.

        Parameters:
        :   - **dev** – Device instance.

        Return values:
        :   - **true** – If device is currently powered, or is assumed to be powered (i.e. it does not support PM or is not under a PM domain)
            - **false** – If device is not currently powered

    int pm\_device\_driver\_init(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, [pm\_device\_action\_cb\_t](#c.pm_device_action_cb_t) action\_cb)
    :   Setup a device driver into the lowest valid power mode.

        This helper function is intended to be called at the end of a driver init function to automatically setup the device into the lowest power mode. It assumes that the device has been configured as if it is in [PM\_DEVICE\_STATE\_OFF](#group__subsys__pm__device_1gga561c0789071e3c3963f21f4c4a1bb2c6a2456389354b744d4e96847e38f8b61c2).

        Parameters:
        :   - **dev** – Device instance.
            - **action\_cb** – Device PM control callback function.

        Return values:
        :   - **0** – On success.
            - **-errno** – Error code from *action\_cb* on failure.

    struct pm\_device\_base
    :   *#include <device.h>*

        Device PM info.

        Structure holds fields which are common for two PM devices: generic and synchronous.

        Public Members

        atomic\_t flags
        :   Device PM status flags.

        enum [pm\_device\_state](#c.pm_device_state) state
        :   Device power state.

        [pm\_device\_action\_cb\_t](#c.pm_device_action_cb_t) action\_cb
        :   Device PM action callback.

        uint32\_t usage
        :   Device usage count.

    struct pm\_device
    :   *#include <device.h>*

        Runtime PM info for device with generic PM.

        Generic PM involves suspending and resuming operations which can be blocking, long lasting or asynchronous. Runtime PM API is limited when used from interrupt context.

        Public Members

        struct [pm\_device\_base](#c.pm_device_base) base
        :   Base info.

        const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev
        :   Pointer to the device.

        struct k\_sem lock
        :   Lock to synchronize the get/put operations.

        struct [k\_event](../../../kernel/services/synchronization/events.md#c.k_event "k_event") event
        :   Event var to listen to the sync request events.

        struct [k\_work\_delayable](../../../kernel/services/threads/workqueue.md#c.k_work_delayable "k_work_delayable") work
        :   Work object for asynchronous calls.

    struct pm\_device\_isr
    :   *#include <device.h>*

        Runtime PM info for device with synchronous PM.

        Synchronous PM can be used with devices which suspend and resume operations can be performed in the critical section as they are short and non-blocking. Runtime PM API can be used from any context in that case.

        Public Members

        struct [pm\_device\_base](#c.pm_device_base) base
        :   Base info.

        struct [k\_spinlock](../../../kernel/services/smp/smp.md#c.k_spinlock "k_spinlock") lock
        :   Lock to synchronize the synchronous get/put operations.

## Device Runtime PM APIs

*group* subsys\_pm\_device\_runtime
:   Device Runtime Power Management API.

    Functions

    int pm\_device\_runtime\_auto\_enable(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Automatically enable device runtime based on devicetree properties.

        Note

        Must not be called from application code. See the zephyr,pm-device-runtime-auto property in pm.yaml and z\_sys\_init\_run\_level.

        Parameters:
        :   - **dev** – Device instance.

        Return values:
        :   - **0** – If the device runtime PM is enabled successfully or it has not been requested for this device in devicetree.
            - **-errno** – Other negative errno, result of enabled device runtime PM.

    int pm\_device\_runtime\_enable(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Enable device runtime PM.

        This function will enable runtime PM on the given device. If the device is in [PM\_DEVICE\_STATE\_ACTIVE](#group__subsys__pm__device_1gga561c0789071e3c3963f21f4c4a1bb2c6a54b207e01b4dfc5e1ff56149817120c7) state, the device will be suspended.

        See also

        [pm\_device\_init\_suspended()](#group__subsys__pm__device_1ga4c366f49e326a8b8e01d90cb2ee424ba)

        **Function properties (list may not be complete)**
        :   [pre-kernel-ok](../../../develop/api/terminology.md#api-term-pre-kernel-ok)

        Parameters:
        :   - **dev** – Device instance.

        Return values:
        :   - **0** – If the device runtime PM is enabled successfully.
            - **-EPERM** – If device has power state locked.
            - **-ENOTSUP** – If the device does not support PM.
            - **-errno** – Other negative errno, result of suspending the device.

    int pm\_device\_runtime\_disable(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Disable device runtime PM.

        If the device is currently suspended it will be resumed.

        **Function properties (list may not be complete)**
        :   [pre-kernel-ok](../../../develop/api/terminology.md#api-term-pre-kernel-ok)

        Parameters:
        :   - **dev** – Device instance.

        Return values:
        :   - **0** – If the device runtime PM is disabled successfully.
            - **-ENOTSUP** – If the device does not support PM.
            - **-errno** – Other negative errno, result of resuming the device.

    int pm\_device\_runtime\_get(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Resume a device based on usage count.

        This function will resume the device if the device is suspended (usage count equal to 0). In case of a resume failure, usage count and device state will be left unchanged. In all other cases, usage count will be incremented.

        If the device is still being suspended as a result of calling [pm\_device\_runtime\_put\_async()](#group__subsys__pm__device__runtime_1ga9e90089b0ab78f365905418646e196c6), this function will wait for the operation to finish to then resume the device.

        **Function properties (list may not be complete)**
        :   [pre-kernel-ok](../../../develop/api/terminology.md#api-term-pre-kernel-ok)

        Note

        It is safe to use this function in contexts where blocking is not allowed, e.g. ISR, provided the device PM implementation does not block.

        Parameters:
        :   - **dev** – Device instance.

        Return values:
        :   - **0** – If it succeeds. In case device runtime PM is not enabled or not available this function will be a no-op and will also return 0.
            - **-EWOUDBLOCK** – If call would block but it is not allowed (e.g. in ISR).
            - **-errno** – Other negative errno, result of the PM action callback.

    int pm\_device\_runtime\_put(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Suspend a device based on usage count.

        This function will suspend the device if the device is no longer required (usage count equal to 0). In case of suspend failure, usage count and device state will be left unchanged. In all other cases, usage count will be decremented (down to 0).

        See also

        [pm\_device\_runtime\_put\_async()](#group__subsys__pm__device__runtime_1ga9e90089b0ab78f365905418646e196c6)

        **Function properties (list may not be complete)**
        :   [pre-kernel-ok](../../../develop/api/terminology.md#api-term-pre-kernel-ok)

        Parameters:
        :   - **dev** – Device instance.

        Return values:
        :   - **0** – If it succeeds. In case device runtime PM is not enabled or not available this function will be a no-op and will also return 0.
            - **-EALREADY** – If device is already suspended (can only happen if get/put calls are unbalanced).
            - **-errno** – Other negative errno, result of the action callback.

    int pm\_device\_runtime\_put\_async(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev, [k\_timeout\_t](../../../kernel/services/timing/clocks.md#c.k_timeout_t "k_timeout_t") delay)
    :   Suspend a device based on usage count (asynchronously).

        This function will schedule the device suspension if the device is no longer required (usage count equal to 0). In all other cases, usage count will be decremented (down to 0).

        See also

        [pm\_device\_runtime\_put()](#group__subsys__pm__device__runtime_1ga98daba53a992fb6bd2c2b31cb445844f)

        **Function properties (list may not be complete)**
        :   [pre-kernel-ok](../../../develop/api/terminology.md#api-term-pre-kernel-ok) ,  [async](../../../develop/api/terminology.md#api-term-async) ,  [isr-ok](../../../develop/api/terminology.md#api-term-isr-ok)

        Note

        Asynchronous operations are not supported when in pre-kernel mode. In this case, the function will be blocking (equivalent to [pm\_device\_runtime\_put()](#group__subsys__pm__device__runtime_1ga98daba53a992fb6bd2c2b31cb445844f)).

        Parameters:
        :   - **dev** – Device instance.
            - **delay** – Minimum amount of time before triggering the action.

        Return values:
        :   - **0** – If it succeeds. In case device runtime PM is not enabled or not available this function will be a no-op and will also return 0.
            - **-EBUSY** – If the device is busy.
            - **-EALREADY** – If device is already suspended (can only happen if get/put calls are unbalanced).

    bool pm\_device\_runtime\_is\_enabled(const struct [device](../../../kernel/drivers/index.md#c.device "device") \*dev)
    :   Check if device runtime is enabled for a given device.

        See also

        [pm\_device\_runtime\_enable()](#group__subsys__pm__device__runtime_1gaabcd2cc694c9e201dd87bf42f02b454c)

        **Function properties (list may not be complete)**
        :   [pre-kernel-ok](../../../develop/api/terminology.md#api-term-pre-kernel-ok)

        Parameters:
        :   - **dev** – Device instance.

        Return values:
        :   - **true** – If device has device runtime PM enabled.
            - **false** – If the device has device runtime PM disabled.

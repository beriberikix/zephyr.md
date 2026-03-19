---
version: v4.1.0
source_url: https://docs.zephyrproject.org/4.1.0/services/zbus/index.html
original_path: services/zbus/index.html
---

# Zephyr bus (zbus)

The *Zephyr bus - zbus* is a lightweight and flexible software bus enabling a simple way for
threads to talk to one another in a many-to-many way.

## [Concepts](#id16)

Threads can send messages to one or more observers using zbus. It makes the many-to-many
communication possible. The bus implements message-passing and publish/subscribe communication
paradigms that enable threads to communicate synchronously or asynchronously through shared memory.

The communication through zbus is channel-based. Threads (or callbacks) use channels to exchange
messages. Additionally, besides other actions, threads can publish and observe channels. When a
thread publishes a message on a channel, the bus will make the message available to all the
published channel’s observers. Based on the observer’s type, it can access the message directly,
receive a copy of it, or even receive only a reference of the published channel.

The figure below shows an example of a typical application using zbus in which the application logic
(hardware independent) talks to other threads via software bus. Note that the threads are decoupled
from each other because they only use zbus channels and do not need to know each other to talk.

[![zbus usage overview](../../_images/zbus_overview.svg)
](../../_images/zbus_overview.svg)

A typical zbus application architecture.

The bus comprises:

- Set of channels that consists of the control metadata information, and the message itself;
- *Virtual Distributed Event Dispatcher* (VDED), the bus logic responsible for sending
  notifications/messages to the observers. The VDED logic runs inside the publishing action in the same
  thread context, giving the bus an idea of a distributed execution. When a thread publishes to a
  channel, it also propagates the notifications to the observers;
- Threads (subscribers and message subscribers) and callbacks (listeners) publishing, reading, and
  receiving notifications from the bus.

[![ZBus anatomy](../../_images/zbus_anatomy.svg)
](../../_images/zbus_anatomy.svg)

ZBus anatomy.

The bus makes the publish, read, claim, finish, notify, and subscribe actions available over
channels. Publishing, reading, claiming, and finishing are available in all RTOS thread contexts,
including ISRs. The publish and read operations are simple and fast; the procedure is channel
locking followed by a memory copy to and from a shared memory region and then a channel unlocking.
Another essential aspect of zbus is the observers. There are three types of observers:

[![ZBus observers type](../../_images/zbus_type_of_observers.svg)
](../../_images/zbus_type_of_observers.svg)

ZBus observers.

- Listeners, a callback that the event dispatcher executes every time an observed channel is
  published or notified;
- Subscriber, a thread-based observer that relies internally on a message queue where the event
  dispatcher puts a changed channel’s reference every time an observed channel is published or
  notified. Note this kind of observer does not receive the message itself. It should read the
  message from the channel after receiving the notification;
- Message subscribers, a thread-based observer that relies internally on a FIFO where the event
  dispatcher puts a copy of the message every time an observed channel is published or notified.

Channel observation structures define the relationship between a channel and its observers. For
every observation, a pair channel/observer. Developers can statically allocate observation using the
[`ZBUS_CHAN_DEFINE`](../../doxygen/html/group__zbus__apis.md#ga29a3a39e5c78a34b2d8491615d1f0687) or [`ZBUS_CHAN_ADD_OBS`](../../doxygen/html/group__zbus__apis.md#gaf63215f3f53741edf52b4d0d7b2b97df). There are also runtime observers,
enabling developers to create runtime observations. It is possible to disable an observer entirely
or observations individually. The event dispatcher will ignore disabled observers and observations.

[![ZBus observation mask.](../../_images/zbus_observation_mask.svg)
](../../_images/zbus_observation_mask.svg)

ZBus observation mask.

The above figure illustrates some states, from (a) to (d), for channels from `C1` to `C5`,
`Subscriber 1`, and the observations. The last two are in orange to indicate they are dynamically
allocated (runtime observation). (a) shows that the observer and all observations are enabled. (b)
shows the observer is disabled, so the event dispatcher will ignore it. (c) shows the observer
enabled. However, there is one static observation disabled. The event dispatcher will only stop
sending notifications from channel `C3`. In (d), the event dispatcher will stop sending
notifications from channels `C3` and `C5` to `Subscriber 1`.

Suppose a usual sensor-based solution is in the figure below for illustration purposes. When
triggered, the timer publishes to the `Trigger` channel. As the sensor thread subscribed to the
`Trigger` channel, it receives the sensor data. Notice the VDED executes the `Blink` because it
also listens to the `Trigger` channel. When the sensor data is ready, the sensor thread publishes
it to the `Sensor data` channel. The core thread receives the message as a `Sensor data` channel
message subscriber, processes the sensor data, and stores it in an internal sample buffer. It
repeats until the sample buffer is full; when it happens, the core thread aggregates the sample
buffer information, prepares a package, and publishes that to the `Payload` channel. The Lora
thread receives that because it is a `Payload` channel message subscriber and sends the payload to
the cloud. When it completes the transmission, the Lora thread publishes to the `Transmission
done` channel. The VDED executes the `Blink` again since it listens to the `Transmission done`
channel.

[![ZBus sensor-based application](../../_images/zbus_operations.svg)
](../../_images/zbus_operations.svg)

ZBus sensor-based application.

This way of implementing the solution makes the application more flexible, enabling us to change
things independently. For example, we want to change the trigger from a timer to a button press. We
can do that, and the change does not affect other parts of the system. Likewise, we would like to
change the communication interface from LoRa to Bluetooth; we only need to change the LoRa thread.
No other change is required in order to make that work. Thus, the developer would do that for every
block of the image. Based on that, there is a sign zbus promotes decoupling in the system
architecture.

Another important aspect of using zbus is the reuse of system modules. If a code portion with
well-defined behaviors (we call that module) only uses zbus channels and not hardware interfaces, it
can easily be reused in other solutions. The new solution must implement the interfaces (set of
channels) the module needs to work. That indicates zbus could improve the module reuse.

The last important note is the zbus solution reach. We can count on many ways of using zbus to
enable the developer to be as free as possible to create what they need. For example, messages can
be dynamic or static allocated; notifications can be synchronous or asynchronous; the developer can
control the channel in so many different ways claiming the channel, developers can add their
metadata information to a channel by using the user-data field, the discretionary use of a validator
enables the systems to be accurate over message format, and so on. Those characteristics increase
the solutions that can be done with zbus and make it a good fit as an open-source community tool.

### [Virtual Distributed Event Dispatcher](#id17)

The VDED execution always happens in the publisher’s context. It can be a thread or an ISR. Be
careful with publications inside ISR because the scheduler won’t preempt the VDED. Use that wisely.
The basic description of the execution is as follows:

- The channel lock is acquired;
- The channel receives the new message via direct copy (by a raw [`memcpy()`](../../doxygen/html/string_8h.md#af0f01bffcd16daa9143f6014d10a25ad));
- The event dispatcher logic executes the listeners, sends a copy of the message to the message
  subscribers, and pushes the channel’s reference to the subscribers’ notification message queue in
  the same sequence they appear on the channel observers’ list. The listeners can perform non-copy
  quick access to the constant message reference directly (via the [`zbus_chan_const_msg()`](../../doxygen/html/group__zbus__apis.md#gafee07c355df9ac86b85e601196b56a10)
  function) since the channel is still locked;
- At last, the publishing function unlocks the channel.

To illustrate the VDED execution, consider the example illustrated below. We have four threads in
ascending priority `S1`, `MS2`, `MS1`, and `T1` (the highest priority); two listeners,
`L1` and `L2`; and channel A. Supposing `L1`, `L2`, `MS1`, `MS2`, and `S1` observer
channel A.

[![ZBus example scenario](../../_images/zbus_publishing_process_example_scenario.svg)
](../../_images/zbus_publishing_process_example_scenario.svg)

ZBus VDED execution example scenario.

The following code implements channel A. Note the `struct a_msg` is illustrative only.

```c
ZBUS_CHAN_DEFINE(a_chan,                       /* Name */
         struct a_msg,                         /* Message type */

         NULL,                                 /* Validator */
         NULL,                                 /* User Data */
         ZBUS_OBSERVERS(L1, L2, MS1, MS2, S1), /* observers */
         ZBUS_MSG_INIT(0)                      /* Initial value {0} */
);
```

In the figure below, the letters indicate some action related to the VDED execution. The X-axis
represents the time, and the Y-axis represents the priority of threads. Channel A’s message,
represented by a voice balloon, is only one memory portion (shared memory). It appears several times
only as an illustration of the message at that point in time.

[![ZBus publish processing detail](../../_images/zbus_publishing_process_example.svg)
](../../_images/zbus_publishing_process_example.svg)

ZBus VDED execution detail for priority T1 > MS1 > MS2 > S1.

The figure above illustrates the actions performed during the VDED execution when T1 publishes to
channel A. Thus, the table below describes the activities (represented by a letter) of the VDED
execution. The scenario considers the following priorities: T1 > MS1 > MS2 > S1. T1 has the highest
priority.

VDED execution steps in detail for priority T1 > MS1 > MS2 > S1.

| Actions | Description |
| --- | --- |
| a | T1 starts and, at some point, publishes to channel A. |
| b | The publishing (VDED) process starts. The VDED locks the channel A. |
| c | The VDED copies the T1 message to the channel A message. |
| d, e | The VDED executes L1 and L2 in the respective sequence. Inside the listeners, usually, there is a call to the [`zbus_chan_const_msg()`](../../doxygen/html/group__zbus__apis.md#gafee07c355df9ac86b85e601196b56a10) function, which provides a direct constant reference to channel A’s message. It is quick, and no copy is needed here. |
| f, g | The VDED copies the message and sends that to MS1 and MS2 sequentially. Notice the threads get ready to execute right after receiving the notification. However, they go to a pending state because they have less priority than T1. |
| h | The VDED pushes the notification message to the queue of S1. Notice the thread gets ready to execute right after receiving the notification. However, it goes to a pending state because it cannot access the channel since it is still locked. |
| i | VDED finishes the publishing by unlocking channel A. The MS1 leaves the pending state and starts executing. |
| j | MS1 finishes execution. The MS2 leaves the pending state and starts executing. |
| k | MS2 finishes execution. The S1 leaves the pending state and starts executing. |
| l, m, n | The S1 leaves the pending state since channel A is not locked. It gets in the CPU again and starts executing. As it did receive a notification from channel A, it performed a channel read (as simple as lock, memory copy, unlock), continues its execution and goes out of the CPU. |
| o | S1 finishes its workload. |

The figure below illustrates the actions performed during the VDED execution when T1 publishes to
channel A. The scenario considers the following priorities: T1 < MS1 < MS2 < S1.

[![ZBus publish processing detail](../../_images/zbus_publishing_process_example2.svg)
](../../_images/zbus_publishing_process_example2.svg)

ZBus VDED execution detail for priority T1 < MS1 < MS2 < S1.

Thus, the table below describes the activities (represented by a letter) of the VDED execution.

VDED execution steps in detail for priority T1 < MS1 < MS2 < S1.

| Actions | Description |
| --- | --- |
| a | T1 starts and, at some point, publishes to channel A. |
| b | The publishing (VDED) process starts. The VDED locks the channel A. |
| c | The VDED copies the T1 message to the channel A message. |
| d, e | The VDED executes L1 and L2 in the respective sequence. Inside the listeners, usually, there is a call to the [`zbus_chan_const_msg()`](../../doxygen/html/group__zbus__apis.md#gafee07c355df9ac86b85e601196b56a10) function, which provides a direct constant reference to channel A’s message. It is quick, and no copy is needed here. |
| f | The VDED copies the message and sends that to MS1. MS1 preempts T1 and starts working. After that, the T1 regain MCU. |
| g | The VDED copies the message and sends that to MS2. MS2 preempts T1 and starts working. After that, the T1 regain MCU. |
| h | The VDED pushes the notification message to the queue of S1. |
| i | VDED finishes the publishing by unlocking channel A. |
| j, k, l | The S1 leaves the pending state since channel A is not locked. It gets in the CPU again and starts executing. As it did receive a notification from channel A, it performs a channel read (as simple as lock, memory copy, unlock), continues its execution, and goes out the CPU. |

#### HLP priority boost

ZBus implements the Highest Locker Protocol that relies on the observers’ thread priority to
determine a temporary publisher priority. The protocol considers the channel’s Highest Observer
Priority (HOP); even if the observer is not waiting for a message on the channel, it is considered
in the calculation. The VDED will elevate the publisher’s priority based on the HOP to ensure small
latency and as few preemptions as possible.

Note

The priority boost is enabled by default. To deactivate it, you must set the
[`CONFIG_ZBUS_PRIORITY_BOOST`](../../kconfig.md#CONFIG_ZBUS_PRIORITY_BOOST "CONFIG_ZBUS_PRIORITY_BOOST") configuration.

Warning

ZBus priority boost does not consider runtime observers on the HOP calculations.

The figure below illustrates the actions performed during the VDED execution when T1 publishes to
channel A. The scenario considers the priority boost feature and the following priorities: T1 < MS1
< MS2 < S1.

[![ZBus publishing process details using priority boost.](../../_images/zbus_publishing_process_example_HLP.svg)
](../../_images/zbus_publishing_process_example_HLP.svg)

ZBus VDED execution detail with priority boost enabled and for priority T1 < MS1 < MS2 < S1.

To properly use the priority boost, attaching the observer to a thread is necessary. When the
subscriber is attached to a thread, it assumes its priority, and the priority boost algorithm will
consider the observer’s priority. The following code illustrates the thread-attaching function.

```c
ZBUS_SUBSCRIBER_DEFINE(s1, 4);
void s1_thread(void *ptr1, void *ptr2, void *ptr3)
{
        ARG_UNUSED(ptr1);
        ARG_UNUSED(ptr2);
        ARG_UNUSED(ptr3);

        const struct zbus_channel *chan;

        zbus_obs_attach_to_thread(&s1);

        while (1) {
                zbus_sub_wait(&s1, &chan, K_FOREVER);

                /* Subscriber implementation */

        }
}
K_THREAD_DEFINE(s1_id, CONFIG_MAIN_STACK_SIZE, s1_thread, NULL, NULL, NULL, 2, 0, 0);
```

On the above code, the [`zbus_obs_attach_to_thread()`](../../doxygen/html/group__zbus__apis.md#gabecf160e4d468d0275ad79e22fd0fb5b) will set the `s1` observer with
priority two as the thread has that priority. It is possible to reverse that by detaching the
observer using the [`zbus_obs_detach_from_thread()`](../../doxygen/html/group__zbus__apis.md#ga493c125c31e44d5a222f0e9c6d01249e). Only enabled observers and observations
will be considered on the channel HOP calculation. Masking a specific observation of a channel will
affect the channel HOP.

In summary, the benefits of the feature are:

- The HLP is more effective for zbus than the mutexes priority inheritance;
- No bounded priority inversion will happen among the publisher and the observers;
- No other threads (that are not involved in the communication) with priority between T1 and S1 can
  preempt T1, avoiding unbounded priority inversion;
- Message subscribers will wait for the VDED to finish the message delivery process. So the VDED
  execution will be faster and more consistent;
- The HLP priority is dynamic and can change in execution;
- ZBus operations can be used inside ISRs;
- The priority boosting feature can be turned off, and plain semaphores can be used as the channel
  lock mechanism;
- The Highest Locker Protocol’s major disadvantage, the Inheritance-related Priority Inversion, is
  acceptable in the zbus scenario since it will ensure a small bus latency.

### [Limitations](#id18)

Based on the fact that developers can use zbus to solve many different problems, some challenges
arise. ZBus will not solve every problem, so it is necessary to analyze the situation to be sure
zbus is applicable. For instance, based on the zbus benchmark, it would not be well suited to a
high-speed stream of bytes between threads. The [Pipe](../../kernel/services/data_passing/pipes.md#pipes-v2) kernel object solves this
kind of need.

#### Delivery guarantees

ZBus always delivers the messages to the listeners and message subscribers. However, there are no
message delivery guarantees for subscribers because zbus only sends the notification, but the
message reading depends on the subscriber’s implementation. It is possible to increase the delivery
rate by following design tips:

- Keep the listeners quick-as-possible (deal with them as ISRs). If some processing is needed,
  consider submitting a work item to a work-queue;
- Try to give producers a high priority to avoid losses;
- Leave spare CPU for observers to consume data produced;
- Consider using message queues or pipes for intensive byte transfers.

Warning

ZBus uses [include/zephyr/net\_buf.h](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/net_buf.h) (network buffers) to exchange data with message
subscribers. Thus, choose carefully the configurations
[`CONFIG_ZBUS_MSG_SUBSCRIBER_NET_BUF_POOL_SIZE`](../../kconfig.md#CONFIG_ZBUS_MSG_SUBSCRIBER_NET_BUF_POOL_SIZE "CONFIG_ZBUS_MSG_SUBSCRIBER_NET_BUF_POOL_SIZE") and
[`CONFIG_HEAP_MEM_POOL_SIZE`](../../kconfig.md#CONFIG_HEAP_MEM_POOL_SIZE "CONFIG_HEAP_MEM_POOL_SIZE"). They are crucial to a proper VDED execution
(delivery guarantee) considering message subscribers. If you want to keep an isolated pool for a
specific set of channels, you can use
[`CONFIG_ZBUS_MSG_SUBSCRIBER_NET_BUF_POOL_ISOLATION`](../../kconfig.md#CONFIG_ZBUS_MSG_SUBSCRIBER_NET_BUF_POOL_ISOLATION "CONFIG_ZBUS_MSG_SUBSCRIBER_NET_BUF_POOL_ISOLATION") with a dedicated pool. Look
at the [Message subscriber](../../samples/subsys/zbus/msg_subscriber/README.md#zbus-msg-subscriber "Use zbus message subscribers to listen to messages published to channels.") to see the isolation in action.

Warning

Subscribers will receive only the reference of the changing channel. A data loss may be perceived
if the channel is published twice before the subscriber reads it. The second publication
overwrites the value from the first. Thus, the subscriber will receive two notifications, but
only the last data is there.

#### Message delivery sequence

The message delivery will follow the precedence:

1. Observers defined in a channel using the [`ZBUS_CHAN_DEFINE`](../../doxygen/html/group__zbus__apis.md#ga29a3a39e5c78a34b2d8491615d1f0687) (following the definition
   sequence);
2. Observers defined using the [`ZBUS_CHAN_ADD_OBS`](../../doxygen/html/group__zbus__apis.md#gaf63215f3f53741edf52b4d0d7b2b97df) based on the sequence priority
   (parameter of the macro);
3. The latest is the runtime observers in the addition sequence using the
   [`zbus_chan_add_obs()`](../../doxygen/html/group__zbus__apis.md#gaddd8ce480bc29ead4442e529915cfbf6).

Note

The VDED will ignore all disabled observers or observations.

## [Usage](#id19)

ZBus operation depends on channels and observers. Therefore, it is necessary to determine its
message and observers list during the channel definition. A message is a regular C struct; the
observer can be a subscriber (asynchronous), a message subscriber (asynchronous), or a listener
(synchronous).

The following code defines and initializes a regular channel and its dependencies. This channel
exchanges accelerometer data, for example.

```c
struct acc_msg {
        int x;
        int y;
        int z;
};

ZBUS_CHAN_DEFINE(acc_chan,                           /* Name */
         struct acc_msg,                             /* Message type */

         NULL,                                       /* Validator */
         NULL,                                       /* User Data */
         ZBUS_OBSERVERS(my_listener, my_subscriber,
                        my_msg_subscriber),          /* observers */
         ZBUS_MSG_INIT(.x = 0, .y = 0, .z = 0)       /* Initial value */
);

void listener_callback_example(const struct zbus_channel *chan)
{
        const struct acc_msg *acc;
        if (&acc_chan == chan) {
                acc = zbus_chan_const_msg(chan); // Direct message access
                LOG_DBG("From listener -> Acc x=%d, y=%d, z=%d", acc->x, acc->y, acc->z);
        }
}

ZBUS_LISTENER_DEFINE(my_listener, listener_callback_example);

ZBUS_LISTENER_DEFINE(my_listener2, listener_callback_example);

ZBUS_CHAN_ADD_OBS(acc_chan, my_listener2, 3);

ZBUS_SUBSCRIBER_DEFINE(my_subscriber, 4);
void subscriber_task(void)
{
        const struct zbus_channel *chan;

        while (!zbus_sub_wait(&my_subscriber, &chan, K_FOREVER)) {
                struct acc_msg acc = {0};

                if (&acc_chan == chan) {
                        // Indirect message access
                        zbus_chan_read(&acc_chan, &acc, K_NO_WAIT);
                        LOG_DBG("From subscriber -> Acc x=%d, y=%d, z=%d", acc.x, acc.y, acc.z);
                }
        }
}
K_THREAD_DEFINE(subscriber_task_id, 512, subscriber_task, NULL, NULL, NULL, 3, 0, 0);

ZBUS_MSG_SUBSCRIBER_DEFINE(my_msg_subscriber);
static void msg_subscriber_task(void *ptr1, void *ptr2, void *ptr3)
{
        ARG_UNUSED(ptr1);
        ARG_UNUSED(ptr2);
        ARG_UNUSED(ptr3);
        const struct zbus_channel *chan;

        struct acc_msg acc = {0};

        while (!zbus_sub_wait_msg(&my_msg_subscriber, &chan, &acc, K_FOREVER)) {
                if (&acc_chan == chan) {
                        LOG_INF("From msg subscriber -> Acc x=%d, y=%d, z=%d", acc.x, acc.y, acc.z);
                }
        }
}
K_THREAD_DEFINE(msg_subscriber_task_id, 1024, msg_subscriber_task, NULL, NULL, NULL, 3, 0, 0);
```

It is possible to add static observers to a channel using the [`ZBUS_CHAN_ADD_OBS`](../../doxygen/html/group__zbus__apis.md#gaf63215f3f53741edf52b4d0d7b2b97df). We call
that a post-definition static observer. The command enables us to indicate an initialization
priority that affects the observers’ initialization order. The sequence priority param only affects
the post-definition static observers. There is no possibility to overwrite the message delivery
sequence of the static observers.

Note

It is unnecessary to claim/lock a channel before accessing the message inside the listener since
the event dispatcher calls listeners with the notifying channel already locked. Subscribers,
however, must claim/lock that or use regular read operations to access the message after being
notified.

Channels can have a *validator function* that enables a channel to accept only valid messages.
Publish attempts invalidated by hard channels will return immediately with an error code. This
allows original creators of a channel to exert some authority over other developers/publishers who
may want to piggy-back on their channels. The following code defines and initializes a *hard
channel* and its dependencies. Only valid messages can be published to a *hard channel*. It is
possible because a *validator function* was passed to the channel’s definition. In this example,
only messages with `move` equal to 0, -1, and 1 are valid. Publish function will discard all other
values to `move`.

```c
struct control_msg {
        int move;
};

bool control_validator(const void* msg, size_t msg_size) {
        const struct control_msg* cm = msg;
        bool is_valid = (cm->move == -1) || (cm->move == 0) || (cm->move == 1);
        return is_valid;
}

static int message_count = 0;

ZBUS_CHAN_DEFINE(control_chan,    /* Name */
         struct control_msg,      /* Message type */

         control_validator,       /* Validator */
         &message_count,          /* User data */
         ZBUS_OBSERVERS_EMPTY,    /* observers */
         ZBUS_MSG_INIT(.move = 0) /* Initial value */
);
```

The following sections describe in detail how to use zbus features.

### [Publishing to a channel](#id20)

Messages are published to a channel in zbus by calling [`zbus_chan_pub()`](../../doxygen/html/group__zbus__apis.md#gadfcaba65b397c1d8c31836ef3cf61244). For example, the
following code builds on the examples above and publishes to channel `acc_chan`. The code is
trying to publish the message `acc1` to channel `acc_chan`, and it will wait up to one second
for the message to be published. Otherwise, the operation fails. As can be inferred from the code
sample, it’s OK to use stack allocated messages since VDED copies the data internally.

```c
struct acc_msg acc1 = {.x = 1, .y = 1, .z = 1};
zbus_chan_pub(&acc_chan, &acc1, K_SECONDS(1));
```

Warning

Only use this function inside an ISR with a [`K_NO_WAIT`](../../doxygen/html/group__clock__apis.md#ga3d9541cfe2e8395af66d186efa77362f) timeout.

### [Reading from a channel](#id21)

Messages are read from a channel in zbus by calling [`zbus_chan_read()`](../../doxygen/html/group__zbus__apis.md#ga8209721e0a295c84d112ba1a7171100e). So, for example, the
following code tries to read the channel `acc_chan`, which will wait up to 500 milliseconds to
read the message. Otherwise, the operation fails.

```c
struct acc_msg acc = {0};
zbus_chan_read(&acc_chan, &acc, K_MSEC(500));
```

Warning

Only use this function inside an ISR with a [`K_NO_WAIT`](../../doxygen/html/group__clock__apis.md#ga3d9541cfe2e8395af66d186efa77362f) timeout.

Warning

Choose the timeout of [`zbus_chan_read()`](../../doxygen/html/group__zbus__apis.md#ga8209721e0a295c84d112ba1a7171100e) after receiving a notification from
[`zbus_sub_wait()`](../../doxygen/html/group__zbus__apis.md#ga84a65e276a01ef97eeb5c81b880da72b) carefully because the channel will always be unavailable during the VDED
execution. Using `K_NO_WAIT` for reading is highly likely to return a timeout error if there
are more than one subscriber. For example, consider the VDED illustration again and notice how
`S1` read attempts would definitely fail with K\_NO\_WAIT. For more details, check
the [Virtual Distributed Event Dispatcher](#virtual-distributed-event-dispatcher) section.

### [Notifying a channel](#id22)

It is possible to force zbus to notify a channel’s observers by calling [`zbus_chan_notify()`](../../doxygen/html/group__zbus__apis.md#ga6ec2f463801499e23a011fa4e68aa3e7).
For example, the following code builds on the examples above and forces a notification for the
channel `acc_chan`. Note this can send events with no message, which does not require any data
exchange. See the code example under [Claim and finish a channel](#claim-and-finish-a-channel) where this may become useful.

```c
zbus_chan_notify(&acc_chan, K_NO_WAIT);
```

Warning

Only use this function inside an ISR with a [`K_NO_WAIT`](../../doxygen/html/group__clock__apis.md#ga3d9541cfe2e8395af66d186efa77362f) timeout.

### [Declaring channels and observers](#id23)

For accessing channels or observers from files other than its defining files, it is necessary to
declare them by calling [`ZBUS_CHAN_DECLARE`](../../doxygen/html/group__zbus__apis.md#ga0662b2db8077a8075c07a3afd0161d0f) and [`ZBUS_OBS_DECLARE`](../../doxygen/html/group__zbus__apis.md#ga49f169c6d50a3bad57e1b319362d2924). In other
words, zbus channel definitions and declarations with the same channel names in different files
would point to the same (global) channel. Thus, developers should be careful about existing
channels, and naming new channels or linking will fail. It is possible to declare more than one
channel or observer on the same call. The following code builds on the examples above and displays
the defined channels and observers.

```c
ZBUS_OBS_DECLARE(my_listener, my_subscriber);
ZBUS_CHAN_DECLARE(acc_chan, version_chan);
```

#### Unique channel identifiers

To simplify integrations with external entities, it is possible to assign a unique numeric identifier
to a channel. Users can then retrieve the channel reference by using the identifier with
[`zbus_chan_from_id()`](../../doxygen/html/group__zbus__apis.md#gacef06cf9818ab91be97d45ab5f58a4a3), rather than needing to obtain the reference at compile time with
[`ZBUS_CHAN_DECLARE`](../../doxygen/html/group__zbus__apis.md#ga0662b2db8077a8075c07a3afd0161d0f). Channels using this feature are declared with
[`ZBUS_CHAN_DEFINE_WITH_ID()`](../../doxygen/html/group__zbus__apis.md#ga7c49cba434b90d417859b37722843e5f).

```c
ZBUS_CHAN_DEFINE_WITH_ID(control_chan,    /* Name */
    0x12345678,              /* Unique channel identifier */
    struct control_msg,      /* Message type */
    control_validator,       /* Validator */
    &message_count,          /* User data */
    ZBUS_OBSERVERS_EMPTY,    /* observers */
    ZBUS_MSG_INIT(.move = 0) /* Initial value */
);

static void channel_retrieve(void)
{
    const struct zbus_channel *chan = zbus_chan_from_id(0x12345678);

    ...
}
```

### [Iterating over channels and observers](#id24)

ZBus subsystem also implements [Iterable Sections](../../kernel/iterable_sections/index.md#iterable-sections-api) for channels and
observers, for which there are supporting APIs like [`zbus_iterate_over_channels()`](../../doxygen/html/group__zbus__apis.md#ga6dffd25f4eb368e773c2bd55f34a0e10),
[`zbus_iterate_over_channels_with_user_data()`](../../doxygen/html/group__zbus__apis.md#gab8df108b0238757ff631ec1e120fa2c3), [`zbus_iterate_over_observers()`](../../doxygen/html/group__zbus__apis.md#ga2fa50316993afc5807e9d707d664be14) and
[`zbus_iterate_over_observers_with_user_data()`](../../doxygen/html/group__zbus__apis.md#ga2f4e39c500fed0a6bcfedb5dec3f797a). This feature enables developers to call a
procedure over all declared channels, where the procedure parameter is a [`zbus_channel`](../../doxygen/html/structzbus__channel.md).
The execution sequence is in the alphabetical name order of the channels (see [Iterable
Sections](../../kernel/iterable_sections/index.md#iterable-sections-api) documentation for details). ZBus also implements this feature for
[`zbus_observer`](../../doxygen/html/structzbus__observer.md).

```c
static bool print_channel_data_iterator(const struct zbus_channel *chan, void *user_data)
{
      int *count = user_data;

      LOG_INF("%d - Channel %s:", *count, zbus_chan_name(chan));
      LOG_INF("      Message size: %d", zbus_chan_msg_size(chan));
      LOG_INF("      Observers:");

      ++(*count);

      struct zbus_channel_observation *observation;

      for (int16_t i = *chan->observers_start_idx, limit = *chan->observers_end_idx; i < limit;
            ++i) {
            STRUCT_SECTION_GET(zbus_channel_observation, i, &observation);

            LOG_INF("      - %s", observation->obs->name);
      }

      struct zbus_observer_node *obs_nd, *tmp;

      SYS_SLIST_FOR_EACH_CONTAINER_SAFE(chan->observers, obs_nd, tmp, node) {
            LOG_INF("      - %s", obs_nd->obs->name);
      }

      return true;
}

static bool print_observer_data_iterator(const struct zbus_observer *obs, void *user_data)
{
      int *count = user_data;

      LOG_INF("%d - %s %s", *count, obs->queue ? "Subscriber" : "Listener", zbus_obs_name(obs));

      ++(*count);

      return true;
}

int main(void)
{
      int count = 0;

      LOG_INF("Channel list:");

      zbus_iterate_over_channels_with_user_data(print_channel_data_iterator, &count);

      count = 0;

      LOG_INF("Observers list:");

      zbus_iterate_over_observers_with_user_data(print_observer_data_iterator, &count);

      return 0;
}
```

The code will log the following output:

```shell
D: Channel list:
D: 0 - Channel acc_chan:
D:       Message size: 12
D:       Observers:
D:       - my_listener
D:       - my_subscriber
D: 1 - Channel version_chan:
D:       Message size: 4
D:       Observers:
D: Observers list:
D: 0 - Listener my_listener
D: 1 - Subscriber my_subscriber
```

### [Advanced channel control](#id25)

ZBus was designed to be as flexible and extensible as possible. Thus, there are some features
designed to provide some control and extensibility to the bus.

#### Listeners message access

For performance purposes, listeners can access the receiving channel message directly since they
already have the channel locked for it. To access the channel’s message, the listener should use the
[`zbus_chan_const_msg()`](../../doxygen/html/group__zbus__apis.md#gafee07c355df9ac86b85e601196b56a10) because the channel passed as an argument to the listener function is
a constant pointer to the channel. The const pointer return type tells developers not to modify the
message.

```c
void listener_callback_example(const struct zbus_channel *chan)
{
        const struct acc_msg *acc;
        if (&acc_chan == chan) {
                acc = zbus_chan_const_msg(chan); // Use this
                // instead of zbus_chan_read(chan, &acc, K_MSEC(200))
                // or zbus_chan_msg(chan)

                LOG_DBG("From listener -> Acc x=%d, y=%d, z=%d", acc->x, acc->y, acc->z);
        }
}
```

#### User Data

It is possible to pass custom data into the channel’s `user_data` for various purposes, such as
writing channel metadata. That can be achieved by passing a pointer to the channel definition
macro’s `user_data` field, which will then be accessible by others. Note that `user_data` is
individual for each channel. Also, note that `user_data` access is not thread-safe. For
thread-safe access to `user_data`, see the next section.

#### Claim and finish a channel

To take more control over channels, two functions were added [`zbus_chan_claim()`](../../doxygen/html/group__zbus__apis.md#ga00bfb7db54594029f4d288bcf5b56b3a) and
[`zbus_chan_finish()`](../../doxygen/html/group__zbus__apis.md#ga74747affb345e68ce1d564c349409e59). With these functions, it is possible to access the channel’s metadata
safely. When a channel is claimed, no actions are available to that channel. After finishing the
channel, all the actions are available again.

Warning

Never change the fields of the channel struct directly. It may cause zbus behavior
inconsistencies and scheduling issues.

Warning

Only use this function inside an ISR with a [`K_NO_WAIT`](../../doxygen/html/group__clock__apis.md#ga3d9541cfe2e8395af66d186efa77362f) timeout.

The following code builds on the examples above and claims the `acc_chan` to set the `user_data`
to the channel. Suppose we would like to count how many times the channels exchange messages. We
defined the `user_data` to have the 32 bits integer. This code could be added to the listener code
described above.

```c
if (!zbus_chan_claim(&acc_chan, K_MSEC(200))) {
        int *message_counting = (int *) zbus_chan_user_data(&acc_chan);
        *message_counting += 1;
        zbus_chan_finish(&acc_chan);
}
```

The following code has the exact behavior of the code in [Publishing to a channel](#publishing-to-a-channel).

```c
if (!zbus_chan_claim(&acc_chan, K_MSEC(200))) {
        struct acc_msg *acc1 = (struct acc_msg *) zbus_chan_msg(&acc_chan);
        acc1.x = 1;
        acc1.y = 1;
        acc1.z = 1;
        zbus_chan_finish(&acc_chan);
        zbus_chan_notify(&acc_chan, K_SECONDS(1));
}
```

The following code has the exact behavior of the code in [Reading from a channel](#reading-from-a-channel).

```c
if (!zbus_chan_claim(&acc_chan, K_MSEC(200))) {
        const struct acc_msg *acc1 = (const struct acc_msg *) zbus_chan_const_msg(&acc_chan);
        // access the acc_msg fields directly.
        zbus_chan_finish(&acc_chan);
}
```

#### Runtime observer registration

It is possible to add observers to channels in runtime. This feature uses the heap to allocate the
nodes dynamically. The heap size limits the number of dynamic observers zbus can create. Therefore,
set the [`CONFIG_ZBUS_RUNTIME_OBSERVERS`](../../kconfig.md#CONFIG_ZBUS_RUNTIME_OBSERVERS "CONFIG_ZBUS_RUNTIME_OBSERVERS") to enable the feature. It is possible to
adjust the heap size by changing the configuration [`CONFIG_HEAP_MEM_POOL_SIZE`](../../kconfig.md#CONFIG_HEAP_MEM_POOL_SIZE "CONFIG_HEAP_MEM_POOL_SIZE"). The
following example illustrates the runtime registration usage.

```c
ZBUS_LISTENER_DEFINE(my_listener, callback);
// ...
void thread_entry(void) {
        // ...
        /* Adding the observer to channel chan1 */
        zbus_chan_add_obs(&chan1, &my_listener, K_NO_WAIT);
        /* Removing the observer from channel chan1 */
        zbus_chan_rm_obs(&chan1, &my_listener, K_NO_WAIT);
```

## [Samples](#id26)

For a complete overview of zbus usage, take a look at the samples. There are the following samples
available:

- [zbus Hello World](../../samples/subsys/zbus/hello_world/README.md#zbus-hello-world "Make three threads talk to each other using zbus.") illustrates the code used above in action;
- [Work queue](../../samples/subsys/zbus/work_queue/README.md#zbus-work-queue "Use a work queue to process zbus messages in various ways.") shows how to define and use different kinds of observers.
  Note there is an example of using a work queue instead of executing the listener as an execution
  option;
- [Message subscriber](../../samples/subsys/zbus/msg_subscriber/README.md#zbus-msg-subscriber "Use zbus message subscribers to listen to messages published to channels.") illustrates how to use message subscribers;
- [Dynamic channel](../../samples/subsys/zbus/dyn_channel/README.md#zbus-dyn-channel "Use zbus channels with dynamically allocated messages.") demonstrates how to use dynamically allocated exchanging
  data in zbus;
- [UART bridge](../../samples/subsys/zbus/uart_bridge/README.md#zbus-uart-bridge "Redirect channel events to the host over UART.") shows an example of sending the operation of the channel to
  a host via serial;
- [Remote mock sample](../../samples/subsys/zbus/remote_mock/README.md#zbus-remote-mock "Publish to a zbus instance using UART as a bridge.") illustrates how to implement an external mock (on the host)
  to send and receive messages to and from the bus;
- [zbus Priority Boost](../../samples/subsys/zbus/priority_boost/README.md#zbus-priority-boost "Illustrates zbus priority boost feature with a priority inversion scenario.") illustrates zbus priority boost feature with a priority
  inversion scenario;
- [Runtime observer registration](../../samples/subsys/zbus/runtime_obs_registration/README.md#zbus-runtime-obs-registration "Use zbus' runtime observer registration to filter data generated by a producer.") illustrates a way of using the runtime
  observer registration feature;
- [Confirmed channel](../../samples/subsys/zbus/confirmed_channel/README.md#zbus-confirmed-channel "Use confirmed zbus channels to ensure all subscribers consume a message.") implements a way of implement confirmed channel only
  with subscribers;
- [Benchmarking](../../samples/subsys/zbus/benchmark/README.md#zbus-benchmark "Measure the time for sending 256KB from a producer to N consumers.") implements a benchmark with different combinations of inputs.

## [Suggested Uses](#id27)

Use zbus to transfer data (messages) between threads in one-to-one, one-to-many, and many-to-many
synchronously or asynchronously. Choosing the proper observer type is crucial. Use subscribers for
scenarios that can tolerate message losses and duplications; when they cannot, use message
subscribers (if you need a thread) or listeners (if you need to be lean and fast). In addition to
the listener, another asynchronous message processing mechanism (like [message queues](../../kernel/services/data_passing/message_queues.md#message-queues-v2)) may be necessary to retain the pending message until it gets processed.

Note

ZBus can be used to transfer streams from the producer to the consumer. However, this can
increase zbus’ communication latency. So maybe consider a Pipe a good alternative for this
communication topology.

## [Configuration Options](#id28)

For enabling zbus, it is necessary to enable the [`CONFIG_ZBUS`](../../kconfig.md#CONFIG_ZBUS "CONFIG_ZBUS") option.

Related configuration options:

- [`CONFIG_ZBUS_PRIORITY_BOOST`](../../kconfig.md#CONFIG_ZBUS_PRIORITY_BOOST "CONFIG_ZBUS_PRIORITY_BOOST") zbus Highest Locker Protocol implementation;
- [`CONFIG_ZBUS_CHANNELS_SYS_INIT_PRIORITY`](../../kconfig.md#CONFIG_ZBUS_CHANNELS_SYS_INIT_PRIORITY "CONFIG_ZBUS_CHANNELS_SYS_INIT_PRIORITY") determine the [`SYS_INIT`](../../doxygen/html/group__sys__init.md#gaf507cc0613add8113c41896bd631254f)
  priority used by zbus to organize the channels observations by channel;
- [`CONFIG_ZBUS_CHANNEL_NAME`](../../kconfig.md#CONFIG_ZBUS_CHANNEL_NAME "CONFIG_ZBUS_CHANNEL_NAME") enables the name of channels to be available inside the
  channels metadata. The log uses this information to show the channels’ names;
- [`CONFIG_ZBUS_OBSERVER_NAME`](../../kconfig.md#CONFIG_ZBUS_OBSERVER_NAME "CONFIG_ZBUS_OBSERVER_NAME") enables the name of observers to be available inside
  the channels metadata;
- [`CONFIG_ZBUS_MSG_SUBSCRIBER`](../../kconfig.md#CONFIG_ZBUS_MSG_SUBSCRIBER "CONFIG_ZBUS_MSG_SUBSCRIBER") enables the message subscriber observer type;
- [`CONFIG_ZBUS_MSG_SUBSCRIBER_BUF_ALLOC_DYNAMIC`](../../kconfig.md#CONFIG_ZBUS_MSG_SUBSCRIBER_BUF_ALLOC_DYNAMIC "CONFIG_ZBUS_MSG_SUBSCRIBER_BUF_ALLOC_DYNAMIC") uses the heap to allocate message
  buffers;
- [`CONFIG_ZBUS_MSG_SUBSCRIBER_BUF_ALLOC_STATIC`](../../kconfig.md#CONFIG_ZBUS_MSG_SUBSCRIBER_BUF_ALLOC_STATIC "CONFIG_ZBUS_MSG_SUBSCRIBER_BUF_ALLOC_STATIC") uses the stack to allocate message
  buffers;
- [`CONFIG_ZBUS_MSG_SUBSCRIBER_NET_BUF_POOL_SIZE`](../../kconfig.md#CONFIG_ZBUS_MSG_SUBSCRIBER_NET_BUF_POOL_SIZE "CONFIG_ZBUS_MSG_SUBSCRIBER_NET_BUF_POOL_SIZE") the available number of message
  buffers to be used simultaneously;
- [`CONFIG_ZBUS_MSG_SUBSCRIBER_NET_BUF_POOL_ISOLATION`](../../kconfig.md#CONFIG_ZBUS_MSG_SUBSCRIBER_NET_BUF_POOL_ISOLATION "CONFIG_ZBUS_MSG_SUBSCRIBER_NET_BUF_POOL_ISOLATION") enables the developer to isolate
  a pool for the message subscriber for a set of channels;
- [`CONFIG_ZBUS_MSG_SUBSCRIBER_NET_BUF_STATIC_DATA_SIZE`](../../kconfig.md#CONFIG_ZBUS_MSG_SUBSCRIBER_NET_BUF_STATIC_DATA_SIZE "CONFIG_ZBUS_MSG_SUBSCRIBER_NET_BUF_STATIC_DATA_SIZE") the biggest message of zbus
  channels to be transported into a message buffer;
- [`CONFIG_ZBUS_RUNTIME_OBSERVERS`](../../kconfig.md#CONFIG_ZBUS_RUNTIME_OBSERVERS "CONFIG_ZBUS_RUNTIME_OBSERVERS") enables the runtime observer registration.

## [API Reference](#id29)

[Zbus APIs](../../doxygen/html/group__zbus__apis.md)

Related code samples

- [Benchmarking](../../samples/subsys/zbus/benchmark/README.md#zbus-benchmark "Measure the time for sending 256KB from a producer to N consumers.")Measure the time for sending 256KB from a producer to N consumers.
- [Confirmed channel](../../samples/subsys/zbus/confirmed_channel/README.md#zbus-confirmed-channel "Use confirmed zbus channels to ensure all subscribers consume a message.")Use confirmed zbus channels to ensure all subscribers consume a message.
- [Dynamic channel](../../samples/subsys/zbus/dyn_channel/README.md#zbus-dyn-channel "Use zbus channels with dynamically allocated messages.")Use zbus channels with dynamically allocated messages.
- [Message subscriber](../../samples/subsys/zbus/msg_subscriber/README.md#zbus-msg-subscriber "Use zbus message subscribers to listen to messages published to channels.")Use zbus message subscribers to listen to messages published to channels.
- [Remote mock sample](../../samples/subsys/zbus/remote_mock/README.md#zbus-remote-mock "Publish to a zbus instance using UART as a bridge.")Publish to a zbus instance using UART as a bridge.
- [Runtime observer registration](../../samples/subsys/zbus/runtime_obs_registration/README.md#zbus-runtime-obs-registration "Use zbus' runtime observer registration to filter data generated by a producer.")Use zbus' runtime observer registration to filter data generated by a producer.
- [UART bridge](../../samples/subsys/zbus/uart_bridge/README.md#zbus-uart-bridge "Redirect channel events to the host over UART.")Redirect channel events to the host over UART.
- [Work queue](../../samples/subsys/zbus/work_queue/README.md#zbus-work-queue "Use a work queue to process zbus messages in various ways.")Use a work queue to process zbus messages in various ways.
- [zbus Hello World](../../samples/subsys/zbus/hello_world/README.md#zbus-hello-world "Make three threads talk to each other using zbus.")Make three threads talk to each other using zbus.
- [zbus Priority Boost](../../samples/subsys/zbus/priority_boost/README.md#zbus-priority-boost "Illustrates zbus priority boost feature with a priority inversion scenario.")Illustrates zbus priority boost feature with a priority inversion scenario.

---
version: v4.0.0
source_url: https://docs.zephyrproject.org/4.0.0/services/smf/index.html
original_path: services/smf/index.html
---

# State Machine Framework

## Overview

The State Machine Framework (SMF) is an application agnostic framework that
provides an easy way for developers to integrate state machines into their
application. The framework can be added to any project by enabling the
[`CONFIG_SMF`](../../kconfig.md#CONFIG_SMF "CONFIG_SMF") option.

## State Creation

A state is represented by three functions, where one function implements the
Entry actions, another function implements the Run actions, and the last
function implements the Exit actions. The prototype for these functions is as
follows: `void funct(void *obj)`, where the `obj` parameter is a user
defined structure that has the state machine context, [`smf_ctx`](../../doxygen/html/structsmf__ctx.md), as
its first member. For example:

```c
struct user_object {
   struct smf_ctx ctx;
   /* All User Defined Data Follows */
};
```

The [`smf_ctx`](../../doxygen/html/structsmf__ctx.md) member must be first because the state machine
framework’s functions casts the user defined object to the [`smf_ctx`](../../doxygen/html/structsmf__ctx.md)
type with the [`SMF_CTX`](../../doxygen/html/group__smf.md#ga0bccd3bf96e0887e8a610c1b06e22237) macro.

For example instead of doing this `(struct smf_ctx *)&user_obj`, you could
use `SMF_CTX(&user_obj)`.

By default, a state can have no ancestor states, resulting in a flat state
machine. But to enable the creation of a hierarchical state machine, the
[`CONFIG_SMF_ANCESTOR_SUPPORT`](../../kconfig.md#CONFIG_SMF_ANCESTOR_SUPPORT "CONFIG_SMF_ANCESTOR_SUPPORT") option must be enabled.

By default, the hierarchical state machines do not support initial transitions
to child states on entering a superstate. To enable them the
[`CONFIG_SMF_INITIAL_TRANSITION`](../../kconfig.md#CONFIG_SMF_INITIAL_TRANSITION "CONFIG_SMF_INITIAL_TRANSITION") option must be enabled.

The following macro can be used for easy state creation:

- [`SMF_CREATE_STATE`](../../doxygen/html/group__smf.md#ga5760b98a36ed1ac55eba700cf44c7e1e) Create a state

## State Machine Creation

A state machine is created by defining a table of states that’s indexed by an
enum. For example, the following creates three flat states:

```c
enum demo_state { S0, S1, S2 };

const struct smf_state demo_states[] = {
   [S0] = SMF_CREATE_STATE(s0_entry, s0_run, s0_exit, NULL, NULL),
   [S1] = SMF_CREATE_STATE(s1_entry, s1_run, s1_exit, NULL, NULL),
   [S2] = SMF_CREATE_STATE(s2_entry, s2_run, s2_exit, NULL, NULL)
};
```

And this example creates three hierarchical states:

```c
enum demo_state { S0, S1, S2 };

const struct smf_state demo_states[] = {
   [S0] = SMF_CREATE_STATE(s0_entry, s0_run, s0_exit, parent_s0, NULL),
   [S1] = SMF_CREATE_STATE(s1_entry, s1_run, s1_exit, parent_s12, NULL),
   [S2] = SMF_CREATE_STATE(s2_entry, s2_run, s2_exit, parent_s12, NULL)
};
```

This example creates three hierarchical states with an initial transition
from parent state S0 to child state S2:

```c
enum demo_state { S0, S1, S2 };

/* Forward declaration of state table */
const struct smf_state demo_states[];

const struct smf_state demo_states[] = {
   [S0] = SMF_CREATE_STATE(s0_entry, s0_run, s0_exit, NULL, demo_states[S2]),
   [S1] = SMF_CREATE_STATE(s1_entry, s1_run, s1_exit, demo_states[S0], NULL),
   [S2] = SMF_CREATE_STATE(s2_entry, s2_run, s2_exit, demo_states[S0], NULL)
};
```

To set the initial state, the [`smf_set_initial()`](../../doxygen/html/group__smf.md#ga4389086c6aa3167e8c49226323ae208d) function should be
called.

To transition from one state to another, the [`smf_set_state()`](../../doxygen/html/group__smf.md#ga3e5ac3e2ad105d1a01b4cf0b1a8a6fcb)
function is used.

Note

If [`CONFIG_SMF_INITIAL_TRANSITION`](../../kconfig.md#CONFIG_SMF_INITIAL_TRANSITION "CONFIG_SMF_INITIAL_TRANSITION") is not set,
[`smf_set_initial()`](../../doxygen/html/group__smf.md#ga4389086c6aa3167e8c49226323ae208d) and [`smf_set_state()`](../../doxygen/html/group__smf.md#ga3e5ac3e2ad105d1a01b4cf0b1a8a6fcb) function should
not be passed a parent state as the parent state does not know which
child state to transition to. Transitioning to a parent state is OK
if an initial transition to a child state is defined. A well-formed
HSM should have initial transitions defined for all parent states.

Note

While the state machine is running, [`smf_set_state()`](../../doxygen/html/group__smf.md#ga3e5ac3e2ad105d1a01b4cf0b1a8a6fcb) should
only be called from the Entry or Run function. Calling
[`smf_set_state()`](../../doxygen/html/group__smf.md#ga3e5ac3e2ad105d1a01b4cf0b1a8a6fcb) from Exit functions will generate a warning in the
log and no transition will occur.

## State Machine Execution

To run the state machine, the [`smf_run_state()`](../../doxygen/html/group__smf.md#ga8399cfa9e793a7f188b4ed4fec9f4f90) function should be
called in some application dependent way. An application should cease calling
smf\_run\_state if it returns a non-zero value.

## Preventing Parent Run Actions

Calling [`smf_set_handled()`](../../doxygen/html/group__smf.md#gaa187bbd70434d29c319089faf50c2526) prevents calling the run action of parent
states. It is not required to call [`smf_set_handled()`](../../doxygen/html/group__smf.md#gaa187bbd70434d29c319089faf50c2526) if the state
calls [`smf_set_state()`](../../doxygen/html/group__smf.md#ga3e5ac3e2ad105d1a01b4cf0b1a8a6fcb).

## State Machine Termination

To terminate the state machine, the [`smf_set_terminate()`](../../doxygen/html/group__smf.md#gaae28c66f0652c99ba8e843eeaf02aaf7) function
should be called. It can be called from the entry, run, or exit actions. The
function takes a non-zero user defined value that will be returned by the
[`smf_run_state()`](../../doxygen/html/group__smf.md#ga8399cfa9e793a7f188b4ed4fec9f4f90) function.

## UML State Machines

SMF follows UML hierarchical state machine rules for transitions i.e., the
entry and exit actions of the least common ancestor are not executed on
transition, unless said transition is a transition to self.

The UML Specification for StateMachines may be found in chapter 14 of the UML
specification available here: [https://www.omg.org/spec/UML/](https://www.omg.org/spec/UML/)

SMF breaks from UML rules in:

1. Executing the actions associated with the transition within the context
   of the source state, rather than after the exit actions are performed.
2. Only allowing external transitions to self, not to sub-states. A transition
   from a superstate to a child state is treated as a local transition.
3. Prohibiting transitions using [`smf_set_state()`](../../doxygen/html/group__smf.md#ga3e5ac3e2ad105d1a01b4cf0b1a8a6fcb) in exit actions.

SMF also does not provide any pseudostates except the Initial Pseudostate.
Terminate pseudostates can be modelled by calling [`smf_set_terminate()`](../../doxygen/html/group__smf.md#gaae28c66f0652c99ba8e843eeaf02aaf7)
from the entry action of a ‘terminate’ state. Orthogonal regions are modelled
by calling [`smf_run_state()`](../../doxygen/html/group__smf.md#ga8399cfa9e793a7f188b4ed4fec9f4f90) for each region.

## State Machine Examples

### Flat State Machine Example

This example turns the following state diagram into code using the SMF, where
the initial state is S0.

digraph smf\_flat {
node [style=rounded];
init [shape = point];
STATE\_S0 [shape = box];
STATE\_S1 [shape = box];
STATE\_S2 [shape = box];
init -> STATE\_S0;
STATE\_S0 -> STATE\_S1;
STATE\_S1 -> STATE\_S2;
STATE\_S2 -> STATE\_S0;
}

Flat state machine diagram

Code:

```c
#include <zephyr/smf.h>

/* Forward declaration of state table */
static const struct smf_state demo_states[];

/* List of demo states */
enum demo_state { S0, S1, S2 };

/* User defined object */
struct s_object {
        /* This must be first */
        struct smf_ctx ctx;

        /* Other state specific data add here */
} s_obj;

/* State S0 */
static void s0_entry(void *o)
{
        /* Do something */
}
static void s0_run(void *o)
{
        smf_set_state(SMF_CTX(&s_obj), &demo_states[S1]);
}
static void s0_exit(void *o)
{
        /* Do something */
}

/* State S1 */
static void s1_run(void *o)
{
        smf_set_state(SMF_CTX(&s_obj), &demo_states[S2]);
}
static void s1_exit(void *o)
{
        /* Do something */
}

/* State S2 */
static void s2_entry(void *o)
{
        /* Do something */
}
static void s2_run(void *o)
{
        smf_set_state(SMF_CTX(&s_obj), &demo_states[S0]);
}

/* Populate state table */
static const struct smf_state demo_states[] = {
        [S0] = SMF_CREATE_STATE(s0_entry, s0_run, s0_exit, NULL, NULL),
        /* State S1 does not have an entry action */
        [S1] = SMF_CREATE_STATE(NULL, s1_run, s1_exit, NULL, NULL),
        /* State S2 does not have an exit action */
        [S2] = SMF_CREATE_STATE(s2_entry, s2_run, NULL, NULL, NULL),
};

int main(void)
{
        int32_t ret;

        /* Set initial state */
        smf_set_initial(SMF_CTX(&s_obj), &demo_states[S0]);

        /* Run the state machine */
        while(1) {
                /* State machine terminates if a non-zero value is returned */
                ret = smf_run_state(SMF_CTX(&s_obj));
                if (ret) {
                        /* handle return code and terminate state machine */
                        break;
                }
                k_msleep(1000);
        }
}
```

### Hierarchical State Machine Example

This example turns the following state diagram into code using the SMF, where
S0 and S1 share a parent state and S0 is the initial state.

digraph smf\_hierarchical {
node [style = rounded];
init [shape = point];
STATE\_S0 [shape = box];
STATE\_S1 [shape = box];
STATE\_S2 [shape = box];
subgraph cluster\_0 {
label = "PARENT";
style = rounded;
STATE\_S0 -> STATE\_S1;
}
init -> STATE\_S0;
STATE\_S1 -> STATE\_S2;
STATE\_S2 -> STATE\_S0;
}

Hierarchical state machine diagram

Code:

```c
#include <zephyr/smf.h>

/* Forward declaration of state table */
static const struct smf_state demo_states[];

/* List of demo states */
enum demo_state { PARENT, S0, S1, S2 };

/* User defined object */
struct s_object {
        /* This must be first */
        struct smf_ctx ctx;

        /* Other state specific data add here */
} s_obj;

/* Parent State */
static void parent_entry(void *o)
{
        /* Do something */
}
static void parent_exit(void *o)
{
        /* Do something */
}

/* State S0 */
static void s0_run(void *o)
{
        smf_set_state(SMF_CTX(&s_obj), &demo_states[S1]);
}

/* State S1 */
static void s1_run(void *o)
{
        smf_set_state(SMF_CTX(&s_obj), &demo_states[S2]);
}

/* State S2 */
static void s2_run(void *o)
{
        smf_set_state(SMF_CTX(&s_obj), &demo_states[S0]);
}

/* Populate state table */
static const struct smf_state demo_states[] = {
        /* Parent state does not have a run action */
        [PARENT] = SMF_CREATE_STATE(parent_entry, NULL, parent_exit, NULL, NULL),
        /* Child states do not have entry or exit actions */
        [S0] = SMF_CREATE_STATE(NULL, s0_run, NULL, &demo_states[PARENT], NULL),
        [S1] = SMF_CREATE_STATE(NULL, s1_run, NULL, &demo_states[PARENT], NULL),
        /* State S2 do not have entry or exit actions and no parent */
        [S2] = SMF_CREATE_STATE(NULL, s2_run, NULL, NULL, NULL),
};

int main(void)
{
        int32_t ret;

        /* Set initial state */
        smf_set_initial(SMF_CTX(&s_obj), &demo_states[S0]);

        /* Run the state machine */
        while(1) {
                /* State machine terminates if a non-zero value is returned */
                ret = smf_run_state(SMF_CTX(&s_obj));
                if (ret) {
                        /* handle return code and terminate state machine */
                        break;
                }
                k_msleep(1000);
        }
}
```

When designing hierarchical state machines, the following should be considered:
:   - Ancestor entry actions are executed before the sibling entry actions. For
      example, the parent\_entry function is called before the s0\_entry function.
    - Transitioning from one sibling to another with a shared ancestry does not
      re-execute the ancestor's entry action or execute the exit action.
      For example, the parent\_entry function is not called when transitioning
      from S0 to S1, nor is the parent\_exit function called.
    - Ancestor exit actions are executed after the exit action of the current
      state. For example, the s1\_exit function is called before the parent\_exit
      function is called.
    - The parent\_run function only executes if the child\_run function does not
      call either [`smf_set_state()`](../../doxygen/html/group__smf.md#ga3e5ac3e2ad105d1a01b4cf0b1a8a6fcb) or [`smf_set_handled()`](../../doxygen/html/group__smf.md#gaa187bbd70434d29c319089faf50c2526).

### Event Driven State Machine Example

Events are not explicitly part of the State Machine Framework but an event driven
state machine can be implemented using Zephyr [Events](../../kernel/services/synchronization/events.md#events).

digraph smf\_flat {
node [style=rounded];
init [shape = point];
STATE\_S0 [shape = box];
STATE\_S1 [shape = box];
init -> STATE\_S0;
STATE\_S0 -> STATE\_S1 [label = "BTN EVENT"];
STATE\_S1 -> STATE\_S0 [label = "BTN EVENT"];
}

Event driven state machine diagram

Code:

```c
#include <zephyr/kernel.h>
#include <zephyr/drivers/gpio.h>
#include <zephyr/smf.h>

#define SW0_NODE        DT_ALIAS(sw0)

/* List of events */
#define EVENT_BTN_PRESS BIT(0)

static const struct gpio_dt_spec button =
        GPIO_DT_SPEC_GET_OR(SW0_NODE, gpios, {0});

static struct gpio_callback button_cb_data;

/* Forward declaration of state table */
static const struct smf_state demo_states[];

/* List of demo states */
enum demo_state { S0, S1 };

/* User defined object */
struct s_object {
        /* This must be first */
        struct smf_ctx ctx;

        /* Events */
        struct k_event smf_event;
        int32_t events;

        /* Other state specific data add here */
} s_obj;

/* State S0 */
static void s0_entry(void *o)
{
        printk("STATE0\n");
}

static void s0_run(void *o)
{
        struct s_object *s = (struct s_object *)o;

        /* Change states on Button Press Event */
        if (s->events & EVENT_BTN_PRESS) {
                smf_set_state(SMF_CTX(&s_obj), &demo_states[S1]);
        }
}

/* State S1 */
static void s1_entry(void *o)
{
        printk("STATE1\n");
}

static void s1_run(void *o)
{
        struct s_object *s = (struct s_object *)o;

        /* Change states on Button Press Event */
        if (s->events & EVENT_BTN_PRESS) {
                smf_set_state(SMF_CTX(&s_obj), &demo_states[S0]);
        }
}

/* Populate state table */
static const struct smf_state demo_states[] = {
        [S0] = SMF_CREATE_STATE(s0_entry, s0_run, NULL, NULL, NULL),
        [S1] = SMF_CREATE_STATE(s1_entry, s1_run, NULL, NULL, NULL),
};

void button_pressed(const struct device *dev,
                struct gpio_callback *cb, uint32_t pins)
{
        /* Generate Button Press Event */
        k_event_post(&s_obj.smf_event, EVENT_BTN_PRESS);
}

int main(void)
{
        int ret;

        if (!gpio_is_ready_dt(&button)) {
                printk("Error: button device %s is not ready\n",
                        button.port->name);
                return;
        }

        ret = gpio_pin_configure_dt(&button, GPIO_INPUT);
        if (ret != 0) {
                printk("Error %d: failed to configure %s pin %d\n",
                        ret, button.port->name, button.pin);
                return;
        }

        ret = gpio_pin_interrupt_configure_dt(&button,
                GPIO_INT_EDGE_TO_ACTIVE);
        if (ret != 0) {
                printk("Error %d: failed to configure interrupt on %s pin %d\n",
                        ret, button.port->name, button.pin);
                return;
        }

        gpio_init_callback(&button_cb_data, button_pressed, BIT(button.pin));
        gpio_add_callback(button.port, &button_cb_data);

        /* Initialize the event */
        k_event_init(&s_obj.smf_event);

        /* Set initial state */
        smf_set_initial(SMF_CTX(&s_obj), &demo_states[S0]);

        /* Run the state machine */
        while(1) {
                /* Block until an event is detected */
                s_obj.events = k_event_wait(&s_obj.smf_event,
                                EVENT_BTN_PRESS, true, K_FOREVER);

                /* State machine terminates if a non-zero value is returned */
                ret = smf_run_state(SMF_CTX(&s_obj));
                if (ret) {
                        /* handle return code and terminate state machine */
                        break;
                }
        }
}
```

### State Machine Example With Initial Transitions And Transition To Self

[tests/lib/smf/src/test\_lib\_self\_transition\_smf.c](https://github.com/zephyrproject-rtos/zephyr/blob/main/tests/lib/smf/src/test_lib_self_transition_smf.c) defines a state
machine for testing the initial transitions and transitions to self in a parent
state. The statechart for this test is below.

digraph smf\_hierarchical\_initial {
compound=true;
node [style = rounded];
"smf\_set\_initial()" [shape=plaintext fontname=Courier];
ab\_init\_state [shape = point];
STATE\_A [shape = box];
STATE\_B [shape = box];
STATE\_C [shape = box];
STATE\_D [shape = box];
DC[shape=point height=0 width=0 label=<>]
subgraph cluster\_root {
label = "ROOT";
style = rounded;
subgraph cluster\_ab {
label = "PARENT\_AB";
style = rounded;
ab\_init\_state -> STATE\_A;
STATE\_A -> STATE\_B;
}
subgraph cluster\_c {
label = "PARENT\_C";
style = rounded;
STATE\_B -> STATE\_C [ltail=cluster\_ab]
}
STATE\_C -> DC [ltail=cluster\_c, dir=none];
DC -> STATE\_C [lhead=cluster\_c];
STATE\_C -> STATE\_D
}
"smf\_set\_initial()" -> STATE\_A [lhead=cluster\_ab]
}

Test state machine for UML State Transitions

## API Reference

[State Machine Framework API](../../doxygen/html/group__smf.md)

Related code samples

- [Hierarchical State Machine Demo based on example from PSiCC2](../../samples/subsys/smf/hsm_psicc2/README.md#smf_hsm_psicc2 "Implement an event-driven hierarchical state machine using State Machine Framework (SMF).")Implement an event-driven hierarchical state machine using State Machine Framework (SMF).
- [SMF Calculator](../../samples/subsys/smf/smf_calculator/README.md#smf_calculator "Create a simple desk calculator using the State Machine Framework.")Create a simple desk calculator using the State Machine Framework.

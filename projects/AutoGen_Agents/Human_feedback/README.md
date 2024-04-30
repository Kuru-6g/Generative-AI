**Currently AutoGen supports three modes for human input. The mode is specified through the human_input_mode argument of the ConversableAgent. The three modes are:**

1.NEVER: human input is never requested.

2.TERMINATE (default): human input is only requested when a termination condition is met. Note that in this mode if the human chooses to intercept and reply, the conversation continues and the counter used by max_consecutive_auto_reply is reset.

3.ALWAYS: human input is always requested and the human can choose to skip and trigger an auto-reply, intercept and provide feedback, or terminate the conversation. Note that in this mode termination based on max_consecutive_auto_reply is ignored.

---
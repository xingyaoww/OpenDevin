# Security

Given the impressive capabilities of OpenDevin and similar coding agents, ensuring robust security measures is essential to prevent unintended actions or security breaches. The SecurityAnalyzer framework provides a structured approach to monitor and analyze agent actions for potential security risks.

## SecurityAnalyzer Base Class

The `SecurityAnalyzer` class (analyzer.py) is an abstract base class designed to listen to an event stream and analyze actions for security risks and eventually act before the action is executed. Below is a detailed explanation of its components and methods:

### Initialization

- **event_stream**: An instance of `EventStream` that the analyzer will listen to for events.

### Event Handling

- **on_event(event: Event)**: Handles incoming events. If the event is an `Action`, it evaluates its security risk and acts upon it.

### Abstract Methods

- **handle_api_request(request: Request)**: Abstract method to handle API requests.
- **log_event(event: Event)**: Logs events.
- **act(event: Event)**: Defines actions to take based on the analyzed event.
- **security_risk(event: Action)**: Evaluates the security risk of an action and returns the risk level.

In conclusion, a concrete security analyzer should evaluate the risk of each event and act accordingly (e.g. auto-confirm, send Slack message, etc).

For customization and decoupling from the OpenDevin core logic, the security analyzer can define its own API endpoints that can then be accessed from the frontend. These API endpoints need to be secured (do not allow more capabilities than the core logic provides).

## Implemented Security Analyzers

### Invariant

It uses the [Invariant Analyzer](https://github.com/invariantlabs-ai/invariant) to analyze traces and detect potential issues with OpenDevin's workflow. It uses confirmation mode to ask for user confirmation on potentially risky actions. 

This allows the agent to run autonomously without fear that it will inadvertently compromise security or perform unintended actions that could be harmful.

Features:

* Detects:
    * potential secret leaks by the agent
    * security issues in Python code
    * malicious bash commands
* Logs:
    * actions and their associated risk
    * OpenDevin traces in JSON format
* Run-time settings:
    * the [invariant policy](https://github.com/invariantlabs-ai/invariant?tab=readme-ov-file#policy-language)
    * acceptable risk threshold
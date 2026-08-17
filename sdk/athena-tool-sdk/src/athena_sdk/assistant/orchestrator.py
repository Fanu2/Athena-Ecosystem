from athena_sdk.runtime import (
    run_plugin
)

from .router import (
    route_request
)

from .planner import (
    create_plan
)

from .selector import (
    select_tool
)


def execute_request(
    request: str
):

    intent = route_request(
        request
    )

    plan = create_plan(
        intent
    )

    results = []

    for step in plan.steps:

        tool = select_tool(
            step.capability
        )

        result = run_plugin(
            tool
        )

        results.append(
            {
                "tool": tool.name,
                "result": result
            }
        )

    return {
        "intent": intent,
        "plan": plan,
        "results": results
    }

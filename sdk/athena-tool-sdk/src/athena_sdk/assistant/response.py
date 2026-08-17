from dataclasses import dataclass


@dataclass
class AssistantResponse:

    status: str

    message: str

    tool: str | None = None



def compose_response(
    execution_result
):

    results = execution_result.get(
        "results",
        []
    )

    if not results:

        return AssistantResponse(
            status="failed",
            message="No execution result"
        )


    first = results[0]

    tool = first["tool"]

    result = first["result"]


    if result["result"].status == "success":

        return AssistantResponse(
            status="success",
            message=(
                f"Task completed using {tool}"
            ),
            tool=tool
        )


    return AssistantResponse(
        status="failed",
        message=(
            f"Task failed using {tool}"
        ),
        tool=tool
    )

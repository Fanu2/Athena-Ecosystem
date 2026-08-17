from .models import (
    AssistantIntent
)


def route_request(
    request: str
):

    text = request.lower()


    if "messenger" in text:

        return AssistantIntent(
            action="import",
            capability="conversation_import",
            input_type="messenger_export"
        )


    if "git" in text or "repository" in text:

        return AssistantIntent(
            action="analyze",
            capability="repository_analysis",
            input_type="git_repository"
        )


    raise LookupError(
        "No matching intent"
    )

from .profile import (
    ModelProfile,
)


def select_model(
    models: list[ModelProfile],
    capability: str
):

    matches = []

    for model in models:

        if capability in model.specialization:

            matches.append(
                model
            )


    if not matches:

        return None


    return sorted(
        matches,
        key=lambda m:
        (
            m.speed == "fast"
        ),
        reverse=True
    )[0]

from dataclasses import dataclass

from .profile import (
    ModelProfile,
)


@dataclass
class ModelMatch:

    model: ModelProfile

    score: float



def match_capabilities(
    models: list[ModelProfile],
    requirements: list[str]
):

    matches = []


    for model in models:

        score = 0


        for requirement in requirements:

            if (
                requirement
                in model.specialization
            ):

                score += 1


        if score > 0:

            matches.append(
                ModelMatch(
                    model=model,
                    score=score / len(requirements)
                )
            )


    return sorted(
        matches,
        key=lambda item:
        item.score,
        reverse=True
    )

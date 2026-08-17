from athena_sdk.models import (
    ModelProfile,
    match_capabilities,
)


def test_capability_matching():

    models = [

        ModelProfile(
            name="general",
            provider="ollama",
            context_size=4096,
            memory_requirement="4GB",
            speed="fast",
            specialization=[
                "chat"
            ]
        ),

        ModelProfile(
            name="coder",
            provider="ollama",
            context_size=8192,
            memory_requirement="8GB",
            speed="medium",
            specialization=[
                "coding",
                "reasoning"
            ]
        ),
    ]


    result = match_capabilities(
        models,
        [
            "coding",
            "reasoning"
        ]
    )


    assert len(result) == 1


    assert (
        result[0].model.name
        ==
        "coder"
    )


    assert (
        result[0].score
        ==
        1.0
    )

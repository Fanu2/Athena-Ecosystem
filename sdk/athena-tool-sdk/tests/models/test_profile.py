from athena_sdk.models import (
    ModelProfile,
)


def test_model_profile():

    profile = ModelProfile(
        name="qwen3",
        provider="ollama",
        context_size=8192,
        memory_requirement="8GB",
        speed="fast",
        specialization=[
            "coding",
            "reasoning"
        ]
    )


    assert (
        profile.name
        ==
        "qwen3"
    )


    assert (
        "coding"
        in profile.specialization
    )

from athena_sdk.models import (
    ModelProfile,
    select_model,
)


def test_model_router():

    models = [

        ModelProfile(
            name="small-chat",
            provider="ollama",
            context_size=4096,
            memory_requirement="4GB",
            speed="fast",
            specialization=[
                "chat"
            ]
        ),

        ModelProfile(
            name="code-model",
            provider="ollama",
            context_size=8192,
            memory_requirement="8GB",
            speed="medium",
            specialization=[
                "coding"
            ]
        ),
    ]


    result = select_model(
        models,
        "coding"
    )


    assert (
        result.name
        ==
        "code-model"
    )

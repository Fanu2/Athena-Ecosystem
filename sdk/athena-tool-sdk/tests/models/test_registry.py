from athena_sdk.models import (
    ModelRegistry,
    ModelInfo,
)


def test_model_registry():

    registry = ModelRegistry()


    registry.add(
        ModelInfo(
            name="qwen3",
            provider="ollama",
            model_type="llm",
            capabilities=[
                "chat",
                "reasoning"
            ]
        )
    )


    result = registry.find(
        "reasoning"
    )


    assert len(result) == 1


    assert (
        result[0].name
        ==
        "qwen3"
    )

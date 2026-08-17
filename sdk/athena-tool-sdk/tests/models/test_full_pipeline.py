from athena_sdk.models import (
    ModelRegistry,
    ModelInfo,
    ModelProfile,
    select_model,
    match_capabilities,
)


def test_model_intelligence_pipeline():

    # Registry

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


    assert len(
        registry.all()
    ) == 1


    # Profiles

    models = [

        ModelProfile(
            name="qwen3",
            provider="ollama",
            context_size=8192,
            memory_requirement="8GB",
            speed="fast",
            specialization=[
                "chat",
                "reasoning"
            ]
        )
    ]


    # Router

    selected = select_model(
        models,
        "reasoning"
    )


    assert (
        selected.name
        ==
        "qwen3"
    )


    # Capability Matching

    matches = match_capabilities(
        models,
        [
            "chat",
            "reasoning"
        ]
    )


    assert (
        matches[0].score
        ==
        1.0
    )

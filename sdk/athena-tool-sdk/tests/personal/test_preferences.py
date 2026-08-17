from athena_sdk.personal import (
    Preference,
    PreferenceStore,
)


def test_preferences():

    store = PreferenceStore()


    store.add(
        Preference(
            key="response_style",
            value="developer",
            category="assistant"
        )
    )


    result = store.get(
        "response_style"
    )


    assert result.value == "developer"


    assert len(
        store.all()
    ) == 1

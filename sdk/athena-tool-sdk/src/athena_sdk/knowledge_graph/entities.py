from dataclasses import dataclass


@dataclass
class Entity:

    name: str

    entity_type: str



def extract_entities(
    text: str
):

    entities = []

    words = text.split()

    for word in words:

        clean = (
            word
            .strip(
                ".,!?()[]{}"
            )
        )

        if (
            clean
            and clean[0].isupper()
        ):

            entities.append(
                Entity(
                    name=clean,
                    entity_type="concept"
                )
            )

    return entities

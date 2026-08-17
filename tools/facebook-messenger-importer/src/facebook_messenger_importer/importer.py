from .parser import parse_messenger_export
from .converter import conversation_to_akp
from .exporter import export_akp


def import_messenger(
    input_file,
    output_dir
):

    conversations = parse_messenger_export(
        input_file
    )

    exported = 0

    for index, conversation in enumerate(
        conversations,
        start=1
    ):

        package = conversation_to_akp(
            conversation
        )

        export_akp(
            package,
            output_dir,
            f"conversation-{index:03d}.akp.json"
        )

        exported += 1

    return {
        "input": len(conversations),
        "exported": exported,
        "status": "success"
    }

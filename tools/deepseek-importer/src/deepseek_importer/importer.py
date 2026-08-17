from .parser import parse_deepseek_export
from .normalizer import normalize_conversation
from .converter import conversation_to_akp
from .exporter import export_akp
from .report import ImportReport


def import_deepseek(
    input_file: str,
    output_dir: str
) -> dict:
    """
    Complete DeepSeek import pipeline.
    """

    conversations = parse_deepseek_export(
        input_file
    )

    exported = 0
    warnings = []

    for index, conversation in enumerate(
        conversations,
        start=1
    ):

        if not conversation.title:
            warnings.append(
                f"Conversation {index} had no title"
            )

        normalized = normalize_conversation(
            conversation
        )

        package = conversation_to_akp(
            normalized
        )

        export_akp(
            package,
            output_dir,
            f"conversation-{index:03d}.akp.json"
        )

        exported += 1

    report = ImportReport(
        tool="athena-deepseek-importer",
        version="0.1",
        source="DeepSeek",
        input_count=len(conversations),
        output_count=exported,
        warnings=warnings
    )

    return {
        "input": len(conversations),
        "exported": exported,
        "status": "success",
        "report": report
    }

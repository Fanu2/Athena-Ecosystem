from dataclasses import dataclass, field
from datetime import datetime, timezone


@dataclass
class ImportReport:
    """
    Athena tool import report.
    """

    tool: str
    version: str
    source: str

    input_count: int
    output_count: int

    warnings: list[str] = field(
        default_factory=list
    )

    created_at: str = field(
        default_factory=lambda:
        datetime.now(
            timezone.utc
        ).isoformat()
    )

    def display(self) -> str:
        lines = [
            "Athena DeepSeek Import Report",
            "=============================",
            "",
            f"Tool: {self.tool}",
            f"Version: {self.version}",
            f"Source: {self.source}",
            "",
            f"Input conversations: {self.input_count}",
            f"AKP created: {self.output_count}",
            "",
            "Warnings:"
        ]

        if self.warnings:
            for warning in self.warnings:
                lines.append(
                    f"- {warning}"
                )
        else:
            lines.append(
                "- None"
            )

        lines.extend(
            [
                "",
                f"Created: {self.created_at}"
            ]
        )

        return "\n".join(lines)

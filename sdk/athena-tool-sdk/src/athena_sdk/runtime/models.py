from dataclasses import dataclass


@dataclass
class ExecutionResult:

    tool: str

    status: str

    output: str

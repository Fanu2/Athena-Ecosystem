from .models import KnowledgePackage


class AKPValidationError(Exception):
    pass


def validate(package: KnowledgePackage) -> bool:
    """
    Validate Athena Knowledge Package v1.0
    """

    if not package.akp_version:
        raise AKPValidationError(
            "Missing AKP version"
        )

    if not package.title:
        raise AKPValidationError(
            "Missing title"
        )

    if not package.source:
        raise AKPValidationError(
            "Missing source"
        )

    if not package.confidence:
        raise AKPValidationError(
            "Missing confidence"
        )

    if not package.evidence:
        raise AKPValidationError(
            "Missing evidence"
        )

    return True

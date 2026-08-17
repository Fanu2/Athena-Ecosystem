from dataclasses import dataclass


@dataclass
class EvidenceScore:

    node_id: str

    score: float

    explanation: str



def evaluate_evidence_path(
    graph,
    answer_id: str
):

    score = 0.0

    evidence_nodes = []


    for edge in graph.edges:

        if (
            edge.source == answer_id
            and edge.relation
            == "supported_by"
        ):

            score += 1.0

            evidence_nodes.append(
                edge.target
            )


    explanation = (
        "Evidence found"
        if evidence_nodes
        else
        "No supporting evidence found"
    )


    return EvidenceScore(

        node_id=answer_id,

        score=score,

        explanation=explanation
    )

from dataclasses import dataclass


@dataclass
class SearchResult:

    item: str

    score: float



def search_workspace(
    workspace,
    query: str
):

    query = query.lower()

    results = []

    for item in workspace.knowledge:

        score = 0.0

        if query in item.lower():

            score = 1.0

        elif any(
            word in item.lower()
            for word in query.split()
        ):

            score = 0.5


        if score > 0:

            results.append(
                SearchResult(
                    item=item,
                    score=score
                )
            )

    return results

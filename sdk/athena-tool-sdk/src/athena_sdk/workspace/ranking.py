def rank_memory(
    memories
):

    def score(item):

        value = 0

        if item.important:

            value += 10

        value += item.access_count

        return value


    return sorted(
        memories,
        key=score,
        reverse=True
    )

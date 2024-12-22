from collections import defaultdict, deque

from utils import load_file


def parse_input() -> tuple[dict, list]:
    data = load_file(day=5)
    rules_text, updates_text = data.split("\n\n")

    rules = defaultdict(list)
    for rule in rules_text.split("\n"):
        key, value = rule.split("|")
        rules[key].append(value)

    updates = updates_text.split("\n")
    return rules, updates


def get_valid_updates(rules: dict, updates: list) -> list:
    valid_updates = []
    for update in updates:
        pages = update.split(",")
        seen = []
        failed = False
        for page in pages:
            if seen == []:
                seen.append(page)
                continue

            for num in rules.get(page, []):
                if num in seen:
                    failed = True

            seen.append(page)

        if not failed:
            valid_updates.append(update)
    return valid_updates


def part1():
    rules, updates = parse_input()
    valid_updates = get_valid_updates(rules, updates)

    result = 0
    for update in valid_updates:
        numbers = update.split(",")
        result += int(numbers[len(numbers) // 2])
    print(result)


def parse_rules(rules: dict) -> tuple[dict, dict]:
    graph = defaultdict(list)
    in_degree = defaultdict(int)

    for node, neighbors in rules.items():
        for neighbor in neighbors:
            graph[node].append(neighbor)
            in_degree[neighbor] += 1
        if node not in in_degree:
            in_degree[node] = 0
    return graph, in_degree


def get_correct_ordering(update: str, rules: dict) -> list:
    graph, in_degree = parse_rules(rules)
    update = update.split(",")
    irrelevant_nodes = [node for node in in_degree if node not in update]
    for node in irrelevant_nodes:
        pages = graph[node]
        for page in pages:
            in_degree[page] -= 1

    queue = deque([node for node, degree in in_degree.items() if degree == 0])
    result = []
    while queue:
        node = queue.popleft()
        result.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return [page for page in result if page in update]


def part2():
    rules, updates = parse_input()
    valid_updates = get_valid_updates(rules, updates)
    invalid_updates = [update for update in updates if update not in valid_updates]

    result = 0
    for update in invalid_updates:
        correct_ordering = get_correct_ordering(update, rules)
        result += int(correct_ordering[len(correct_ordering) // 2])
    print(result)


if __name__ == "__main__":
    part1()
    part2()

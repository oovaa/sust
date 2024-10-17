class KnowledgeBase:
    def __init__(self):
        self.rules = []
        self.facts = []

    def add_rule(self, rule):
        self.rules.append(rule)

    def add_fact(self, fact):
        self.facts.append(fact)

    def backward_chain(self, query):
        if query in self.facts:
            return True
        for rule in self.rules:
            if rule.consequent == query:
                if all(
                    self.backward_chain(antecedent) for antecedent in rule.antecedents
                ):
                    self.facts.append(query)
                    return True
        return False


class Rule:
    def __init__(self, antecedents, consequent):
        self.antecedents = antecedents
        self.consequent = consequent


# Example usage
if __name__ == "__main__":
    kb = KnowledgeBase()

    # Adding facts
    kb.add_fact("A")
    kb.add_fact("B")

    # Adding rules
    kb.add_rule(Rule(["A", "B"], "C"))
    kb.add_rule(Rule(["C"], "D"))

    # Querying
    query = "D"
    result = kb.backward_chain(query)
    print(f"Query '{query}' is {'true' if result else 'false'}")

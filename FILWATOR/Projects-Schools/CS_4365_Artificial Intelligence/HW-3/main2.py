import sys

def complement(lit):
    return lit[1:] if lit.startswith("~") else "~" + lit

class Clause:
    def __init__(self, literals, parent_info="{}"):
        # Remove duplicates while preserving order.
        seen = set()
        self.literals = []
        for lit in literals:
            if lit not in seen:
                self.literals.append(lit)
                seen.add(lit)
        self.parent_info = parent_info

    def canonical(self):
        # Return a canonical representation (order-independent) used for duplicate checking.
        return " ".join(sorted(self.literals))

    def is_trivial(self):
        # A clause is trivial if it contains a literal and its complement.
        lits = set(self.literals)
        for lit in lits:
            if complement(lit) in lits:
                return True
        return False

    def clause_string(self):
        # Return "Contradiction" for an empty clause.
        return "Contradiction" if not self.literals else " ".join(self.literals)

def read_kb(filepath):
    kb = []
    with open(filepath, "r") as f:
        lines = [line.strip() for line in f if line.strip()]
    # All lines except the last are the KB clauses.
    for line in lines[:-1]:
        tokens = line.split()
        clause = Clause(tokens)
        if not clause.is_trivial():
            kb.append(clause)
    # The last line is the target clause.
    target = lines[-1]
    target_tokens = target.split()
    # Negate the target clause: if the negation is a conjunction, split it into separate clauses.
    for lit in target_tokens:
        new_clause = Clause([complement(lit)])
        kb.append(new_clause)
    return kb

def resolve_direction(c1, c2, num1, num2):
    """Try resolving clause c1 with c2 in one direction.
       For each literal in c1, if its complement is in c2, create a new clause."""
    resolvents = []
    for lit in c1.literals:
        comp = complement(lit)
        if comp in c2.literals:
            # Build new clause: union of c1 and c2 without the complementary pair.
            new_literals = []
            for l in c1.literals:
                if l != lit:
                    new_literals.append(l)
            for l in c2.literals:
                if l != comp and l not in new_literals:
                    new_literals.append(l)
            resolvent = Clause(new_literals, "{" + f"{num1}, {num2}" + "}")
            if not resolvent.is_trivial():
                resolvents.append(resolvent)
    return resolvents

def resolve_clauses(c1, c2, num1, num2):
    # Try both directions to catch all complementary pairs.
    res = []
    res += resolve_direction(c1, c2, num1, num2)
    res += resolve_direction(c2, c1, num2, num1)
    return res

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <path_to_kb_file>")
        sys.exit(1)
    
    kb_path = sys.argv[1]
    kb = read_kb(kb_path)
    # Set for checking duplicates using canonical representation.
    clause_set = set(c.canonical() for c in kb)
    
    contradiction_found = False
    i = 0
    # Resolution loop: process new clauses until either a contradiction is found or no new clauses.
    while i < len(kb):
        # For each clause i, try with every clause j with j < i.
        for j in range(i):
            new_resolvents = resolve_clauses(kb[i], kb[j], i+1, j+1)
            for resolvent in new_resolvents:
                canon = resolvent.canonical()
                if canon in clause_set:
                    continue
                clause_set.add(canon)
                kb.append(resolvent)
                # As soon as the empty clause (contradiction) is produced, break out.
                if not resolvent.literals:
                    contradiction_found = True
                    # Break out of inner loops by setting i to len(kb)
                    i = len(kb)
                    break
            if contradiction_found:
                break
        if contradiction_found:
            break
        i += 1

    # Print every clause in order.
    for index, clause in enumerate(kb):
        print(f"{index+1}. {clause.clause_string()} {clause.parent_info}")
    # Print final result.
    print("Valid" if contradiction_found else "Fail")

if __name__ == "__main__":
    main()

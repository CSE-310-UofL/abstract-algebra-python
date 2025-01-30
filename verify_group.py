def isNonEmpty(operationTable):
    """Checks if the table is non-empty."""
    return len(operationTable) > 0 and len(operationTable[0]) > 0

def isClosed(operationTable, elements):
    """Checks if the set is closed under the operation (i.e., results remain in the set)."""
    validElements = set(elements)
    for row in operationTable:
        for val in row:
            if val not in validElements:
                return False
    return True

def findIdentity(operationTable, elements):
    """Finds the identity element of the operation if it exists."""
    size = len(elements)
    for i in range(size):
        identityCandidate = elements[i]
        if all(operationTable[i][j] == elements[j] and operationTable[j][i] == elements[j] for j in range(size)):
            return identityCandidate
    return None

def findAdditiveInverse(operationTable, elements,identity):
    """Finds the additive inverse for each element in the set, if it exists."""
    size = len(elements)
    inverseDict = {}
    
    if identity is None:
        return inverseDict
    
    for i in range(size):
        for j in range(size):
            if operationTable[i][j] == identity:
                inverseDict[elements[i]] = elements[j]
                break
    
    return inverseDict

def getAllInverses(operationTable, elements,identity):
    """Returns an array of additive inverses."""
    inverses = findAdditiveInverse(operationTable, elements,identity)
    return [inverses.get(e, None) for e in elements]

def isAssociative(operationTable, elements):
    """Checks if the operation satisfies associativity: (a * b) * c == a * (b * c)."""
    indexMap = {elem: i for i, elem in enumerate(elements)}
    
    for a in elements:
        for b in elements:
            for c in elements:
                left = operationTable[indexMap[operationTable[indexMap[a]][indexMap[b]]]][indexMap[c]]
                right = operationTable[indexMap[a]][indexMap[operationTable[indexMap[b]][indexMap[c]]]]
                if left != right:
                    return False
    return True

# Example usage
if __name__ == "__main__":
    operationTable = [["a", "b"], ["b", "a"]]  # Replace with actual operation table
    elements = list(set(sum(operationTable, [])))
    elements.sort()
    identity = findIdentity(operationTable,elements)
    
    print("Non-empty:", isNonEmpty(operationTable))
    print("Closed under operation:", isClosed(operationTable, elements))
    print("Identity element:", findIdentity(operationTable, elements))
    print("Additive inverses:", findAdditiveInverse(operationTable, elements,identity))
    print("Array of inverses:", getAllInverses(operationTable, elements,identity))
    print("Associativity:", isAssociative(operationTable, elements))

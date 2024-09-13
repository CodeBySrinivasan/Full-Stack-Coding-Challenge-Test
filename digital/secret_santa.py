import random

def assign_santas(participants):
    if len(participants) < 2:
        raise ValueError("Need at least two participants")
    
    santas = participants[:]
    while True:
        random.shuffle(santas)
        # Check if no participant is assigned to themselves
        if all(participant != santas[i] for i, participant in enumerate(participants)):
            break
    
    return {participant: santas[i] for i, participant in enumerate(participants)}

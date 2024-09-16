import random

def create_initial_state(N):
    # Cria uma solução inicial aleatória
    state = list(range(N))
    random.shuffle(state)
    return state

def get_attacking_pairs(state):
    # Conta o número de pares de rainhas que se atacam
    N = len(state)
    attacking_pairs = 0
    for i in range(N):
        for j in range(i + 1, N):
            if (state[i] == state[j] or
                abs(state[i] - state[j]) == abs(i - j)):
                attacking_pairs += 1
    return attacking_pairs

def get_neighbors(state):
    # Gera todos os vizinhos possíveis (troca duas rainhas de coluna)
    neighbors = []
    for i in range(len(state)):
        for j in range(i + 1, len(state)):
            new_state = state[:]
            new_state[i], new_state[j] = new_state[j], new_state[i]
            neighbors.append(new_state)
    return neighbors

def hill_climbing(N):
    current_state = create_initial_state(N)
    current_attacks = get_attacking_pairs(current_state)

    while True:
        neighbors = get_neighbors(current_state)
        next_state = None
        next_attacks = current_attacks

        for neighbor in neighbors:
            attacks = get_attacking_pairs(neighbor)
            if attacks < next_attacks:
                next_attacks = attacks
                next_state = neighbor
        
        if next_attacks >= current_attacks:
            # Não há melhoria, então terminamos
            break

        current_state = next_state
        current_attacks = next_attacks

    return current_state, current_attacks

def print_solution(state):
    N = len(state)
    board = [['.'] * N for _ in range(N)]
    for i in range(N):
        board[i][state[i]] = 'Q'
    for row in board:
        print(' '.join(row))
    print()

def main():
    N = 4  # Tamanho do tabuleiro (NxN)
    solution, attacks = hill_climbing(N)
    print(f"Solução encontrada com {attacks} pares de rainhas atacando.")
    print_solution(solution)

if __name__ == "__main__":
    main()

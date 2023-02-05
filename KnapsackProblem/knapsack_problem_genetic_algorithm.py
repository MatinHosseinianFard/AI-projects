import random
import time

class style:
    GREEN = '\033[32m'
    RESET = '\033[0m'
    
REPRODUCTION_RATE = 0.30
# CROSSOVER_RATE = 0.8
CROSSOVER_RATE = 0.5
# MUTATION_RATE = 0.8
MUTATION_RATE = 0.1

MAX_KNAPSACK_WEIGHT = 25
POPULATION_SIZE = 100


class Item:
    def __init__(self, name, value, weight):
        self.name = name
        self.value = value
        self.weight = weight

    def __repr__(self):
        return f"{self.name}"

class Individual:
    def __init__(self, bits):
        self.bits = bits

    def fitness(self) -> float:
        total_value = sum([
            bit * item.value
            for item, bit in zip(items, self.bits)
        ])
        total_weight = sum([
            bit * item.weight
            for item, bit in zip(items, self.bits)
        ])

        if total_weight <= MAX_KNAPSACK_WEIGHT:
            return total_value

        return 0

    def total_weight(self):
        total_weight = sum([
            bit * item.weight
            for item, bit in zip(items, self.bits)
        ])

        return total_weight

    def __repr__(self):
        return f"{self.bits}"


def generate_initial_population(count=50) -> list[Individual]:
    population = set()

    # generate initial population having `count` individuals
    while len(population) != count:
        # pick random bits one for each item and
        # create an individual
        bits = [random.choice([0, 1])
                for _ in items
                ]
        population.add(Individual(bits))

    return list(population)


def selection(population: list[Individual]) -> list[Individual]:
    parents = []

    # randomly shuffle the population
    random.shuffle(population)
    # print(population[0])
    # print(population[0].bits)
    # we use the first 4 individuals
    # run a tournament between them and
    # get two fit parents for the next steps of evolution

    # tournament between first and second
    
    if population[0].fitness() > population[1].fitness():
        parents.append(population[0])
    else:
        parents.append(population[1])

    # tournament between third and fourth
    if population[2].fitness() > population[3].fitness():
        parents.append(population[2])
    else:
        parents.append(population[3])

    return parents


def crossover(parents: list[Individual]) -> list[Individual]:
    N = len(items)
    child1 = parents[0].bits[:N//2] + parents[1].bits[N//2:]
    child2 = parents[1].bits[:N//2] + parents[0].bits[N//2:]
    return [Individual(child1), Individual(child2)]


def mutate(individuals: list[Individual]) -> list[Individual]:
    for individual in individuals:
        for i in range(len(individual.bits)):
            if random.random() < MUTATION_RATE:
                # Flip the bit
                individual.bits[i] ^= 1


def next_generation(population: list[Individual]) -> list[Individual]:
    next_gen = []
    while len(next_gen) < len(population):
        children = []

        # we run selection and get parents
        parents = selection(population)
        
        # reproduction
        if random.random() < REPRODUCTION_RATE:
            children = parents
        else:
            # crossover
            if random.random() < CROSSOVER_RATE:
                children = crossover(parents)

            # mutation
            if random.random() < MUTATION_RATE:
                mutate(children)

        next_gen.extend(children)

    return next_gen[:len(population)]


def solve_knapsack() -> Individual:
    population = generate_initial_population(POPULATION_SIZE)
    population = sorted(population, key=lambda i: i.fitness(), reverse=True)
    best = population[0]
    maxx = 50
    j = 0
    while True:
        while j < maxx:
            population = next_generation(population)
            j += 1
        population = sorted(population, key=lambda i: i.fitness(), reverse=True)
        if best.fitness() == population[0].fitness():
            return population[0]
        else:
            best = population[0]
            j += 50


items = [Item(name = "A", value=5, weight=7),
         Item(name = "B", value=4, weight=2),
         Item(name = "C", value=7, weight=1),
         Item(name = "D", value=2, weight=9),
         Item(name = "E", value=3, weight=5),
         Item(name = "F", value=1, weight=2),
         Item(name = "G", value=10, weight=1),
         Item(name = "H", value=4, weight=6),
         Item(name = "I", value=6, weight=1),
         Item(name = "J", value=2, weight=4)]

for i in range(10):
    start_time = time.time()
    x = solve_knapsack()
    print(f"{ x}{style.GREEN if x.fitness() == 40 else style.RESET} fitness:{x.fitness()}  weight:{x.total_weight()}  time:{round(time.time() - start_time, 2)}s{style.RESET} ", "✅" if x.fitness() == 40 else "❌")

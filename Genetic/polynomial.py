import random
import math

NUM_GENERATIONS = 1000
POPULATION_SIZE = 100
MAX_GENERATIONS_WITHOUT_IMPROVEMENT = 50


# Genetic algorithm parameters
MUTATION_RATE = 0.01
TOURNAMENT_SIZE = 5

degree = int(input('Enter the degree of equation:'))
if degree == 1: 
  a = float(input('Enter parametrs'))
  b = float(input())
  POLYNOMIAL = lambda x: a*x + b 
elif degree == 2: 
  a = float(input('Enter parametrs'))
  b = float(input())
  e = float(input())
  POLYNOMIAL = lambda x: a*(x**2) + b*x + e
elif degree == 3: 
  a = float(input('Enter parametrs'))
  b = float(input())
  e = float(input())
  d = float(input())
  POLYNOMIAL = lambda x: a*(x**3) + b*(x**2) + e*x + d

# Representation of a chromosome 
class Chromosome:
  def __init__(self, genes):
    self.genes = genes
  
  def fitness(self):
    error = 0
    for x in self.genes:
      error += abs(POLYNOMIAL(x))**2
    return 1 / (error + 1)


  
# Initialize random starting population  
population = [Chromosome([random.uniform(-10, 10) for _ in range(degree)]) 
              for _ in range(POPULATION_SIZE)]

best_fitness = 0
no_improvement_count = 0

for g in range(NUM_GENERATIONS):
  
  # Calculate fitnesses
  for c in population:
    c.fitness()

  # Track best
  best = max(population, key=lambda c: c.fitness())
  best_fitness = best.fitness()
  
  if best_fitness > 0:
    print("Generations:", g, "Best roots found:", best.genes)

  # Tournament selection    
  new_population = []
  for _ in range(POPULATION_SIZE):
    parents = random.sample(population, TOURNAMENT_SIZE) 
    winner = max(parents, key=lambda p: p.fitness())
    new_population.append(winner)

  # Mutation  
  for c in new_population:
    for i in range(len(c.genes)):
      if random.random() < MUTATION_RATE:
        c.genes[i] = random.uniform(-10, 10)

  # Replace population
  population = new_population

  # Check for no improvement  
  if best_fitness <= 0:
    no_improvement_count += 1
  else:
    no_improvement_count = 0

  if no_improvement_count > MAX_GENERATIONS_WITHOUT_IMPROVEMENT:
    break

print("Final best roots found:", best.genes)
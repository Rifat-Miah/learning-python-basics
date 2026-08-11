'''
Problem 2: Consider the problem of maximizing the function f(x) = 27x –x2, where x can vary 
between integer values 0 and 31. Encode x as a binary string of length 5. Thus, the chromosomes 
for our genetic algorithm will be sequences of 0’s and 1’s with a length of 5 bits and have a 
range from 0 (00000) to 31 (11111). 
Start with an initial population of four (4) chromosomes at random and apply Genetic Algorithm 
Operators (Selection, Crossover, and Mutation) to illustrate how genetic algorithm ‘evolve’ 
toward fitter candidate solution.
'''
import random

population = ["00000", "01010", "10100", "01101"]

for generation in range(1, 6):

    print("\nGeneration", generation)

    for chromosome in population:
        x = int(chromosome, 2)
        f = 27 * x - x ** 2
        print(chromosome, "Fitness =", f)

    parent1 = random.choice(population)
    parent2 = random.choice(population)

    print("Parent 1:", parent1)
    print("Parent 2:", parent2)

    point = random.randint(1, 4)

    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]

    print("Crossover Point:", point)
    print("Child 1:", child1)
    print("Child 2:", child2)

    p = random.randint(0, 4)

    child1 = list(child1)
    child1[p] = "1" if child1[p] == "0" else "0"
    child1 = "".join(child1)

    print("After Mutation:", child1)

    population = [child1, child2,
                  random.choice(population),
                  random.choice(population)]
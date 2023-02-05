#include <iostream>
#include <time.h>
#include <algorithm>
#include <cmath>
#include <random>
#include <windows.h>

using namespace std;

#define REPRODUCTION_RATE 0.3
#define CROSSOVER_RATE 0.5
#define MUTATION_RATE 0.02

#define MAX_KNAPSACK_WEIGHT 25
#define NUMBER_OF_ITEM 10
#define POPULATION_SIZE 600

#define EXPECTED_FITNESS 40

template <typename T>
void printArray(const T *const array, int size)
{
    cout << "[";
    for (int i = 0; i < size; ++i)
        cout << array[i] << " ";

    cout << "\b] ";
}
class Item
{
public:
    string name;
    int weight, value;
    Item(){};
    Item(string name, int value, int weight)
    {
        this->name = name;
        this->value = value;
        this->weight = weight;
    };
};

Item items[NUMBER_OF_ITEM] = {
    Item("A", 5, 7),
    Item("B", 4, 2),
    Item("C", 7, 1),
    Item("D", 2, 9),
    Item("E", 3, 5),
    Item("F", 1, 2),
    Item("G", 10, 1),
    Item("H", 4, 6),
    Item("I", 6, 1),
    Item("J", 2, 4),
};

class Individual
{
public:
    int bits[NUMBER_OF_ITEM];
    Individual(){};
    Individual(int bits[NUMBER_OF_ITEM])
    {
        for (int i = 0; i < NUMBER_OF_ITEM; i++)
            this->bits[i] = bits[i];
    };
    int fitness()
    {
        int total_value = 0;
        int total_weight = 0;

        for (int i = 0; i < NUMBER_OF_ITEM; i++)
        {
            total_value += items[i].value * this->bits[i];
            total_weight += items[i].weight * this->bits[i];
        }

        if (total_weight <= MAX_KNAPSACK_WEIGHT)
            return total_value;

        return 0;
    };
    int total_weight()
    {
        int total_weight = 0;
        for (int i = 0; i < NUMBER_OF_ITEM; i++)
            total_weight += items[i].weight * this->bits[i];
        return total_weight;
    }
};

Individual *generate_initial_population()
{
    static Individual population[POPULATION_SIZE];
    // generate initial population
    for (int i = 0; i < POPULATION_SIZE; i++)
    {
        int bits[NUMBER_OF_ITEM];

        // pick random bits one for each item and
        // create an individual
        for (int j = 0; j < NUMBER_OF_ITEM; j++)
            bits[j] = rand() % 2;

        population[i] = Individual(bits);
    }

    return population;
}

Individual *slection(Individual population[POPULATION_SIZE])
{
    static Individual parents[2];

    // randomly shuffle the population
    shuffle(population, population + POPULATION_SIZE, mt19937{random_device{}()});

    // we use the first 4 individuals
    // run a tournament between them and
    // get two fit parents for the next steps of evolution
    if (population[0].fitness() > population[1].fitness())
        parents[0] = population[0];
    else
        parents[0] = population[1];

    if (population[2].fitness() > population[3].fitness())
        parents[1] = population[2];
    else
        parents[1] = population[3];

    return parents;
}

Individual *crossover(Individual parents[2])
{
    int child1[NUMBER_OF_ITEM], child2[NUMBER_OF_ITEM];

    for (int i = 0; i < (int)floor(NUMBER_OF_ITEM / 2); i++)
    {
        child1[i] = parents[0].bits[i];
        child1[i + (int)floor(NUMBER_OF_ITEM / 2)] = parents[1].bits[i + (int)floor(NUMBER_OF_ITEM / 2)];
        child2[i] = parents[0].bits[i + (int)floor(NUMBER_OF_ITEM / 2)];
        child2[i + (int)floor(NUMBER_OF_ITEM / 2)] = parents[1].bits[i];
    }
 
    static Individual childs[2];
    childs[0] = Individual(child1);
    childs[1] = Individual(child2);
    return childs;
}

void mutate(Individual (&individuals)[2], int size)
{
    for (int i = 0; i < size; i++)
        for (int j = 0; j < NUMBER_OF_ITEM; j++)
            if ((float)rand() / RAND_MAX < MUTATION_RATE)
            {
                // Flip the bit
                individuals[i].bits[j] ^= 1;
            }
}

Individual *next_generation(Individual population[POPULATION_SIZE])
{
    static Individual next_gen[POPULATION_SIZE];
    int i = 0;
    bool flag;
    //
    while (i < POPULATION_SIZE)
    {
        Individual children[2];
        flag = false;
        
        // we run selection and get parents
        Individual *parentsPointer = slection(population);
        Individual parents[2] = {*parentsPointer, *(parentsPointer + 1)};
        
        // reproduction
        if ((float)rand() / RAND_MAX < REPRODUCTION_RATE)
        {
            children[0] = parents[0];
            i++;
            if (i != POPULATION_SIZE)
            {
                children[1] = parents[1];
                i++;
            }

            flag = true;
        }

        else
        {
            // crossover
            if ((float)rand() / RAND_MAX < CROSSOVER_RATE)
            {
                Individual *crossoverPointer = crossover(parents);
                children[0] = *crossoverPointer;
                i++;
                if (i != POPULATION_SIZE)
                {
                    children[1] = *(crossoverPointer + 1);
                    i++;
                }
                flag = true;
            }
            // mutation
            if (flag && ((float)rand() / RAND_MAX < MUTATION_RATE))
                mutate(children, 2);
        }
        if (flag)
        {
            next_gen[i - 2] = children[0];
            next_gen[i - 1] = children[1];
        }
    }
    return next_gen;
}

bool compareIndividual(Individual i1, Individual i2)
{
    return (i1.fitness() > i2.fitness());
}

Individual solve_knapsack()
{
    Individual *p = generate_initial_population();
    static Individual population[POPULATION_SIZE];
    int max = 50;
    int j = 0;
    for (int i = 0; i < POPULATION_SIZE; i++)
        population[i] = *(p + i);
    sort(population, population + POPULATION_SIZE, compareIndividual);
    Individual best = population[0];
    while (true)
    {
        while (j < max)
        {
            Individual *p = next_generation(population);
            for (int j = 0; j < POPULATION_SIZE; j++)
                population[j] = *(p + j);
            j++;
        }
        sort(population, population + POPULATION_SIZE, compareIndividual);
        if (best.fitness() == population[0].fitness())
        {
            return population[0];
        }
        else
        {
            best = population[0];
            j += 50;
        }
    }

    sort(population, population + POPULATION_SIZE, compareIndividual);
    return population[0];
}

int main()
{
    SetConsoleOutputCP(CP_UTF8);
    srand((unsigned)time(NULL));
    Individual inv;
    clock_t tStart;
    for (int i = 0; i < 10; i++)
    {
        tStart = clock();
        inv = solve_knapsack();
        printArray(inv.bits, NUMBER_OF_ITEM);

        if (inv.fitness() == EXPECTED_FITNESS)
            printf("\033[32m| fitenss: %d | weight: %d | Time taken: %.3fs ✅ \033[0m \n", inv.fitness(), inv.total_weight(), (double)(clock() - tStart) / CLOCKS_PER_SEC);
        else
            printf("| fitenss: %d | weight: %d | Time taken: %.3fs ❌\n", inv.fitness(), inv.total_weight(), (double)(clock() - tStart) / CLOCKS_PER_SEC);
    }

    return 0;
}
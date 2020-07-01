import random
import numpy
import math
import copy
import matplotlib.pyplot as plt

gene_length = 4 # 遺伝子長
individual_length = 100 # 個体数
generation = 10 # 世代数
mutate_rate = 0.2 # 突然変異の確率
elite_rate = 0.02 # エリート選択の割合
Gene = [0]
fitn = []
X = []



def get_population():
    population = []
    for i in range(individual_length):
        #population.append([random.randint(0,1) for j in range(gene_length)])
        population.append([0 for j in range(gene_length)])
    return population

def ptype(pop):
    #y = str(pop)
    #z = int(y,2)
    Y=[]
    for i in range(0,len(pop)):
        y=pop[i]*2**i
        Y.append(y)
    z=sum(Y)
    #g= z/10000000


    return z


def func(x):
    y =  (x-2.01)*(x-5)*(x-3.2)*(x-8)
    return y

def func2(x):
    y= (x**2-2)
    return y


def evaluate(pop):
    pop.sort(reverse=True)
    return pop

def fitness(x):
    y = 1/(1+abs(func(ptype(x))))
    return y

def two_point_crossover(parent1, parent2):
    r1 = random.randint(0, gene_length-1)
    r2 = random.randint(r1, gene_length-1)
    child = copy.deepcopy(parent1)
    child[r1:r2] = parent2[r1:r2]
    return child


def mutate(parent):
    r = random.randint(0, gene_length-1)
    child = copy.deepcopy(parent)
    child[r] = 1 if child[r]==0 else 0
    return child

def main():
    pop = evaluate([(fitness(p), p) for p in get_population()])
    #print(pop)
    p = pop[:1]
    fu = ptype(p[0][1])
    X.append(fu)
    fitn.append(p[0][0])
    print('Generation: 0')
    print('Min : {}'.format(pop[-1][0]))
    print('Max : {}'.format(pop[0][0]))
    print('--------------------------')
    #ここからトーナメント方式test
    #print(evaluate(random.sample(pop,3)))
    #print(evaluate(random.sample(pop, 3)))

    for g in range(generation):
        print('Generation: ' + str(g + 1))

        # エリートを選択
        eva = evaluate(pop)
        elites = eva[:int(len(pop) * elite_rate)]
        #トーナメント
        tour1 = evaluate(evaluate(random.sample(pop,3)))
        tour2 = evaluate(evaluate(random.sample(pop,3)))
        print(tour1)
        print(tour2)
        tour1 = tour1[:1]
        tour2 = tour2[:1]
        #print(tour1)
        #print(tour2)
        tour3= tour1+ tour2
        #print(tour3)


        # 突然変異、交叉
        pop = elites
        while len(pop) < individual_length:
            if random.random() < mutate_rate:
                m = random.randint(0, len(tour3) - 1)
                child = mutate(tour3[m][1])
                #print("突然変異した！",fitness(child))
            else:
                #m1 = random.randint(0, len(elites) - 1)
                #m2 = random.randint(0, len(elites) - 1)
                # print(m1,m2)
                # print(elites[m1][1])
                # print(elites[m2][1])
                child = two_point_crossover(tour1[0][1], tour2[0][1])
                #print("交叉した！",fitness(child))
            pop.append((fitness(child), child))
            print(len(pop))

        # 評価
        eva = evaluate(pop)
        pop = eva
        p = pop[:1]
        fu = ptype(p[0][1])
        X.append(fu)
        fitn.append(p[0][0])
        Gene.append(g+1)
        #print(fitn)
        #print(Gene)
        print(X)

        #print(pop[:1])
        print('Min : {}'.format(pop[-1][0]))
        print('Max : {}'.format(pop[0][0]))
        print('--------------------------')
    print('Result : {}'.format(pop[0]))
    #グラフ作成
    fig = plt.figure()
    ax1 = fig.add_subplot(1, 1, 1)
    ax2 = ax1.twinx()

    ax1.plot(Gene, fitn,label="fitness")
    ax2.plot(Gene, X,color='r', label="X")

    ax1.set_title("GA100")
    ax1.set_ylabel("fitness")
    ax2.set_ylabel("X")

    ax1.legend()
    ax2.legend(loc='upper center')

    plt.grid(True)
    fig.savefig("GA100_test.png")
    plt.show()





if __name__ == '__main__':
    main()
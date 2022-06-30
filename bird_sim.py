class NCurve():

    def __init__(self, number = None, mean = None, standard_deviation = None, zScore = None):
        self.num = number
        self.zScore = zScore
        self.mean = mean
        self.stddev = standard_deviation

    def Zscore(self):
        return (self.num - self.mean) / self.stddev 

class population():

    def __init__(self, initial_pop, mean, stddev):
        self.initial = initial_pop
        self.population = NCurve(initial_pop, mean, stddev)
        self.dependencies = []

    def dependencies_calc(self):
        #print(self.dependencies)
        final = 0
        dp_type_score = []
        importance = []
        for dependencyType in self.dependencies:
            score = 0
            for dependency in dependencyType[0]:
                score += dependency[0].population.Zscore() * dependency[1]
                #print(dependency[0].population.Zscore() , dependency[1])
            importance.append(dependencyType[1])
            #print(score, dependencyType[1])
            dp_type_score.append(score)
        for i in range(len(dp_type_score)):
            final += dp_type_score[i] * importance[i]
        #print(dp_type_score)
        #print(importance)
        return final

birds = population(500, 400, 50)
birds.dependencies = [[[[population(10,20,2), 5], [population(120,100,30),2]],5],[[[population(15,20,5),2], [population(500,300,150),3]],5]]
#            specific population ^ importance ^        importance of resource ^   all populations that contribute to resource end here ^
print(birds.dependencies_calc())
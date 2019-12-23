class KiwiJuiceEasy:
    def thePouring(self, capacities, bottles, from_id, to_id):
        for i, v in range(len(from_id)):
            index_from = from_id[i]
            index_to = to_id[i]
            full_bottles = capacities[index_to]

            if (bottles[index_from] == 0):
                continue
            elif (bottles[index_to] + bottles[index_from] > full_bottles):
                bottles[index_from] -= full_bottles - bottles[index_to]
                bottles[index_to] = full_bottles        
            else:
                bottles[index_to] += bottles[index_from]
                bottles[index_from] = 0
            print(bottles)
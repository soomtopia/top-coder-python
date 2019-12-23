class InterestingParty:
    def bestInvitation(self, first, second):
        topic_count = dict()
        for i,v in enumerate(first):
            if (v not in topic_count):
                topic_count[v] = 1
            else:
                topic_count[v] += 1
            
            if (second[i] not in topic_count):
                topic_count[second[i]] = 1
            else:
                topic_count[second[i]] += 1


        print(max(topic_count.values()))
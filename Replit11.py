l=[12,34,76,65,69,23,10,1]
max_score=max(l)
print(max_score)



l=[12,34,76,65,69,23,10,1]
max_score=0
for score in l:
    if score>max_score:
        max_score=score
print(max_score)        

#python file of soem of the neo4j code written in the repl

import pickle
from py2neo import Graph
graph = Graph("bolt://localhost:8687",auth=('neo4j','yusurfRules321'))
tx = graph.begin()
from py2neo import Node
from py2neo import Relationship as Rel
a = Node("Person",name='alice')
tx.create(a)
b = Node('Person',name='Bob')
tx.create(b)
ab = Rel(a,'KNOWS',a)
tx.create(ab)
tx.commit()
graph.exists(ab)
ab = Rel(a,'KNOWS',b)
tx.commit()
tx.create(ab)
tx = graph.begin()
tx.create(ab)
tx.commit()
with open('recipe.pkl','rb') as f:
	recipes = pickle.load(f)
add ='''
with split(tolower("{title}"),' ') as text
unwind range(0,size(text)-2) AS i
merge (w1:Word {name: text[i]})
merge (w2:Word {name: text[i+1]})
merge (w1)-[:NEXT]->(w2)
'''
add
graph.run(add,title=recipes[0]['title']).evaluate()
graph.run(add,title=recipes[0]['title'])
c = graph.run(add,title=recipes[0]['title'])
c.current['name']
c
tx = graph.begin()
c = tx.evaluate(add,title=recipes[0]['title'])
c
tx.commit()
cypher = graph.cypher
add1 = add.format(title=recipes[0]['title'])
add1='''
with split(tolower("yummy chocolate smartie cake"),' ') as text
unwind range(0,size(text)-2) AS i
merge (w1:Word {name: text[i]})
merge (w2:Word {name: text[i+1]})
merge (w1)-[:NEXT]->(w2)
'''
grpah.run(add1)
graph.run(add1)
graph.run(add1).execute()
graph.run(add1).evaluate()
add2 = '''
with split(tolower("%s"),' ') as text
unwind range(0,size(text)-2) AS i
merge (w1:Word {name: text[i]})
merge (w2:Word {name: text[i+1]})
merge (w1)-[:NEXT]->(w2)
'''
for recipe in recipes:
	graph.run(add2%recipe['title']).evaluate()
print('\n'.join([a['title'] for a in recipes[0:100]]))

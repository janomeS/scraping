from neo4jrestclient.client import GraphDatabase
import csv
import sys

#connect neo4j server
url = "http://neo4j:mats@6688@153.126.137.206:7474/db/data"
gdb = GraphDatabase(url)

#Delete graph
gdb.query('MATCH (n) OPTIONAL MATCH(n)-[r]-() DELETE n,r', data_contents=True)


product_list = []
reviewer_list = []
product_dict = {}
reviewer_dict = {}

#open csv file
f = open('reviewData.csv', 'r')
reader = csv.reader(f)

#read reviewerData.csv and arrange data format for insert Neo4j
for row in reader:
  reviewer_str = row

  reviewer_name = reviewer_str[0]
  reviewer_score = reviewer_str[1]
  productname = reviewer_str[2]

#product_list_uniq is the productname List
  product_list.append(productname)
  product_list_uniq =list(set(product_list))
  
#reviewerlist is the reviewer name list
  reviewer_list.append(reviewer_name)
  reviewer_list_uniq = list(set(reviewer_list))

f.close


#create reviewernode
for line in reviewer_list_uniq:
  reviewer_dict[line] = gdb.nodes.create(name=line)
  reviewer_dict[line].labels.add("reviewer")

#create productnode
for line in product_list_uniq:
  product_dict[line] = gdb.nodes.create(name=line)
  product_dict[line].labels.add("product")

#create relationship
for line in open('reviewData.csv','r'):
  fr,rel,to = line.strip().split(',')
  reviewer_dict[fr].relationships.create(rel,product_dict[to])




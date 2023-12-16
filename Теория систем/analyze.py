import psycopg2
from matplotlib.pyplot import axis

import numpy as np

# connecting to database
conn = psycopg2.connect(

    host="89.108.115.118",
    database="balance906",
    user="balance906",
    password="Sa_906_etb;")











cur = conn.cursor()



# get sum of all product's prices for every consumer
def get_sum_products_prices_by_consumer():
    cur.execute('select p.company_id,sum(count_product * price) from consumer_requirement_base cr ' +
                'join product p on p.id= cr.product_id ' +
                'group by p.company_id order by p.company_id')

    sum_products = np.array(cur.fetchall())
    cur.execute('select id from company')
    companies = np.array(cur.fetchall()).flatten()

    print(sum_products)


# get every companies sell
def get_sells():
    cur.execute('select id from company')
    sell = cur.fetchall()
    for i in sell:
        text = 'select cr.company_id,sum(count_product * price) from company_requirement cr join product p on p.id= cr.product_id where p.company_id={} group by cr.company_id order by cr.company_id'.format(
            i[0])
        cur.execute(text)
        all_companies_sell = cur.fetchall()
        print(all_companies_sell)


# get balance table
cur.execute('select id from company')
sell = [i[0] for i in cur.fetchall()]
cur.execute('select * from make_balance_table(ARRAY{})'.format(sell))
f = cur.fetchall()
data = np.array([f[i][0].split(';') for i in range(1, len(sell) + 1)])
comp_num = len(sell)

# X_i
X_i = np.array([])
for i in range(len(data)):
    X_i = np.append(X_i, sum(data[i, 1:].astype(np.int64)))

# matrix A
A = np.zeros((comp_num, comp_num))
for i in range(comp_num):
    for j in range(comp_num):
        if X_i[i] == 0:
            A[i][j] = 0
        else:
            A[i][j] = data[i][j].astype(np.int64) / X_i[i]


# create E matrix
def e_matrix():
    E = np.identity(comp_num)
    return E


Y = np.array([[1], [3], [7], [5], [7], [8], [9], [8], [7], [6], [3], [4], [7]])
result = np.power(np.linalg.inv(np.subtract(e_matrix(), A)), Y)
# print(result)

get_sum_products_prices_by_consumer()

# close the communication with the database
cur.close()
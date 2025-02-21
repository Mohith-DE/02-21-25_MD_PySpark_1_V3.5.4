# -*- coding: utf-8 -*-
"""Pyspark_1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1vwWnbu_U9lnK_mc2ppNec60l2ssrVqAD
"""

import findspark
findspark.init()
import pyspark
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Pyspark_1").getOrCreate()
print(spark.version)

!pip install pyspark
!pip install findspark

data = [(1, 'Jay'), (2, 'Avi'), (3, 'Saint'), (4,'Jerome')]
columns = ['ID', 'Name']
df=spark.createDataFrame(data,columns)
df.show()

df.show(3)

df_1=spark.read.csv('small_zipcode.csv', header=True, escape="\"")
df_1.show()
df_1.count()

x=spark.read.csv('sample.csv', header=True, escape="\"")
x.show()

x.select('age').distinct().show()

y=spark.read.csv('people-100.csv', header=True, escape="\"")
y.show()

from pyspark.sql.functions import *
from pyspark.sql.types import *
y.groupBy('Sex').agg(countDistinct('User Id')).show()
y.printSchema()
y.describe()

y1=y.withColumn('Full Name', concat_ws(" ","First Name","Last Name"))
y1.show()

y2=y1.drop('First Name', 'Last Name')
y2.show()

y2.show()
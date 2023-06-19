from scipy import stats
import scikit_posthocs as sp

#we have non parametric data. this is why we didn't use one way anova
#compares the  mean ranks
#The null hypothesis (H0): The median is equal across all groups.
#The alternative hypothesis: (Ha): The median is not equal across all groups.

#=====KB CURATION===========

group1 = [8.215,11.28,3.84,1.195,1.315,0.655,0,0,0,0,0.105,3.965,0.765,0.55,0.215,0,0,0,0,0]
group2 = [15.455,31.09,11.93,0,0.415,0,0,0.31,2.495,0.125,0.195,8.955,0,0,0,0,0,0.195,0.055,0]
group3 = [10.735,27.12,5.275,1.76,0.29,0.43,0,0,0.875,0,0,0.595,0.585,0.29,0,0,0,0.29,0,0]


#perform Kruskal-Wallis Test 
stats.kruskal(group1, group2, group3)
#(statistic=0.030303586168927532, pvalue=0.9849624177716853)

#============TAXONOMIC ACTIONS
group1 = [3.26,6.01,1.635,2.185]
group2 = [0.115,0.655,0,0.3]
group3 = [1.91,3.565,1.015,0]


#perform Kruskal-Wallis Test 
stats.kruskal(group1, group2, group3)
#(statistic=5.799122807017544, pvalue=0.0550473583407565)

data = [group1, group2, group3]
sp.posthoc_dunn(data, p_adjust = 'bonferroni')
#          1         2         3
#1  1.000000  0.048301  0.775878
#2  0.048301  1.000000  0.604818
#3  0.775878  0.604818  1.000000


#============Domain-based contents
group1 = [3.04,14.97,0.43,0.64]
group2 = [1.17,7.495,0.055,0]
group3 = [0.29,5.95,0,0]


#perform Kruskal-Wallis Test 
stats.kruskal(group1, group2, group3)
#(statistic=2.2234042553191498, pvalue=0.32899848678679555)



#============wikidata rules
group1 = [0.325,3.27,0.105,0]
group2 = [0.54,2.56,0.285,0]
group3 = [2.155,7.2,1.31,0]


#perform Kruskal-Wallis Test 
stats.kruskal(group1, group2, group3)
#(statistic=0.7411347517730524, pvalue=0.6903425357921394)


#============COnnection with wikimedia projects
group1 = [1.945,4.595,5.78,4.365]
group2 = [0.335,0.76,0,0.07]
group3 = [2.065,2.955,0.29,0.29]


#perform Kruskal-Wallis Test 
stats.kruskal(group1, group2, group3)
#(statistic=6.638596491228076, pvalue=0.036178211066275084)
data = [group1, group2, group3]
sp.posthoc_dunn(data, p_adjust = 'bonferroni')
#          1         2         3
#1  1.000000  0.031950  0.348075
#2  0.031950  1.000000  0.977857
#3  0.348075  0.977857  1.000000
#============controversies
group1 = [6.92,0.33]
group2 = [5.955,0.125]
group3 = [8.785,0,0.875]


#perform Kruskal-Wallis Test 
stats.kruskal(group1, group2, group3)
#(statistic=0.7142857142857117, pvalue=0.6996725373751312)

















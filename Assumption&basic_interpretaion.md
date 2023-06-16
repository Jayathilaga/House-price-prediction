**Assumption:**
1. As the column names are not very explanatory, I was not able to remove some columns which was unwanted.
2. We could group the community_id and id_municipality_id and make them into few buckets, this will help our model to have better prediction. ( as of now I am not sure which are closely connected hence left as it is)
3. As there were many features created I had used Ridge reg as we could drop some features.

**Interpretation:** 
1. Increasing lp_dol by 1 scaled unit increases the predicted price by $\sim\$468780$.
2. If you change the category from property_type_A. to property_type_C. the prediction price goes down by $\sim\$31467$
2. If you change the category from property_type_A. to property_type_D. the prediction price goes down by $\sim\$23935$

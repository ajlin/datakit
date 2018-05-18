# datakit
helpers for working w/ pandas, scikit-learn in the General Assembly Data Science course

##example:
`from datakit import build`

```
#accepts custom dataframes
sqft = pd.DataFrame(df['1st Flr SF']+df['2nd Flr SF'],columns=["sqft"])
remodel = pd.DataFrame(df['Year Remod/Add'].map(lambda x: x>1975))*1

recipe = [
    ( columns , ['Id','Overall Cond'] ),
    ( dummies , 'Sale Type' ),
    ( manual , remodel ),
    ( manual , sqft ),
    ( mapfunc , ('Year Remod/Add',lambda x: 'PIZZA') )
]

crazy = build(recipe)
crazy_Xtrain = crazy.transform(train_df)

```

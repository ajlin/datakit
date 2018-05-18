# datakit
some helpers for working w/ scikit-learn for the General Assembly Data Science Intensive course

### About:  
accidentally wrote my own version of `preprocessing.Pipeline`!  but for building engineered X tables.  still learning how to python and everything so if you find it useful, would love some help expanding it's capabilities. <3

### To do:
- **almost** generalized the function that can turn tuples into `func(arg)`.  which would basically generalize this to sequencing any workflow you want...
- also need to figure out how to pass explicit arguments instead of every argument being unlabeled and mandatory...  for some reason they keep ending up as `str`


### Recipe Parsing

```python
from datakit import build
```

- `build()` is an `obj` that will house our "recipe"

- recipe is a `list` of commands `recipe = [commands]`  
- where each command is a `tuple` of  `(function,args)`
- args can be a `tuple` as well, for multiple arguments.

**ie:**
```python
recipe = [  
    ( function1 , [arg] ),  
    ( function2 , ( [arg],[arg],opt,opt) ),  
    ( function1 , [arg] ),
    ( function3 , arg )
    ]
```

### Examples:


##### run one command `columns()` to pull columns from DataFrame `df`:
```python
recipe = [( columns , ['Id','Overall Cond'] )]


basic = build(recipe)
basic_X = basic.transform(df)
```

##### string two commands together and output DataFrame:

```python
recipe = [( columns , ['Id','Overall Cond'] ),
          ( columns , ['1st Flr SF'])]
basic2 = build(recipe)
basic2_X = basic2.transform(df)
```

##### it also accepts custom dataframes, and custom transform functions:
build custom columns (you can do this with datakit's helper functions too)
```python
sqft = pd.DataFrame(df['1st Flr SF']+df['2nd Flr SF'],columns=["sqft"])
remodel = pd.DataFrame(df['Year Remod/Add'].map(lambda x: x>1975))*1
```

feed them into the recipe...
```python
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

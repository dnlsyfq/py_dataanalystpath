
### 

```
df.head()
df.describe(include='all') // numerical summarization
```

### Example Chaining Pandas
```
  df.groupby('website_goal')\
  	.first_name.count()\
  	.reset_index()\
  	.rename(columns={'first_name': 'number_of_citizens'})
```

```
df = pd.read_csv('page_visits.csv')

# Calculate survey results
survey_results = df.groupby('website_goal')\
  	.first_name.count()
  
# Make a pie chart
plt.pie(survey_results.values,
        labels=survey_results.index,
        autopct='%d%%'
       )
plt.title('Why do citizens visit our website?')
plt.axis('equal')
```
# Text
```commandline
//div[contains(@class, 'result__snippet')][contains(., 'bamboo')]
```
# And / Or
```commandline
//img[@width<20][@height<20]
//img[@width<20 and @height<20]
//input[@name='q' or @id='search_form_input']
```
# Contains
Careful, checks for substrings, not equality.
```commandline
//div[contains(@class, 'result__snippet')]
```
# Not
```commandline
//a[not(contains(@class, 'header'))]
```
# Starts with
Would also match 'result__snippet'
```commandline
//div[starts-with(@class, 'result')]
```
# Within
All 'a' elements that have an 'img' element  
. : to start from the current nose  
// : any descendents
```commandline
//a[.//img]
```

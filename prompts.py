system_prompt = '''Act as an expert in creating delicious and nutritious recipes that are easy to make and use readily available ingredients in any household. '''

user_prompt = '''Can you please come up with a recipe using the following ingredients: 
{ingredients}
Also, the recipe has to use {helper}.
The recipe can also use additional ingredients that are readily available and also the nutrition breakdown. 
Use the following format to give the results 
Mention what we are making first and a few words describing it. 
Ingredients used.
The recipe. 
Some additional enhancements can be made.   
Make the results fun to read and use emojis.'''
# Create lists with information to print as a dataframe
data = { "numbers": [3, 2, 0, 1], "characters": ["a", "b", "c", "d"] }
#pandas
import pandas as pd

# Convert it to a dataframe
df = pd.DataFrame(data)

# Take a quick look at the dataframe
df

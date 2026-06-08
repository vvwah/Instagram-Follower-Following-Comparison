#CONDENSED
#STEP ONE: Once you have ensured that there is a space between all names in your follower or following list 
# (by first pasting the lists into Excel or Google Sheets, and inserting spaces in one column, then joining the 
# space column and the name column together - in Google sheets you can do so by =JOIN((" ", B1:C1)) -), run this code
# and copy and paste the new list which has the spaces seperating the names, whereby this function will then create a list which 
# can then be copy and pasted into the next step
ENTER = input("Enter your list of names >> ")
a=ENTER.split()
print(a)

#STEP TWO: the code will run with placeholders which will be filled in by your results from STEP ONE, 
# disregard placeholder values until STEP ONE is completed

#followers: this is where you insert your follower list from STEP ONE
followers = ['placeholder']

#following: this is where you insert your following list from STEP ONE
following = ['placeholder', 'test']

#this output prints a list of the OVERLAPPING names between your follower and following list
output = set(followers).intersection(following)

filtered_list = [item for item in following if item not in output]

print(filtered_list)

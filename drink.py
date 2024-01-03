# Script calculating how much did I drink during the day.

pool = 0
goal = 2500

# Read previously saved value form a file.
# Handled as an exception in case the file does not exist or is empty.
# https://www.quora.com/What-happens-if-you-try-to-open-a-file-for-reading-that-doesnt-exist-in-Python
try:
    pool = int(open("vypito.txt", "r").read())
#    print(pool)
except:
    print("So far dry as tinder.")

# Adding to the pool
drank = int(input("How much liquids did you drink now? "))

# Sum of already drank liquids and currently added
poolupdate = pool+drank
print("Today drank totally", poolupdate, "ml.")

remaining = goal - poolupdate
print("Still remaining", remaining, "ml to reach the daily goal.")

# Converting an integer to string so the write function can save it to the file
# https://realpython.com/convert-python-string-to-int/
poolupdateconverted = str(poolupdate)

# Verifying the data type in variable
# print ("type of number", type(drank))

# Writing to a file:
# https://www.prepbytes.com/blog/python/write-function-in-python/
file = open("vypito.txt", "w")
file.write(poolupdateconverted)
file.close()

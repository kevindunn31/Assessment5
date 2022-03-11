log_file = open("um-server-01.txt")

# This is pulling from a file that is already logged and tracked. Itss saying open the text from
# server 01


def sales_reports(log_file):
    for line in log_file:
        line = line.rstrip()
        day = line[0:3]
        if day == "Mon":
            print(line)

# This is a for loop that was originally for Tuesday to go through all the sales. 
#  The Rline strip is asking for the return a copy for the day with trailing characteristics to be removed 
# from the argument. Then the end is basiccally printing out the requested sales line         


sales_reports(log_file)
# Saving or logging/tracking the sales reports

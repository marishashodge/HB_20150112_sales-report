
def sales_report(sales_report):

    """
    sales_report.py - Generates sales report showing the total number
                  of melons each sales person sold.
    """

    salespeople = []    # initialize salesperson as empty list
    melons_sold = []    # initialize melons_sold as empty list

    f = open(sales_report)    # open file
    for line in f:                  # for every line
        line = line.rstrip()        # remove whitespace from right side 
        entries = line.split("|")   # split line into list 
        salesperson = entries[0]    # salesperson is word at index 0
        melons = int(entries[2])    # melons is integer at index 2

    if salesperson in salespeople:  # if salesperson already in list of salespeople:
        position = salespeople.index(salesperson)   
        # get index of salesperson in list of salespeople
        melons_sold[position] += melons  
        # add melons sold at same index to list of melons_sold   
    else:    # otherwise (if salesperson not in the list of salespeople)
        salespeople.append(salesperson)  # append salesperson to list of salespeople
        melons_sold.append(melons)  # append melons sold to list of melons


    for i in range(len(salespeople)):   # for each index in the length of salespeople list
        print "{} sold {} melons".format(salespeople[i], melons_sold[i]) 
    # print "[Salesperson] sold [#] melons" for each index



# alternate dictionary answer

def sales_report_dict(file_name):

    salespeople_dict = {} 

    f = open(file_name)    
    

    for line in f:                  
        line = line.rstrip()        
        entries = line.split("|")   
        salesperson = entries[0]    
        melons = int(entries[2])    

        if salesperson in salespeople_dict:
            salespeople_dict[salesperson] += melons

        else:
            salespeople_dict[salesperson] = melons

    for salesperson, melon_count in salespeople_dict.iteritems():
        print "{} sold {:,} melons".format(salesperson, melon_count)


sales_report_dict("sales-report.txt")


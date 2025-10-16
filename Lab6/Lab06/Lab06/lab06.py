import csv
from operator import itemgetter

INDUSTRIES = ['Agriculture', 'Business services', 'Construction', 'Leisure/hospitality', 'Manufacturing']

import csv
def read_file(fp):
    """Docstring"""
    reader=csv.reader(fp)
    L=[]
    lines=list(reader)

    L=lines
    return L


def get_totals(L):
    """Docstring"""
    total_pop=0
    data = iter(L)
    us_pop = next(data)
    us_pop = next(data)
    us_pop = next(data)
    us_pop = next(data)
    us_pop = next(data)[1]
    us_pop=us_pop.replace(',','')
    us_pop=int(us_pop)
    for line in L[6:]:
        num = line[1]
        if line[1][0] == "<":
            num = num.replace("<","")

        num = num.replace(",","")
        total_pop+=int(num)
    return us_pop, total_pop






def get_industry_counts(L):
    """Docstring"""
    counters=[]
    construction=0
    manufacturing=0
    business=0
    leisure=0
    agriculture=0
    for line in L:
        if line[9]=="Construction":
            construction+=1
        if line[9]=="Manufacturing":
            manufacturing+=1
        if line[9]=="Leisure/hospitality":
            leisure+=1
        if line[9]=="Business services":
            business+=1
        if line[9]=="Agriculture":
            agriculture+=1
        else:
            continue
    counters.append(("Construction",construction))
    counters.append(("Manufacturing",manufacturing))
    counters.append(("Leisure/hospitality",leisure))
    counters.append(("Business services",business))
    counters.append(("Agriculture",agriculture))
    #[{name,value} etc etc etc]
    counters.sort(key=itemgetter(1), reverse=True)
    return counters
def get_largest_states(L):
    """Docstring"""
    states=[]
    average=L[4][2]
    average=average.replace("%","")
    average=float(average)
    for line in L[6:]:
        if float(line[2][:-1]) > average:
            states.append(line[0])
        else:
            continue

    return states  # temporary return value so main runs


def main():
    fp = open("immigration.csv")
    L = read_file(fp)

    us_pop, total_pop = get_totals(L)
    if us_pop and total_pop:  # if their values are not None
        print("\nData on Illegal Immigration\n")
        print("Summative:", us_pop)
        print("Total    :", total_pop)

    states = get_largest_states(L)
    if states:  # if their value is not None
        print("\nStates with large immigrant populations")
        for state in states:
            state = state.replace('\n', ' ')
            print(state)

    counters = get_industry_counts(L)
    if counters:  # if their value is not None
        print("\nIndustries with largest immigrant populations by state")
        print("{:24s} {:10s}".format("industry", "count"))
        for tup in counters:
            print("{:24s} {:2d}".format(tup[0], tup[1]))


if __name__ == "__main__":
    main()
#user_input = input("Enter a File Name")
    #try:
        #fp=open(user_input,"r")
        #fp.close()
        #return user_input
    #except FileNotFoundError:
        #print("File Not Found")
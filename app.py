import os

def ClearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

def GPANormalizer(scores_list):
    normalized_list = []
    for score in scores_list:
        if score >= 16:
            score = 4
        elif score >= 14:
            score = 3
        elif score >= 12:
            score = 2
        elif score >= 10:
            score = 1
        else:
            score = 0
        normalized_list.append(score)
    return normalized_list

def AverageCalculator(scores_list, units_list):
    scores_sum = 0.0
    units_sum = 0
    for i in range(len(scores_list)):
        scores_sum += scores_list[i] * units_list[i]
        units_sum += units_list[i]
    average = scores_sum / units_sum
    return average
        
def main():
    scores_list = ["N/A"]
    units_list = ["N/A"]
    while(True):
        ClearConsole()
        print("Last Score:\t" + str(scores_list[-1]))
        print("Last Unit:\t" + str(units_list[-1]))
        print("-------------------------")
        print("control chars:\n-1:\tEnd\n-2:\tIgnore\n-3:\tPOP\n")
        score = input("Enter Score: ")
        if score == "":
            continue
        else:
            score = float(score)
        if (int(score) == -1):
            break
        elif (int(score) == -2):
            continue
        elif (int(score) == -3):
            if(len(scores_list) > 1):
                scores_list = scores_list[ : -1]
                units_list = units_list[ : -1]
            continue
        unit = input("Enter Unit: ")
        if unit == "":
            continue
        else:
            unit = int(unit)
        if (unit == -1):
            break
        elif (unit == -2):
            continue
        elif (unit == -3):
            if(len(scores_list) > 1):
                scores_list = scores_list[ : -1]
                units_list = units_list[ : -1]
            continue
        if (score >= 10):
            scores_list.append(score)
            units_list.append(unit)
    ClearConsole()
    scores_list = scores_list[1 : ]
    units_list = units_list[1 : ]
    scores_list = GPANormalizer(scores_list)
    average = AverageCalculator(scores_list, units_list)
    print(average)

if __name__ == "__main__": main()

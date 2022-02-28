import sys 
import csv
import json
import numpy as np
import pandas as pd
from io import StringIO


NULL = np.zeros(1)
portfolio_data = NULL


def upload():
    print()#csv
    portfolio_data = np.genfromtxt()


def import_data(file):
    #to optimize compatability assume file located in current directory and use upload function at begin of new data  
    #if variable file directories are required use this function and add "filelocation" in first argument of genfromtxt in front of file
    #prompt user for file location
    #file_location = input("Enter file location:")

    #Remove String Columns
    file = file.drop(['Symbol'], axis = 1)

    #Remove unnecessary signs
    file = file.replace(to_replace = ['\$','%',','], value = ['','',''], regex = True) 

    #Convert BUY and SHORT to INT/FLOAT Values
    file = file.replace(to_replace = ['BUY', 'SHORT'], value = ['0','1'])
    file = file.astype(float)
    
    #Convert data to numpy matrix
    matrix = file.to_numpy(dtype = float)
    
    #Determine number of rows and columns 
    rows, columns = matrix.shape

    #Add columns for calculations to end of matrix
    add_columns = 3
    zero_array = np.zeros(rows)
    for i in range(add_columns):
        matrix = np.insert(matrix, columns+i, zero_array, axis = 1)

    return matrix


def get_name(file):
    #returns the name of the stock (first entry in each row of csv file)

    #Output first column entries as list
    names = df['Symbol'].tolist() 


    return names


def save_data(matrix):
    #saves data from import_data
    np.save("data/holding_data.npy", matrix)


def save_names(stock_names):
    #saves stock names from import_data
    with open("data/holding_names.json", 'w') as f:
        json.dump(stock_names, f, indent = 2)


def calc_sharpe_ratio(portfolio_return, risk_free_return, stdev):
    sharpe_ratio = (portfolio_return - risk_free_return) / stdev

    return sharpe_ratio


def get_stdev(matrix, column):
    columns_stdev = np.std(matrix, axis = 0, dtype=np.float64)
    stdev = columns_stdev[column]

    return stdev


def total_gains(matrix):
    matrix_sum = matrix.sum(axis=0)
    total_gain = matrix_sum[7]

    return total_gain


def max_gain(matrix):
    max_values = np.amax(matrix, axis = 0)
    max_gain = max_values[7]
    
    return max_gain


def min_gain(matrix):
    min_values = np.amin(matrix, axis = 0)
    min_gain = min_values[7]
    
    return min_gain


def best_stock(matrix):
    max_values = np.amax(matrix, axis = 0)
    best_stock = max_values[5]
    
    return best_stock


def name_best_stock(matrix, names):
    indices_max_columns = np.argmax(matrix, axis = 0)
    index_best_stock = indices_max_columns[5]
    name_best_stock = names[index_best_stock]
    
    return name_best_stock


def worst_stock(matrix):
    min_values = np.amin(matrix, axis = 0)
    worst_stock = min_values[5]
    
    return worst_stock


def name_worst_stock(matrix, names):
    indices_min_columns = np.argmin(matrix, axis = 0)
    index_worst_stock = indices_min_columns[5]
    name_worst_stock = names[index_worst_stock]

    return name_worst_stock



"""main function"""

#input and command handler
if len(sys.argv) == 2:
    command = sys.argv[1]


    #import file
    if command == "upload":
        filename = input("Enter filename:")

        valid_input = filename.endswith(".csv")


        #check if valid input else repromt user
        while valid_input == False:
            print("This file is not of .csv file format and is therefore not compatible. To exit the Programm type [exit].") 
            filename = input("Enter filename:")

            if filename == "exit":
                sys.exit(0)
            else:
                valid_input = filename.endswith(".csv")


        #run upload
 
        #read into pandas
        df = pd.read_csv(filename)
        
        #convert data to np_array
        portfolio_data = import_data(df)
        
        #list containing stock names 
        stock_names = get_name(df) 

        #save the data to holding file for other commands to use
        save_data(portfolio_data)
        
        #get names of stocks
        stock_names = get_name(df)

        #save list with stock names
        save_names(stock_names)


    else: 
        #check that some data exists
        try:
            portfolio_data = np.load("data/holding_data.npy")

        except:
            print("Use the upload command before using any other commands")

        else:
            portfolio_data = np.load("data/holding_data.npy")
            with open ("data/holding_names.json", 'r') as f:
                names = json.load(f) 

            #running the commands
            if command == "run_all":
                #print("run_all is currently in development")

                #get total_gains
                total_gain = total_gains(portfolio_data)
                print(f"The total gain is {total_gain}$")

                #get max_gains
                max_gain = max_gain(portfolio_data)
                print(f"The maximum gain is {max_gain}$")

                #get min_gains
                min_gain = min_gain(portfolio_data)
                print(f"The minimum gain is {min_gain}$")

                #get_sharpe_ratio
                portfolio_return = total_gain
                stdev = get_stdev(portfolio_data, 7)
                risk_free_rate = 0.0119
                #risk_free_rate = input("Enter risk-free rate as a decimal:")
                risk_free_return = 0.0119 * 100000
                sharpe_ratio = calc_sharpe_ratio(portfolio_return, risk_free_return, stdev)
                print(f"With a Portfolio Return of {portfolio_return}$, a standard deviation of {stdev} and a Risk-free Return of {risk_free_return},")
                print(f"the calculated Sharpe-Ratio for this portfolio is = {sharpe_ratio}") 

                #get best_stock
                best_stock = best_stock(portfolio_data)
                name_best_stock = name_best_stock(portfolio_data, names)
                print(f"The best stock was {name_best_stock} with {best_stock}%%")

                #get worst_stock
                worst_stock = worst_stock(portfolio_data)
                name_worst_stock = name_worst_stock(portfolio_data, names)
                print(f"The worst stock was {name_worst_stock} with {worst_stock}%%")

            elif command == "total_gains":
                total_gain = total_gains(portfolio_data)
                print(f"The total gain is {total_gain}$")

            elif command == "max_gains":
                max_gain = max_gain(portfolio_data)
                print(f"The maximum gain is {max_gain}$") 

            elif command == "min_gains":
                min_gain = min_gain(portfolio_data)
                print(f"The minimum gain is {min_gain}$")

            elif command == "get_sharpe_ratio":
                #import the portfolio return (same as total gain function)
                portfolio_return = total_gains(portfolio_data)

                #calculate standard deviation
                stdev = get_stdev(portfolio_data, 7)

                #get risk free return value
                risk_free_rate = 0.0119
                #risk_free_rate = input("Enter risk-free rate as a decimal:")
                risk_free_return = 0.0119 * 100000

                #calculate sharp ratio
                sharpe_ratio = calc_sharpe_ratio(portfolio_return, risk_free_return, stdev)

                #print results
                print(f"With a Portfolio Return of {portfolio_return}$, a standard deviation of {stdev} and a Risk-free Return of {risk_free_return},")
                print(f"the calculated Sharpe-Ratio for this portfolio is = {sharpe_ratio}")    
            
            elif command == "best_stock":
                best_stock = best_stock(portfolio_data)

                name_best_stock = name_best_stock(portfolio_data, names)

                print(f"The best stock was {name_best_stock} with {best_stock}%%")
                

            elif command == "worst_stock":
                worst_stock = worst_stock(portfolio_data)

                name_worst_stock = name_worst_stock(portfolio_data, names)

                print(f"The worst stock was {name_worst_stock} with {worst_stock}%%")
                

            else:
                #error message to user
                print("Unknown command. Please try again.\n Available commands are:\n") 
                #list of possible commands
                print("upload \t run_all \t get_sharpe_ratio \t max_gains \t min_gains \t total_gains \t best_stock \t worst_stock") 


else:
    print("Please pass exactly one command.")  

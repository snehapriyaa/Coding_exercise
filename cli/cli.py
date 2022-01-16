#local import
import argparse
import pandas as pandasForSortingCSV

# Parsing arguments using argparser
parser = argparse.ArgumentParser(description='Data Parser for Stock Computation') # initialize
parser.add_argument('--csvFilePath', help = 'path of csv file containing the stock data')
parser.add_argument('--sort',default='asc', help = 'sorting order of stock data')
parser.add_argument('--stockName', help = 'name of stock')
parser.add_argument('--startDate', help = 'start date')
parser.add_argument('--endDate', help = 'end date')
args = parser.parse_args() # parse arguments to dictionary

# Sorting the data in ascending or descending order
csvData = pandasForSortingCSV.read_csv(args.csvFilePath)
sort = True if args.sort == 'asc' else False
csvData.sort_values([csvData.columns[6], csvData.columns[0]],
                    axis=0,
                    ascending=[sort, sort],
                    inplace=True)
csvData.to_csv(r"soln1.csv",index=False)

#Changing the column object values to float
csvData['high']=pandasForSortingCSV.to_numeric(csvData['high'],errors='coerce')
csvData['open']=pandasForSortingCSV.to_numeric(csvData['open'],errors='coerce')

#Highest price per stock calculation
result = csvData[csvData['high'].notnull()]
#Retain the highest price value in each group of stock
result = result.sort_values('high').drop_duplicates(['Name'],keep='last')
cols_to_keep = ['Name', 'high']
result = result[cols_to_keep]

result.to_json (r"soln2.json",orient = "records", date_format = "epoch", double_precision = 10, force_ascii = True, date_unit = "ms", default_handler = None)

#Maximum and minimum difference calculation for open and close price
result = csvData.loc[csvData['Name'] == args.stockName]
#Find the rows with maximum difference
maxresult = result[(result['open']-result['close']).abs() == (result['open']-result['close']).abs().max()]
#Filter the one with the highest volume.
maxresult = maxresult[maxresult['volume']==maxresult['volume'].max()]
maxresult['difference_value'] = (maxresult['open']-maxresult['close']).abs()
maxresult['difference_type'] = 'maximum'
cols_to_keep = ['Name', 'date', 'difference_value', 'difference_type', 'volume', 'open', 'close']
maxresult = maxresult[cols_to_keep]


minresult = result[(result['open']-result['close']).abs() == (result['open']-result['close']).abs().min()]
minresult = minresult[minresult['volume']==minresult['volume'].max()]
minresult['difference_value'] = (minresult['open']-minresult['close']).abs()
minresult['difference_type'] = 'minimum'
minresult = minresult[cols_to_keep]

#Combine maximum difference and minimum difference result and store as json
frames = [maxresult,minresult]
result = pandasForSortingCSV.concat(frames)
result.to_json (r"soln3.json",orient = "records", date_format = "epoch", double_precision = 10, force_ascii = True, date_unit = "ms", default_handler = None)

#Lowest and Highest price of the given stock in date range calculation
result = csvData.loc[csvData['Name'] == args.stockName]
#Filter the records in the given date range
result = result[result['date']>=args.startDate]
result = result[result['date']<=args.endDate]
maxresult = result[result['high']==result['high'].max()]
maxresult['price'] = 'Highest'
minresult =  result[result['low']==result['low'].min()]
minresult['price'] = 'Lowest'
cols_to_keep = ['Name', 'date', 'price', 'high']
maxresult = maxresult[cols_to_keep]
cols_to_keep = ['Name', 'date', 'price', 'low']
minresult = minresult[cols_to_keep]
frames = [maxresult,minresult]
result = pandasForSortingCSV.concat(frames)
result.to_json (r"soln4.json",orient = "records", date_format = "epoch", double_precision = 10, force_ascii = True, date_unit = "ms", default_handler = None)

from tabulate import tabulate
import pandas as pd

def load_file(filename):
    """Loads csv file"""
    try:
        df = pd.read_csv(filename)
        return df
    except FileNotFoundError:
        return "File Not found"
    
    
portfolio_table = []
portfolio_dic = {}
total_invested = 0
total_current_value = 0

headers = ["Balance", "Profit/Loss", "Symbol"]

while True:

    """Getting inputs"""
    file = input('Enter Symbol (AAPL, MSFT, TSLA) / Press "Done" to exit : ').upper()
    if file == 'DONE':
        break
    elif file not in ['AAPL', 'MSFT', 'TSLA']:
        print('Please enter a valid symbol')
        continue

    #Purchase price input
    try:
        purchase_p = float(input('Enter purchase price: '))
        if purchase_p <= 0:
            print('Purchase price must be greater than 0')
            continue
    except ValueError:
        print('Please enter a numeric value')
        continue
    #Number of shares input
    try:
        sh_num = int(input("Number of shares owned: "))
        if sh_num <= 0:
            print('Number of shares must be greater than 0')
            continue
    except ValueError:
        print('Please enter a whole integer number')
        continue

    #Load CSV data
    data = load_file(f'{file}.csv')
    if isinstance(data, str):
        print(data)
        continue
    try:

        latest_close = float(data.iloc[-1]['Close'])
    except KeyError:
        print(f"CSV for {file} missing 'Close' column.")
        continue



    balance = sh_num * latest_close
    pl_percen = ((latest_close - purchase_p) / purchase_p) * 100
    pl_money = (latest_close - purchase_p) * sh_num

    #Save to portfolio
    portfolio_table.append([
        f'{sh_num} x ${purchase_p:.2f} = ${balance:.2f}', f'{pl_percen:.2f}% ; {pl_money:.2f}$',
        file
    ])

    portfolio_dic[file] = {

        'Balance': round(balance),
        'Profit/Loss': round(pl_percen),
        'Money made/lost ($)': round(pl_money),
        'Shares': round(sh_num),
        'Purchase price': round(purchase_p)
    }

    total_invested += purchase_p * sh_num
    total_current_value += latest_close * sh_num


""" Total values """

portfolio_percent = (((total_current_value - total_invested) / total_invested) * 100 if total_invested else 0)
total_balance = sum(item['Balance'] for item in portfolio_dic.values())
total_money = sum(item['Money made/lost ($)'] for item in portfolio_dic.values())
portfolio_table.append([f'{total_balance:.2f}',
                        f'{portfolio_percent:.2f}% ; {total_money:.2f}$', '---'])




""" Print the full portfolio table """
print(tabulate(portfolio_table, headers, tablefmt="fancy_grid"))
print(portfolio_dic)

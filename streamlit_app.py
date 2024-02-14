import streamlit

import pandas as pd
import numpy
# ENSURE YOUR CSV FILE are CAPITILsed , = UPPER(A1)
# forced the  USER INPUT to capitalise   Str.upper()
#Ensure your CSV HAS NO WHITESAPCE N COL NAME -GIVES KEY ERROR
#REMOVE WHITE SPACE FROM ALL VALUES IN CSV  = strip(A1)
#remove white space from user entry str.strip()
#create function to handle predicition
# files .......
# stock per.csv'
#stock.csv
#stock_main.csv
#salesrecord.csv
#salestemrecord.csv
#things to do .....1. add delete one and all record to stock file
# change font to big one 3. add price and amount made

def fetchSale(see_records):
    # try:
        if see_records[0] == 'ADMIN':  #for security purpose create a file to hold this password
        # if  password is Admin
            df_fetch = pd.read_csv('SalesRecord.csv')
        # dispay the file to user
            streamlit.write(df_fetch)
            count = len(df_fetch)
        # calculate the sum  to user
            total_sales = df_fetch['PRICE'].sum()
            return f'Your total sales is {total_sales} for  {count} sales records'
        else:
            return 'wrong password'
    # except:  # capture bug and error
    #     return 'error in Registration'

#delete sales record
def deleteSalesRecords(sales_delete):  #delet error in sales records
    try:
        if sales_delete[0] == 'ADMIN':
            #proceed if password is admin
            if sales_delete[1]: # if entry for row is not empty
                 #return f'{info_delete[1]}'
                #if entry for row to delete is not empty
                df_fetch2 = pd.read_csv('SalesRecord.csv')
                if sales_delete[1] < len(df_fetch2.index) :
                #drop the row df.index[-1]
                    df_update_sales = df_fetch2.drop(df_fetch2.index[sales_delete[1]])
                    df_update_sales.to_csv('SalesRecord.csv',index =False)  #do not add new index to update file
                    return f'Row {sales_delete[1]} sales record is succesfully deleted '
                else:
                    return 'Row of record doesnt exist. Enter proper row number  '
            else:
                return ' you have not entered row number to delete'
        else:
            return " wrong password"
    except:  # capture bug and error do not show it to ende user
         return 'code error'


#deleteAllSalesRecords
#to drop all rows in dataframe keeper the header/cols
#update the new file csv with no index
def deleteAllSalesRecords(Allsales_delete):  #delet error in sales records
    # try:
    if Allsales_delete[0] == 'ADMIN':
        df_fetch3 = pd.read_csv('SalesRecord.csv')
                #drop all row df.index[-1]
        df_update_all_sales = df_fetch3.drop(df_fetch3.index[1:])
        df_update_all_sales.to_csv('SalesRecord.csv',index =False)  #do not add new index to update file
        streamlit.write(df_update_all_sales)
        return f' all sales record is succesfully deleted '
    else:
        return " wrong password"
    # except:  # capture bug and error do not show it to ende user
    #     return 'error in Registration'




#entering sales records

def salesRecords(sales_details):
    # try:
        if sales_details[0] == 0:
            return 'Enter Sales ID. start from 1  '
        elif sales_details[1] == '':
            return 'Enter Sales item '
        elif sales_details[2] == 0:
            return 'Enter stock id '
        # elif sales_details[3] == '':
        #     return 'Enter  item description '
        elif sales_details[4] == 0.00:
            return 'Enter unit price '
        elif sales_details[5] == 0:
            return 'Enter quantity '
        # elif sales_details[6] == 0.00: zero value is allowed as no dsicount
        #     return 'Enter Discount'
        # elif sales_details[7] == 0 : automatically calclated
        #     return 'Enter price'
        elif sales_details:
            # check for double sales id
            df_sale = pd.read_csv('SalesRecord.csv')
            check_salesid = df_sale['SALES_ID'].values.tolist()  # if does work with pandas convert to list
            if sales_details[0] in check_salesid:
                return 'This sales has been registered. choose another sales id!!!'
            else:
                Input_array = numpy.asarray(sales_details)
                Input_array_reshaped = Input_array.reshape(1, -1)  # one row ,as many cols
                df= pd.DataFrame(Input_array_reshaped)
                df.to_csv('SalesRecord.csv',mode='a',index= False,header=False)
                #for stock taking
                df.to_csv('SalestempRecord.csv',mode= 'a',index= False,header=False)
                return 'Sales entry was sucessful'
        else: # if everrything failed
            return 'Sales entry  failed '
    # except:  # capture bug and error
    #     return 'error in sales recording '



#fetchStock
def fetchStock(see_stkrecords):
    # try:
        if see_stkrecords[0] == 'ADMIN':  #for security purpose create a file to hold this password
        # if  password is Admin
            df_fetchstk = pd.read_csv('Stock.csv')
        # dispay the file to user
            streamlit.write(df_fetchstk)
            count = len(df_fetchstk)
        # calculate the sum  to user
            total_stock_price = df_fetchstk['Total_Cost_Price'].sum()
            Sales_made = df_fetchstk['Total_Sale_Amount'].sum()

            return f'Sales made so far is {Sales_made}. Investement sum is {total_stock_price} Naira for  {count} stock records'
        else:
            return 'wrong password'
    # except:  # capture bug and error
    #     return 'error in Registration'

######## edit a stock file
def editing(usersupdate):  #df.at[index,col label] = new value
    if usersupdate[0] == 'ADMIN':
        #proceed if password is admin
        if usersupdate[1] == 0:  #2
            return ' enter index or row  number to edit '
        elif usersupdate[2] == '': #desc
            return ' enter column name to edit'
        elif usersupdate[3] == '':
            return ' enter new values '
        elif usersupdate: # not empy

            df_update = pd.read_csv('Stock.csv')
            df_update.at[usersupdate[1], usersupdate[2]] = usersupdate[3]
            df_update.to_csv('Stock.csv',index = False)
            df_update.to_csv('Stock_perm.csv', index = False) #backup
            return ' file has been update '
        else:
            return 'no entry found'
    else:
        return 'wrong password'

 ####  get live inventory -
# match two DF, change the value in
# one drop the entire DF rows in another
def fetchliveStock(see_stklive):
    # try:
    if see_stklive[0] == 'ADMIN':  # for security purpose create a file to hold this password
        # if  password is Admin
        #a temp file to hold one sales record to reduce stock at a time
        df_fetchtempsales = pd.read_csv('SalestempRecord.csv')
        df_fetchstock = pd.read_csv('Stock.csv') # keep a copy of mainstock eleswhere
        streamlit.write(df_fetchtempsales)

        for j in range(len(df_fetchtempsales)):  #use df.at it uses index and col label to pick a cell
            for i in range(len(df_fetchstock)):
                #the index where stockid in both dframes matched
                if  df_fetchtempsales.at[j,'Stock_id'] ==df_fetchstock.at[i,'Stock_id']:
                    diff_in_qty = df_fetchstock.at[i,'Qty_in_Stock'] - df_fetchtempsales.at[j, 'QTY']
                    # return f'{diff_in_qty}'
                    df_fetchstock.at[i,'Qty_in_Stock'] = diff_in_qty

                    #calculate amount sold
                    amount_sold = df_fetchstock.at[i, 'Total_Sale_Amount'] + df_fetchtempsales.at[j, 'PRICE']
                    df_fetchstock.at[i, 'Total_Sale_Amount'] = amount_sold
                    profit_made = df_fetchstock.at[i, 'Total_Sale_Amount'] -df_fetchstock.at[i, 'Total_Cost_Price']
                    #update record
                    df_fetchstock.at[i, 'Profit'] = profit_made
                    #update the stock file
                    df_fetchstock.to_csv('Stock.csv', index=False)
                    #go to necxt row in df_fetchtempsales until finished

        # print out the live stocking when for lopp finishes
        df_fetchstocklive = pd.read_csv('Stock.csv')
        streamlit.write(df_fetchstocklive)  # it holds THE LIVE STOCK after the for loop
        #drop the row in SalestempRecord.csv where the qty has been update in stock
        df_fetchtempsales_update = df_fetchtempsales.drop(df_fetchtempsales.index[:])                    #evry time index =1 is drop, the next item becomes index 1 in temp file
        df_fetchtempsales_update.to_csv('SalestempRecord.csv', index =False)
        streamlit.write(df_fetchtempsales_update)

    else:
        return 'wrong password'
# except:  # capture bug and error
#     return 'error in Registration'
#stock entry stckRecords


#uploading stock  sales
#writing new values of list into csv with numpy. asrray, then append, no index ,no header to csv
def stckRecords(stock_details):
    # try:
        if stock_details[0] == 0:
            return 'Enter stock ID.  '
        elif stock_details[1] == '':
            return 'Enter stock item generic name'
        elif stock_details[2] == '':
            return 'Enter  stock description '
        elif stock_details[3] == 0:
            return 'Enter stock qty '
        elif stock_details[4] == 0.00:
            return 'Enter stock price.Pleae dont add comma '
        # elif stock_details[5] == 0.00:
        #     return 'Enter amount made '
        # elif stock_details[6] == 0.00:
        #     return 'Enter profit_ made '
        elif stock_details[7] == 0.00:
            return 'Enter unit selling price.Pleae dont add comma '
        elif stock_details:
            # check for double stock entry
            df_sale = pd.read_csv('Stock.csv')
            check_stkid = df_sale['Stock_id'].values.tolist()  # if does work with pandas convert to list
            if stock_details[0] in check_stkid:
                return 'This stock has been entered. choose another stock id for new stock!'
            else:
                Input_array = numpy.asarray(stock_details)
                Input_array_reshaped = Input_array.reshape(1, -1)  # one row ,as many cols
                df= pd.DataFrame(Input_array_reshaped)
                df.to_csv('Stock.csv',mode='a',index= False,header=False)
                df.to_csv('Stock_main.csv', mode='a', index=False, header=False)
                return 'Stock was added sucessfully'
        else: # if everrything failed
            return 'Stock  entry  failed '
    # except:  # capture bug and error
    #     return 'error in Stock  recording '

##### build interface
def main():

    # # sales inteface
    # # give a title
    streamlit.title(' aPP for every ShOp')
    streamlit.title(' Enter Sales')
    streamlit.subheader ('MY, ShOp @ 25 kenneth Street,Lagos')
    # with streamlit.form("Salesform", clear_on_submit=True):
    Enter_sale_id = streamlit.number_input('enter sales id', min_value=0, max_value=1000000, value=0, step=1, key='sid')
    Enter_sale_id = int(Enter_sale_id)
    # fect last sales id
    dflast_sales_id= pd.read_csv('SalesRecord.csv')
    last_sales_id = dflast_sales_id['SALES_ID'].iloc[-1]
    Next_sales_ID = last_sales_id + 1
    streamlit.write('Next sales id is:',Next_sales_ID)

        # Enter_items = streamlit.text_input('enter Sales items /make them category from stock file', value="",key= 'sitems')
        # Enter_items_cl = Enter_items.upper().strip() # pass an upper
    dfs = pd.read_csv('Stock.csv')
    selected_item = streamlit.selectbox("Select items",dfs['Items'] + "  "+  "  "+ dfs['Desc'] + "  "+  "  "+ dfs['Unit_price'].astype(str),key='salcategory')
    Enter_items_cl = str(selected_item) # convert when fetching from file or user
        # Enter_stck_id = streamlit.number_input('enter stock id /sub category from stock file', min_value=0, max_value=1000000, value=0, step=1, key='stc2id')
        # Enter_stck_id = int(Enter_stck_id)
    #what your select from above pass it to filtered_df
    filtered_df = dfs[dfs['Items'] + "  "+  "  "+ dfs['Desc'] + "  "+  "  "+ dfs['Unit_price'].astype(str) == selected_item]
        # #from the filtered row bring only values of stock id
    selcect_stck_id = filtered_df['Stock_id']
    selcect_stck_id=int(selcect_stck_id)  # convert when fetching from file or user
    Enter_stck_id = streamlit.number_input('enter stock id', min_value=0, max_value=1000000, value=selcect_stck_id, step=1, key='stc2id')

    # Enter_Desc = streamlit.text_input('items description//sub category from stock file', value="", key='sdesc')
    # Enter_Desc_cl = Enter_Desc.upper().strip()  # pass an upper
    Enter_Desc= filtered_df['Desc']
    Enter_Desc2= str(Enter_Desc) # convert when fetching from file or user
    Enter_Desc_cl = streamlit.text_input('items description', value=Enter_Desc2, key='sdesc')

    Enter_unit_price = streamlit.number_input('enter unit price of item', min_value=0.00, max_value=1000000.00, value=0.00, step=1.00, key='uprice')
    Enter_unit_price =float(Enter_unit_price) # convert when fetching from file or user
    Enter_qty = streamlit.number_input('enter quantity of item', min_value=0, max_value=1000000, value=0, step=1,key='uqty')
    Enter_qty = int(Enter_qty) # convert when fetching from file or user

    Enter_Discount = streamlit.number_input('enter discount', min_value=0.00, max_value=1000000.00, value=0.00, step=1.00, key='dis')
    Enter_Discount = float(Enter_Discount) # convert when fetching from file or user

    Enter_price2 = (Enter_unit_price * Enter_qty) - Enter_Discount
    Enter_price1= float(Enter_price2) # convert when fetching from file or user
    Enter_price = streamlit.number_input('enter Price', min_value=0.00, max_value=1000000000.00, value=Enter_price1, step=1.00, key='price')
        # Enter_price1= streamlit.write('THE PRICE IS :',Enter_price1,'cross check your entry')

    Enter_notes = streamlit.text_input('enter sales observation  if any', value="", key='ob')

    current_time = pd.Timestamp.now()
    time = streamlit.text_input('date and Time of sales', value=current_time, key='tim')

        # submit = streamlit.form_submit_button(label="Upload Sales")
    salesrecords = ""  # declare this variable to hold result like empty list
    # if submit:          #
    if streamlit.button('Upload Sales',key = 'upsal'):
        # Reg ...call the function to process input
        salesrecords = salesRecords([Enter_sale_id,Enter_items_cl,Enter_stck_id,Enter_Desc_cl,Enter_unit_price,Enter_qty ,Enter_Discount,Enter_price,Enter_notes,time])
    streamlit.success(salesrecords)

########

    #  ----- fetch all sales records
    # give a title
    streamlit.title('MY Sales Now Now')

    admin_password = streamlit.text_input('enter password', value="", key='salpass')
    admin_password_upper = admin_password.upper().strip()
    fetchsale = ""  # declare this variable to hold result like empty list

    if streamlit.button('See all Sales', key='fetsale'):
        # fetchRecords ...call the function to process input
        fetchsale = fetchSale([admin_password_upper])
    streamlit.success(fetchsale)

    # DELeTING wrong sales RECORDS

    admin_del = streamlit.number_input('enter row number of record to delete', min_value=0, max_value=1000000, value=0,step=1, key='delrows')
    # admin_del_upper = admin_del.upper().strip()
    delectesal = ""
    if streamlit.button('Delete one Sales Record', key='delsal'):
        delectesal = deleteSalesRecords([admin_password_upper, int(admin_del)])
    streamlit.success(delectesal)  # return the result

    # DELeTING all sales RECORDS fro new business day
    #
    # admin_del = streamlit.number_input('enter row number of record to delete', min_value=0, max_value=1000000, value=0,
    #                                    step=1, key='delrows')
    # admin_del_upper = admin_del.upper().strip()
    delecteallsal = ""
    if streamlit.button('Delete All Sales Record', key='delallsal'):
        delecteallsal = deleteAllSalesRecords([admin_password_upper])
    streamlit.success(delecteallsal)  # return the result

# give a title
    #  ----- fetch all stock records
    # give a title
    streamlit.title('Check Inventory & stock taking ')

    admin_stk_password = streamlit.text_input('enter password', value="", key='stkpass')
    admin_stk_password_upper = admin_stk_password.upper().strip()
    fetchstk = ""  # declare this variable to hold result like empty list

    if streamlit.button('See last inventory', key='fetstck'):
        # fetchRecords ...call the function to process input
        fetchstk = fetchStock([admin_stk_password_upper])
    streamlit.success(fetchstk)

#### edit button of a file
    col1, col2, col3 = streamlit.columns(( 1, 1, 1))   # layout element
    with col1:
        Enter_row_number  = streamlit.number_input('Enter_row_number ', min_value=0, max_value=10000,value=0, step=1, key='rowno')
        Enter_row_number = int(Enter_row_number)
    with col2:
        Enter_col_title = streamlit.text_input('Enter_col_title as it is', value="", key='colabel')
        Enter_col_title_cl = Enter_col_title.strip()  # col must match the document
    with col3:
        Enter_new_value = streamlit.text_input('Enter_new_value', value="", key='newval')
        Enter_new_value_cl = Enter_new_value.strip()

    edit = ""  # declare this variable to hold result like empty list

    if streamlit.button('edit file', key='ed'):
        # Reg ...call the function to process input
        edit = editing([admin_stk_password_upper,Enter_row_number,Enter_col_title_cl,Enter_new_value_cl])

    streamlit.success(edit)

#### getting live inventory
    fetchstklive = ""  # declare this variable to hold result like empty list

    if streamlit.button('See live inventory', key='fetlivstck'):
        # fetchRecords ...call the function to process input
        fetchstklive = fetchliveStock([admin_stk_password_upper])
    streamlit.success(fetchstklive)

#upload stock
    streamlit.title(' upload new stock')
    with streamlit.form("myform", clear_on_submit=True):
        Enter_stk_id = streamlit.number_input('enter stock category id', min_value=0, max_value=1000000, value=0, step=1, key='sitemid')
        Enter_stk_id = int(Enter_stk_id)
        # fect curent stock id
        dflast_stcok_id = pd.read_csv('Stock.csv')
        dflast_stcok_id = dflast_stcok_id['Stock_id'].iloc[-1]
        Next_stcok_id = dflast_stcok_id + 1
        streamlit.write('the next stock id is:', Next_stcok_id)

        Enter_stk_items = streamlit.text_input('enter stock category name', value="",key= 'stckitems')
        Enter_stk_items_cl = Enter_stk_items.upper().strip() # pass an upper

        Enter_stk_Desc = streamlit.text_input('stock item description', value="", key='stkdesc')
        Enter_stk_Desc_cl = Enter_stk_Desc.upper().strip()  # pass an upper

        Enter_stk_oty = streamlit.number_input('enter quantity ', min_value=0, max_value=1000000, value=0, step=1, key='stkqty')
        Enter_stk_oty =int(Enter_stk_oty)

        Enter_stk_price = streamlit.number_input('enter cost price of stock', min_value=0.00, max_value=1000000000.00, value=0.00, step=1.00,key='stkprice')
        Enter_stk_price = int(Enter_stk_price)
        Enter_amount_made = 0
        Enter_profit_made = 0
        Enter_stk_uprice = streamlit.number_input('enter selling unit price of stock', min_value=0.00, max_value=1000000000.00,
                                                 value=0.00, step=1.00, key='unstkprice')
        Enter_stk_uprice = int(Enter_stk_uprice)

        Enter_stk_notes = streamlit.text_input('enter  observation about product if any', value="", key='stkob')

        current_time = pd.Timestamp.now()
        time_stk = streamlit.text_input('date and Time of stock', value=current_time, key='stktim')
        submit = streamlit.form_submit_button(label="Upload stock")
    stockrecords= ""  # declare this variable to hold result like empty list

    if submit:                 #streamlit.button('Upload stock',key = 'upstck'):
        # Reg ...call the function to process input
        stockrecords = stckRecords([Enter_stk_id,Enter_stk_items_cl,Enter_stk_Desc_cl,Enter_stk_oty,Enter_stk_price,Enter_amount_made,Enter_profit_made,Enter_stk_uprice,Enter_stk_notes,time_stk])

    streamlit.success(stockrecords)

    streamlit.title('aPP for every shop developers')

if __name__ == '__main__':
    main()

# web app  on your desktop local host
#run  on your pycharm terminal ' streamlit run sales.py '

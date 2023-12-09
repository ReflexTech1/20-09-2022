import os
import fnmatch
import sqlite3
import pandas as pd
from datetime import datetime

dateTimeObj = datetime.now()

timestampStr = dateTimeObj.strftime("%d-%b-%Y")

# creates a directory without throwing an error


def create_dir(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)
    return dir

# finds files in a directory corresponding to a regex query


def find(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result


# convert sqlite databases(.db,.sqlite) to pandas dataframe(excel with each table as a different sheet or individual csv sheets)
def save_db(dbpath=r'C:\RSoft\Current\Reflex Footwear.sql3', excel_path=None, csv_path=None, extension="*.sqlite", csvs=True, excels=True):
    if (excels == False and csvs == True):
        return -1

    # little code to find files by extension
    if dbpath == None:
        files = find(extension, os.getcwd())
        if len(files) > 1:
            dbpath = find(extension, os.getcwd())[
                0] if dbpath == None else dbpath

    # path handling

    external_folder, base_name = os.path.split(os.path.abspath(dbpath))
    file_name = os.path.splitext(base_name)[0]  # firstname without .
    exten = os.path.splitext(base_name)[-1]  # .file_extension

    internal_folder = "Production - " + timestampStr
    main_path = os.path.join(external_folder, internal_folder)
    create_dir(main_path)

    excel_path = os.path.join(
        main_path, "Production Balances.xlsx") if excel_path == None else excel_path
    csv_path = main_path if csv_path == None else csv_path

    db = sqlite3.connect(dbpath)
    cursor = db.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = cursor.fetchone()

# SELECT Table
    if (excels == True and csvs == True):
        writer = pd.ExcelWriter(excel_path, engine='xlsxwriter')
        i = 0
        for table_name in tables:
            table_name = table_name[0]
            table = pd.read_sql_query("SELECT Order2,Style,Deldate,Orderqty,Cutting,Assembly,Closing,Finishing,Despatch,ToShip,Shipped from Production_Balances ORDER BY DelDate ASC", db)
            {cursor.description[i][0]: _ for i, _ in enumerate(zip(*cursor.fetchall()))
             if all(val is not None for val in _)}
            table.to_excel(writer, sheet_name=table_name, index=False)

        writer.save()
        cursor.close()
        db.close()
        return 0


save_db()

os.system('python export_success.py')

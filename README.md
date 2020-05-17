# Excel To Database

A tool for exporting any excel table to an sqlite database by dynamically creating table based on column headers

usage: excel2db.py [-h] -f INPUT_FOLDER -s INPUT_SHEET

optional arguments:
  -h, --help            show this help message and exit
  -f INPUT_FOLDER, --folder INPUT_FOLDER
                        point to the folder containing the excel files
  -s INPUT_SHEET, --sheet INPUT_SHEET
                        Sheet name in Excel to be coverted to SQL tables




Feel free to hit me up with suggestions.


### Installing

Download the latest version from Git Repo

```
git clone git@github.com:riazibrahim/Excel2DB.git

or

git clone https://github.com/riazibrahim/Excel2DB.git
```

Change to the source code folder

```
cd Excel2DB
```
Start a new virtual environment

```
python -m venv venv

source venv/bin/activate
```

Install all the requirements

```
pip install -r requirements.pip
```

Put all the excel files in an 'inputs' folder (or any name, however, change name in subsequent commands)

(Optional) Configure the table name based on patterns in input excel file names in config.py (Default: Table name is file name without extension)

```
nano config.py


TABLE_NAMES_DICT = {
        'Preferred_table_name': 'substring in filename',
        'Table_1': 'MAZ',
        'Table_1': 'SAZ',
        'Table_2': 'APAC',
    }

In the above example, all data in excel files containing 'MAZ' or 'SAZ' in its filename will be dumped to same table 'Table 1'. Warning: Ensure column headings are same for files mapped to same table name.
```

## Running the tool

This will go through all excel files in and export data in Sheet1 to database.

```
python excel2db.py -f inputs -s 'Sheet1'
```
Rerun if there are multiple sheets, the database table will be updated as long as column headings are same.

The output will be generated as reports.db in root folder. Go crazy with the database.

##### To get help:
```
python excel2db.py -h
```


## Built With

* [Python3](https://www.python.org/download/releases/3.0/)


## Authors

* **Riaz Ibrahim** - [riazibrahim](https://github.com/https://github.com/riazibrahim/)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details

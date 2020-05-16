# Cyber word cloud

A tool for generating word cloud from a list of input URLs or single URL in command.

usage: cyber_cloud.py [-h] (-u URL | -f FILE) -o OUTPUT

optional arguments:
  -h, --help                    show this help message and exit
  -u URL, --url URL             Give URL to obtain word cloud
  -f FILE, --file FILE          Give URLs in a file
  -o OUTPUT, --output OUTPUT    Give output file name


Feel free to hit me up with suggestions.


### Installing

Download the latest version from Git Repo

```
git clone git@github.com:riazibrahim/cyber_cloud.git
```

Change to the source code folder

```
cd cyber_cloud
```
Start a new virtual environment

```
python -m venv venv

source venv/bin/activate
```

Install all the requirements

```
pip install -r requirements.txt
```

Update the stopwords.lst file that exclude words from the word cloud (if required)

```
nano stopwords.lst
```


## Running the tool


##### Usage 1: To obtain word cloud from a single URL:
```
python cyber_cloud.py -u 'https://www.us-cert.gov/ncas/alerts/aa20-107a' -o cyberwordcloud
```
##### Usage 2: To obtain word cloud from a list of  URLs:
```
python cyber_cloud.py -f url_list.lst -o cyberwordcloud 
```

##### Usage 2: To get help:
```
python cyber_cloud.py -h
```


## Built With

* [Python3](https://www.python.org/download/releases/3.0/) 


## Authors

* **Riaz Ibrahim** - [riazibrahim](https://github.com/https://github.com/riazibrahim/)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details
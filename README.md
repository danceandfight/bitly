# Bitly url shorterer

This program creates short link with [bit.ly](bitly.com) or counts clicks for short link.

### How to install

For using this program you must register on [bit.ly](bitly.com) and get `GENERIC ACCESS TOKEN` in your profile. Token looks like `d453e0707bfdc3c7fa31db6f40e15ad3d1801a98`. Then create `.env` file in program folder and add token there using this form: `TOKEN=Bearer d453e0707bfdc3c7fa31db6f40e15ad3d1801a98`.

Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

### Simple Example

```python
$ python main.py https://dvmn.org/modules/
http://bit.ly/2Jq1PGj
$ python main.py http://bit.ly/2Jq1PGj
[{'date': '2019-03-21T00:00:00+0000', 'clicks': 1}]
```

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).
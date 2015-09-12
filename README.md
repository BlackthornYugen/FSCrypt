# FSCrypt.py
## Requirements
You will need to have the pycrypto library installed. You can get it with pip:
OSX / Linux: 
```
sudo pip install pycrypto
```
Windows:
```
pip install pycrypto
```
## Turn a Vault savefile into readable json
OSX / Linux:
```
cat example.sav | ./FSCrypt.py | python -m json.tool > example.json
```
Windows:
```
type example.sav | .\FSCrypt.py | python -m json.tool > example.json
```
## Turn readable json into a Vault Savefile

Coming soon...
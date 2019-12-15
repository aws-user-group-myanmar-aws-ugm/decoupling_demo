### Install packages
```bash
sudo yum install git python3 -y
```

### Prepare environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### Install dependencies
```bash
pip install -r requirements.txt
```

### Run music player frontend
```bash
python3 -m http.server
```

### Run Producer
```bash
env FLASK_APP=producer.py flask run --host=0.0.0.0
```

### Run Stats frontend
```bash
env FLASK_APP=stats.py flask run --host=0.0.0.0
```

### Run Consumer
```bash
python listener.py
```

### Gist of things
1. acquire sqs url
2. edit sqs url in
3. edit ec2 front-end instance ip in `player.js` (line 61 and 88)
4. run music player front-end
5. run producer/api
6. create database
7. run stat front-end
8. run listener
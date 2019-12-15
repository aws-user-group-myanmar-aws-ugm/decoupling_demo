### Prepare environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### Install dependencies
```bash
pip install -r requirements.txt
```

### Run Producer
```bash
env FLASK_APP=producer.py flask run
```

### Run Consumer
```bash
python listener.py
```
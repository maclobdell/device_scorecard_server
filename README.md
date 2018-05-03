# Platform Scorecard Server

Receives data on targets (in specific json format).  Data contains information on what features are enabled.  In the future it will support tests results.  It can serve it back via json or show it on simple web interface.  

## Starting the server app
```
python app_target_data.py
```

## Sending data on a new target
```
curl -i -H "Content-Type: application/json" -X POST -d @target_data_new_target.json http://localhost:5000/target_data/api/v1.0/targets
```

## Appending data on an existing target
```
curl -i -H "Content-Type: application/json" -X PUT -d @target_data_test_record.json http://localhost:5000/target_data/api/v1.0/targets/1
```


//to create a new target record
curl -i -H "Content-Type: application/json" -X POST -d "{"""command""":"""show"""}" http://localhost:5000/target_data/api/v1.0/targets

//to modify a target record
curl -i -H "Content-Type: application/json" -X PUT -d @target_data_test_record.json http://localhost:5000/target_data/api/v1.0/targets/1

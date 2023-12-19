import confluent_kafka as _a

producer_conf = {
    'bootstrap.servers': 'broker:9094',
    'client.id': 'my-app'
}

producer = _a.Producer(producer_conf)

def produce():
    try:
        data = "kkkkkk"
        producer.produce('topic1', value=data)
        producer.flush()
        return {"status": "success", "message": data}
    except Exception as e:
        return {"status": "error", "message": str(e)}
    
produce()

# from modules.model import metadata

# # target_metadata = mymodel.Base.metadata
# target_metadata = metadata
# qlalchemy.url = postgresql://postgres:601246@host.docker.internal:5432/egov
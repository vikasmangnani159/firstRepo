from elasticsearch import Elasticsearch as ES



#Function to connect to ES
def connect_database():
    print ("Setup connection...")
    global es
    es= ES(
        ['http://ilvpbg1939'],
        port=9200,
        use_ssl=False
    )

    print(es.ping())
    if not es.ping():
        raise ValueError("Connection failed")
    print ("Done!, connection is successfully established")

    # Here I'll fetch the data after successful connection

    n=es.search(index='plto-oc-cd-master',size=1000000) #here, give size = number that should be biggere then the enteries in your database
    print(n)



if __name__ == "__main__":
    connect_database()


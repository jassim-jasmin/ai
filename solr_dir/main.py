import pysolr

# for creating a collection
# solr-8.5.0:$ bin/post -c mycol1 example/exampledocs/*
# sudo su - solr -c "/opt/solr/bin/solr create -c mycol1 -n data_driven_schema_configs" # follow
# ref link = https://tecadmin.net/install-apache-solr-on-ubuntu/

solr = pysolr.Solr('http://localhost:8983/solr/mycol1/', always_commit=True, timeout=10)
health = solr.ping()
print("hi", health)
# How you'd index data.
status = solr.add([
    {
        "id": "doc_3",
        "title": "A test document 2",
    },
    {
        "id": "doc_4",
        "title": "The apple: Tasty or Dangerous?",
        "_doc": [
            { "id": "child_doc_21", "title": "2peel" },
            { "id": "child_doc_22", "title": "2seed" },
        ]
    },
])

print("status", status)
results = solr.search('')
results = solr.search(q="title:apple") # collen is needed for searching

def r():
    print("Saw {0} result(s).".format(len(results)))

    for result in results:
        print("The title is '{0}'.".format(result['title']))

r()
# For a more advanced query, say involving highlighting, you can pass
# additional options to Solr.
results = solr.search('Banana', **{
    'hl': 'true',
    'hl.fragsize': 10,
})
r()
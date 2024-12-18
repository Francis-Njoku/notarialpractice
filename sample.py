import pandas as pd
from rdflib import Graph, Literal, RDF, URIRef, Namespace

# Load CSV
data = pd.read_csv("data.csv")

# Initialize RDF graph
g = Graph()
EX = Namespace("http://example.org/")

# Iterate and add triples
for _, row in data.iterrows():
    person = URIRef(f"http://example.org/person/{row['Person_ID']}")
    g.add((person, RDF.type, EX.Person))
    g.add((person, EX.name, Literal(row['Name'])))
    g.add((person, EX.age, Literal(row['Age'])))
    g.add((person, EX.country, Literal(row['Country'])))

# Save RDF file
g.serialize("data.rdf", format="turtle")
print("RDF file created as data.rdf")


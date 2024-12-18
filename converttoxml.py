from rdflib import Graph

# Load Turtle file
g = Graph()
g.parse("data.rdf", format="turtle")  # Replace 'data.rdf' with your file path

# Convert to RDF/XML
g.serialize("data.rdfxml", format="xml")
print("File converted to RDF/XML as 'data.rdfxml'")
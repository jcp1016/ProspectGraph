//---------------------------------------------------------------------------------------
// create_PeopleRoles.cypher
//
// Desc: creates relationships from People to Roles Nodes 
// Author:  Sam Guleff
// Date  :  Nov 2015
//
// To run this from the bash shell go to $NEO4J_HOME:
// ./bin/neo4j-shell -file $BDA_DEV/create_roles.cypher > $BDA_DEV/DATA/All_PeopleRoles.txt
//---------------------------------------------------------------------------------------
//'file:///C:/Users/Sam/Desktop/Data/All_PeopleRoles_Test.txt'
export INFILE="file:/Users/janetprumachuk/dev/Python/Columbia/bda-dev/All_PeopleRoles.txt"

LOAD CSV WITH HEADERS 
FROM {INFILE} AS row 
FIELDTERMINATOR "|"
MATCH (p:Person {personID: row.personID}), (r:Role {Name: row.Name})
MERGE (p)-[:EMPLOYEE_TYPE {roleType: row.Name}]->(r);

MATCH (p:Person)-[r:WORKS_AT]->(c:Company)
RETURN p.Name, r, c.Name LIMIT 5;

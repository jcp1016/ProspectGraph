//---------------------------------------------------------------------------------------
// create_companies.cypher
//
// Desc: creates nodes with label Company
// Author:  Janet Prumachuk
// Date  :  Nov 2015
// 
// To run this from the bash shell go to $NEO4J_HOME:        
// ./bin/neo4j-shell -file $BDA_DEV/create_companies.cypher > $BDA_DEV/DATA/results.txt 
//---------------------------------------------------------------------------------------
USING PERIODIC COMMIT 500
LOAD CSV WITH HEADERS 
FROM "file:/Users/janetprumachuk/dev/Python/Columbia/BDAProject/all_companies.csv" AS row
FIELDTERMINATOR '|'
CREATE (:Company {ID: row.ID, 
                  Name: row.Name, 
                  logoURL: row.logoURL, 
                  thumbURL: row.thumbURL, 
                  dataQuality: row.dataQuality, 
                  highConcept: row.highConcept, 
                  companyURL: row.companyURL, 
                  crunchbaseURL: row.crunchbaseURL, 
                  twitterURL: row.twitterURL, 
                  linkedinURL: row.linkedinURL, 
                  primaryLocation: row.primaryLocation, 
                  companySize: row.companySize, 
                  raisingAmount: row.raisingAmount, 
                  preMoneyValuation: row.preMoneyValuation, 
                  raisedAmount: row.raisedAmount});

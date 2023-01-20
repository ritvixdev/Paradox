// Indexing in MongoDB

// indexes allow the database server to perform specific queries to find documents 
// much more efficiently without needing to examine an entire collection of documents

// example of how you can create an index on the "email" field using the createIndex() method:

db.users.createIndex( { email: 1 } )

// In this example, the value 1 indicates that the index should be in ascending order,
// and a value of -1 would indicate descending order.

// You can also create a compound index, which is an index on multiple fields. 
// For example, you might want to create an index on both the "email" and "age" fields:

db.users.createIndex( { email: 1, age: 1 } )

// It's also possible to create a unique index, which ensures that there are no duplicate
// values in the indexed field.

db.users.createIndex( { email: 1 }, { unique: true } )

// You can also check which indexes are currently available for a collection using 
db.collection.getIndexes()
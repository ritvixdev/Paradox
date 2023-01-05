// Promise way to Fetch API

const url = 'https://hub.dummyapis.com/employee?noofRecords=10&idStarts=1001'

fetch(url)
.then((response) => response.json())
.then((data) => console.log(data))
.catch((err) => console.log(err))
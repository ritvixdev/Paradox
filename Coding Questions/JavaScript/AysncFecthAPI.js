//Async/Await way to fetch data

const url = 'https://hub.dummyapis.com/employee?noofRecords=10&idStarts=1001';

const fetchData = async () => {
  try {
    const response = await fetch(url);
    const data = await response.json();
    console.log(data);
  } catch (err) {
    console.log(err);
  }
};

fetchData();


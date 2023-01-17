// Print value in input field from input field

import React, { useState} from 'react';

const App = () => {
  const [user, setUser] = useState('');
  const [itemList, setItemList] = useState([]);

  const onChangeHandler = (e) => {
    console.log(e.target.value);
    setUser(e.target.value);
  };

  const addItemToList = () => {
    setItemList([...itemList, user]);
    setUser('');
    console.log('list Items', itemList);
  };

  return (
    <div>
      <p>Give input Below</p>
      <input value={user} onChange={onChangeHandler} />
      <button onClick={addItemToList}>send</button>
      <br/>
      <input value={itemList.slice(-1)} />
    </div>
  );
};

export default App;
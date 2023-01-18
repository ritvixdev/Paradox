// Build a React Todo List

// File: App.js

import React, { useState} from 'react';
import List from './List.js.js'

const App = () => {
  const [currentItem, setCurrentItem] = useState('');
  const [itemList, setItemList] = useState([]);

  const onChangeHandler = (e) => {
    setCurrentItem(e.target.value);
  };

  const addItemToList = () => {
    setItemList([...itemList, {item:currentItem, key:Date.now()}]);
    setCurrentItem('');
  };

  return (
    <div>
      <p>Give input Below</p>
      <input value={currentItem} onChange={onChangeHandler} />
      <button onClick={addItemToList}>+</button>
     <List itemList={itemList} setItemList={setItemList}/>
    </div>
  );
};


// File: List.js

import React from 'react';

// we are using destructing insted of props
const List = ({itemList, setItemList}) => {

    const deleteItemFromList = key => {
      const newList = itemList.filter(itemObj => {
        return itemObj.key !== key
      });
      setItemList(newList)
    }
  return (
    <div>
      {itemList.map((itemObj) => {
        return (
          <div key={itemObj.key}>
            <p>{itemObj.item}</p>
            <button onClick={()=> deleteItemFromList(itemObj.key)}>X</button>
          </div>
        );
      })}
    </div>
  );
};

export default List;

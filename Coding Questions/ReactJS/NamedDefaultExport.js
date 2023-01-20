// Named export

export const App1 = () => {

}

import {App1} from './'
// we are using {} in named brackets because we could be exporting multiple things


// Default export

const App = () => {

}

export default App

import App from './'



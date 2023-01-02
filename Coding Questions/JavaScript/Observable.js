// Interview Example for Observable
// https://www.freecodecamp.org/news/what-are-observables-how-they-are-different-from-promises/
// https://medium.com/javascript-everyday/javascript-theory-promise-vs-observable-d3087bc1239a

//Invoking Obhservable in JavaScript

import { Observable } from 'rxjs';
let observable = new Observable(observer => {
setTimeout(() => {
observer.next('Hi This will invoke Observables')
},5000)
console.log('Observables invoked!');
});
observable.subscribe();




// An Async request is one where the client does not wait for the response. 
// Nothing is blocked.

// Observables are also like callbacks and promises - that are responsible for handling async requests. 
// Observables are a part of the RXJS library. This library introduced Observables.

// -- Pull & Push Model

// Pull Model: In this model, the consumer of data is king. This means that the
// consumer of data determines when it wants data from the producer. The producer
// does not decide when the data will get delivered. You can better understand
// if you relate functions to it.

// Push Model: In this model, the producer of data is king. Producer determines when
// to send data to consumer. The Consumer does not know when data is going to come. 

// Both functions and observables are lazy.

// Subscriptions to observables are quite similar to calling a function. 
// But where observables are different is in their ability to return multiple 
// values called streams (a stream is a sequence of data over time).

// observables are simply a function that are able to give multiple values over 
// time, either synchronously or asynchronously.


// ===Promise Vs Observable===

// Observables are lazy whereas promises are not
// This is pretty self-explanatory: observables are lazy, that is we have to subscribe 
// observables to get the results. In the case of promises, they execute immediately.

// Observables handle multiple values unlike promises
// Promises can only provide a single value whereas observables can give you multiple values.

// Observables are cancelable
// You can cancel observables by unsubscribing it using the unsubscribe method 
// whereas promises don’t have such a feature.
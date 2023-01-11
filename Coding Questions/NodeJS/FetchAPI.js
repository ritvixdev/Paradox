// Get API data by Fetch in Node Js

const url = 'https://httpbin.org/post'
const data = {
    x: 1920,
    y: 1080,
};
const customHeaders = {
    "Content-Type": "application/json",
}

fetch(url, {
    method: "POST",
    headers: customHeaders,
    body: JSON.stringify(data),
})
    .then((response) => response.json())
    .then((data) => {
        console.log(data);
    })
    .catch((error) => {
        console.error(error);
    });



/* fetch('https://example.com')
.then(res => {
    res.text()       // response body (=> Promise)
    res.json()       // parse response body (=> Promise)
    res.status       //=> 200
    res.statusText   //=> 'OK'
    res.redirected   //=> false
    res.ok           //=> true
    res.url          //=> 'https://new.example.com'
    res.type         //=> 'basic'
                     //   ('cors' 'default' 'error'
                     //    'opaque' 'opaqueredirect')
    res.headers.get('Content-Type')
}) */
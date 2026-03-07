Interview Questions Asked
1. Introduction / Resume Walkthrough

Q1. Can you introduce yourself and walk us through your resume?

2. Project Experience

Q2. Can you explain one technically challenging project you worked on?
Q3. What modules were you responsible for in that project?
Q4. How did you develop the modules and solution?

3. Frontend / React Experience

Q5. Which tech stack have you worked on?
Q6. Have you worked on the frontend part of the project?
Q7. How much experience do you have in React?
Q8. Are you hands-on with class-based components or functional components?
Q9. Have you worked on class-based components or do you only know the concept?

4. API Calls and State Management

Q10. What are you using for API calls in your project?
Q11. What are you using for state management?
Q12. Are you using pure Context API or useContext hook?
Q13. What is the basic structure of Context API and how do you manage state inside it?

5. Redux vs Context

Q14. If you get a chance to work with Redux, how comfortable are you with it?
Q15. Do you understand the Redux flow, and would you need time to learn it?
Q16. In Context API, what is the use of the Provider?
Q17. What happens if you do not wrap components with the Provider?

6. React Hooks

Q18. Which React hooks have you used?
Q19. Have you worked with custom hooks?
Q20. If you use setInterval inside useEffect, where should you clear it?
Q21. In what scenario have you used useMemo?

7. useMemo / Search / Optimization Scenarios

Q22. If there is frontend search and frontend sorting, would useMemo be useful?
Q23. In which case is useMemo effective: frontend search or backend search?
Q24. If backend data is coming and you need extra logic on top of it, would useMemo help?

8. Authentication / Persistence / Roles

Q25. After login, if you get a token and user details needed across pages, where would you store them so they survive refresh?
Q26. If you need to store confidential information but do not want other users to access it, how would you manage that?
Q27. What is the difference between authentication and authorization?

9. React Concepts

Q28. Have you heard about controlled and uncontrolled components in React?
Q29. Are you aware of React Fragments?
Q30. What is the use of React Fragment?
Q31. Why should we use React Fragment instead of a div?

10. Higher-Order Components

Q32. Have you used HOC in React?
Q33. Can you give an example of HOC?
Q34. Can you give a real-world example where you used HOC?

11. React Project Optimization

Q35. How do you optimize a React project?

12. Database / MongoDB

Q36. Have you worked with databases?
Q37. Why did you use MongoDB?
Q38. How did you use MongoDB in your project?
Q39. Which programming language did you use with MongoDB?

13. Python / FastAPI

Q40. Did you get a chance to work on Python in the backend?
Q41. Are you aware of how to use MongoDB in Python?
Q42. What are the different data types in Python?
Q43. Have you used FastAPI?
Q44. How do you define APIs in FastAPI?

14. Authentication / SSO / HTTPS / Middleware

Q45. Have you worked on authentication in any application?
Q46. Are you aware of SSO authentication?
Q47. What changes when an API becomes authenticated compared to an unauthenticated one?
Q48. If you plan to integrate SSO-based authentication into an app, what changes do you need to make?

15. Real-Time Communication / Messaging

Q49. Apart from WebSockets and REST APIs, what other options are available to send real-time data to the UI?
Q50. What other communication services are available between modules?
Q51. Have you worked on Kafka?
Q52. Are you aware of Redis?
Q53. Have you used OAuth 2.0?
Q54. With which microservice did you use OAuth 2.0?
Q55. Are you aware OAuth can also be integrated with Kafka/backend communication?
Q56. If Kafka is running on one VM and another VM reads from it, how would you secure the data transfer?

16. Python OOP Basics

Q57. In Python, what is a class?
Q58. What is the difference between a class and a function definition?

17. Docker / Containers

Q59. Have you worked with Docker to bring up containers?
Q60. If I give you a Python script and ask you to create a container, how would you do it?
Q61. How would you create an image for that Python script?

18. Live Coding Exercise

Q62. Create a counter with plus and minus buttons.
Q63. When the counter reaches 5, the display text color should become red.
Q64. Why were multiple numbers increasing automatically even though no button was clicked?
Q65. Do you really need useEffect for this problem?

19. Backend Security Design

Q66. If you have a plain unauthenticated FastAPI backend with no persona-based operations, how would you integrate authentication and persona-based access?

20. Self-Rating Questions

Q67. Out of 10, how would you rate yourself in Python?
Q68. How would you rate yourself in databases, MongoDB, and Kafka?
Q69. How would you rate yourself in FastAPI and authentication integrations?
Q70. How would you rate yourself in React?

21. Closing

Q71. Do you have any questions for us?










Interview Questions Asked
1. Introduction / Background

Q1. Can you briefly introduce yourself?
Q2. Can you explain your roles and responsibilities?
Q3. Can you talk about any major projects you worked on in your previous organization?

2. Project Experience

Q4. In that project, were you involved in both backend and frontend?
Q5. Was your frontend stack React along with Next.js?
Q6. Do you have experience working with UI libraries?
Q7. How was your component structure?
Q8. What did you use for state management or context management?

3. JavaScript Fundamentals

Q9. Can you explain closures?
Q10. Given the closure code snippet, what will be the output?
Q11. Why is the output 1 2 3?
Q12. Can you explain the event loop in JavaScript?
Q13. Given the async/event loop snippet, what will be the output?
Q14. Why will C print before B?

4. React Rendering

Q15. In the given React snippet, will the child component re-render on every click of the button?
Q16. Why do you think it will or will not re-render?

5. Infinite Scroll / API Trigger Logic

Q17. How would you implement infinite loading on a product listing page?
Q18. Can you explain your approach first?
Q19. Can you write the JavaScript logic/function that triggers an API call when the user scrolls to the bottom?
Q20. How would you prevent multiple API calls while the user keeps scrolling?
Q21. Can you use debounce or throttle for that?

6. React Performance Optimization

Q22. Suppose a React application takes about 10 seconds for first paint and its JavaScript bundle is around 7–8 MB. How would you optimize it?
Q23. How would you first identify what exactly is taking time to load?
Q24. What debugging points would you check?
Q25. Once you know the React application is not optimized and the JS bundle is huge, how would you optimize it?
Q26. Anything else you would do for optimization?

7. Closing

Q27. Do you have any questions or clarifications for me?





Technical Interview Questions
Introduction / Background

Q1. Can you talk about yourself and your experience?

Project / Firmware Upgrade / IoT

Q2. In this project, was the work mainly to periodically push updates in a phased manner?
Q3. Was it only for updates, or did it also connect to devices for troubleshooting and diagnostics?
Q4. How is the UI used to schedule updates for devices?
Q5. How do you choose which set of devices should receive updates in a particular schedule?
Q6. How is the update pushed from the gateway to the device?
Q7. Were your changes only for scheduling and pushing updates till the gateway, while gateway-to-device pushing was handled by another team?
Q8. What does this pipeline involve?

SDK / Middleware / Security

Q9. You mentioned establishing reusable SDK and middleware layers — can you explain that?
Q10. Can you talk specifically about the API-versioning-based middleware layer?
Q11. When building an SDK, what security aspects do you need to take care of?
Q12. How do you set up authentication and authorization when the SDK calls your APIs?

AI / Tooling

Q13. Do you use any AI agents as part of your day-to-day development?

Power BI + React Integration

Q14. If you want to integrate or embed a Power BI report into a React web application, what steps would you follow?
Q15. Is there any React library available for embedding Power BI into React?
Q16. What do you understand from the Power BI React client / embed flow?
Q17. What data or objects do you think Power BI returns after connection — pages, visuals, etc.?

Backend / Languages

Q18. Apart from React, Next.js, and Node.js, is there any other language you have used to write APIs?

Architecture

Q19. Do you know what monorepo architecture is?
Q20. What is the advantage of using monorepo architecture?



Interview Questions Asked
1. Intro / Background

Q1. Can you briefly talk about yourself?
Q2. Are you a full-stack developer or more frontend-focused?
Q3. What are your primary skill sets?
Q4. You have full-stack experience, right?
Q5. How would you rate yourself in React?
Q6. How would you rate yourself in JavaScript?
Q7. How would you rate yourself in HTML/CSS?

2. React Experience / Versions

Q8. Which version of React are you using?
Q9. Are you comfortable with React 18 concepts?
Q10. Are you familiar with older React versions and class-based components?

3. React Fundamentals

Q11. What is React?
Q12. What do you mean by state and props?
Q13. What is a component?
Q14. How does React work?
Q15. How is the virtual DOM created?
Q16. How does React know which part got updated?
Q17. Can we see the virtual DOM or only the normal DOM?
Q18. How do you see the DOM?
Q19. What is JSX?

4. Coding / Component Writing

Q20. Can you write a simple React component and share your screen?
Q21. Do you need state for a component?
Q22. What are stateful and stateless components?
Q23. What is the simplest form of a React component?
Q24. If there is no state change and no data change, is React still a good fit?
Q25. In that case, can we still use React and how would it be handled?

5. Forms / Component Types

Q26. Do you know about controlled and uncontrolled components?

6. Data Passing / State Sharing

Q27. How do you pass data from one component to another?
Q28. Given the hierarchy Company → Department → Employee → Employee Details, how would you pass data from Company to Employee Details?
Q29. Can you write where you pass the data and where you consume it?
Q30. Have you worked on any state management tool?
Q31. What is state in your application?
Q32. If your app has multiple pages and each page header must show the same name and department, how would you show that data on all pages?
Q33. How would you update data from child to parent?

7. JavaScript Basics

Q34. Have you worked on plain JavaScript?
Q35. How do you create an object in JavaScript?
Q36. How do you inherit a variable or object?
Q37. In JavaScript, do you have the concept of objects as classes?

8. Array Methods

Q38. What is the difference between map and filter?
Q39. When would you use map, and when would you use filter?
Q40. If we do not use filter, can we achieve the same functionality using loops?

9. let, var, Scope, Hoisting

Q41. Can you explain let and var?
Q42. What do you mean by block scope and function scope?
Q43. What is hoisting?

10. Promises / Async JavaScript

Q44. Do you know promises?
Q45. What is a promise?
Q46. What do you mean by async and await?
Q47. Given this console.log / setTimeout snippet, what will be the output?

11. Context vs Redux / React Hooks

Q48. If you are not using Redux, can everything be achieved using Context API?
Q49. Do you know about useReducer?
Q50. In useEffect, what are dependencies?
Q51. What happens if you pass an empty dependency array?
Q52. What happens if you completely avoid the dependency array?

12. CSS / Styling

Q53. How good are you in CSS?
Q54. What is MUI?
Q55. What is the flex model?
Q56. Do you know relative positioning?
Q57. What are the different ways to style a React component?

13. Job Search / Closing

Q58. How long have you been searching for a React opening?
Q59. Why do you want to move out of your current company?
Q60. Which company are you currently working for?
Q61. Do you have any questions?
Q62. Are you comfortable?



Interview Questions Asked
1. Introduction / Project Background

Q1. Can we start with an introduction?
Q2. What was your role in that project?
Q3. Did you work on both frontend and backend?
Q4. Was the backend built using Node.js?
Q5. Was the frontend built using React?
Q6. Did you use Express.js or Nest.js for the backend?
Q7. On the frontend, was it Next.js?
Q8. Why did you choose Next.js?
Q9. You said you moved from Angular to React — what was the reason?
Q10. Did you work on both Angular and React, or only React?
Q11. How many years of experience do you have in React and Node.js?

2. Node.js Fundamentals

Q12. What is the event loop?
Q13. How does Node.js handle concurrency?
Q14. What are middlewares in Node.js?
Q15. Can you explain what a middleware is?
Q16. How do you handle errors in Node.js?
Q17. What is clustering in Node.js?
Q18. What is a promise?
Q19. If you have multiple promises and want to do some processing after all are completed, how would you handle that?
Q20. What is the difference between process.nextTick and setImmediate?
Q21. What are worker threads in Node.js?
Q22. If your Node.js application has memory leaks or performance issues, how would you debug and fix them?

3. React Fundamentals

Q23. What are hooks, and why do we use hooks?
Q24. What is the difference between useMemo and useCallback?
Q25. What is a higher-order component?
Q26. What is the difference between useEffect and useLayoutEffect?
Q27. How would you implement lazy loading in React?
Q28. If a React application has performance issues, how would you handle them?
Q29. What is the virtual DOM?
Q30. Have you used Redux?
Q31. So you used Context API, right?

4. Code Output / JavaScript Reasoning

Q32. Can you tell me what will be the output of this code?
Q33. What will be the output of this array transformation / lookup code?
Q34. What will be the output of this simple object mutation code?
Q35. Why will that object-mutation output happen?
Q36. What will be the output of this console.log / setTimeout / Promise code?
Q37. Why will that async output happen?
Q38. What will be the output of this loop code using var?

5. Closing

Q39. Do you have anything for me?


Interview Questions Asked
1. Introduction / Background

Q1. Can you briefly introduce yourself?

2. Coding / Algorithms

Q2. Can you share your screen?
Q3. Can you open any JavaScript online compiler?
Q4. Write a program to sort an array without using any built-in functions.
Q5. What is your approach to solve this sorting problem?
Q6. What will be the time complexity of this problem?
Q7. How many loops are required to solve this problem?
Q8. Do you think this can be solved in a single loop?

3. TypeScript

Q9. Can you tell me what exactly this TypeScript code snippet is doing?
Q10. In what scenario can this type definition be used?
Q11. What is the difference between type and interface?
Q12. Do you know generics in TypeScript?

4. JavaScript / Output Questions

Q13. Can you guess the output of this second code snippet?
Q14. Will it be undefined or will it throw an error?
Q15. How do you deep copy an object?
Q16. If I give you a nested object, will you be able to deep copy it?

5. Databases / SQL / NoSQL

Q17. Do you know about temporal tables?
Q18. What is the difference between window functions and stored procedures?
Q19. Which database type are you using — SQL or NoSQL?
Q20. What is partitioning in a NoSQL database?
Q21. When should one consider partitioning?
Q22. How do you maintain versions in MongoDB documents?
Q23. If a record needs multiple versions, how would you maintain them?

6. AWS / S3 / Cloud

Q24. Do you have exposure to DynamoDB?
Q25. Have you worked with AWS services?
Q26. If it comes to cloud infrastructure, which one are you using?
Q27. What is the use case of S3 apart from storing images or static files?

7. Frontend Tooling / Testing

Q28. Which build tool were you using on the frontend?
Q29. How do you write unit tests in backend or frontend?
Q30. Which framework were you using for testing?
Q31. When should one use Mocha and when should one use Chai?
Q32. What different use cases do Mocha and Chai provide?
Q33. Do you have experience working with Jest?

8. Redis / Caching

Q34. What methods are you familiar with in Redis?
Q35. Do you know how to store a value in Redis?
Q36. Conceptually, how does Redis work?
Q37. When should one consider using Redis?
Q38. Can you explain the caching mechanism you worked with?
Q39. What is TTL in Redis?

9. React

Q40. How many years of experience do you have in React?
Q41. What is reconciliation?
Q42. Which state management library did you use?
Q43. Did you use Context API instead of Redux?
Q44. What are the different functions or methods used in Redux?
Q45. Do you know about reducers?
Q46. What are you really good at — frontend, backend, framework, or database?
Q47. What is prop drilling?
Q48. Is prop drilling a good practice, or should we avoid it?
Q49. What is lazy loading?
Q50. What is Suspense?
Q51. Did you implement lazy loading?

10. Backend / Node.js

Q52. On the backend, which runtime or framework were you mostly using?
Q53. How does Node.js handle concurrency?

11. Closing

Q54. Do you have any questions for me?
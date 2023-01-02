//interview Promise.all example

const myPromiseOne = () => {
  return new Promise((resolve) => {
    setTimeout(() => {
      resolve('Hi');
    }, 2000);
  });
};

const myPromiseTwo = () => {
  return new Promise((resolve) => {
    setTimeout(() => {
      resolve('welcome');
    }, 3000);
  });
};

const myPromiseThree = () => {
  return new Promise((resolve) => {
    setTimeout(() => {
      resolve('to the matrix');
    }, 4000);
  });
};

const msg = async () => {
  try {
    const [a, b, c] = await Promise.all([myPromiseOne(),myPromiseTwo(), myPromiseThree() ]);
    console.log(`${a} ${b} ${c}`);
  } catch (err) {
    console.log(err);
  }
};

msg();


'use strict'

var namesToAges = {
    "Alyssa": 22,
    "Charley": 25,
    "Dan": 25,
    "Jeff": 20,
    "Kasey": 20,
    "Kim": 20,
    "Morgan": 25,
    "Ryan": 25,
    "Stef": 22
};

var agesCount = _.countBy(_.values(namesToAges));

function getValue(obj) {
  return agesCount[obj];
}

var rarestAge = _.minBy(_.keys(agesCount), getValue);

console.dir(rarestAge);

#!/usr/bin/node

const x = parseInt(process.argv[2]);
const str = 'C is fun';

if (x) {
    for (let i = 0; i < x; ++i) {
	console.log(str);
    }
} else {
    console.log('Missing number of occurrences');
}

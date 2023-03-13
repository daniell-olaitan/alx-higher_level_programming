#!/usr/bin/node

const c = 'X';
const size = parseInt(process.argv[2]);

if (size) {
    for (let i = 0; i < size; ++i) {
	for (let j = 0; j < size; ++j) {
	    process.stdout.write(c);
	}

	console.log('');
    }
} else {
    concole.log('Missing size');
}
